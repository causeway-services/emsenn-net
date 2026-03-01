#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path


LINK_PATTERN = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
WIKI_PATTERN = re.compile(r"\[\[([^\]]+)\]\]")


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


def classify_target(target: str) -> str:
    if target.startswith("http://") or target.startswith("https://"):
        return "external"
    if target.startswith("#"):
        return "anchor"
    return "internal"


def extract_links(text: str) -> list[dict]:
    links: list[dict] = []
    for match in LINK_PATTERN.finditer(text):
        label = match.group(1).strip()
        target = match.group(2).strip()
        links.append({"label": label, "target": target, "kind": classify_target(target)})
    for match in WIKI_PATTERN.finditer(text):
        target = match.group(1).strip()
        links.append({"label": target, "target": target, "kind": "wiki"})
    return links


def gather_links(path: Path) -> list[dict]:
    text = path.read_text(encoding="utf-8")
    return extract_links(text)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--path")
    parser.add_argument("--root")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    script_dir = Path(__file__).resolve().parent
    library_root = resolve_library_root()
    payload: dict = {"args": vars(args), "status": "ok"}

    try:
        if not args.path and not args.root:
            raise ValueError("provide --path or --root")
        results = []
        if args.path:
            target = resolve_path(library_root, args.path)
            results.append(
                {
                    "path": str(target.relative_to(library_root)),
                    "links": gather_links(target),
                }
            )
        else:
            root = resolve_path(library_root, args.root)
            for path in sorted(root.rglob("*.md")):
                results.append(
                    {
                        "path": str(path.relative_to(library_root)),
                        "links": gather_links(path),
                    }
                )
        payload["result"] = {"results": results}
    except Exception as exc:
        payload["status"] = "error"
        payload["error"] = str(exc)

    append_log(script_dir, payload)
    if payload["status"] != "ok":
        raise SystemExit(payload["error"])
    if args.json:
        print(json.dumps(payload["result"], ensure_ascii=True))
    else:
        print(payload["result"])


if __name__ == "__main__":
    main()
