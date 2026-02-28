#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import subprocess
from datetime import datetime, timezone
from pathlib import Path


def resolve_library_root() -> Path:
    env_root = Path(os.environ.get("LIBRARY_ROOT", "library"))
    if env_root.is_absolute():
        return env_root.resolve()
    return (Path.cwd() / env_root).resolve()


def resolve_root(library_root: Path, raw_root: str | None) -> Path:
    if not raw_root:
        return library_root
    raw = raw_root.strip()
    if raw.startswith("/"):
        raw = raw[1:]
    if raw.startswith("library/"):
        relative = Path(raw).relative_to("library")
    else:
        relative = Path(raw)
    candidate = (library_root / relative).resolve()
    if not candidate.is_relative_to(library_root):
        raise ValueError("root outside library")
    return candidate


def append_log(script_dir: Path, payload: dict) -> None:
    payload["timestamp"] = datetime.now(timezone.utc).isoformat()
    log_path = script_dir / "run-log.jsonl"
    with log_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(payload, ensure_ascii=True) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--query", required=True)
    parser.add_argument("--root")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    script_dir = Path(__file__).resolve().parent
    library_root = resolve_library_root()
    payload: dict = {"args": vars(args), "status": "ok"}

    try:
        root = resolve_root(library_root, args.root)
        command = [
            "rg",
            "--json",
            args.query,
            str(root),
            "--glob",
            "!**/.git/*",
        ]
        proc = subprocess.run(
            command,
            capture_output=True,
            text=True,
            cwd=str(library_root),
        )
        if proc.returncode not in {0, 1}:
            raise RuntimeError(proc.stderr.strip() or "rg failed")
        results: list[dict] = []
        for line in proc.stdout.splitlines():
            event = json.loads(line)
            if event.get("type") != "match":
                continue
            data = event.get("data", {})
            path_text = data.get("path", {}).get("text")
            line_number = data.get("line_number")
            lines = data.get("lines", {}).get("text", "").rstrip("\n")
            for submatch in data.get("submatches", []):
                results.append(
                    {
                        "path": str(Path(path_text).resolve().relative_to(library_root)),
                        "line": line_number,
                        "column": submatch.get("start"),
                        "text": lines,
                    }
                )
        payload["result"] = {"matches": results}
    except Exception as exc:
        payload["status"] = "error"
        payload["error"] = str(exc)

    append_log(script_dir, payload)

    if payload["status"] != "ok":
        raise SystemExit(payload["error"])
    if args.json:
        print(json.dumps(payload["result"], ensure_ascii=True))
    else:
        for match in payload["result"]["matches"]:
            print(f"{match['path']}:{match['line']}: {match['text']}")


if __name__ == "__main__":
    main()
