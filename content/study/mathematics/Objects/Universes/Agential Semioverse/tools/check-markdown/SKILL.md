---

skill_spec_version: "1"
id: check-markdown-skill
name: check-markdown
summary: Validate Markdown frontmatter/H1 consistency across library documents.
description: |
  Runs the repository's Markdown well-formedness checker to confirm frontmatter
  exists, IDs and names match conventions, and H1/title alignment is sane. Use
  before publishing or committing bulk edits.
kind: skill
skill_kind: programming
authors:
  - gpt-5.2-codex
date-created: 2026-01-06
tags:
  - agential-semioverse
runtime:
  entrypoint: scripts/check-markdown.py
  language: python
  invocation: cli
inputs:
  - name: paths
    type: array
    description: File or directory paths under library/ to check
    required: false
    default: ["library"]
outputs:
  - name: stdout
    type: string
    description: Checker output; empty when clean
  - name: exit_code
    type: integer
    description: 0 when clean, non-zero on issues
---

- Invokes the canonical checker at `library/media/writing/tools/check-markdown-well-formed/scripts/check-markdown.py`.
- Pass file or directory paths (default: `library/`).
- Exit code mirrors the underlying checker (non-zero when issues are found).
