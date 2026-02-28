#!/usr/bin/env python3
import argparse
from pathlib import Path


def normalize_frontmatter(text: str) -> str:
    if not text.startswith("---"):
        return text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return text
    fm = parts[1].splitlines()
    new_lines = []
    for line in fm:
        if line.startswith("title: "):
            value = line[len("title: "):].strip()
            if ":" in value and not (value.startswith('"') or value.startswith("'")):
                value = f"\"{value}\""
            line = f"title: {value}"
        if line.startswith("name: "):
            value = line[len("name: "):].strip()
            if ":" in value and not (value.startswith('"') or value.startswith("'")):
                value = f"\"{value}\""
            line = f"name: {value}"
        new_lines.append(line)
    return "---\n" + "\n".join(new_lines) + "\n---" + parts[2]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="*", default=["library"])
    args = parser.parse_args()

    for root in args.paths:
        root_path = Path(root)
        if root_path.is_file():
            candidates = [root_path]
        else:
            candidates = list(root_path.rglob("*.md"))
        for path in candidates:
            text = path.read_text(encoding="utf-8")
            new_text = normalize_frontmatter(text)
            if new_text != text:
                path.write_text(new_text, encoding="utf-8")


if __name__ == "__main__":
    main()
