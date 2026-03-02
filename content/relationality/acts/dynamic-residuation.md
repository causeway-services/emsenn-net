---
title: Dynamic Residuation
act: DynamicResiduation
slug: dynamic-residuation
top: FlowIndexImplication
bottom: ContextGeometry
summary: >-
  Restrict dynamic residuation to the context geometry by letting
  `FlowIndexImplication` witness `ContextGeometry`.
tags:
  - act
date-created: 2025-04-01T00:00:00
---
# Dynamic Residuation

Dynamic residuation states that flowing a context and then testing implication
is equivalent to testing implication against a closed context.  We express this
by composing [FlowIndexImplication](flow-index-implication.md) with
[ContextGeometry](context-geometry.md):
`(FlowIndexImplication ContextGeometry)` earns
***DynamicResiduation***.

The act records that the law “`c ≤ a ⇒_F b` iff `F(c ∧ a) ≤ b`” continues to
hold when both sides are restricted to the context flow and nucleus.