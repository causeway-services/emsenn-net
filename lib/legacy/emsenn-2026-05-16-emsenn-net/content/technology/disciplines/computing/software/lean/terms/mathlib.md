---
title: "Mathlib"
aliases:
  - "Mathlib"
  - "mathlib"
date-created: 2026-03-01T00:00:00
tags:
  - proof-assistant
  - lean
  - mathematics
---

Mathlib is Lean's primary library of formalized mathematics, maintained as an open-source project. It contains formalized definitions, theorems, and proofs spanning algebra (groups, rings, fields, modules), order theory (lattices, complete lattices, Galois connections), topology, analysis, number theory, category theory, and combinatorics.

For this project, Mathlib is relevant because it already formalizes many of the structures the [Semiotic Universe](../../../../../../mathematics/objects/universes/semiotic-universe/index.md) builds on:

- Complete lattices and Heyting algebras (`Mathlib.Order.Heyting`, `Mathlib.Order.CompleteLattice`)
- Closure operators (`Mathlib.Order.Closure`)
- Fixed-point theorems (`Mathlib.Order.FixedPoints`)
- Category theory foundations (`Mathlib.CategoryTheory`)

Using Mathlib means building on verified foundations rather than re-formalizing standard mathematics from scratch.

## Related terms

- [tactic](tactic.md) — Mathlib extends Lean's tactic set with `linarith`, `ring`, `omega`, `aesop`, `norm_num`, and others
