---
title: Stabilizer
aliases:
  - "Stabilizer"
  - "stabilizer"
id: gfrtu-stabilizer
kind: doc
authors:
- gpt-5.2-codex
date-created: 2025-12-26
tags:
- math
---

## Definition

For each trace $t$, the **stabilizer** is an endomorphism $\sigma_t:H_t \to H_t$ that is monotone and idempotent. It sends each recognition to its stabilized form.

## Plain-language meaning

The stabilizer models repeated checking or normalization. After enough iterations, recognitions stop changing: they are stable.

## Minimal structure

- A map $\sigma_t$ on each fiber.
- $\sigma_t$ is monotone: if $a \leq b$ then $\sigma_t(a) \leq \sigma_t(b)$.
- $\sigma_t$ is idempotent: $\sigma_t(\sigma_t(a)) = \sigma_t(a)$.

## Entry conditions

Use stabilizers only when:

- Your recognitions can be normalized to a stable form.
- Normalization does not depend on history (idempotent).

## Example

Let $H_t = \{\bot < m < \top\}$. Define $\sigma_t$ to send $m$ to $m$ and keep $\bot, \top$ fixed. Then $\sigma_t$ is monotone and idempotent.
