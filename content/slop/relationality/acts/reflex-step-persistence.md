---
title: "Persisting Reflex Step"
aliases:
  - "Persisting Reflex Step"
  - "persisting reflex step"
act: ReflexStepPersistence
slug: reflex-step-persistence
top: ReflexStepIterate
bottom: TailTrace
summary: >-
  Iteration alone does not detect stabilization. We therefore let the iterated
  step observe the remaining tail to see whether that remainder persists.
tags:
  - act
---

## Interpretation

Iteration alone does not detect stabilization.  We therefore let the iterated step observe the remaining tail to see whether that remainder persists.

In `(ReflexStepIterate TailTrace)` the whole iteration looks specifically at the tail.  If nothing changes, the reiteration has stabilized, so this composition rightfully earns the name *Reflex Step Persistence*.


{{ act_info(page.meta) }}

{{ act_nav(page.meta) }}
