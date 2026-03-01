---

skill_spec_version: "1"
id: beancount-validate-ledger-skill
name: beancount-validate-ledger
summary: Validate a Beancount ledger using bean-check when available.
description: Validate a Beancount ledger using bean-check when available. Use when checking ledger integrity before or after edits.
kind: skill
skill_kind: programming
authors:
- gpt-5.2-codex
date-created: 2025-12-31
tags:
- beancount
- accounting
runtime:
  entrypoint: scripts/validate-ledger.py
  language: python
  invocation: cli
inputs:
  - name: path
    type: string
    description: Ledger file path
    required: true
outputs:
  - name: status
    type: string
    description: Validation result or error
---

- Run the script: `scripts/validate-ledger.py`
- Provide `--path` to the ledger file.
- If `bean-check` is unavailable, the script returns an error.
