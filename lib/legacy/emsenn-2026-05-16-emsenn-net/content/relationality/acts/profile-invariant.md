---
title: Stabilizing Profile Invariant
act: ProfileInvariant
slug: profile-invariant
top: StabilizeInvariant
bottom: ProfileRecognitions
summary: >-
  Pick out physics states that are flow-invariant and lie inside the active
  profile by composing `StabilizeInvariant` with `ProfileRecognitions`.
tags:
  - act
date-created: 2025-04-01T00:00:00
---
# Stabilizing Profile Invariant

`StabilizeInvariant = (FixFlow PhysicsState)` records states left unchanged by
the global flow.  [ProfileRecognitions](profile-recognitions.md) restrict the
system to the recognitions preserved by the active filter.  Composing them,
`(StabilizeInvariant ProfileRecognitions)` earns
***ProfileInvariant***.

The resulting states are genuine physics states fixed by the flow and recognised
within the chosen profile.