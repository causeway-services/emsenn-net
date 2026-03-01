#!/usr/bin/env python3
"""Fix index.md titles to Title Case and set dual aliases.

For each index.md:
1. Apply Title Case to the title
2. Set aliases to [Title Case, lowercase] — two entries
3. Exception: proper nouns get only one alias (the title itself)
"""

import os
import re
import glob
import sys

_script_dir = os.path.dirname(os.path.abspath(__file__))
CONTENT_ROOT = os.path.normpath(os.path.join(_script_dir, '..', '..'))

# Words that stay lowercase in Title Case (unless first word)
SMALL_WORDS = {
    'a', 'an', 'the', 'and', 'but', 'or', 'for', 'nor',
    'in', 'on', 'at', 'to', 'by', 'of', 'with', 'is', 'as',
    'vs', 'via',
}

# Proper nouns / abbreviations that must keep specific casing
PRESERVE_CASE = {
    'fdm': 'FDM', 'fff': 'FFF', '3d': '3D',
    'oop': 'OOP', 'rpg': 'RPG', 'rpgs': 'RPGs', 'ttrpg': 'TTRPG',
    'activitypub': 'ActivityPub', 'mkdocs': 'MkDocs',
    'gnoponemacs': 'GnoponEmacs', 'github': 'GitHub',
    'git': 'Git', 'mastodon': 'Mastodon',
    'foucault': 'Foucault', 'kripke': 'Kripke',
    'frege': 'Frege', 'bayes': 'Bayes',
    'beancount': 'Beancount',
    'heyting': 'Heyting',
    'emsenn': 'emsenn',
    'inaturalist': 'iNaturalist',
    'fediverse': 'Fediverse',
    'scs': 'SCS',
    'asr': 'ASR',
    'gfrtu': 'GFRTU',
    'ai': 'AI',
    'css': 'CSS', 'html': 'HTML', 'json': 'JSON',
    'api': 'API', 'apis': 'APIs',
    'url': 'URL', 'urls': 'URLs',
    'http': 'HTTP', 'https': 'HTTPS',
    'tcp': 'TCP', 'ip': 'IP',
    'dns': 'DNS',
    'ssh': 'SSH',
    'yaml': 'YAML',
    'xml': 'XML',
    'sql': 'SQL',
    'pdf': 'PDF',
    'svg': 'SVG',
    'csv': 'CSV',
    'toml': 'TOML',
    '(infinity,1)-topoi': '(Infinity,1)-Topoi',
}

# Titles that are entirely proper nouns — should get only ONE alias (the title).
# We detect these by checking if lowering the title would lose meaning.
# People, specific software products, named frameworks, etc.
PROPER_NOUN_TITLES = set()  # populated dynamically below


def is_proper_noun_title(title: str) -> bool:
    """Heuristic: a title is a proper noun if it's a single word that's
    in PRESERVE_CASE, or if it's a known person/product name."""
    lower = title.lower()
    # Single-word titles that are in preserve_case are proper nouns
    words = title.split()
    if len(words) == 1 and lower in PRESERVE_CASE:
        return True
    # Multi-word: if ALL words are proper nouns or small words, it's likely proper
    # But most index titles are generic ("Card Games", "Probability") — not proper
    return False


def title_case(s: str) -> str:
    """Apply Title Case with small-word and preserve-case rules."""
    lower = s.lower()
    if lower in PRESERVE_CASE:
        return PRESERVE_CASE[lower]

    words = s.split()
    result = []
    for i, word in enumerate(words):
        # Separate trailing punctuation
        stripped = word.rstrip('?:,;.)')
        punctuation = word[len(stripped):]
        # Also handle leading punctuation like (
        leading = ''
        core = stripped
        if core and core[0] in '(':
            leading = core[0]
            core = core[1:]

        core_lower = core.lower()

        # Handle possessives: strip 's before checking preserve-case
        possessive = ''
        base_lower = core_lower
        if base_lower.endswith("'s"):
            possessive = "'s"
            base_lower = base_lower[:-2]

        if base_lower in PRESERVE_CASE:
            result.append(leading + PRESERVE_CASE[base_lower] + possessive + punctuation)
        elif i == 0:
            # First word always capitalized
            if core:
                result.append(leading + core[0].upper() + core[1:] + punctuation)
            else:
                result.append(word)
        elif core_lower in SMALL_WORDS:
            result.append(leading + core.lower() + punctuation)
        else:
            # Handle hyphenated words
            parts = core.split('-')
            capped_parts = []
            for part in parts:
                part_lower = part.lower()
                if part_lower in PRESERVE_CASE:
                    capped_parts.append(PRESERVE_CASE[part_lower])
                elif part:
                    capped_parts.append(part[0].upper() + part[1:])
                else:
                    capped_parts.append(part)
            result.append(leading + '-'.join(capped_parts) + punctuation)

    return ' '.join(result)


def parse_frontmatter(content: str):
    """Parse YAML frontmatter, return (fm_text, body, title, aliases_raw)."""
    if not content.startswith('---'):
        return None, content, None, None

    end = content.find('\n---', 3)
    if end == -1:
        return None, content, None, None

    fm = content[3:end].strip()
    body = content[end + 4:]

    # Extract title
    title_match = re.search(r'^title:\s*"?([^"\n]+)"?\s*$', fm, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else None

    # Extract raw aliases block for replacement
    aliases_match = re.search(r'^(aliases:\s*\n(?:\s+-\s+.*\n)*)', fm, re.MULTILINE)
    aliases_raw = aliases_match.group(1) if aliases_match else None

    return fm, body, title, aliases_raw


def rebuild_frontmatter(fm: str, new_title: str, proper_noun: bool) -> str:
    """Replace title and set aliases in frontmatter."""
    # Replace title
    fm = re.sub(
        r'^(title:\s*)"?[^"\n]+"?\s*$',
        f'\\1"{new_title}"',
        fm,
        flags=re.MULTILINE
    )

    lower_title = new_title.lower()
    if proper_noun or lower_title == new_title:
        # Proper noun or already lowercase: single alias
        alias_block = f'aliases:\n  - "{new_title}"\n'
    else:
        # Two aliases: Title Case and lowercase
        alias_block = f'aliases:\n  - "{new_title}"\n  - "{lower_title}"\n'

    # Replace or add aliases
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


def process_file(filepath: str, dry_run: bool = False):
    """Process a single index.md file. Returns change info or None."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    fm, body, title, aliases_raw = parse_frontmatter(content)
    if fm is None or title is None:
        return None

    new_title = title_case(title)
    proper_noun = is_proper_noun_title(new_title)

    # Check if anything needs changing
    lower_title = new_title.lower()
    if proper_noun or lower_title == new_title:
        expected_aliases = f'aliases:\n  - "{new_title}"\n'
    else:
        expected_aliases = f'aliases:\n  - "{new_title}"\n  - "{lower_title}"\n'

    title_changed = (new_title != title)
    aliases_changed = (aliases_raw != expected_aliases)

    if not title_changed and not aliases_changed:
        return None

    rel = os.path.relpath(filepath, CONTENT_ROOT)

    if dry_run:
        changes = []
        if title_changed:
            changes.append(f'title: "{title}" -> "{new_title}"')
        if aliases_changed:
            if proper_noun or lower_title == new_title:
                changes.append(f'aliases: ["{new_title}"]')
            else:
                changes.append(f'aliases: ["{new_title}", "{lower_title}"]')
        if changes:
            print(f"  {rel}")
            for c in changes:
                print(f"    {c}")
        return True

    new_fm = rebuild_frontmatter(fm, new_title, proper_noun)
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

    # Exclude private, .obsidian
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
