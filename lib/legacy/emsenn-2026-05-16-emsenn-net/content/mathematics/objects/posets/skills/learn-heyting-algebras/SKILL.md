---
name: learn-heyting-algebras
description: >-
  Compute Heyting implication in a finite lattice, determine whether a lattice
  is a Heyting algebra, and explain why excluded middle fails in the general case.
kind: skill
skill-kind: learning
date-created: 2026-03-01
tags:
  - mathematics
  - order-theory
  - logic
---

# Learn Heyting Algebras

## What you will be able to do

- Given a finite bounded lattice, compute the Heyting implication $a \Rightarrow b$ by finding the largest element $c$ such that $c \wedge a \leq b$.
- Determine whether a given bounded lattice is a Heyting algebra by checking that the implication operation exists for every pair of elements.
- Compute pseudocomplements ($\neg a = a \Rightarrow \bot$) and show whether $a \vee \neg a = \top$ holds — that is, whether excluded middle holds for a given element.
- Explain in plain language why Heyting algebras are the natural algebraic setting for constructive (intuitionistic) reasoning, where not every proposition need be true or false.

## Prerequisites

- **learn-partial-orders** — the definition of a partial order, meets and joins, and the ability to check whether a poset is a lattice (you need all of this to work with the lattice structures that Heyting algebras extend)

## Lessons

- [[heyting-algebras|Heyting Algebras]] — the definition, the residuation law, pseudocomplements, the connection to intuitionistic logic, and the Sierpinski space as a worked example

[Gap: the existing `lattices` lesson (`content/mathematics/objects/posets/curricula/lattices.md`) is a thin stub in the old format. It defines meets and joins but does not follow backward design, has no self-check exercises, and gives only one worked example. A proper lattices lesson — sitting between partial orders and Heyting algebras — would strengthen this skill's prerequisite chain. For now, the Heyting algebras lesson itself reviews the necessary lattice concepts.]

This is a single lesson. Work through it fully, including computing the implication table for the Sierpinski space example.

## Scope

This skill covers Heyting algebras as algebraic structures: the definition, the implication operation, pseudocomplements, and the distinction from Boolean algebras. It does not cover:

- The full theory of intuitionistic logic (the logical system whose algebraic semantics is a Heyting algebra — that is a separate skill)
- Heyting algebras in topos theory (the subobject classifier — this requires category theory prerequisites not covered here)
- The role of Heyting algebras in the semiotic universe (covered by **learn-semiotic-universe**, which depends on this skill plus others)
- Stone duality or representation theorems for Heyting algebras

## Verification

Given the three-element chain $\{0, a, 1\}$ with $0 < a < 1$: compute the full implication table (all nine values of $x \Rightarrow y$), find the pseudocomplement of $a$, and determine whether this is a Boolean algebra. (Hint: check whether $a \vee \neg a = 1$.)
