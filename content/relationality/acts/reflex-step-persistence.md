---
title: Persisting Reflex Step
act: ReflexStepPersistence
slug: reflex-step-persistence
top: ReflexStepIterate
bottom: TailTrace
summary: >-
  Iteration alone does not detect stabilization. We therefore let the iterated
  step observe the remaining tail to see whether that remainder persists.
tags:
  - act
date-created: 2025-04-01T00:00:00
---
# Persisting Reflex Step

## Interpretation

Iteration alone does not detect stabilization.  We therefore let the iterated step observe the remaining tail to see whether that remainder persists.

In `(ReflexStepIterate TailTrace)` the whole iteration looks specifically at the tail.  If nothing changes, the reiteration has stabilized, so this composition rightfully earns the name *Reflex Step Persistence*.