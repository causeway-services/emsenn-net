---
title: Drift
aliases:
  - "Drift"
  - "drift"
id: gfrtu-drift
kind: doc
authors:
- gpt-5.2-codex
date-created: 2025-12-26
tags:
- math
---

## Definition

For each trace $t$, **drift** is an endomorphism $\Delta_t:H_t \to H_t$ that is monotone and inflationary. It models how recognitions shift over time or context.

## Plain-language meaning

Drift captures unavoidable change. Even if a recognition is stable under normalization, it may still drift as context changes.

## Minimal structure

- A map $\Delta_t$ on each fiber.
- $\Delta_t$ is monotone.
- $\Delta_t$ is inflationary: $a \leq \Delta_t(a)$.

## Entry conditions

Use drift only when:

- Recognitions change in a predictable, monotone direction.
- "Change" is not arbitrary but can be modeled by a fixed map.

## Example

Let $H_t = \{\bot < m < \top\}$. Define $\Delta_t(\bot)=\bot$, $\Delta_t(m)=\top$, and $\Delta_t(\top)=\top$. This is monotone and inflationary.
