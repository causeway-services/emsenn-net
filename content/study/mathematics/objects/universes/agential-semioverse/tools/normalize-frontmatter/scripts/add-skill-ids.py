#!/usr/bin/env python3
import argparse
from pathlib import Path
import re
import yaml


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def update_skill(path: Path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return False
    parts = text.split("---", 2)
    if len(parts) < 3:
        return False
    fm_text = parts[1]
    body = parts[2]
    data = yaml.safe_load(fm_text) or {}
    if data.get("id"):
        return False
    name = data.get("name")
    if not name:
        return False
    data["id"] = slugify(name)
    # Preserve key order where possible
    new_fm = yaml.safe_dump(data, sort_keys=False).strip()
    path.write_text(f"---\n{new_fm}\n---{body}", encoding="utf-8")
    return True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="*", default=["library"])
    args = parser.parse_args()

    updated = 0
    for root in args.paths:
        for path in Path(root).rglob("SKILL.md"):
            if update_skill(path):
                updated += 1
    print(f"updated {updated} skill files")


if __name__ == "__main__":
    main()
