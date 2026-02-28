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
        skill_dir = Path(args.path).resolve()
        if not skill_dir.is_dir():
            raise ValueError("skill directory not found")
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.exists():
            raise ValueError("SKILL.md missing")
        meta = load_frontmatter(skill_md)
        name = meta.get("name")
        if name != skill_dir.name:
            raise ValueError("skill name does not match directory")
        if meta.get("kind") not in {"skill", "agent-skill"}:
            raise ValueError("skill kind invalid")
        payload["result"] = {"path": str(skill_dir), "name": name}
    except Exception as exc:
        payload["status"] = "error"
        payload["error"] = str(exc)

    append_log(script_dir, payload)
    if payload["status"] != "ok":
        raise SystemExit(payload["error"])
    if args.json:
        print(json.dumps(payload["result"], ensure_ascii=True))
    else:
        print(payload["result"]["name"])


if __name__ == "__main__":
    main()
