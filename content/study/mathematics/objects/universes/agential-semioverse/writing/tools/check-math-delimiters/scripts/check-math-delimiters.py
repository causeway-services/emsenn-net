#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Iterable


def iter_markdown_files(path: Path) -> Iterable[Path]:
    if path.is_file():
        yield path
        return
    yield from path.rglob("*.md")


def strip_inline_code(line: str) -> str:
    result = []
    in_code = False
    i = 0
    while i < len(line):
        if line[i] == "`":
            in_code = not in_code
            i += 1
            continue
        if not in_code:
            result.append(line[i])
        i += 1
    return "".join(result)


def find_unmatched_math(text: str) -> list[str]:
    issues: list[str] = []
    in_fence = False
    inline_open = False
    display_open = False

    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        line = strip_inline_code(line)
        i = 0
        while i < len(line):
            if line[i : i + 2] == "$$":
                display_open = not display_open
                i += 2
                continue
            if line[i] == "$":
                inline_open = not inline_open
            i += 1

    if display_open:
        issues.append("unmatched_display_math")
    if inline_open:
        issues.append("unmatched_inline_math")
    return issues


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="+")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    failures = []
    for raw in args.paths:
        path = Path(raw)
        for file_path in iter_markdown_files(path):
            text = file_path.read_text(encoding="utf-8", errors="ignore")
            issues = find_unmatched_math(text)
            if issues:
                failures.append({"path": str(file_path), "issues": issues})

    if args.json:
        print(json.dumps({"failures": failures}, ensure_ascii=True))
    else:
        for entry in failures:
            print(f"{entry['path']}: {', '.join(entry['issues'])}")

    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
