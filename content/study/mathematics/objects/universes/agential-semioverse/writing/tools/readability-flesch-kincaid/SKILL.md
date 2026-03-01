---





name: readability-flesch-kincaid
description: Measure Flesch Reading Ease and Flesch-Kincaid Grade Level for text. Use when targeting specific readability levels.
kind: agent-skill
skill-kind: writing
authors:
- gpt-5.2-codex
date-created: 2025-12-30
id: readability-flesch-kincaid-skill
tags:
  - media
  - writing
---

- Run the script: [/media/writing/tools/readability-flesch-kincaid/scripts/measure-flesch-kincaid.py](/media/writing/tools/readability-flesch-kincaid/scripts/measure-flesch-kincaid.py)
- Provide file paths or `--stdin` with text.
- Use `--json` for machine-readable output.
- Target ranges:
  - Grade 6-8: 60-80 Reading Ease.
  - Grade 9-12: 40-60 Reading Ease.
