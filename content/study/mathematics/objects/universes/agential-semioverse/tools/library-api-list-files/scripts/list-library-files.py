#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
from datetime import datetime, timezone
from pathlib import Path


def resolve_library_root() -> Path:
    env_root = Path(os.environ.get("LIBRARY_ROOT", "library"))
    if env_root.is_absolute():
        return env_root.resolve()
    return (Path.cwd() / env_root).resolve()


def resolve_path(library_root: Path, raw_path: str) -> Path:
    raw = raw_path.strip()
    if raw.startswith("/"):
        raw = raw[1:]
    if raw.startswith("library/"):
        relative = Path(raw).relative_to("library")
    else:
        relative = Path(raw)
    candidate = (library_root / relative).resolve()
    if not candidate.is_relative_to(library_root):
        raise ValueError("path outside library root")
    return candidate


def append_log(script_dir: Path, payload: dict) -> None:
    payload["timestamp"] = datetime.now(timezone.utc).isoformat()
    log_path = script_dir / "run-log.jsonl"
    with log_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(payload, ensure_ascii=True) + "\n")


def normalize_ext(ext: str) -> str:
    ext = ext.strip().lower()
    if ext.startswith("."):
        ext = ext[1:]
    return ext


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default="library")
    parser.add_argument("--ext", action="append", default=[])
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    script_dir = Path(__file__).resolve().parent
    library_root = resolve_library_root()
    payload: dict = {"args": vars(args), "status": "ok"}

    try:
        root_path = resolve_path(library_root, args.root)
        if not root_path.exists():
            raise ValueError("root not found")
        exts = {normalize_ext(ext) for ext in args.ext if ext.strip()}
        entries = []
        for path in sorted(root_path.rglob("*")):
            if path.is_dir():
                continue
            if exts:
                suffix = normalize_ext(path.suffix)
                if suffix not in exts:
                    continue
            stat = path.stat()
            entries.append(
                {
                    "path": str(path.relative_to(library_root)),
                    "size": stat.st_size,
                    "mtime": stat.st_mtime,
                }
            )
        payload["result"] = {"count": len(entries), "files": entries}
    except Exception as exc:
        payload["status"] = "error"
        payload["error"] = str(exc)

    append_log(script_dir, payload)
    if payload["status"] != "ok":
        raise SystemExit(payload["error"])
    if args.json:
        print(json.dumps(payload["result"], ensure_ascii=True))
    else:
        for entry in payload["result"]["files"]:
            print(entry["path"])


if __name__ == "__main__":
    main()
