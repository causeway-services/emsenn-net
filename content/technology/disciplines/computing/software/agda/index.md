---
title: "Agda"
aliases:
  - "Agda"
  - "agda"
date-created: 2026-03-01T00:00:00
tags:
  - proof-assistant
  - programming-languages
  - formal-methods
---

Agda is a dependently typed functional programming language and proof assistant based on Martin-Löf type theory. Unlike tactic-based systems, Agda proofs are written as programs directly — there is no separate tactic language. The type checker verifies that every function is total (terminates on all inputs and covers all cases), and the propositions-as-types principle means that writing a well-typed program of type $P$ is the same as proving $P$.

Agda's design emphasizes explicit proof terms, dependent pattern matching, and a close correspondence with the underlying type theory. This makes it a natural environment for constructive and [intuitionistic](../../../../../mathematics/disciplines/logic/curricula/intuitionistic-logic.md) mathematics, where proofs carry computational content.

## Why Agda for this project

The mathematical structures underlying the [Semiotic Universe](../../../../../mathematics/objects/universes/semiotic-universe/index.md) are rooted in intuitionistic logic and [Heyting algebras](../../../../../mathematics/objects/posets/curricula/heyting-algebras.md). Agda's type theory is natively intuitionistic — excluded middle is not assumed, and every proof is a construction. This makes Agda well-suited to formalizing structures where the intuitionistic character is part of the point.

Where [Lean](../lean/index.md) offers a large library (Mathlib) and powerful automation, Agda offers a closer connection to type theory and explicit control over proof structure. Both tools are valuable; they complement each other.

## Contents

- [Curricula](curricula/index.md) — structured lessons for learning Agda
- [Terms](terms/index.md) — glossary of Agda-specific concepts
- [Skills](skills/index.md) — operational skills for writing Agda proofs
