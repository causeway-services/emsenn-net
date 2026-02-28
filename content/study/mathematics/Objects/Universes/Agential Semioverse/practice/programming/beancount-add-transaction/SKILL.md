---

skill_spec_version: "1"
id: beancount-add-transaction-skill
name: beancount-add-transaction
summary: Append a validated Beancount transaction to a ledger.
description: Append a validated Beancount transaction to a ledger. Use when adding ledger entries via scripts instead of raw edits.
kind: skill
skill_kind: programming
authors:
- gpt-5.2-codex
date-created: 2025-12-31
tags:
- beancount
- accounting
runtime:
  entrypoint: scripts/add-transaction.py
  language: python
  invocation: cli
inputs:
  - name: path
    type: string
    description: Ledger file path
    required: true
  - name: date
    type: string
    description: Transaction date (YYYY-MM-DD)
    required: true
  - name: narration
    type: string
    description: Narration/description
    required: true
  - name: posting
    type: array
    description: Postings (account amount commodity)
    required: true
outputs:
  - name: status
    type: string
    description: Success or error message
---

- Run the script: `scripts/add-transaction.py`
- Provide `--path`, `--date`, `--narration`, and one or more `--posting` lines.
- Postings must balance by commodity (sum to zero).
