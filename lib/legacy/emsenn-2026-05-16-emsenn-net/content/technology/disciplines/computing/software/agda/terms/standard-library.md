---
title: "standard library"
aliases:
  - "standard library"
  - "agda-stdlib"
date-created: 2026-03-01T00:00:00
tags:
  - proof-assistant
  - agda
---

The Agda standard library (`agda-stdlib`) provides formalized definitions and proofs for common mathematical and computational structures. It covers:

- **Data types**: natural numbers, integers, lists, vectors, finite sets, strings.
- **Relations**: binary relations, equivalence relations, partial orders, total orders, decidability.
- **Algebra**: monoids, groups, rings, lattices, with an algebraic hierarchy using record types.
- **Logic**: propositional logic, predicate logic, decidability, classical axioms (importable but not default).
- **Category theory**: basic definitions of categories, functors, natural transformations.

The standard library is smaller and more manually curated than Lean's [Mathlib](../../lean/terms/mathlib.md). Where Mathlib aims for broad coverage with automation, agda-stdlib emphasizes explicit, readable definitions that stay close to the underlying type theory.

For formalizing [Heyting algebras](../../../../../../mathematics/objects/posets/curricula/heyting-algebras.md) and [closure operators](../../../../../../mathematics/objects/posets/curricula/closure-operators.md), the standard library provides the algebraic hierarchy and order-theoretic foundations to build on.
