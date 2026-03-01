#!/usr/bin/env python3
"""Fix lesson file titles, aliases, and filenames across the vault.

Changes:
1. Strip "Lesson N: " / "Lesson N, " prefixes from titles
2. Apply Title Case to all titles
3. Ensure alias matches the corrected title
4. Rename files by dropping the lesson-N- prefix
5. Print a report of all changes for review
"""

import os
import re
import glob
import sys

# Script lives at content/slop/tools/fix-lessons.py; content/ is 2 levels up
_script_dir = os.path.dirname(os.path.abspath(__file__))
CONTENT_ROOT = os.path.normpath(os.path.join(_script_dir, '..', '..'))

# Words that stay lowercase in Title Case (unless first word)
SMALL_WORDS = {
    'a', 'an', 'the', 'and', 'but', 'or', 'for', 'nor',
    'in', 'on', 'at', 'to', 'by', 'of', 'with', 'is', 'as',
    'vs', 'via',
}

# Words/abbreviations that should keep specific casing
PRESERVE_CASE = {
    'fdm': 'FDM', 'fff': 'FFF', '3d': '3D',
    'oop': 'OOP', 'rpg': 'RPG', 'ttrpg': 'TTRPG',
    'activitypub': 'ActivityPub', 'mkdocs': 'MkDocs',
    'gnoponemacs': 'GnoponEmacs', 'github': 'GitHub',
    'git': 'Git', 'mastodon': 'Mastodon',
    'foucault': 'Foucault', 'kripke': 'Kripke',
    'frege': 'Frege', 'bayes': 'Bayes',
    'beancount': 'Beancount',
    'heyting': 'Heyting',
    # Math terms with specific formatting
    '(infinity,1)-topoi': '(Infinity,1)-Topoi',
}


def title_case(s: str) -> str:
    """Apply Title Case with small-word and preserve-case rules."""
    # Handle the special compound case
    lower = s.lower()
    if lower in PRESERVE_CASE:
        return PRESERVE_CASE[lower]

    words = s.split()
    result = []
    for i, word in enumerate(words):
        word_lower = word.lower().rstrip('?:,;.')
        punctuation = word[len(word_lower):]  # trailing punctuation

        # Check preserve-case first (whole word match)
        if word_lower in PRESERVE_CASE:
            result.append(PRESERVE_CASE[word_lower] + punctuation)
        elif i == 0:
            # First word always capitalized
            result.append(word[0].upper() + word[1:] if word else word)
        elif word_lower in SMALL_WORDS:
            result.append(word.lower())
        else:
            # Capitalize first letter, preserve rest for hyphenated words
            parts = word.split('-')
            capped_parts = []
            for j, part in enumerate(parts):
                part_lower = part.lower().rstrip('?:,;.')
                part_punct = part[len(part_lower):] if part_lower else ''
                if part_lower in PRESERVE_CASE:
                    capped_parts.append(PRESERVE_CASE[part_lower] + part_punct)
                elif part:
                    capped_parts.append(part[0].upper() + part[1:])
                else:
                    capped_parts.append(part)
            result.append('-'.join(capped_parts))

    return ' '.join(result)


def strip_lesson_prefix(title: str) -> str:
    """Remove 'Lesson N: ' or 'Lesson N, ' prefix."""
    m = re.match(r'^Lesson\s+\d+[,:]\s*', title, re.IGNORECASE)
    if m:
        return title[m.end():]
    return title


def new_filename(old_name: str) -> str:
    """Drop lesson-N- prefix from filename."""
    m = re.match(r'^lesson-\d+-(.+)$', old_name)
    if m:
        return m.group(1)
    return old_name


def parse_frontmatter(content: str):
    """Parse YAML frontmatter, return (frontmatter_text, body, title, aliases)."""
    if not content.startswith('---'):
        return None, content, None, None

    end = content.find('\n---', 3)
    if end == -1:
        return None, content, None, None

    fm = content[3:end].strip()
    body = content[end + 4:]  # skip \n---

    # Extract title
    title_match = re.search(r'^title:\s*"?([^"\n]+)"?\s*$', fm, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else None

    # Extract aliases
    aliases = []
    alias_match = re.search(r'^aliases:\s*\n((?:\s+-\s+.*\n)*)', fm, re.MULTILINE)
    if alias_match:
        for a in re.finditer(r'^\s+-\s+"?([^"\n]+)"?\s*$', alias_match.group(1), re.MULTILINE):
            aliases.append(a.group(1).strip())

    return fm, body, title, aliases


def rebuild_frontmatter(fm: str, new_title: str) -> str:
    """Replace title and aliases in frontmatter text."""
    # Replace title
    fm = re.sub(
        r'^(title:\s*)"?[^"\n]+"?\s*$',
        f'\\1"{new_title}"',
        fm,
        flags=re.MULTILINE
    )

    # Replace aliases block with single alias matching title
    alias_pattern = r'^aliases:\s*\n(?:\s+-\s+.*\n)*'
    alias_replacement = f'aliases:\n  - "{new_title}"\n'
    if re.search(alias_pattern, fm, re.MULTILINE):
        fm = re.sub(alias_pattern, alias_replacement, fm, flags=re.MULTILINE)
    else:
        # Add aliases after title line
        fm = re.sub(
            r'^(title:\s*"[^"]*")\s*$',
            f'\\1\naliases:\n  - "{new_title}"',
            fm,
            flags=re.MULTILINE
        )

    return fm


def process_file(filepath: str, dry_run: bool = False):
    """Process a single lesson file. Returns (old_path, new_path, old_title, new_title) or None."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    fm, body, title, aliases = parse_frontmatter(content)
    if fm is None or title is None:
        print(f"  SKIP (no frontmatter/title): {filepath}", file=sys.stderr)
        return None

    # Fix title
    stripped = strip_lesson_prefix(title)
    new_title = title_case(stripped)

    # Compute new filename
    dirname = os.path.dirname(filepath)
    old_name = os.path.basename(filepath)
    new_name = new_filename(old_name)
    new_path = os.path.join(dirname, new_name)

    changed_title = (new_title != title)
    changed_file = (new_name != old_name)
    changed_alias = True  # Always ensure alias matches

    if not changed_title and not changed_file:
        # Check if alias needs fixing
        if aliases == [new_title]:
            return None  # Nothing to do

    if dry_run:
        changes = []
        if changed_title:
            changes.append(f'title: "{title}" -> "{new_title}"')
        if changed_file:
            changes.append(f'file: {old_name} -> {new_name}')
        if changes:
            print(f"  {os.path.relpath(filepath, CONTENT_ROOT)}")
            for c in changes:
                print(f"    {c}")
        return (filepath, new_path, title, new_title)

    # Rebuild frontmatter
    new_fm = rebuild_frontmatter(fm, new_title)
    new_content = f'---\n{new_fm}---{body}'

    # Write updated content
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    # Rename file if needed
    if changed_file and filepath != new_path:
        if os.path.exists(new_path):
            print(f"  WARNING: target exists, skipping rename: {new_path}", file=sys.stderr)
        else:
            os.rename(filepath, new_path)

    return (filepath, new_path, title, new_title)


def main():
    dry_run = '--dry-run' in sys.argv

    if dry_run:
        print("=== DRY RUN — no files will be modified ===\n")

    pattern = os.path.join(CONTENT_ROOT, '**', 'lesson-*.md')
    files = sorted(glob.glob(pattern, recursive=True))

    print(f"Found {len(files)} lesson files\n")

    changes = []
    for f in files:
        result = process_file(f, dry_run=dry_run)
        if result:
            changes.append(result)

    print(f"\n{'Would change' if dry_run else 'Changed'} {len(changes)} of {len(files)} files")

    if not dry_run:
        # Print rename mapping for reference (old -> new basenames)
        renames = [(r[0], r[1]) for r in changes if r[0] != r[1]]
        if renames:
            print(f"\nRenamed {len(renames)} files:")
            for old, new in renames:
                old_rel = os.path.relpath(old, CONTENT_ROOT)
                new_rel = os.path.relpath(new, CONTENT_ROOT)
                print(f"  {old_rel} -> {os.path.basename(new_rel)}")


if __name__ == '__main__':
    main()
