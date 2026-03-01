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


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", required=True)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    script_dir = Path(__file__).resolve().parent
    library_root = resolve_library_root()
    payload: dict = {"args": vars(args), "status": "ok"}

    try:
        ledger_path = resolve_path(library_root, args.path)
        if not ledger_path.exists():
            raise ValueError("ledger not found")
        result = {"path": str(ledger_path.relative_to(library_root)), "ok": True, "details": ""}
        try:
            proc = subprocess.run(
                ["bean-check", str(ledger_path)],
                capture_output=True,
                text=True,
                check=False,
            )
            if proc.returncode != 0:
                result["ok"] = False
                result["details"] = proc.stderr.strip() or proc.stdout.strip()
        except FileNotFoundError:
            result["ok"] = False
            result["details"] = "bean-check not installed"
        payload["result"] = result
        if not result["ok"]:
            payload["status"] = "error"
            payload["error"] = "ledger_validation_failed"
    except Exception as exc:
        payload["status"] = "error"
        payload["error"] = str(exc)

    append_log(script_dir, payload)
    if payload["status"] != "ok":
        if args.json and "result" in payload:
            print(json.dumps(payload["result"], ensure_ascii=True))
        raise SystemExit(payload["error"])
    if args.json:
        print(json.dumps(payload["result"], ensure_ascii=True))
    else:
        print(payload["result"])


if __name__ == "__main__":
    main()
