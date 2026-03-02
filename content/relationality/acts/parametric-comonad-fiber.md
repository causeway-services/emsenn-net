---
title: Parametric Comonad Fiber
act: ParametricComonadFiber
slug: parametric-comonad-fiber
top: FixedFlowProfile
bottom: FixedFiberCategory
summary: >-
  Lift the flow comonad to each fibre by composing the flow with the
  fibre judgements.
tags:
  - act
date-created: 2025-04-01T00:00:00
---
# Parametric Comonad Fiber

The fixed flow acts as a comonad on recognitions.  We lift it to each fibre by
letting the flow witness fibre judgements:
`(FixedFlowProfile FixedFiberCategory)` earns
***ParametricComonadFiber***.