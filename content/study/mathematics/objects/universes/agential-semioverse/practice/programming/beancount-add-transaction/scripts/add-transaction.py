#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
from datetime import datetime, timezone
from pathlib import Path


def resolve_library_root() -> Path:
    env_root = Path(os.environ.get("LIBRARY_ROOT", "library"))
    if env_root.is_absolute():
        return env_root.resolve()
    return (Path.cwd() / env_root).resolve()


def resolve_path(library_root: Path, raw_path: str) -> Path:
    raw = raw_path.strip()
    if raw.startswith("/"):
        raw = raw[1:]
    if raw.startswith("library/"):
        relative = Path(raw).relative_to("library")
    else:
        relative = Path(raw)
    candidate = (library_root / relative).resolve()
    if not candidate.is_relative_to(library_root):
        raise ValueError("path outside library root")
    return candidate


def append_log(script_dir: Path, payload: dict) -> None:
    payload["timestamp"] = datetime.now(timezone.utc).isoformat()
    log_path = script_dir / "run-log.jsonl"
    with log_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(payload, ensure_ascii=True) + "\n")


def parse_posting(line: str) -> tuple[str, float, str] | None:
    parts = line.strip().split()
    if len(parts) < 3:
        return None
    account = parts[0]
    try:
        amount = float(parts[1])
    except ValueError:
        return None
    commodity = parts[2]
    return account, amount, commodity


def check_balanced(postings: list[str]) -> tuple[bool, dict[str, float]]:
    totals: dict[str, float] = {}
    for line in postings:
        parsed = parse_posting(line)
        if not parsed:
            continue
        _, amount, commodity = parsed
        totals[commodity] = totals.get(commodity, 0.0) + amount
    for commodity, total in totals.items():
        if abs(total) > 1e-6:
            return False, totals
    return True, totals


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", required=True)
    parser.add_argument("--date", required=True)
    parser.add_argument("--narration", required=True)
    parser.add_argument("--posting", action="append", default=[])
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    script_dir = Path(__file__).resolve().parent
    library_root = resolve_library_root()
    payload: dict = {"args": vars(args), "status": "ok"}

    try:
        ledger_path = resolve_path(library_root, args.path)
        postings = args.posting
        if not postings:
            raise ValueError("no postings provided")
        balanced, totals = check_balanced(postings)
        if not balanced:
            raise ValueError(f"unbalanced postings: {totals}")

        lines = [f"{args.date} * \"{args.narration}\""]
        for line in postings:
            lines.append(f"  {line}")
        entry = "\n".join(lines) + "\n"

        ledger_path.parent.mkdir(parents=True, exist_ok=True)
        with ledger_path.open("a", encoding="utf-8") as handle:
            handle.write("\n" + entry)

        payload["result"] = {
            "path": str(ledger_path.relative_to(library_root)),
            "added": entry,
            "balanced": balanced,
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
        print(entry)


if __name__ == "__main__":
    main()
