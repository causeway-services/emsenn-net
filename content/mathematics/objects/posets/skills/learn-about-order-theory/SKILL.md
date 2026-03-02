---
name: learn-partial-orders
description: >-
  Determine whether a relation is a partial order, compute meets and joins in
  a finite lattice, and draw Hasse diagrams.
kind: skill
skill-kind: learning
date-created: 2026-03-01
tags:
  - mathematics
  - order-theory
---

# Learn Partial Orders

## What you will be able to do

- Given a relation on a finite set, determine whether it is a partial order by checking reflexivity, antisymmetry, and transitivity.
- Draw a Hasse diagram for a finite partial order.
- Given a finite lattice, compute the meet and join of two elements.
- Identify whether a poset is a lattice, a bounded lattice, or a complete lattice.

## Prerequisites

None. This skill is a starting point. It requires comfort with sets and relations (what a set is, what a binary relation is) but no formal training.

## Lessons

[Gap: no lesson on partial orders exists yet that follows the lesson design principles (backward design, concrete-before-abstract, exercises). The existing `heyting-algebras` lesson in `mathematics/objects/posets/curricula/` covers Heyting algebras but assumes partial orders are already known. A dedicated partial orders lesson needs to be written.]

When that lesson exists, it should cover: the definition via three axioms checked against concrete examples (divisibility, subset inclusion, ancestry), Hasse diagrams as a tool for visualization, and meets/joins as greatest lower bound and least upper bound.

## Scope

This skill covers partial orders, lattices, and basic lattice operations. It does not cover:

- Heyting algebras or Boolean algebras (covered by **learn-heyting-algebras**, which depends on this skill)
- Closure operators (covered by a separate skill, also depending on this one)
- Order-preserving maps, Galois connections, or domain theory
- Total orders, well-orders, or ordinals

## Verification

Given the divisibility relation on {1, 2, 3, 4, 6, 12}: draw its Hasse diagram, compute the meet and join of 4 and 6, and determine whether this poset is a lattice.
