---

name: atomized-math-docs
description: Write mathematical documentation as small, self-contained units that
  define terms and only reference adjacent units. Use when documenting a mathematical
  object in this repository.
kind: agent-skill
skill-kind: writing
authors:
- gpt-5.2-codex
date-created: 2025-12-26
id: atomized-math-docs-skill
---

- Create one file per concept, with a clear title matching the term.
- Include: definition, plain-language explanation, minimal formal structure, and a worked example.
- List explicit entry conditions for applying the concept.
- Avoid depending on the full paper; instead, link to adjacent concept files.
- Ensure each file can stand alone without external context.
