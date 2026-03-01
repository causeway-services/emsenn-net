---
title: "Beancount Basics"
aliases:
  - "Beancount Basics"
id: accounting-lesson-beancount-basics
kind: lesson
authors:
- gpt-5.2-codex
date-created: 2025-12-31
tags:
- accounting
- finance
- beancount
dependencies:
- /domestic/accounting/curricula/plain-text-accounting.md---


Beancount is a plain-text accounting system with a precise syntax and tooling
for validation and reporting.

## Files and directives

- A Beancount file holds transactions, balances, and metadata.
- Directives include `open`, `close`, `balance`, `pad`, and `price`.
- Transactions are dated and list postings that balance.

## Workflow

- Write or import transactions into a `.beancount` file.
- Run the Beancount checker to validate the ledger.
- Use reporting tools to inspect balances and activity.
