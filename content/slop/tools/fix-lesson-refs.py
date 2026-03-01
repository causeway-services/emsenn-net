#!/usr/bin/env python3
"""Fix references to renamed lesson files across the vault.

Replaces all occurrences of lesson-N-slug patterns with just slug
in wikilinks, markdown links, and plain text references.
"""

import os
import re
import glob
import sys

_script_dir = os.path.dirname(os.path.abspath(__file__))
CONTENT_ROOT = os.path.normpath(os.path.join(_script_dir, '..', '..'))


def fix_lesson_refs(content: str) -> str:
    """Replace lesson-N-foo references with just foo."""
    # Match lesson-N- prefix in various contexts:
    # - wikilinks: [[.../lesson-1-foo|...]]
    # - markdown links: (lesson-1-foo.md)
    # - plain text references: lesson-1-foo.md or lesson-1-foo
    return re.sub(r'lesson-(\d+)-', '', content)


def process_file(filepath: str, dry_run: bool = False):
    """Process a single file. Returns True if changes were made."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip if no lesson-N- references
    if not re.search(r'lesson-\d+-', content):
        return False

    new_content = fix_lesson_refs(content)

    if new_content == content:
        return False

    if dry_run:
        # Show what would change
        rel = os.path.relpath(filepath, CONTENT_ROOT)
        old_lines = content.splitlines()
        new_lines = new_content.splitlines()
        print(f"  {rel}")
        for i, (old, new) in enumerate(zip(old_lines, new_lines)):
            if old != new:
                print(f"    L{i+1}: {old.strip()}")
                print(f"      -> {new.strip()}")
        return True

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    return True


def main():
    dry_run = '--dry-run' in sys.argv

    if dry_run:
        print("=== DRY RUN ===\n")

    pattern = os.path.join(CONTENT_ROOT, '**', '*.md')
    files = sorted(glob.glob(pattern, recursive=True))

    changed = 0
    for f in files:
        if process_file(f, dry_run=dry_run):
            changed += 1

    print(f"\n{'Would update' if dry_run else 'Updated'} {changed} files")


if __name__ == '__main__':
    main()
