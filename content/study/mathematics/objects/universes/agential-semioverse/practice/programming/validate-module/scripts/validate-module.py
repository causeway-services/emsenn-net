#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml


REQUIRED_FILES = ["README.md", "SPECIFICATIONS.md"]
REQUIRED_DIRS = ["curricula", "skills", "tests"]


def append_log(script_dir: Path, payload: dict) -> None:
    payload["timestamp"] = datetime.now(timezone.utc).isoformat()
    log_path = script_dir / "run-log.jsonl"
    with log_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(payload, ensure_ascii=True) + "\n")


def load_frontmatter(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        raise ValueError(f"missing frontmatter in {path.name}")
    parts = text.split("---", 2)
    if len(parts) < 3:
        raise ValueError(f"unterminated frontmatter in {path.name}")
    data = yaml.safe_load(parts[1]) or {}
    if not isinstance(data, dict):
        raise ValueError(f"frontmatter not a mapping in {path.name}")
    return data


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", required=True)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    script_dir = Path(__file__).resolve().parent
    payload: dict = {"args": vars(args), "status": "ok"}

    try:
        module_dir = Path(args.path).resolve()
        if not module_dir.is_dir():
            raise ValueError("module directory not found")
        missing_files = [name for name in REQUIRED_FILES if not (module_dir / name).exists()]
        missing_dirs = [name for name in REQUIRED_DIRS if not (module_dir / name).exists()]
        if missing_files or missing_dirs:
            raise ValueError(
                "missing items: "
                + ", ".join(missing_files + missing_dirs)
            )
        readme_meta = load_frontmatter(module_dir / "README.md")
        spec_meta = load_frontmatter(module_dir / "SPECIFICATIONS.md")
        payload["result"] = {
            "path": str(module_dir),
            "readme_id": readme_meta.get("id"),
            "spec_id": spec_meta.get("id"),
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
        print(payload["result"]["path"])


if __name__ == "__main__":
    main()
