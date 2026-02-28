#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import time
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import urlopen


def fetch_json(url: str) -> dict:
    with urlopen(url) as response:
        return json.loads(response.read().decode("utf-8"))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--acct", help="user@host")
    parser.add_argument("--user")
    parser.add_argument("--host")
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument("--output-dir", required=True)
    args = parser.parse_args()

    if args.acct:
        if "@" not in args.acct:
            raise SystemExit("acct must be user@host")
        user, host = args.acct.split("@", 1)
    else:
        if not args.user or not args.host:
            raise SystemExit("provide --acct or --user and --host")
        user, host = args.user, args.host

    if args.limit < 1 or args.limit > 20:
        raise SystemExit("limit must be between 1 and 20")

    lookup_params = urlencode({"acct": f"{user}@{host}"})
    lookup_url = f"https://{host}/api/v1/accounts/lookup?{lookup_params}"
    account = fetch_json(lookup_url)
    account_id = account.get("id")
    if not account_id:
        raise SystemExit("account id not found")

    statuses_url = f"https://{host}/api/v1/accounts/{account_id}/statuses?limit={args.limit}"
    statuses = fetch_json(statuses_url)

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    output_path = output_dir / f"{user}-{host}-{timestamp}.json"
    output_path.write_text(json.dumps(statuses, ensure_ascii=True, indent=2), encoding="utf-8")
    print(str(output_path))


if __name__ == "__main__":
    main()
