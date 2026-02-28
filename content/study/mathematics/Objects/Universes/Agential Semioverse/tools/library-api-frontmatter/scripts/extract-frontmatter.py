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


def extract_frontmatter(text: str) -> tuple[dict | None, str | None]:
    if not text.startswith("---"):
        return None, "missing_frontmatter"
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None, "unterminated_frontmatter"
    raw = parts[1].strip()
    try:
        data = yaml.safe_load(raw) or {}
    except yaml.YAMLError as exc:
        return None, f"invalid_yaml: {exc}"
    if not isinstance(data, dict):
        return None, "frontmatter_not_mapping"
    return data, None


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", required=True)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    script_dir = Path(__file__).resolve().parent
    library_root = resolve_library_root()
    payload: dict = {"args": vars(args), "status": "ok"}

    try:
        target = resolve_path(library_root, args.path)
        text = target.read_text(encoding="utf-8")
        data, err = extract_frontmatter(text)
        if err:
            payload["result"] = {"path": str(target.relative_to(library_root)), "frontmatter": None, "error": err}
        else:
            payload["result"] = {
                "path": str(target.relative_to(library_root)),
                "frontmatter": data,
                "error": None,
            }
    except Exception as exc:
        payload["status"] = "error"
        payload["error"] = str(exc)

    append_log(script_dir, payload)
    if payload["status"] != "ok":
        raise SystemExit(payload["error"])
    if args.json:
        print(json.dumps(payload["result"], ensure_ascii=True))
    else:
        print(payload["result"]["frontmatter"])


if __name__ == "__main__":
    main()
