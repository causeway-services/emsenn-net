#!/usr/bin/env python3
"""Browse the library filesystem."""

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
    parser = argparse.ArgumentParser(description="Browse the library filesystem")
    parser.add_argument(
        "--library-root",
        type=str,
        default=None,
        help="Path to the library/ directory (optional)",
    )
    parser.add_argument(
        "--action",
        choices=["list", "read", "metadata"],
        required=True,
        help="Action to perform",
    )
    parser.add_argument(
        "--path",
        type=str,
        default="",
        help="Path relative to library root",
    )
    parser.add_argument(
        "--recursive",
        action="store_true",
        help="List recursively",
    )
    parser.add_argument(
        "--max-depth",
        type=int,
        default=3,
        help="Maximum depth for recursive listing",
    )
    parser.add_argument(
        "--include-hidden",
        action="store_true",
        help="Include hidden files",
    )
    parser.add_argument(
        "--output",
        choices=["json", "text"],
        default="json",
        help="Output format",
    )
    return parser.parse_args()


def resolve_path(relative_path: str) -> Path:
    """Resolve a relative path to an absolute path within the library."""
    if relative_path:
        full_path = (LIBRARY_ROOT / relative_path).resolve()
    else:
        full_path = LIBRARY_ROOT
    
    if not str(full_path).startswith(str(LIBRARY_ROOT)):
        raise ValueError(f"Path escapes library root: {relative_path}")
    
    return full_path


def list_directory(
    path: Path,
    recursive: bool = False,
    max_depth: int = 3,
    include_hidden: bool = False,
    current_depth: int = 0,
) -> list[dict[str, Any]]:
    """List directory contents."""
    entries = []
    
    if not path.exists():
        return entries
    
    if not path.is_dir():
        return [make_entry(path)]
    
    for item in sorted(path.iterdir()):
        if not include_hidden and item.name.startswith("."):
            continue
        
        entry = make_entry(item)
        entries.append(entry)
        
        if recursive and item.is_dir() and current_depth < max_depth:
            children = list_directory(
                item,
                recursive=True,
                max_depth=max_depth,
                include_hidden=include_hidden,
                current_depth=current_depth + 1,
            )
            entry["children"] = children
    
    return entries


def make_entry(path: Path) -> dict[str, Any]:
    """Create an entry dict for a path."""
    relative = path.relative_to(LIBRARY_ROOT)
    entry: dict[str, Any] = {
        "path": str(relative),
        "name": path.name,
        "type": "directory" if path.is_dir() else "file",
    }
    
    if path.is_file():
        entry["extension"] = path.suffix.lstrip(".")
        
        if path.suffix == ".md":
            frontmatter = read_frontmatter(path)
            if frontmatter:
                entry["frontmatter"] = {
                    k: frontmatter.get(k)
                    for k in ["id", "name", "title", "kind", "description", "summary"]
                    if k in frontmatter
                }
    
    return entry


def read_frontmatter(path: Path) -> dict[str, Any] | None:
    """Read YAML frontmatter from a markdown file."""
    try:
        text = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return None
    
    lines = text.splitlines()
    if not lines or lines[0].strip() != FRONTMATTER_BOUNDARY:
        return None
    
    for index in range(1, len(lines)):
        if lines[index].strip() == FRONTMATTER_BOUNDARY:
            frontmatter_text = "\n".join(lines[1:index])
            try:
                data = yaml.safe_load(frontmatter_text)
                if isinstance(data, dict):
                    return data
            except yaml.YAMLError:
                pass
            break
    
    return None


def read_file(path: Path) -> str:
    """Read file contents."""
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(encoding="utf-8", errors="replace")


def get_metadata(path: Path) -> dict[str, Any]:
    """Get metadata from a file."""
    result: dict[str, Any] = {
        "path": str(path.relative_to(LIBRARY_ROOT)),
        "name": path.name,
        "exists": path.exists(),
    }
    
    if not path.exists():
        return result
    
    result["type"] = "directory" if path.is_dir() else "file"
    
    if path.is_file():
        result["extension"] = path.suffix.lstrip(".")
        result["size"] = path.stat().st_size
        
        if path.suffix == ".md":
            frontmatter = read_frontmatter(path)
            if frontmatter:
                result["frontmatter"] = frontmatter
    
    return result


def main() -> None:
    args = parse_args()
    global LIBRARY_ROOT
    LIBRARY_ROOT = find_library_root(args.library_root)
    
    try:
        path = resolve_path(args.path)
    except ValueError as e:
        print(json.dumps({"error": str(e)}))
        return
    
    if args.action == "list":
        result = list_directory(
            path,
            recursive=args.recursive,
            max_depth=args.max_depth,
            include_hidden=args.include_hidden,
        )
        output = {"entries": result}
    elif args.action == "read":
        if not path.exists():
            output = {"error": f"File not found: {args.path}"}
        elif path.is_dir():
            output = {"error": f"Cannot read directory: {args.path}"}
        else:
            content = read_file(path)
            output = {"content": content}
    elif args.action == "metadata":
        output = get_metadata(path)
    else:
        output = {"error": f"Unknown action: {args.action}"}
    
    if args.output == "json":
        print(json.dumps(output, indent=2))
    else:
        if "error" in output:
            print(f"Error: {output['error']}")
        elif "content" in output:
            print(output["content"])
        elif "entries" in output:
            for entry in output["entries"]:
                prefix = "d" if entry["type"] == "directory" else "f"
                print(f"[{prefix}] {entry['path']}")
        else:
            for key, value in output.items():
                print(f"{key}: {value}")


if __name__ == "__main__":
    main()
