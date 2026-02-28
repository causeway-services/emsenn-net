---

skill_spec_version: "1"
id: create-module-skill
name: create-module
summary: Bootstrap a module directory with README, SPECIFICATIONS, and subdirectories.
description: Create a module directory with README, SPECIFICATIONS, and standard subdirectories. Use when bootstrapping new study or application modules.
kind: skill
skill_kind: programming
authors:
- gpt-5.2-codex
date-created: 2025-12-30
tags:
- programming
runtime:
  entrypoint: scripts/create-module.py
  language: python
  invocation: cli
inputs:
  - name: path
    type: string
    description: Module directory to create (relative to library/)
    required: true
  - name: title
    type: string
    description: Title for README frontmatter
    required: true
  - name: kind
    type: string
    description: "README kind (default: readme)"
    required: false
  - name: dry_run
    type: boolean
    description: Preview without writing files
    required: false
    default: false
outputs:
  - name: created_paths
    type: array
    description: Paths created or touched
---

- Run the script: `scripts/create-module.py`
- Provide `--path` and `--title`.
- Use `--kind` to set README kind (default: readme).
- Use `--dry-run` to preview without writing files.
