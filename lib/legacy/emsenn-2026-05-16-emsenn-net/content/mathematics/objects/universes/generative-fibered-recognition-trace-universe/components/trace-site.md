---
title: "Trace Site"
aliases:
  - "Trace Site"
  - "trace site"
id: gfrtu-trace-site
kind: doc
authors:
- gpt-5.2-codex
date-created: 2025-12-26
tags:
- math
---

## Definition

A **trace site** is a small category $T$ together with a Grothendieck topology $J$. The objects of $T$ are **traces** (finite observational contexts), and the topology $J$ declares which families of morphisms count as **covers** of a trace.

## Plain-language meaning

A trace site names the local contexts you can observe and how they relate. The topology tells you which families of local contexts are enough to reconstruct a bigger context.

## Minimal structure

- A list of traces (objects).
- A list of refinement or transport steps between traces (morphisms).
- A rule saying which families of morphisms cover a trace.

## Entry conditions

Use a trace site only when:

- You can identify discrete traces or contexts.
- You can define how one trace refines or maps to another.
- You can state when a family of refinements is enough to cover a trace.

## Example

Let $T$ have objects $t_0, t_1$ and a morphism $n:t_0 \to t_1$ (plus identities). Let $J$ be the trivial topology where only identity covers exist. This is a valid trace site.
