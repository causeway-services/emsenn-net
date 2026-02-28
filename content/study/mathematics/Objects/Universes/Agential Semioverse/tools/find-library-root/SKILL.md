---

skill_spec_version: "1"
id: find-library-root-skill
name: find-library-root
summary: Resolve the library/ directory path from any working directory.
description: |
  Walks parent directories to locate the repository's `library/` root and prints
  the absolute path. Use when chaining tools that need an explicit library path.
kind: skill
skill_kind: programming
authors:
  - gpt-5.2-codex
date-created: 2026-01-06
tags:
  - agential-semioverse
runtime:
  entrypoint: scripts/find-library-root.py
  language: python
  invocation: cli
inputs: []
outputs:
  - name: stdout
    type: string
    description: Absolute path to library/
---

- Invokes `scripts/find-library-root.py`.
- Exits with non-zero status if `library/` cannot be found.
