#!/usr/bin/env python3
"""Add dual aliases (Title Case + lowercase) to non-index .md files.

For files that have a title and only one alias matching the title,
adds a lowercase alias. Skips files where title == lowercase (already lowercase),
proper nouns, and files with no aliases block.
"""

import os
import re
import glob
import sys

_script_dir = os.path.dirname(os.path.abspath(__file__))
CONTENT_ROOT = os.path.normpath(os.path.join(_script_dir, '..', '..'))


def process_file(filepath: str, dry_run: bool = False):
    """Add lowercase alias if missing. Returns True if changed."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if not content.startswith('---'):
        return False

    end = content.find('\n---', 3)
    if end == -1:
        return False

    fm = content[3:end].strip()
    body = content[end + 4:]

    # Extract title
    title_match = re.search(r'^title:\s*"?([^"\n]+)"?\s*$', fm, re.MULTILINE)
    if not title_match:
        return False
    title = title_match.group(1).strip()

    # Skip if title is already all lowercase (no dual alias needed)
    if title == title.lower():
        return False

    # Extract aliases
    alias_block_match = re.search(r'^(aliases:\s*\n(?:\s+-\s+.*\n)*)', fm, re.MULTILINE)
    if not alias_block_match:
        return False  # No aliases block — don't add one to non-index files

    alias_block = alias_block_match.group(1)
    aliases = re.findall(r'^\s+-\s+"?([^"\n]+)"?\s*$', alias_block, re.MULTILINE)

    # Skip if already has 2+ aliases
    if len(aliases) >= 2:
        return False

    # Skip if single alias doesn't match title (custom alias, leave alone)
    if len(aliases) == 1 and aliases[0].strip() != title:
        return False

    lower_title = title.lower()

    # Build new alias block
    new_alias_block = f'aliases:\n  - "{title}"\n  - "{lower_title}"\n'

    if dry_run:
        rel = os.path.relpath(filepath, CONTENT_ROOT)
        print(f"  {rel}: + \"{lower_title}\"")
        return True

    new_fm = fm.replace(alias_block, new_alias_block)
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

    # Exclude index.md (already handled), private, .obsidian
    files = [f for f in files
             if os.path.basename(f) != 'index.md'
             and '/private/' not in f.replace('\\', '/')
             and '/.obsidian/' not in f.replace('\\', '/')]

    print(f"Found {len(files)} non-index .md files\n")

    changed = 0
    for f in files:
        if process_file(f, dry_run=dry_run):
            changed += 1

    print(f"\n{'Would add' if dry_run else 'Added'} lowercase alias to {changed} files")


if __name__ == '__main__':
    main()
