---

skill_spec_version: "1"
id: validate-frontmatter-skill
name: validate-frontmatter
summary: Validate Markdown frontmatter against the semioverse canonical schema.
description: |
  Validate Markdown files using the canonical frontmatter schema. Use this before
  publication or manifest generation to catch missing required fields or schema
  drift.
kind: skill
skill_kind: programming
authors:
  - gpt-5.2-codex
date-created: 2025-12-26
date-updated: 2026-01-09
tags:
  - validation
  - agential-semioverse
runtime:
  invocation: cli
  entrypoint: scripts/validate-frontmatter.py
  language: python
inputs:
  - name: paths
    description: One or more Markdown files or directories to validate.
    type: path
    required: true
outputs: []
dependencies:
  - /mathematics/objects/agential-semioverse/tools/frontmatter-schema/schema.json
---

- Uses the canonical schema at `/library/mathematics/objects/agential-semioverse/tools/frontmatter-schema/schema.json`.
- The validator ignores `/library/inbox/triage` by default.
- Fix missing required fields (id, kind, title/name, authors, date-created) before re-running.
