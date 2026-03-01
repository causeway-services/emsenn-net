---

title: Frontmatter Schema (Agential Semioverse)
id: frontmatter-schema-readme
kind: specification
authors:
  - gpt-5.2-codex
date-created: 2026-01-06
summary: Canonical copy of the repository Markdown frontmatter schema for semioverse tools.
---

# Frontmatter Schema (Agential Semioverse)

This directory hosts the canonical schema used by semioverse tools (API validators,
engine execution flows) to check Markdown frontmatter. It replaces the legacy copy
that used to live under `/library/skills/writing/frontmatter-schema/`.

Key files
- `schema.json`: JSON Schema for Markdown frontmatter in this repository.
- `scripts/validate-frontmatter.py`: CLI validator using the canonical schema.
- `SKILL.md`: semioverse skill surface for schema access.

Required fields
- `id` (stable identifier)
- `kind` (document type, e.g. readme, curriculum, glossary, skill)
- `authors` (list)
- `date-created` (`YYYY-MM-DD`)
- One of `title` or `name` (skills must include `name` even if `title` is present)

Common optional fields
- `date-updated`, `description`, `tags`, `concept`, `roles`, `status`, `version`
- `references`, `dependencies`, `publications`
