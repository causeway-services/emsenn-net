#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone
from difflib import unified_diff
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
    parser.add_argument("--content")
    parser.add_argument("--stdin", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    script_dir = Path(__file__).resolve().parent
    library_root = resolve_library_root()
    payload: dict = {"args": vars(args), "status": "ok"}

    try:
        if args.stdin:
            new_content = sys.stdin.read()
        elif args.content is not None:
            new_content = args.content
        else:
            raise ValueError("content not provided")

        target = resolve_path(library_root, args.path)
        existed = target.exists()
        old_content = target.read_text(encoding="utf-8") if existed else ""
        changed = old_content != new_content
        diff = "".join(
            unified_diff(
                old_content.splitlines(keepends=True),
                new_content.splitlines(keepends=True),
                fromfile=str(target),
                tofile=str(target),
            )
        )
        if changed and not args.dry_run:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(new_content, encoding="utf-8")

        result = {
            "path": str(target.relative_to(library_root)),
            "changed": changed,
            "dry_run": args.dry_run,
            "diff": diff,
            "previous_exists": existed,
            "bytes_written": len(new_content.encode("utf-8")) if changed and not args.dry_run else 0,
        }
        payload["result"] = result
    except Exception as exc:
        payload["status"] = "error"
        payload["error"] = str(exc)

    append_log(script_dir, payload)

    if payload["status"] != "ok":
        raise SystemExit(payload["error"])
    if args.json:
        print(json.dumps(payload["result"], ensure_ascii=True))
    else:
        print(payload["result"]["diff"])


if __name__ == "__main__":
    main()
