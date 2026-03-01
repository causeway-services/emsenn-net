#!/usr/bin/env python3
"""Normalize aliases across all .md files.

1. Remove duplicate aliases (case-sensitive dedup)
2. Ensure all aliases are quoted
3. Remove non-alias data that ended up in alias blocks
"""

import os
import re
import glob
import sys

_script_dir = os.path.dirname(os.path.abspath(__file__))
CONTENT_ROOT = os.path.normpath(os.path.join(_script_dir, '..', '..'))


def looks_like_alias(s):
    """Return True if the string looks like a legitimate alias."""
    bad_prefixes = ('id:', 'family:', 'year:', 'literal:', 'doi:')
    lower = s.lower().strip()
    for prefix in bad_prefixes:
        if lower.startswith(prefix):
            return False
    return True


def process_file(filepath, dry_run=False):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if not content.startswith('---\n'):
        return False

    end = content.find('\n---', 3)
    if end == -1:
        return False

    fm = content[4:end]
    body = content[end + 4:]

    # Ensure fm ends with newline so last alias line is captured by regex
    fm_padded = fm if fm.endswith('\n') else fm + '\n'

    # Find the full aliases block: "aliases:" header + all subsequent "  - " lines
    alias_match = re.search(
        r'^aliases:\s*\n((?:[ \t]+-[ \t]+.*\n)*)',
        fm_padded,
        re.MULTILINE
    )
    if not alias_match:
        return False

    full_match_start = alias_match.start()
    full_match_end = alias_match.end()
    alias_body = alias_match.group(1)

    # Parse individual aliases
    raw_aliases = re.findall(r'^[ \t]+-[ \t]+(.*?)$', alias_body, re.MULTILINE)
    aliases = []
    for a in raw_aliases:
        stripped = a.strip()
        if (stripped.startswith('"') and stripped.endswith('"')) or \
           (stripped.startswith("'") and stripped.endswith("'")):
            stripped = stripped[1:-1]
        if stripped and looks_like_alias(stripped):
            aliases.append(stripped)

    # Deduplicate preserving order
    seen = set()
    unique = []
    for a in aliases:
        if a not in seen:
            seen.add(a)
            unique.append(a)

    # Rebuild alias block
    new_alias_lines = '\n'.join(f'  - "{a}"' for a in unique) + '\n'
    new_alias_block = f'aliases:\n{new_alias_lines}'

    # Check if anything changed
    old_alias_block = fm_padded[full_match_start:full_match_end]
    if old_alias_block == new_alias_block:
        return False

    new_fm = fm_padded[:full_match_start] + new_alias_block + fm_padded[full_match_end:]

    if dry_run:
        rel = os.path.relpath(filepath, CONTENT_ROOT)
        print(f'  {rel}: {len(raw_aliases)} -> {len(unique)} aliases')
        return True

    if not new_fm.endswith('\n'):
        new_fm += '\n'
    new_content = f'---\n{new_fm}---{body}'

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return True


def main():
    dry_run = '--dry-run' in sys.argv

    if dry_run:
        print("=== DRY RUN ===\n")

    pattern = os.path.join(CONTENT_ROOT, '**', '*.md')
    files = sorted(glob.glob(pattern, recursive=True))
    files = [f for f in files if '/private/' not in f.replace('\\', '/')
             and '/.obsidian/' not in f.replace('\\', '/')]

    print(f"Scanning {len(files)} files\n")

    changed = 0
    for f in files:
        if process_file(f, dry_run=dry_run):
            changed += 1

    print(f"\n{'Would fix' if dry_run else 'Fixed'} {changed} files")


if __name__ == '__main__':
    main()
