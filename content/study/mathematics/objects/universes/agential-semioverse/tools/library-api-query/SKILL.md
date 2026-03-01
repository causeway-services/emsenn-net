---

skill_spec_version: "1"
id: library-api-query-skill
name: library-api-query
summary: Query library files by frontmatter fields and emit JSON results.
description: Query library files by frontmatter fields and emit JSON results. Use when remote agents need structured filters like tags or date ranges.
kind: skill
skill_kind: programming
authors:
  - gpt-5.2-codex
date-created: 2025-12-30
tags:
  - agential-semioverse
runtime:
  entrypoint: scripts/query-library.py
  language: python
  invocation: cli
inputs:
  - name: filter
    type: string
    description: JSON filter expression for frontmatter
    required: true
  - name: json
    type: boolean
    description: Emit JSON result
    required: false
    default: true
outputs:
  - name: results
    type: array
    description: Files matching the query
---
## Inputs

- `--tags` comma-separated tags (match any).
- `--kind` match a frontmatter `kind`.
- `--authors` comma-separated authors (match any).
- `--publications` comma-separated publication keys (match any).
- `--id` match exact frontmatter `id`.
- `--title` substring match in frontmatter `title`.
- `--path-prefix` path prefix under `/library`.
- `--date-from` ISO date (`YYYY-MM-DD`) for `date-created`.
- `--date-to` ISO date (`YYYY-MM-DD`) for `date-created`.
- `--json` for machine-readable output.

## Output (JSON)

```json
{
  "matches": [
    {
      "path": "study/...",
      "title": "Title",
      "id": "doc-id",
      "date_created": "YYYY-MM-DD",
      "tags": ["tag1", "tag2"],
      "kind": "doc",
      "authors": ["emsenn"],
      "publications": ["emsenn-net: publishable"]
    }
  ]
}
```

- HTTP: POST /api/v1/skills/library-api-query/execute with {"inputs": {...}}.
