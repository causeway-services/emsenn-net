---

skill_spec_version: "1"
id: library-api-stats-skill
name: library-api-stats
summary: Summarize library file counts and frontmatter distributions.
description: Summarize library file counts and frontmatter distributions. Use when remote agents need basic inventory statistics.
kind: skill
skill_kind: programming
authors:
  - gpt-5.2-codex
date-created: 2025-12-31
tags:
  - agential-semioverse
runtime:
  entrypoint: scripts/library-stats.py
  language: python
  invocation: cli
inputs:
  - name: path
    type: string
    description: Optional subpath under library/ to limit stats
    required: false
  - name: json
    type: boolean
    description: Emit JSON result
    required: false
    default: true
outputs:
  - name: stats
    type: object
    description: Counts and distributions
---
- Run the script: `scripts/library-stats.py`
- Provide `--root` for the library-relative scan root.
- Use `--json` for machine-readable output.

- HTTP: POST /api/v1/skills/library-api-stats/execute with {"inputs": {...}}.
