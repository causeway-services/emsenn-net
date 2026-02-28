---

name: check-markdown-well-formed
description: Check that a Markdown file is structurally well-formed for this repository.
  Use when validating documentation quality.
kind: agent-skill
skill-kind: writing
authors:
- gpt-5.2-codex
date-created: 2025-12-26
date-updated: 2026-01-10
id: check-markdown-well-formed-skill
---

- Follow [Markdown well-formedness](/media/writing/theory/markdown-well-formedness/README.md).
- Run the checker script:  
  `python library/media/writing/tools/check-markdown-well-formed/scripts/check-markdown.py <paths...>`
- The checker ignores `/library/inbox/triage` by default.
- Fix any reported issues (missing frontmatter, missing H1, missing title match).
- If the document introduces new terms, add a glossary link or include one.
