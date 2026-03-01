---
title: "Monoids and Homomorphisms"
aliases:
  - "Monoids and Homomorphisms"
id: prealgebra-lesson-monoids-homomorphisms
kind: lesson
authors:
- gpt-5.2-codex
date-created: 2025-12-31
tags:
- mathematics
- prealgebra
- algebra
dependencies:
- /mathematics/structures/prealgebra/curricula/magmas-semigroups.md
- /mathematics/structures/prealgebra/terms/index.md---


Monoids add an identity element, and homomorphisms describe structure-preserving
maps between monoids.

## Monoid

A monoid is a semigroup with an identity element `e` such that `e * a = a` and
`a * e = a` for all `a` in the set.

Example: The natural numbers with addition form a monoid, with identity `0`.

## Homomorphism

Given monoids `(M, *)` and `(N, o)`, a homomorphism `f : M -> N` preserves the
operation: `f(a * b) = f(a) o f(b)` for all `a, b` in `M`.

Homomorphisms let us compare algebraic structures while respecting their
operations.
