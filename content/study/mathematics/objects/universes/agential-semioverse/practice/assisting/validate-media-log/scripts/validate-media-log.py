#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


DATE_HEADING = re.compile(r"^## (\d{4}-\d{2}-\d{2})$")


def validate(text: str) -> tuple[bool, list[str]]:
    errors = []
    lines = [line.rstrip() for line in text.splitlines()]
    headings = [i for i, line in enumerate(lines) if line.startswith("## ")]
    if not headings:
        errors.append("missing_date_headings")
        return False, errors
    for index in headings:
        if not DATE_HEADING.match(lines[index]):
            errors.append(f"invalid_date_heading:{lines[index]}")
        if index + 1 < len(lines) and lines[index + 1].startswith("## "):
            errors.append(f"empty_section:{lines[index]}")
    return not errors, errors


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", required=True)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    text = Path(args.path).read_text(encoding="utf-8")
    ok, errors = validate(text)
    result = {"ok": ok, "errors": errors}
    if args.json:
        print(json.dumps(result, ensure_ascii=True))
    else:
        print(result)
    if not ok:
        raise SystemExit("invalid media log")


if __name__ == "__main__":
    main()
