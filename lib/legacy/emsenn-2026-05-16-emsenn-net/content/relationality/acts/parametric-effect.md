---
title: Parametric Effect Monad
act: ParametricEffect
slug: parametric-effect
top: ParametricMonadFiber
bottom: ParametricMonadReindex
summary: >-
  Combine the fibrewise monad with its reindexing compatibility to obtain the
  indexed effect monad on fixed contexts.
tags:
  - act
date-created: 2025-04-01T00:00:00
---
# Parametric Effect Monad

Combining the fibrewise monad and its compatibility with reindexing yields the
full indexed monad describing parametric effects:
`(ParametricMonadFiber ParametricMonadReindex)` earns
***ParametricEffect***.