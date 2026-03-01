---


title: Markdown Well-Formedness
id: markdown-well-formedness-readme
kind: specification
authors: [gpt-5.2-codex]
date-created: 2025-12-26
date-updated: 2026-01-10
---

# Markdown Well-Formedness

This specification defines what "well-formed" means for Markdown files in this repository.

## Requirements

1. File begins with YAML frontmatter delimited by `---`.
2. Frontmatter includes `title` or `name`.
3. Non-skill documents contain exactly one H1 (`# ...`) heading.
4. For non-skill documents, the H1 matches the frontmatter `title`.
5. File references are Markdown links, not monospaced paths.
6. `SKILL.md` must have `name` matching the parent directory name.
7. `README.md` must have `id` matching `<directory>-readme`.
8. `IDEAS.md`, `PLANS.md`, `GLOSSARY.md` must have `id` matching `<directory>-ideas`, `<directory>-plans`, `<directory>-glossary`.

## Related tools

- [Frontmatter schema](/mathematics/objects/agential-semioverse/tools/frontmatter-schema/README.md)
- [Markdown checker](/media/writing/tools/check-markdown-well-formed/SKILL.md)

## Tool defaults

The validation tools ignore `/library/inbox/triage` by default. Use explicit
paths to include triage content when needed.
