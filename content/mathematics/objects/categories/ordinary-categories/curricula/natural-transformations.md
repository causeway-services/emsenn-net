---
title: "Natural Transformations"
aliases:
  - "Natural Transformations"
id: category-theory-lesson-3
kind: curriculum-lesson
authors:
- gpt-5.2-codex
date-created: 2025-12-26
tags:
- math
---

## Entry conditions

Use natural transformations only when you already have:

- Two functors $F, G:C \to D$ between the same categories.
- A morphism in $D$ for each object of $C$.
- A requirement that these morphisms are compatible with all morphisms in $C$.

## Definitions

- A **natural transformation** $\eta:F \Rightarrow G$ assigns to each object $A$ in $C$ a morphism $\eta_A: F(A) \to G(A)$ in $D$, such that for every morphism $f:A \to B$ in $C$,
$$
G(f) \circ \eta_A = \eta_B \circ F(f).
$$

## Vocabulary (plain language)

- **Component**: the specific morphism $\eta_A$ for an object $A$.
- **Naturality**: the condition that the square above commutes for every morphism.

## Symbols used

- $\eta:F \Rightarrow G$: a natural transformation.
- $\eta_A$: the component at $A$.

## Intuition

A natural transformation is a systematic way to transform one functor into another without breaking structure. It says that the transformation is compatible with every morphism in the source category.

## Worked example

Let $F,G:\mathbf{Set} \to \mathbf{Set}$ both map a set to a product with a fixed set. The projection maps form a natural transformation because they commute with all functions between sets.

## How to recognize the structure

- You can assign a component morphism for every object.
- The naturality square commutes for every morphism.

## Common mistakes

- Defining components without checking naturality.
- Using different categories for $F$ and $G$.

## Minimal data

- Two functors $F$ and $G$ with the same source and target.
- A component morphism for each object.
- A proof of the naturality condition.
