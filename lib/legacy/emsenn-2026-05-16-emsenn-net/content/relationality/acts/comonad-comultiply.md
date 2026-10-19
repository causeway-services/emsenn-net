---
title: Comonad Comultiplication
act: ComonadComultiply
slug: comonad-comultiply
top: FixedFlowProfile
bottom: FixedFlowProfile
summary: >-
  Duplicate the flow co-structure by composing the flow with itself,
  yielding the comultiplication.
tags:
  - act
date-created: 2025-04-01T00:00:00
---
# Comonad Comultiplication

Comultiplication duplicates context: from one flow we obtain a “flowed flow” by
letting the flow observe itself:
`(FixedFlowProfile FixedFlowProfile)` earns
***ComonadComultiply***.

Applying the flow twice corresponds to extending the co-context one more
step, so the act records `δ_X : G(X) → G(G(X))`.