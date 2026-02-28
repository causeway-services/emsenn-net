#!/usr/bin/env python3
"""Search the library content."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

import yaml


def find_library_root(explicit: str | None = None) -> Path:
    if explicit:
        return Path(explicit).resolve()
    for parent in [Path.cwd(), *Path.cwd().parents, *Path(__file__).resolve().parents]:
        if parent.name == "library":
            return parent
    raise RuntimeError("library root not found; pass --library-root")


LIBRARY_ROOT = find_library_root()
FRONTMATTER_BOUNDARY = "---"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Search the library content")
    parser.add_argument(
        "--library-root",
        type=str,
        default=None,
        help="Path to the library/ directory (optional)",
    )
    parser.add_argument(
        "--query",
        type=str,
        required=True,
        help="Search query string",
    )
    parser.add_argument(
        "--scope",
        choices=["all", "content", "frontmatter", "title"],
        default="all",
        help="Where to search",
    )
    parser.add_argument(
        "--path",
        type=str,
        default="",
        help="Path to limit search to",
    )
    parser.add_argument(
        "--kind",
        type=str,
        default=None,
        help="Filter by document kind",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=20,
        help="Maximum number of results",
    )
    parser.add_argument(
        "--context-lines",
        type=int,
        default=2,
        help="Context lines around matches",
    )
    parser.add_argument(
        "--output",
        choices=["json", "text"],
        default="json",
        help="Output format",
    )
    return parser.parse_args()


def resolve_search_root(relative_path: str) -> Path:
    """Resolve search root path."""
    if relative_path:
        full_path = (LIBRARY_ROOT / relative_path).resolve()
    else:
        full_path = LIBRARY_ROOT
    
    if not str(full_path).startswith(str(LIBRARY_ROOT)):
        raise ValueError(f"Path escapes library root: {relative_path}")
    
    return full_path


def read_frontmatter(path: Path) -> tuple[dict[str, Any] | None, str]:
    """Read YAML frontmatter and content from a markdown file."""
    try:
        text = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return None, ""
    
    lines = text.splitlines()
    if not lines or lines[0].strip() != FRONTMATTER_BOUNDARY:
        return None, text
    
    for index in range(1, len(lines)):
        if lines[index].strip() == FRONTMATTER_BOUNDARY:
            frontmatter_text = "\n".join(lines[1:index])
            content = "\n".join(lines[index + 1:])
            try:
                data = yaml.safe_load(frontmatter_text)
                if isinstance(data, dict):
                    return data, content
            except yaml.YAMLError:
                pass
            return None, text
    
    return None, text


def search_file(
    path: Path,
    query: str,
    scope: str,
    context_lines: int,
    kind_filter: str | None,
) -> dict[str, Any] | None:
    """Search a single file."""
    frontmatter, content = read_frontmatter(path)
    
    if kind_filter:
        if not frontmatter or frontmatter.get("kind") != kind_filter:
            return None
    
    query_lower = query.lower()
    matches: list[dict[str, Any]] = []
    score = 0.0
    
    if scope in ("all", "frontmatter", "title"):
        if frontmatter:
            title = frontmatter.get("title") or frontmatter.get("name") or ""
            if query_lower in title.lower():
                score += 2.0
                matches.append({
                    "field": "title",
                    "text": title,
                })
            
            if scope in ("all", "frontmatter"):
                for key in ["description", "summary", "id"]:
                    value = frontmatter.get(key)
                    if isinstance(value, str) and query_lower in value.lower():
                        score += 1.0
                        matches.append({
                            "field": key,
                            "text": value,
                        })
                
                tags = frontmatter.get("tags", [])
                if isinstance(tags, list):
                    for tag in tags:
                        if isinstance(tag, str) and query_lower in tag.lower():
                            score += 0.5
                            matches.append({
                                "field": "tags",
                                "text": tag,
                            })
    
    if scope in ("all", "content"):
        lines = content.splitlines()
        for i, line in enumerate(lines):
            if query_lower in line.lower():
                score += 0.5
                
                start = max(0, i - context_lines)
                end = min(len(lines), i + context_lines + 1)
                
                matches.append({
                    "line": i + 1,
                    "text": line.strip(),
                    "context_before": "\n".join(lines[start:i]) if start < i else "",
                    "context_after": "\n".join(lines[i+1:end]) if i + 1 < end else "",
                })
    
    if not matches:
        return None
    
    return {
        "path": str(path.relative_to(LIBRARY_ROOT)),
        "score": round(score, 2),
        "matches": matches[:10],
        "frontmatter": {
            k: frontmatter.get(k)
            for k in ["id", "name", "title", "kind", "description", "summary"]
            if frontmatter and k in frontmatter
        } if frontmatter else None,
    }


def search_library(
    query: str,
    scope: str,
    search_root: Path,
    kind_filter: str | None,
    context_lines: int,
    limit: int,
) -> list[dict[str, Any]]:
    """Search the library for matching content."""
    results: list[dict[str, Any]] = []
    
    for path in search_root.rglob("*.md"):
        if path.name.startswith("."):
            continue
        
        result = search_file(path, query, scope, context_lines, kind_filter)
        if result:
            results.append(result)
    
    results.sort(key=lambda x: x["score"], reverse=True)
    
    return results[:limit]


def main() -> None:
    args = parse_args()
    global LIBRARY_ROOT
    LIBRARY_ROOT = find_library_root(args.library_root)
    
    try:
        search_root = resolve_search_root(args.path)
    except ValueError as e:
        print(json.dumps({"error": str(e)}))
        return
    
    if not search_root.exists():
        print(json.dumps({"error": f"Path not found: {args.path}"}))
        return
    
    results = search_library(
        query=args.query,
        scope=args.scope,
        search_root=search_root,
        kind_filter=args.kind,
        context_lines=args.context_lines,
        limit=args.limit,
    )
    
    output = {
        "query": args.query,
        "total_matches": len(results),
        "results": results,
    }
    
    if args.output == "json":
        print(json.dumps(output, indent=2))
    else:
        print(f"Found {len(results)} matches for '{args.query}':")
        print()
        for result in results:
            print(f"  [{result['score']:.1f}] {result['path']}")
            if result.get("frontmatter", {}).get("title"):
                print(f"        {result['frontmatter']['title']}")


if __name__ == "__main__":
    main()
