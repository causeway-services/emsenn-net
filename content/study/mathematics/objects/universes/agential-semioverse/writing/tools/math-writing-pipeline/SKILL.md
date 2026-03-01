---





name: math-writing-pipeline
description: Chain math writing skills into a single workflow with audience branching.
  Use when producing or revising mathematical documents in this repository.
kind: agent-skill
skill-kind: writing
authors:
- gpt-5.2-codex
date-created: 2025-12-30
id: math-writing-pipeline-skill
tags:
  - media
  - math
---

- Identify the document's audience and apply [define-reader-persona](/media/writing/tools/define-reader-persona/SKILL.md).
- If the audience is expert, apply [math-for-mathematicians](/media/writing/tools/math-for-mathematicians/SKILL.md).
- If the audience is general, apply [math-for-general-audience](/media/writing/tools/math-for-general-audience/SKILL.md).
- Apply [math-symbol-discipline](/media/writing/tools/math-symbol-discipline/SKILL.md) regardless of audience.
- Run [check-math-delimiters](/media/writing/tools/check-math-delimiters/SKILL.md) on math-heavy documents.
- Ensure Markdown is well-formed using [check-markdown-well-formed](/media/writing/tools/check-markdown-well-formed/SKILL.md).
- Validate frontmatter with [validate-frontmatter](/mathematics/objects/agential-semioverse/tools/validate-frontmatter/SKILL.md).
