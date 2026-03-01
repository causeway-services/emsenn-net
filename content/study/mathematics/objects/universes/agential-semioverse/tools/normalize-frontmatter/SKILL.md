---

skill_spec_version: "1"
id: normalize-frontmatter-skill
name: normalize-frontmatter
summary: Normalize Markdown frontmatter to align with semioverse schema expectations.
description: |
  Normalize frontmatter fields (quoting, id fields, required keys) before running
  validation. Use this to fix broad sets of files prior to manifest generation.
kind: skill
skill_kind: programming
authors:
  - gpt-5.2-codex
date-created: 2025-12-26
date-updated: 2026-01-09
tags:
  - normalization
  - agential-semioverse
runtime:
  invocation: cli
  entrypoint: scripts/normalize-frontmatter.py
  language: python
inputs:
  - name: paths
    description: One or more Markdown files or directories to normalize.
    type: path
    required: true
outputs: []
dependencies:
  - /mathematics/objects/agential-semioverse/tools/frontmatter-schema/schema.json
---

- Run: `python library/mathematics/objects/agential-semioverse/tools/normalize-frontmatter/scripts/normalize-frontmatter.py <paths...>`
- For skills missing `id`, run: `python library/mathematics/objects/agential-semioverse/tools/normalize-frontmatter/scripts/add-skill-ids.py`
- Re-run `/library/mathematics/objects/agential-semioverse/tools/validate-frontmatter/SKILL.md` after normalization.
