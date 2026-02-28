#!/usr/bin/env python3
import argparse
import os
import sys
from typing import List, Optional, Tuple


LOG_DIR = os.path.join("library", "agents", "emsenn", "content", "log")


def list_logs() -> List[str]:
    if not os.path.isdir(LOG_DIR):
        raise FileNotFoundError(f"Log directory not found: {LOG_DIR}")
    entries = []
    for name in os.listdir(LOG_DIR):
        if name.endswith(".md"):
            entries.append(name)
    return sorted(entries)


def select_latest(files: List[str], count: int) -> List[str]:
    if count < 1:
        raise ValueError("count must be >= 1")
    return list(reversed(files))[:count]


def split_frontmatter(content: str) -> Tuple[Optional[str], str]:
    if not content.startswith("---"):
        return None, content
    lines = content.splitlines(keepends=True)
    if len(lines) < 2:
        return None, content
    if lines[0].strip() != "---":
        return None, content
    fm_lines = [lines[0]]
    for i in range(1, len(lines)):
        fm_lines.append(lines[i])
        if lines[i].strip() == "---":
            frontmatter = "".join(fm_lines)
            remainder = "".join(lines[i + 1 :])
            return frontmatter, remainder
    return None, content


def read_file(path: str) -> str:
    with open(path, "r", encoding="utf-8") as handle:
        return handle.read()


def render_compact(path: str, content: str) -> str:
    frontmatter, _ = split_frontmatter(content)
    if frontmatter is None:
        print(f"No frontmatter: {path}", file=sys.stderr)
        return ""
    return frontmatter.rstrip()


def render_full(path: str, content: str) -> str:
    header = f"=== {path} ==="
    return f"{header}\n{content.rstrip()}"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Show emsenn's most recent log entries by filename date order."
    )
    parser.add_argument(
        "--count",
        "-n",
        type=int,
        default=1,
        help="Number of most recent logs to output (default: 1).",
    )
    parser.add_argument(
        "--compact",
        action="store_true",
        help="Output only YAML frontmatter for each entry if present.",
    )
    args = parser.parse_args()

    files = list_logs()
    if not files:
        print("No log files found.", file=sys.stderr)
        return 1
    selected = select_latest(files, args.count)

    outputs = []
    for name in selected:
        path = os.path.join(LOG_DIR, name)
        content = read_file(path)
        if args.compact:
            rendered = render_compact(path, content)
            if rendered:
                outputs.append(rendered)
        else:
            outputs.append(render_full(path, content))

    if outputs:
        print("\n\n".join(outputs))
        return 0
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
