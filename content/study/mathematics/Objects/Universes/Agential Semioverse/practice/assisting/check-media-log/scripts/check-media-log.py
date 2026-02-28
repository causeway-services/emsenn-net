#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path


def parse_latest_date(text: str) -> date | None:
    latest = None
    for line in text.splitlines():
        line = line.strip()
        if line.startswith("## "):
            value = line[3:].strip()
            try:
                current = date.fromisoformat(value)
            except ValueError:
                continue
            if latest is None or current > latest:
                latest = current
    return latest


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", required=True)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    path = Path(args.path)
    text = path.read_text(encoding="utf-8")
    latest = parse_latest_date(text)
    today = date.today()
    stale = latest is None or (today - latest).days > 1
    result = {
        "path": str(path),
        "latest_entry": latest.isoformat() if latest else None,
        "days_since": (today - latest).days if latest else None,
        "stale": stale,
    }
    if args.json:
        print(json.dumps(result, ensure_ascii=True))
    else:
        print(result)


if __name__ == "__main__":
    main()
