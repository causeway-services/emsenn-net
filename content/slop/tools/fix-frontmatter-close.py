#!/usr/bin/env python3
"""Fix malformed frontmatter where closing --- is concatenated to the last line.

Finds patterns like:
  - "something"---
and converts to:
  - "something"
---
"""

import os
import re
import glob
import sys

_script_dir = os.path.dirname(os.path.abspath(__file__))
CONTENT_ROOT = os.path.normpath(os.path.join(_script_dir, '..', '..'))


def fix_file(filepath, dry_run=False):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if not content.startswith('---\n'):
        return False

    # Check if there's a properly separated closing ---
    if content.find('\n---', 3) != -1:
        # Check if the first \n--- is the real closing marker
        # (not inside content like a horizontal rule)
        return False

    # Find the concatenated --- pattern: a line ending with ---
    # that isn't the opening marker
    lines = content.split('\n')
    fixed = False
    for i in range(1, len(lines)):
        line = lines[i]
        if line.endswith('---') and line != '---' and len(line) > 3:
            # Split the --- off the end
            lines[i] = line[:-3]
            lines.insert(i + 1, '---')
            fixed = True
            break

    if not fixed:
        return False

    new_content = '\n'.join(lines)

    if dry_run:
        rel = os.path.relpath(filepath, CONTENT_ROOT)
        print(f'  {rel}')
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
    files = [f for f in files if '/private/' not in f.replace('\\', '/')
             and '/.obsidian/' not in f.replace('\\', '/')]

    print(f"Scanning {len(files)} files\n")

    changed = 0
    for f in files:
        if fix_file(f, dry_run=dry_run):
            changed += 1

    print(f"\n{'Would fix' if dry_run else 'Fixed'} {changed} files")


if __name__ == '__main__':
    main()
