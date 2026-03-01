---

name: math-for-mathematicians
description: Write mathematical texts for expert readers with precise definitions,
  clear hypotheses, and proof-oriented structure. Use when the intended audience is
  a mathematician or a mathematically trained researcher.
kind: agent-skill
skill-kind: writing
authors:
- gpt-5.2-codex
date-created: 2025-12-26
id: math-for-mathematicians-skill
---

- State the problem and assumptions up front, using explicit hypotheses and named conventions.
- Use a sparse, formal tone: definitions and propositions first, then proofs.
- Keep proofs linear: each step should cite the exact definition or lemma used.
- Use minimal narrative; prefer symbolic precision and structured claims.
- Separate "interpretation" from "proof" to avoid mixing explanation into the argument.
- Apply [math-symbol-discipline](/media/writing/tools/math-symbol-discipline/SKILL.md) to ensure domain-appropriate notation.

## Proof voice (dense, formal)

- High density of definitions, lemmas, and constructions.
- Hypotheses and notation are enumerated explicitly before use ("Fix", "Let", "Assume").
- Proofs are short, direct, and avoid rhetorical flourish.
- Use named structures and cross-references instead of restating informal intuition.
- Prefer "Construction", "Remark", "Warning", and "Example" blocks for auxiliary material.

## Interpretation voice (clean, operational)

- Use short, declarative sentences.
- Explain what a definition is for, not just what it is.
- Avoid metaphor; use operational descriptions and measurable quantities.
- When introducing a model, name the inputs/outputs and what is being optimized or preserved.

## Example phrasing

- "Assume $T$ is a small site and $H_t$ is finite for all $t\in T$."
- "Define $UG$ as the least closure operator satisfying (i)-(iii)."
- "Proof. By Definition 2.1 and Lemma 2.3, we obtain..."
- "Construction. For each $t$ define a fiber $H_t$ and reindex along $T$."
- "Interpretation. This definition isolates the minimal objects forced by gluing."
- "Interpretation. The bound quantifies how much structure is lost under compression."
