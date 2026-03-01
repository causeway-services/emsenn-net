---

skill_spec_version: "1"
id: create-skill-module-skill
name: create-skill-module
summary: Scaffold a skill directory with SKILL.md and scripts/.
description: Create a new skill directory with SKILL.md and scripts/ scaffolding. Use when bootstrapping new skills.
kind: skill
skill_kind: programming
authors:
- gpt-5.2-codex
date-created: 2025-12-30
tags:
- programming
runtime:
  entrypoint: scripts/create-skill-module.py
  language: python
  invocation: cli
inputs:
  - name: path
    type: string
    description: Directory under library/ to create the skill
    required: true
  - name: name
    type: string
    description: Skill name
    required: true
  - name: description
    type: string
    description: Skill description
    required: true
  - name: skill_kind
    type: string
    description: Skill kind (assisting, programming, researching, writing)
    required: false
  - name: dry_run
    type: boolean
    description: Preview without writing files
    required: false
    default: false
outputs:
  - name: created_path
    type: path
    description: Path of the created skill directory
---

- Run the script: `scripts/create-skill-module.py`
- Provide `--path` (directory under `/library/...`).
- Use `--name`, `--description`, and `--skill-kind` to populate SKILL.md.
- Use `--dry-run` to preview without writing files.
