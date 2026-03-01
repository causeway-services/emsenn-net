#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml


def append_log(script_dir: Path, payload: dict) -> None:
    payload["timestamp"] = datetime.now(timezone.utc).isoformat()
    log_path = script_dir / "run-log.jsonl"
    with log_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(payload, ensure_ascii=True) + "\n")


def load_frontmatter(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        raise ValueError("missing frontmatter")
    parts = text.split("---", 2)
    if len(parts) < 3:
        raise ValueError("unterminated frontmatter")
    data = yaml.safe_load(parts[1]) or {}
    if not isinstance(data, dict):
        raise ValueError("frontmatter not a mapping")
    return data


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", required=True)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    script_dir = Path(__file__).resolve().parent
    payload: dict = {"args": vars(args), "status": "ok"}

    try:
        lesson_path = Path(args.path).resolve()
        if not lesson_path.is_file():
            raise ValueError("lesson file not found")
        meta = load_frontmatter(lesson_path)
        if meta.get("kind") != "lesson":
            raise ValueError("kind must be lesson")
        if not meta.get("title"):
            raise ValueError("title missing")
        if not meta.get("id"):
            raise ValueError("id missing")
        if not meta.get("authors"):
            raise ValueError("authors missing")
        payload["result"] = {"path": str(lesson_path), "id": meta.get("id")}
    except Exception as exc:
        payload["status"] = "error"
        payload["error"] = str(exc)

    append_log(script_dir, payload)
    if payload["status"] != "ok":
        raise SystemExit(payload["error"])
    if args.json:
        print(json.dumps(payload["result"], ensure_ascii=True))
    else:
        print(payload["result"]["id"])


if __name__ == "__main__":
    main()
