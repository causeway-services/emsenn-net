---
title: 'Lesson 2: Lattices'
id: order-theory-lesson-2
kind: curriculum-lesson
authors:
- gpt-5.2-codex
date-created: 2025-12-26
tags:
- math
---
# Lesson 2: Lattices

## Entry conditions

Use lattices only when you can:

- Start from a partial order.
- Define a meet and join for every pair of elements.
- Verify meet and join satisfy the required properties.

## Definitions

- A **lattice** is a partial order where any two elements have a meet and join.

## Vocabulary (plain language)

- **Meet**: the greatest element that is below both elements.
- **Join**: the least element that is above both elements.
- **Lower bound**: an element below both.
- **Upper bound**: an element above both.

## Symbols used

- $a \wedge b$: meet of $a$ and $b$.
- $a \vee b$: join of $a$ and $b$.

## Intuition

A lattice is an order where every pair has a "best common below" and a "best common above." It is the smallest structure where you can consistently combine two elements by taking a meet or join.

## Worked example

Let $S$ be the set of subsets of $\{x,y\}$ ordered by inclusion. The meet is intersection and the join is union. Every pair has both, so this is a lattice.

## How to recognize the structure

- You can compute $a \wedge b$ and $a \vee b$ for any pair.
- The meet is below both, and any other lower bound is below the meet.
- The join is above both, and any other upper bound is above the join.

## Common mistakes

- Assuming a lattice without defining meet and join explicitly.
- Using a "merge" operation that is not actually the least upper bound.

## Minimal data

- A set $S$ and a partial order $\leq$.
- A meet and join operation for all pairs.
