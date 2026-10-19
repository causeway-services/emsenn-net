---
title: Parametric Monad Reindexing
act: ParametricMonadReindex
slug: parametric-monad-reindex
top: Reindexing
bottom: ParametricMonadFiber
summary: >-
  Enforce compatibility between reindexing and the fibrewise monad by letting
  reindexing witness the monad action.
tags:
  - act
date-created: 2025-04-01T00:00:00
---
# Parametric Monad Reindexing

Indexed monads require reindexing to commute with the monadic action.
[Reindexing](reindexing.md) transports judgements along context morphisms, and
[ParametricMonadFiber](parametric-monad-fiber.md) applies the closure in each
fibre.  Their composition, `(Reindexing ParametricMonadFiber)`, earns
***ParametricMonadReindex***.