#!/usr/bin/env python3
"""Reorder 'Y X' index titles to 'X of Y' pattern.

E.g. 'Philosophy Disciplines' -> 'Disciplines of Philosophy'

Also sets aliases to both forms (plus lowercase variants).
"""

import os
import re
import glob
import sys

_script_dir = os.path.dirname(os.path.abspath(__file__))
CONTENT_ROOT = os.path.normpath(os.path.join(_script_dir, '..', '..'))

# Structural category words that trigger the reorder
STRUCTURAL_WORDS = {
    'Schools', 'Disciplines', 'Topics', 'Terms', 'Curricula', 'Curriculum',
    'Concepts', 'Objects', 'Texts', 'Text', 'Specifications', 'Skills',
    'Languages', 'Practices', 'Lessons',
}

# Titles to skip entirely (genuine topic/concept names, not Y-X structural patterns)
SKIP_TITLES = {
    'Card Games',
    'Gambling Games',
    'Role-Playing Games',
    'Tabletop Role-Playing Games',
    'Terms',         # bare title, no prefix to reorder
    'Languages',     # bare title
    'Schools',       # bare title
}

# Adjective-to-noun mappings for subjects that use adjective form in current title
ADJECTIVE_TO_NOUN = {
    'Ecological': 'Ecology',
    'Mathematical': 'Mathematics',
    'Philosophical': 'Philosophy',
}

# Skip reorder for these prefixes (result would be nonsensical)
SKIP_PREFIXES = {'Personal'}


def find_structural_suffix(title):
    """Check if title ends with a structural word. Returns (prefix, word) or None."""
    words = title.rsplit(' ', 1)
    if len(words) == 2 and words[1] in STRUCTURAL_WORDS:
        return words[0], words[1]
    return None


def fix_adjective(prefix):
    """Convert adjective-form prefixes to noun form."""
    if prefix in ADJECTIVE_TO_NOUN:
        return ADJECTIVE_TO_NOUN[prefix]
    parts = prefix.rsplit(' ', 1)
    if len(parts) == 2 and parts[1] in ADJECTIVE_TO_NOUN:
        return parts[0] + ' ' + ADJECTIVE_TO_NOUN[parts[1]]
    return prefix


def reorder_title(title):
    """Convert 'Y X' to 'X of Y'. Returns new_title or None."""
    if title in SKIP_TITLES:
        return None

    # Already in "X of Y" form
    if ' of ' in title:
        return None

    result = find_structural_suffix(title)
    if result is None:
        return None

    prefix, structural = result
    prefix = fix_adjective(prefix)

    if prefix in SKIP_PREFIXES:
        return None

    return f'{structural} of {prefix}'


def parse_frontmatter(content):
    """Parse YAML frontmatter. Returns (fm_text, body, title)."""
    if not content.startswith('---'):
        return None, content, None

    end = content.find('\n---', 3)
    if end == -1:
        return None, content, None

    fm = content[3:end].strip()
    body = content[end + 4:]

    title_match = re.search(r'^title:\s*"?([^"\n]+)"?\s*$', fm, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else None

    return fm, body, title


def rebuild_frontmatter(fm, old_title, new_title):
    """Replace title and update aliases to include both forms."""
    # Replace title
    fm = re.sub(
        r'^(title:\s*)"?[^"\n]+"?\s*$',
        f'\\1"{new_title}"',
        fm,
        flags=re.MULTILINE
    )

    # Build aliases: new title, old title, plus lowercase of each
    aliases = [new_title, old_title]
    lc_new = new_title.lower()
    lc_old = old_title.lower()
    if lc_new != new_title:
        aliases.append(lc_new)
    if lc_old != old_title and lc_old != lc_new:
        aliases.append(lc_old)

    alias_lines = '\n'.join(f'  - "{a}"' for a in aliases)
    alias_block = f'aliases:\n{alias_lines}\n'

    # Replace existing aliases (handle both quoted and unquoted)
    alias_pattern = r'^aliases:\s*\n(?:\s+-\s+.*\n)*'
    if re.search(alias_pattern, fm, re.MULTILINE):
        fm = re.sub(alias_pattern, alias_block, fm, flags=re.MULTILINE)
    else:
        fm = re.sub(
            r'^(title:\s*"[^"]*")\s*$',
            f'\\1\n{alias_block.rstrip()}',
            fm,
            flags=re.MULTILINE
        )

    return fm


def process_file(filepath, dry_run=False):
    """Process a single index.md file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    fm, body, title = parse_frontmatter(content)
    if fm is None or title is None:
        return None

    new_title = reorder_title(title)
    if new_title is None:
        return None

    rel = os.path.relpath(filepath, CONTENT_ROOT)

    if dry_run:
        print(f'  {rel}')
        print(f'    "{title}" -> "{new_title}"')
        return True

    new_fm = rebuild_frontmatter(fm, title, new_title)
    # Ensure frontmatter ends with newline before closing ---
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

    pattern = os.path.join(CONTENT_ROOT, '**', 'index.md')
    files = sorted(glob.glob(pattern, recursive=True))

    files = [f for f in files if '/private/' not in f.replace('\\', '/')
             and '/.obsidian/' not in f.replace('\\', '/')]

    print(f"Found {len(files)} index.md files\n")

    changed = 0
    for f in files:
        result = process_file(f, dry_run=dry_run)
        if result:
            changed += 1

    print(f"\n{'Would change' if dry_run else 'Changed'} {changed} of {len(files)} files")


if __name__ == '__main__':
    main()
