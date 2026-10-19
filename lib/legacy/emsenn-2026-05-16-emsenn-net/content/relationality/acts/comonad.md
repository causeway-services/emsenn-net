---
title: Comonad
act: Comonad
slug: comonad
top: ComonadCounit
bottom: ComonadComultiply
summary: >-
  Package the fixed flow functor, counit, and comultiplication into a comonad
  on the profile.
tags:
  - act
date-created: 2025-04-01T00:00:00
---
# Comonad

The fixed flow functor together with its counit and comultiplication forms a
comonad, so we collect the laws in a single act:
`(ComonadCounit ComonadComultiply)` earns
***Comonad***.

The coassociativity and counit laws follow from the flow compatibility and
persistence properties already recorded (e.g. `IterativePersistence`,
`FixFlow`, `EnsureFixedPoint`).  `ComonadCounit` and
`ComonadComultiply` are the structure maps; `Comonad` names the
resulting co-KZ-style comonad.