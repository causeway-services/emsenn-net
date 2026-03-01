---

name: compose-math-docs
description: Chain math-writing skills to produce a complete documentation unit with
  audience-appropriate style. Use when you must decide how to write and then produce
  the math text.
kind: agent-skill
skill-kind: writing
authors:
- gpt-5.2-codex
date-created: 2025-12-26
id: compose-math-docs-skill
---

- Define the reader persona using [define-reader-persona](/media/writing/tools/define-reader-persona/SKILL.md).
- If the reader is expert-level, apply [math-for-mathematicians](/media/writing/tools/math-for-mathematicians/SKILL.md).
- If the reader is general or mixed, apply [math-for-general-audience](/media/writing/tools/math-for-general-audience/SKILL.md).
- Apply [math-symbol-discipline](/media/writing/tools/math-symbol-discipline/SKILL.md) to ensure notation matches the domain.
- Write the content using [atomized-math-docs](/media/writing/tools/atomized-math-docs/SKILL.md) if the goal is documentation; otherwise write a single narrative.
- If any step fails (unclear reader), stop and request clarification or choose minimal assumptions.
