---
title: "Fixed Layer"
aliases:
  - "Fixed Layer"
  - "fixed layer"
id: gfrtu-fixed-layer
kind: doc
authors:
- gpt-5.2-codex
date-created: 2025-12-26
tags:
- math---

## Definition

The **fixed layer** $H^\ast$ is the collection of recognitions that are fixed by both stabilizer and drift. At each trace $t$:
$$
H_t^\ast = \{ a \in H_t : \sigma_t(a)=a=\Delta_t(a) \}.
$$

## Plain-language meaning

These are the recognitions that are stable and also resist drift. They are the dependable core across traces.

## Minimal structure

- Stabilizer and drift on each fiber.
- Fixed points computed for each fiber.
- Reindexing maps preserve fixed points.

## Entry conditions

Use the fixed layer only when:

- Stabilizer and drift commute.
- Fixed points exist and can be computed.
- Fixed points assemble into a consistent subsheaf.

## Example

If $H_t=\{\bot < m < \top\}$ and $\Delta_t(m)=\top$, then $m$ is not fixed, but $\bot$ and $\top$ are. So $H_t^\ast=\{\bot,\top\}$.
