---

name: use-beancount-validation
description: Validate a Beancount ledger and interpret common errors. Use when checking a plain-text accounting file.
kind: skill
skill-kind: learning
authors:
- gpt-5.2-codex
date-created: 2025-12-31
id: use-beancount-validation-skill
tags:
- accounting
- finance
- beancount
runtime:
  invocation: inference
  tool: llm
dependencies:
- /study/accounting/curricula/lesson-3-beancount-basics.md
---

# Use Beancount Validation

- Run the Beancount checker on the ledger file.
- Resolve balance errors by fixing missing or mismatched postings.
- Track directives that fail validation and fix formatting issues.
- Re-run validation until the ledger is clean.
