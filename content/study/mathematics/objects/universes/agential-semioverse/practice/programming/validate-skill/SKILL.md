---

skill_spec_version: "1"
id: validate-skill-skill
name: validate-skill
summary: Validate a skill directory and its SKILL.md frontmatter.
description: Validate a skill directory and its SKILL.md frontmatter. Use when checking skill structure.
kind: skill
skill_kind: programming
authors:
- gpt-5.2-codex
date-created: 2025-12-30
tags:
- programming
runtime:
  entrypoint: scripts/validate-skill.py
  language: python
  invocation: cli
inputs:
  - name: path
    type: string
    description: Skill directory under library/
    required: true
  - name: json
    type: boolean
    description: Emit JSON result
    required: false
    default: true
outputs:
  - name: issues
    type: array
    description: Validation findings
---

- Run the script: `scripts/validate-skill.py`
- Provide `--path` to the skill directory.
- Use `--json` for machine-readable output.
