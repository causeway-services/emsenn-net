---
title: "Presheaves"
aliases:
  - "Presheaves"
id: sheaf-theory-lesson-2
kind: curriculum-lesson
authors:
- gpt-5.2-codex
date-created: 2025-12-26
tags:
- math
---

## Entry conditions

Use presheaves only when you can:

- Start from a site $(C,J)$ or at least a category $C$ of contexts.
- Assign data to each object in $C$.
- Define restriction maps along morphisms.

## Definitions

- A **presheaf** on a category $C$ assigns to each object $U$ a set $F(U)$, and to each morphism $f:V \to U$ a restriction map $F(f):F(U) \to F(V)$, satisfying identity and composition laws.

## Vocabulary (plain language)

- **Section**: an element of $F(U)$, i.e., data on $U$.
- **Restriction**: a way to move data from a larger context to a smaller one.

## Symbols used

- $F$: a presheaf.
- $F(U)$: the data assigned to object $U$.
- $F(f)$: the restriction map along $f$.

## Intuition

A presheaf is a bookkeeping system for data on each context, together with rules for how to restrict data when you move to a smaller context.

## Worked example

Let $C$ be the category of open sets of a space. A presheaf can assign to each open set $U$ the set of real-valued functions on $U$, and restriction maps are literal restriction of functions to smaller open sets.

## How to recognize the structure

- You can assign data to every object.
- You can restrict data along every morphism.
- Restrictions compose correctly.

## Common mistakes

- Defining restrictions that do not compose.
- Forgetting to define restrictions for some morphisms.

## Minimal data

- A category $C$.
- A set assignment $U \mapsto F(U)$.
- Restriction maps for every morphism.
