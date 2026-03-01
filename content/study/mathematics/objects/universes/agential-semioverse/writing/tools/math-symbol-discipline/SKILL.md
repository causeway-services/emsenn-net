---

name: math-symbol-discipline
description: Enforce domain-appropriate notation and avoid cross-domain symbol misuse.
  Use when writing any mathematical text.
kind: agent-skill
skill-kind: writing
authors:
- gpt-5.2-codex
date-created: 2025-12-26
id: math-symbol-discipline-skill
---

- Identify the mathematical domain of the text (e.g., modal logic, category theory, topology).
- Use standard symbols for that domain and avoid importing symbols from other domains.
- Example: use $\Box$ and $\Diamond$ only in modal logic; do not use them for unrelated operators.
- Example: use $\infty$-category notation only when higher morphisms are part of the structure.
- Example: reserve $\pi_n$ for homotopy groups, not for unrelated indexing.
- If a symbol is nonstandard, define it explicitly before use.
