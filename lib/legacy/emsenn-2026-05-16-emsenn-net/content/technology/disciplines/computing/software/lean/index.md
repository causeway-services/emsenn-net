---
title: "Lean"
aliases:
  - "Lean"
  - "Lean 4"
  - "lean"
date-created: 2026-03-01T00:00:00
tags:
  - proof-assistant
  - programming-languages
  - formal-methods
---

Lean is an interactive theorem prover and functional programming language developed at Microsoft Research. Its type system is based on the Calculus of Inductive Constructions — a dependent type theory where propositions are types and proofs are programs. Lean's kernel is small and trusted; the elaborator and tactic framework build proof terms that the kernel checks independently.

Lean 4 is the current version, rewritten as a self-hosting compiler with a powerful metaprogramming system. Its primary mathematical library, [Mathlib](terms/mathlib.md), contains hundreds of thousands of lines of formalized mathematics covering algebra, analysis, topology, number theory, and category theory.

## Why Lean for this project

The mathematical structures underlying the [Semiotic Universe](../../../../../mathematics/objects/universes/semiotic-universe/index.md) — [Heyting algebras](../../../../../mathematics/objects/posets/curricula/heyting-algebras.md), [closure operators](../../../../../mathematics/objects/posets/curricula/closure-operators.md), typed operator algebras — are the kind of structures Lean and Mathlib handle well. Lean provides a path to machine-checked proofs of the vault's mathematical claims.

## Contents

- [Curricula](curricula/index.md) — structured lessons for learning Lean 4
- [Terms](terms/index.md) — glossary of Lean-specific concepts
- [Skills](skills/index.md) — operational skills for writing Lean proofs
