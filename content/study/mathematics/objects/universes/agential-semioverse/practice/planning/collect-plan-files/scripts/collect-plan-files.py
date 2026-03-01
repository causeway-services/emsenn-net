#!/usr/bin/env python3
import argparse
from pathlib import Path
import yaml


def extract_frontmatter(path: Path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return None
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None
    return yaml.safe_load(parts[1]) or {}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default="library/plans")
    args = parser.parse_args()

    root = Path(args.root)
    for path in root.rglob("*.md"):
        fm = extract_frontmatter(path)
        if fm and fm.get("kind") == "plan":
            title = fm.get("title", "untitled")
            print(f"{path}: {title}")


if __name__ == "__main__":
    main()
