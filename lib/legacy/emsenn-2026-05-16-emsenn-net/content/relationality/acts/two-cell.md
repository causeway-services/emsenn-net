---
title: 2-Cell
act: TwoCell
slug: two-cell
top: ContextNat
bottom: FixedMorphism
summary: >-
  Define natural transformations between morphisms by composing `ContextNat`
  with `FixedMorphism`.
tags:
  - act
date-created: 2025-04-01T00:00:00
---
# 2-Cell

2-cells in the bicategory are natural transformations that respect both context
flow and spectral semantics.  We define them by composing
[ContextNat](context-nat.md) with [FixedMorphism](fixed-morphism.md):
`(ContextNat FixedMorphism)` earns ***TwoCell***.