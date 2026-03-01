---





name: check-math-delimiters
description: Validate use of $ and $$ delimiters in math documents. Use when ensuring LaTeX math is well-formed in Markdown.
kind: agent-skill
skill-kind: writing
authors:
- gpt-5.2-codex
date-created: 2025-12-30
id: check-math-delimiters-skill
tags:
  - media
  - writing
---

- Run the script: [/media/writing/tools/check-math-delimiters/scripts/check-math-delimiters.py](/media/writing/tools/check-math-delimiters/scripts/check-math-delimiters.py)
- Provide file or directory paths to scan.
- The script ignores fenced code blocks and inline code spans.
- Output lists files with unmatched `$` or `$$` delimiters.
