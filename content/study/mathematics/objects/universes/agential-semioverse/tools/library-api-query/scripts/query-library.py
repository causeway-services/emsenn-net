#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

import yaml


FRONTMATTER_BOUNDARY = "---"


def resolve_library_root() -> Path:
    env_root = Path(os.environ.get("LIBRARY_ROOT", "library"))
    if env_root.is_absolute():
        return env_root.resolve()
    return (Path.cwd() / env_root).resolve()


def parse_date(value: str | None) -> date | None:
    if not value:
        return None
    try:
        return date.fromisoformat(value)
    except ValueError:
        return None


def extract_frontmatter(text: str) -> dict[str, Any]:
    if not text.startswith(FRONTMATTER_BOUNDARY):
        return {}
    parts = text.split(FRONTMATTER_BOUNDARY, 2)
    if len(parts) < 3:
        return {}
    try:
        data = yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError:
        return {}
    return data if isinstance(data, dict) else {}


def parse_tags(meta: dict[str, Any]) -> list[str]:
    raw = meta.get("tags") or []
    if isinstance(raw, list):
        return [str(tag).strip() for tag in raw if str(tag).strip()]
    if isinstance(raw, str):
        return [raw.strip()] if raw.strip() else []
    return []


def parse_authors(meta: dict[str, Any]) -> list[str]:
    raw = meta.get("authors") or meta.get("author") or []
    names: list[str] = []
    if isinstance(raw, list):
        for item in raw:
            if isinstance(item, str) and item.strip():
                names.append(item.strip())
            elif isinstance(item, dict):
                literal = item.get("literal")
                if isinstance(literal, str) and literal.strip():
                    names.append(literal.strip())
    elif isinstance(raw, str) and raw.strip():
        names.append(raw.strip())
    return names


def parse_publications(meta: dict[str, Any]) -> list[str]:
    raw = meta.get("publications") or []
    if isinstance(raw, list):
        return [str(item).strip() for item in raw if str(item).strip()]
    if isinstance(raw, str):
        return [raw.strip()] if raw.strip() else []
    if isinstance(raw, dict):
        return [f"{key}: {value}" for key, value in raw.items()]
    return []


def append_log(script_dir: Path, payload: dict) -> None:
    payload["timestamp"] = datetime.now(timezone.utc).isoformat()
    log_path = script_dir / "run-log.jsonl"
    with log_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(payload, ensure_ascii=True) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tags")
    parser.add_argument("--kind")
    parser.add_argument("--authors")
    parser.add_argument("--publications")
    parser.add_argument("--id")
    parser.add_argument("--title")
    parser.add_argument("--path-prefix")
    parser.add_argument("--date-from")
    parser.add_argument("--date-to")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    script_dir = Path(__file__).resolve().parent
    library_root = resolve_library_root()
    payload: dict = {"args": vars(args), "status": "ok"}

    try:
        tags_filter = [tag.strip() for tag in (args.tags or "").split(",") if tag.strip()]
        authors_filter = [
            author.strip() for author in (args.authors or "").split(",") if author.strip()
        ]
        pubs_filter = [
            pub.strip() for pub in (args.publications or "").split(",") if pub.strip()
        ]
        kind_filter = args.kind.strip() if args.kind else None
        id_filter = args.id.strip() if args.id else None
        title_filter = args.title.strip().lower() if args.title else None
        path_prefix = args.path_prefix.strip().lstrip("/") if args.path_prefix else None
        date_from = parse_date(args.date_from)
        date_to = parse_date(args.date_to)

        matches: list[dict[str, Any]] = []
        for path in library_root.rglob("*.md"):
            if path.parts[:3] == ("library", "inbox", "triage"):
                continue
            relative_path = str(path.relative_to(library_root))
            if path_prefix and not relative_path.startswith(path_prefix):
                continue
            text = path.read_text(encoding="utf-8", errors="ignore")
            meta = extract_frontmatter(text)
            tags = parse_tags(meta)
            authors = parse_authors(meta)
            publications = parse_publications(meta)
            date_created = meta.get("date-created") or meta.get("date")
            created = parse_date(date_created) if isinstance(date_created, str) else None

            if tags_filter and not any(tag in tags for tag in tags_filter):
                continue
            if authors_filter and not any(author in authors for author in authors_filter):
                continue
            if pubs_filter and not any(pub in publications for pub in pubs_filter):
                continue
            if kind_filter and meta.get("kind") != kind_filter:
                continue
            if id_filter and meta.get("id") != id_filter:
                continue
            if title_filter:
                title = meta.get("title") or ""
                if title_filter not in str(title).lower():
                    continue
            if date_from and (created is None or created < date_from):
                continue
            if date_to and (created is None or created > date_to):
                continue

            matches.append(
                {
                    "path": relative_path,
                    "title": meta.get("title"),
                    "id": meta.get("id"),
                    "date_created": date_created,
                    "tags": tags,
                    "kind": meta.get("kind"),
                    "authors": authors,
                    "publications": publications,
                }
            )

        payload["result"] = {"matches": matches}
    except Exception as exc:
        payload["status"] = "error"
        payload["error"] = str(exc)

    append_log(script_dir, payload)

    if payload["status"] != "ok":
        raise SystemExit(payload["error"])
    if args.json:
        print(json.dumps(payload["result"], ensure_ascii=True))
    else:
        for match in payload["result"]["matches"]:
            print(f"{match['path']}: {match.get('title')}")


if __name__ == "__main__":
    main()
