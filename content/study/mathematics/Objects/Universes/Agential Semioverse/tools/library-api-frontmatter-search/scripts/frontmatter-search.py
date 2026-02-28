#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
from datetime import datetime, timezone
from pathlib import Path

import yaml


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


def load_frontmatter(path: Path) -> dict | None:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return None
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None
    data = yaml.safe_load(parts[1]) or {}
    if not isinstance(data, dict):
        return None
    return data


def matches_value(value: object, needle: str, contains: bool) -> bool:
    if isinstance(value, str):
        return needle in value if contains else value == needle
    if isinstance(value, list):
        for item in value:
            if isinstance(item, str):
                if needle in item if contains else item == needle:
                    return True
    return False


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default="library")
    parser.add_argument("--key", required=True)
    parser.add_argument("--value", required=True)
    parser.add_argument("--contains", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    script_dir = Path(__file__).resolve().parent
    library_root = resolve_library_root()
    payload: dict = {"args": vars(args), "status": "ok"}

    try:
        root_path = resolve_path(library_root, args.root)
        if not root_path.exists():
            raise ValueError("root not found")
        matches = []
        for path in root_path.rglob("*.md"):
            data = load_frontmatter(path)
            if not data or args.key not in data:
                continue
            if matches_value(data.get(args.key), args.value, args.contains):
                matches.append(
                    {
                        "path": str(path.relative_to(library_root)),
                        "frontmatter": data,
                    }
                )
        payload["result"] = {"matches": matches}
    except Exception as exc:
        payload["status"] = "error"
        payload["error"] = str(exc)

    append_log(script_dir, payload)
    if payload["status"] != "ok":
        raise SystemExit(payload["error"])
    if args.json:
        print(json.dumps(payload["result"], ensure_ascii=True))
    else:
        print(payload["result"])


if __name__ == "__main__":
    main()
