---
title: "Enriched Categories"
aliases:
  - "Enriched Categories"
id: enriched-categories-lesson-enriched-categories
kind: lesson
authors:
- gpt-5.2-codex
date-created: 2025-12-31
tags:
- mathematics
- category-theory
- enriched-categories
dependencies:
- /mathematics/structures/categories/enriched-categories/curricula/monoidal-categories.md
- /mathematics/structures/categories/enriched-categories/terms/index.md
---


An enriched category replaces hom-sets with hom-objects from a fixed monoidal
category.

## Data

An enriched category over a monoidal category `V` has:

- A class of objects.
- For each pair of objects `(x, y)`, a hom-object `V(x, y)` in `V`.
- Composition maps `V(y, z) tensor V(x, y) -> V(x, z)`.
- Unit maps `I -> V(x, x)`.

## Why this matters

Enrichment lets morphisms carry structure such as topology, probability, or
order, instead of being just elements of a set.
