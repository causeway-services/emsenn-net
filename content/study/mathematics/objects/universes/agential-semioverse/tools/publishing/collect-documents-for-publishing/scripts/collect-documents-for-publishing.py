#!/usr/bin/env python3
"""Collect publishable Markdown files into a MkDocs docs_dir."""

from __future__ import annotations

import argparse
import re
import shutil
from pathlib import Path
from typing import Iterable

import yaml


FRONTMATTER_BOUNDARY = "---"
PUBLICATIONS_KEY = "publications"
DEPENDENCIES_KEY = "dependencies"
REQUIRED_CONFIG_KEYS = ("publication_name", "publication_status", "docs_dir")
SKIP_SOURCE_FILENAMES = {"mkdocs.yml", "publication.yml"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Collect Markdown files whose publications list matches a "
            "publication_name/publication_status pair from a publication config."
        ),
    )
    parser.add_argument(
        "config",
        type=Path,
        help="Path to publication.yml",
    )
    parser.add_argument(
        "--source",
        type=Path,
        default=Path("library"),
        help="Source directory to scan (default: ./library)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print matches without copying files",
    )
    return parser.parse_args()


def iter_markdown_files(root: Path) -> Iterable[Path]:
    return root.rglob("*.md")


def read_frontmatter_lines(path: Path) -> list[str]:
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        text = path.read_text(encoding="utf-8", errors="ignore")
    lines = text.splitlines()
    if not lines or lines[0].strip() != FRONTMATTER_BOUNDARY:
        return []
    for index in range(1, len(lines)):
        if lines[index].strip() == FRONTMATTER_BOUNDARY:
            return lines[1:index]
    return []


def read_frontmatter_data(path: Path) -> dict[str, object] | None:
    frontmatter_lines = read_frontmatter_lines(path)
    if not frontmatter_lines:
        return None
    try:
        data = yaml.safe_load("\n".join(frontmatter_lines))
    except yaml.YAMLError:
        return None
    if not isinstance(data, dict):
        return None
    return data


def parse_inline_publications(value: str) -> list[str]:
    if value == "[]":
        return []
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        if not inner:
            return []
        return [item.strip() for item in inner.split(",") if item.strip()]
    return [value]


def parse_publications(lines: list[str]) -> list[str]:
    publications: list[str] = []
    in_publications = False
    for line in lines:
        if not in_publications:
            match = re.match(rf"^{PUBLICATIONS_KEY}\s*:(.*)$", line)
            if match:
                inline = match.group(1).strip()
                if inline:
                    publications.extend(parse_inline_publications(inline))
                in_publications = True
            continue

        if line.strip() == "":
            continue

        if re.match(r"^\S", line) and not line.lstrip().startswith("-"):
            break

        item_match = re.match(r"^\s*-\s*(.+)$", line)
        if item_match:
            item = item_match.group(1).strip()
            if item:
                publications.append(item)

    return publications


def parse_dependencies(lines: list[str]) -> list[str]:
    dependencies: list[str] = []
    in_dependencies = False
    for line in lines:
        if not in_dependencies:
            match = re.match(rf"^{DEPENDENCIES_KEY}\s*:(.*)$", line)
            if match:
                inline = match.group(1).strip()
                if inline:
                    dependencies.extend(parse_inline_publications(inline))
                in_dependencies = True
            continue

        if line.strip() == "":
            continue

        if re.match(r"^\S", line) and not line.lstrip().startswith("-"):
            break

        item_match = re.match(r"^\s*-\s*(.+)$", line)
        if item_match:
            item = item_match.group(1).strip()
            if item:
                dependencies.append(item)

    return dependencies


def split_publication_item(item: str) -> tuple[str, str | None]:
    if ":" not in item:
        return item.strip(), None
    key, value = item.split(":", 1)
    return key.strip(), value.strip()


def matches_publication(
    publications: list[str], publication: str, status: str
) -> bool:
    for item in publications:
        key, value = split_publication_item(item)
        if key == publication and value == status:
            return True
    return False


def strip_quotes(value: str) -> str:
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def parse_publication_config(path: Path) -> dict[str, str]:
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        text = path.read_text(encoding="utf-8", errors="ignore")

    config: dict[str, str] = {}
    for line in text.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith(" ") or line.startswith("\t"):
            continue
        match = re.match(r"^([A-Za-z0-9_-]+)\s*:\s*(.+)$", line)
        if not match:
            continue
        key = match.group(1).strip()
        raw_value = match.group(2).strip()
        value = strip_quotes(raw_value)
        config[key] = value

    return config


def parse_config_list(config: dict[str, str], key: str) -> list[str]:
    raw = config.get(key)
    if not raw:
        return []
    if raw == "[]":
        return []
    if raw.startswith("[") and raw.endswith("]"):
        inner = raw[1:-1].strip()
        if not inner:
            return []
        items = [item.strip() for item in inner.split(",") if item.strip()]
    else:
        items = [item.strip() for item in raw.split(",") if item.strip()]
    return [strip_quotes(item) for item in items]


def resolve_docs_dir(config: dict[str, str], config_path: Path) -> Path:
    docs_dir = config["docs_dir"]
    docs_path = Path(docs_dir)
    if not docs_path.is_absolute():
        base_dir = resolve_output_root_dir(config, config_path) or config_path.parent
        docs_path = (base_dir / docs_path).resolve()
    return docs_path


def resolve_output_root_dir(
    config: dict[str, str], config_path: Path
) -> Path | None:
    output_root = config.get("output_root_dir")
    if not output_root:
        return None
    output_path = Path(output_root)
    if not output_path.is_absolute():
        output_path = (config_path.parent / output_path).resolve()
    return output_path


def is_within(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
    except ValueError:
        return False
    return True


def should_skip_publishable(
    path: Path, config_path: Path, output_root_dir: Path | None
) -> bool:
    config_root = config_path.parent.resolve()
    if is_within(path, config_root):
        return True
    if output_root_dir and is_within(path, output_root_dir):
        return True
    return False


def copy_extra_sources(
    extra_sources: list[Path], docs_dir: Path, dry_run: bool
) -> None:
    for source in extra_sources:
        if not source.exists():
            raise SystemExit(f"missing extra source directory: {source}")
        if not source.is_dir():
            raise SystemExit(f"extra source is not a directory: {source}")
        if is_within(source, docs_dir):
            continue

        for path in source.rglob("*"):
            if path.is_dir():
                continue
            if path.name in SKIP_SOURCE_FILENAMES:
                continue
            relative_path = path.relative_to(source)
            destination_path = docs_dir / relative_path
            if dry_run:
                print(f"would copy extra source: {path} -> {destination_path}")
                continue
            destination_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(path, destination_path)


def copy_matches(
    source_root: Path,
    docs_dir: Path,
    publication: str,
    status: str,
    dry_run: bool,
    config_path: Path,
    output_root_dir: Path | None,
) -> int:
    match_count = 0
    for path in iter_markdown_files(source_root):
        if should_skip_publishable(path, config_path, output_root_dir):
            continue
        if is_within(path, docs_dir):
            continue
        frontmatter = read_frontmatter_lines(path)
        if not frontmatter:
            continue
        publications = parse_publications(frontmatter)
        if not publications:
            continue
        if not matches_publication(publications, publication, status):
            continue

        relative_path = path.relative_to(source_root)
        dependencies = parse_dependencies(frontmatter)
        if should_duplicate_as_index(source_root, relative_path):
            destination_path = docs_dir / relative_path.parent / "index.md"
        else:
            destination_path = docs_dir / relative_path
        match_count += 1

        if dry_run:
            print(f"match: {path} -> {destination_path}")
            continue

        destination_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, destination_path)
        copy_dependencies(
            dependencies=dependencies,
            source_root=source_root,
            relative_path=relative_path,
            docs_dir=docs_dir,
            dry_run=dry_run,
        )

    return match_count


def copy_dependencies(
    dependencies: list[str],
    source_root: Path,
    relative_path: Path,
    docs_dir: Path,
    dry_run: bool,
) -> None:
    if not dependencies:
        return
    base_dir = (source_root / relative_path.parent).resolve()
    for dependency in dependencies:
        if dependency.startswith(("http://", "https://", "/")):
            continue
        dependency_path = (base_dir / dependency).resolve()
        if not dependency_path.exists():
            raise SystemExit(f"missing dependency: {dependency_path}")
        destination_path = docs_dir / relative_path.parent / dependency
        if dry_run:
            print(f"would copy dependency: {dependency_path} -> {destination_path}")
            continue
        destination_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(dependency_path, destination_path)


def iter_reference_entries(docs_dir: Path) -> dict[str, dict[str, object]]:
    references: dict[str, dict[str, object]] = {}
    for path in docs_dir.rglob("*.md"):
        data = read_frontmatter_data(path)
        if not data:
            continue
        items = data.get("references")
        if not isinstance(items, list):
            continue
        for item in items:
            if not isinstance(item, dict):
                continue
            key = item.get("id")
            if not key or not isinstance(key, str):
                continue
            if key not in references:
                references[key] = item
    return references


def format_author_list(authors: list[object]) -> str | None:
    names: list[str] = []
    for author in authors:
        if not isinstance(author, dict):
            continue
        literal = author.get("literal")
        if isinstance(literal, str) and literal:
            names.append(literal)
            continue
        family = author.get("family")
        given = author.get("given")
        if isinstance(family, str) and isinstance(given, str):
            names.append(f"{family}, {given}")
        elif isinstance(family, str):
            names.append(family)
        elif isinstance(given, str):
            names.append(given)
    if not names:
        return None
    return " and ".join(names)


def normalize_text(value: object) -> str | None:
    if not isinstance(value, str):
        return None
    return " ".join(value.split())


def map_reference_type(value: object) -> str:
    if not isinstance(value, str):
        return "misc"
    mapping = {
        "article-journal": "article",
        "report": "misc",
        "webpage": "misc",
    }
    return mapping.get(value, "misc")


def parse_issued_year(issued: object) -> tuple[str | None, str | None, str | None]:
    if not isinstance(issued, list) or not issued:
        return None, None, None
    entry = issued[0]
    if not isinstance(entry, dict):
        return None, None, None
    year = entry.get("year")
    month = entry.get("month")
    day = entry.get("day")
    year_str = str(year) if year is not None else None
    month_str = str(month) if month is not None else None
    day_str = str(day) if day is not None else None
    return year_str, month_str, day_str


def build_bibtex_entry(key: str, item: dict[str, object]) -> str:
    entry_type = map_reference_type(item.get("type"))
    fields: dict[str, str] = {}

    title = normalize_text(item.get("title"))
    if title:
        fields["title"] = title

    authors = item.get("author")
    if isinstance(authors, list):
        author_text = format_author_list(authors)
        if author_text:
            fields["author"] = author_text

    year, month, day = parse_issued_year(item.get("issued"))
    if year:
        fields["year"] = year
    if month:
        fields["month"] = month
    if day:
        fields["day"] = day

    journal = normalize_text(item.get("container-title"))
    if journal:
        fields["journal"] = journal

    volume = normalize_text(item.get("volume"))
    if volume:
        fields["volume"] = volume

    number = normalize_text(item.get("issue"))
    if number:
        fields["number"] = number

    pages = normalize_text(item.get("page"))
    if pages:
        fields["pages"] = pages

    doi = normalize_text(item.get("DOI"))
    if doi:
        fields["doi"] = doi

    url = normalize_text(item.get("URL"))
    if url:
        fields["url"] = url

    lines = [f"@{entry_type}{{{key},"]
    for field_key in sorted(fields.keys()):
        value = fields[field_key].replace("{", "\\{").replace("}", "\\}")
        lines.append(f"  {field_key} = {{{value}}},")
    lines.append("}")
    return "\n".join(lines)


def write_references_bib(
    docs_dir: Path, output_name: str = "references.bib"
) -> None:
    references = iter_reference_entries(docs_dir)
    if not references:
        return
    entries = []
    for key in sorted(references.keys()):
        entries.append(build_bibtex_entry(key, references[key]))
    output_path = docs_dir / output_name
    output_path.write_text("\n\n".join(entries) + "\n", encoding="utf-8")


def main() -> None:
    args = parse_args()
    source_root = args.source.resolve()
    config_path = args.config.resolve()

    if not source_root.exists():
        raise SystemExit(f"missing source directory: {source_root}")
    if not config_path.exists():
        raise SystemExit(f"missing publication config: {config_path}")

    config = parse_publication_config(config_path)
    missing_keys = [key for key in REQUIRED_CONFIG_KEYS if key not in config]
    if missing_keys:
        missing = ", ".join(missing_keys)
        raise SystemExit(f"missing publication config keys: {missing}")

    docs_dir = resolve_docs_dir(config, config_path)
    if not docs_dir.exists():
        docs_dir.mkdir(parents=True, exist_ok=True)

    output_root_dir = resolve_output_root_dir(config, config_path)
    if output_root_dir:
        output_root_dir.mkdir(parents=True, exist_ok=True)
        mkdocs_path = config_path.parent / "mkdocs.yml"
        if mkdocs_path.exists():
            destination = output_root_dir / "mkdocs.yml"
            if args.dry_run:
                print(f"would copy mkdocs.yml: {mkdocs_path} -> {destination}")
            else:
                shutil.copy2(mkdocs_path, destination)
        macros_path = config_path.parent / "main.py"
        if macros_path.exists():
            destination = output_root_dir / "main.py"
            if args.dry_run:
                print(f"would copy main.py: {macros_path} -> {destination}")
            else:
                shutil.copy2(macros_path, destination)

    extra_sources: list[Path] = []
    extra_sources.extend(parse_config_list(config, "extra_source_dirs"))
    extra_source = config.get("extra_source_dir")
    if extra_source:
        extra_sources.append(extra_source)

    extra_source_paths = []
    for source in extra_sources:
        source_path = Path(source)
        if not source_path.is_absolute():
            source_path = (config_path.parent / source_path).resolve()
        extra_source_paths.append(source_path)
    if extra_source_paths:
        copy_extra_sources(extra_source_paths, docs_dir, args.dry_run)

    overrides_dir = config.get("overrides_dir")
    if overrides_dir:
        source_overrides = Path(overrides_dir)
        if not source_overrides.is_absolute():
            source_overrides = (config_path.parent / source_overrides).resolve()
    else:
        source_overrides = config_path.parent / "overrides"

    destination_overrides = docs_dir / "overrides"
    if source_overrides.exists():
        if source_overrides.resolve() != destination_overrides.resolve():
            if args.dry_run:
                print(
                    "would copy overrides: "
                    f"{source_overrides} -> {destination_overrides}"
                )
            else:
                shutil.copytree(
                    source_overrides,
                    destination_overrides,
                    dirs_exist_ok=True,
                )
        if output_root_dir:
            output_overrides = output_root_dir / "overrides"
            if source_overrides.resolve() != output_overrides.resolve():
                if args.dry_run:
                    print(
                        "would copy overrides: "
                        f"{source_overrides} -> {output_overrides}"
                    )
                else:
                    shutil.copytree(
                        source_overrides,
                        output_overrides,
                        dirs_exist_ok=True,
                    )

    count = copy_matches(
        source_root=source_root,
        docs_dir=docs_dir,
        publication=config["publication_name"],
        status=config["publication_status"],
        dry_run=args.dry_run,
        config_path=config_path,
        output_root_dir=output_root_dir,
    )

    if not args.dry_run:
        write_references_bib(docs_dir)

    action = "Would collect" if args.dry_run else "Collected"
    print(f"{action} {count} document(s) into {docs_dir}")


def should_duplicate_as_index(source_root: Path, relative_path: Path) -> bool:
    if relative_path.suffix != ".md":
        return False
    if len(relative_path.parts) < 2:
        return False
    if relative_path.name == "index.md":
        return False

    stub = relative_path.parent.name
    if relative_path.stem != stub:
        return False

    source_index = source_root / relative_path.parent / "index.md"
    return not source_index.exists()


if __name__ == "__main__":
    main()
