---

skill_spec_version: "1"
id: validate-module-skill
name: validate-module
summary: Validate a module directory for required files and directories.
description: Validate a module directory for required files and directories. Use when checking module structure.
kind: skill
skill_kind: programming
authors:
- gpt-5.2-codex
date-created: 2025-12-30
tags:
- programming
runtime:
  entrypoint: scripts/validate-module.py
  language: python
  invocation: cli
inputs:
  - name: path
    type: string
    description: Module directory under library/
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

- Run the script: `scripts/validate-module.py`
- Provide `--path` to the module directory.
- Use `--json` for machine-readable output.
