#!/usr/bin/env python3
"""Emit JSON and RDF metadata files for a MkDocs site."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import yaml


FRONTMATTER_BOUNDARY = "---"


def extract_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    if not text.startswith(FRONTMATTER_BOUNDARY):
        return {}, text
    parts = text.split(FRONTMATTER_BOUNDARY, 2)
    if len(parts) < 3:
        return {}, text
    fm_text = parts[1].strip()
    body = parts[2]
    try:
        data = yaml.safe_load(fm_text) or {}
    except yaml.YAMLError:
        data = {}
    if not isinstance(data, dict):
        data = {}
    return data, body


def first_h1(text: str) -> str | None:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip() or None
    return None


def parse_author_name(author: Any) -> str | None:
    if isinstance(author, str):
        return author.strip() or None
    if isinstance(author, dict):
        literal = author.get("literal")
        if isinstance(literal, str) and literal.strip():
            return literal.strip()
        family = author.get("family")
        given = author.get("given")
        if isinstance(family, str) and isinstance(given, str):
            return f"{family.strip()}, {given.strip()}"
        if isinstance(family, str):
            return family.strip()
        if isinstance(given, str):
            return given.strip()
    return None


def parse_authors(meta: dict[str, Any]) -> list[str]:
    raw = meta.get("authors") or meta.get("author") or []
    names: list[str] = []
    if isinstance(raw, list):
        for item in raw:
            name = parse_author_name(item)
            if name:
                names.append(name)
    else:
        name = parse_author_name(raw)
        if name:
            names.append(name)
    return names


def parse_tags(meta: dict[str, Any]) -> list[str]:
    raw = meta.get("tags") or []
    if isinstance(raw, list):
        return [str(tag).strip() for tag in raw if str(tag).strip()]
    if isinstance(raw, str):
        return [raw.strip()] if raw.strip() else []
    return []


def compute_url(relative: Path) -> str:
    if relative.name == "index.md":
        if relative.parent == Path("."):
            return "/"
        return f"/{relative.parent.as_posix()}/"
    return f"/{relative.with_suffix('').as_posix()}/"


def build_page_record(path: Path, docs_dir: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8", errors="ignore")
    meta, body = extract_frontmatter(text)
    title = meta.get("title") or meta.get("name") or first_h1(body) or path.stem
    relative = path.relative_to(docs_dir)
    url = compute_url(relative)
    return {
        "id": meta.get("id"),
        "title": title,
        "description": meta.get("description"),
        "date_created": meta.get("date-created") or meta.get("date"),
        "date_updated": meta.get("date-updated"),
        "authors": parse_authors(meta),
        "tags": parse_tags(meta),
        "license": meta.get("license"),
        "kind": meta.get("kind"),
        "url": url,
        "source": f"/{relative.as_posix()}",
    }


def escape_ttl(value: str) -> str:
    return value.replace("\\", "\\\\").replace("\"", "\\\"")


def emit_ttl(pages: list[dict[str, Any]], base: str) -> str:
    lines = [
        f"@base <{base}> .",
        "@prefix schema: <https://schema.org/> .",
        "@prefix dcterms: <http://purl.org/dc/terms/> .",
        "",
    ]
    for page in pages:
        url = page.get("url")
        if not url:
            continue
        subject = f"<{url}>"
        lines.append(f"{subject} a schema:CreativeWork ;")
        if page.get("title"):
            lines.append(f'  schema:name "{escape_ttl(str(page["title"]))}" ;')
        if page.get("id"):
            lines.append(f'  dcterms:identifier "{escape_ttl(str(page["id"]))}" ;')
        if page.get("description"):
            lines.append(f'  schema:description "{escape_ttl(str(page["description"]))}" ;')
        if page.get("date_created"):
            lines.append(f'  dcterms:created "{escape_ttl(str(page["date_created"]))}" ;')
        if page.get("date_updated"):
            lines.append(f'  dcterms:modified "{escape_ttl(str(page["date_updated"]))}" ;')
        if page.get("license"):
            lines.append(f'  schema:license "{escape_ttl(str(page["license"]))}" ;')
        tags = page.get("tags") or []
        if tags:
            lines.append(f'  schema:keywords "{escape_ttl(", ".join(tags))}" ;')
        authors = page.get("authors") or []
        if authors:
            if len(authors) == 1:
                lines.append(
                    f'  schema:author [ a schema:Person ; schema:name "{escape_ttl(authors[0])}" ] ;'
                )
            else:
                author_nodes = [
                    f'[ a schema:Person ; schema:name "{escape_ttl(author)}" ]'
                    for author in authors
                ]
                lines.append(f"  schema:author {', '.join(author_nodes)} ;")
        lines[-1] = lines[-1].rstrip(" ;") + " ."
        lines.append("")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Emit JSON and RDF metadata files for a MkDocs site.",
    )
    parser.add_argument("config", type=Path, help="Path to mkdocs.yml")
    args = parser.parse_args()

    config_path = args.config.resolve()
    if not config_path.exists():
        raise SystemExit(f"missing mkdocs config: {config_path}")

    config = yaml.safe_load(config_path.read_text(encoding="utf-8")) or {}
    base_dir = config_path.parent
    docs_dir = base_dir / config.get("docs_dir", "docs")
    site_dir = base_dir / config.get("site_dir", "site")
    site_url = config.get("site_url") or "/"

    pages: list[dict[str, Any]] = []
    for path in docs_dir.rglob("*.md"):
        if "products" in path.parts:
            continue
        pages.append(build_page_record(path, docs_dir))

    api_dir = site_dir / "api"
    api_dir.mkdir(parents=True, exist_ok=True)

    pages_path = api_dir / "pages.json"
    pages_path.write_text(json.dumps(pages, indent=2, sort_keys=True), encoding="utf-8")

    tags: dict[str, list[str]] = {}
    for page in pages:
        for tag in page.get("tags") or []:
            tags.setdefault(tag, []).append(page.get("url", ""))
    tags_payload = [
        {"tag": tag, "count": len(urls), "pages": urls} for tag, urls in sorted(tags.items())
    ]
    tags_path = api_dir / "tags.json"
    tags_path.write_text(json.dumps(tags_payload, indent=2, sort_keys=True), encoding="utf-8")

    ttl_path = api_dir / "pages.ttl"
    ttl_path.write_text(emit_ttl(pages, site_url), encoding="utf-8")


if __name__ == "__main__":
    main()
