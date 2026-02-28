#!/usr/bin/env python3
"""Append IDEAS.md headings to PLANS.md as checklist items."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import List


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Append ideas to PLANS.md.")
    parser.add_argument("ideas", type=Path, help="Path to IDEAS.md")
    parser.add_argument("plans", type=Path, help="Path to PLANS.md")
    parser.add_argument(
        "--roles",
        type=str,
        default="planning-agent",
        help="Comma-separated roles",
    )
    parser.add_argument(
        "--goals",
        type=str,
        default="plan-ideas",
        help="Comma-separated goals",
    )
    return parser.parse_args()


def collect_headings(path: Path) -> List[str]:
    titles = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            title = line[3:].strip()
            if title:
                titles.append(title)
    return titles


def main() -> None:
    args = parse_args()
    ideas = collect_headings(args.ideas)
    roles = ", ".join([r.strip() for r in args.roles.split(",") if r.strip()])
    goals = ", ".join([g.strip() for g in args.goals.split(",") if g.strip()])

    lines = [
        f"- [ ] {title} [roles:: {roles}] [goals:: {goals}]"
        for title in ideas
    ]

    content = args.plans.read_text(encoding="utf-8") if args.plans.exists() else ""
    with args.plans.open("a", encoding="utf-8") as handle:
        if content and not content.endswith("\n"):
            handle.write("\n")
        handle.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
