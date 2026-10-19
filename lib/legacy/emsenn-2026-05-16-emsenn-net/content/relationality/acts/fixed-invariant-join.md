---
title: Joining Fixed Invariant
act: FixedInvariantJoin
slug: fixed-invariant-join
top: ProfileInvariantJoin
bottom: FixedInvariant
summary: >-
  Restrict the join operation to fixed invariant states by composing
  `ProfileInvariantJoin` with `FixedInvariant`.
tags:
  - act
date-created: 2025-04-01T00:00:00
---
# Joining Fixed Invariant

`ProfileInvariantJoin = (JoinRecognition ProfileInvariant)` captures the least
recognition containing a pair of profile invariants.  Restricting it via
[FixedInvariant](fixed-invariant.md) yields the join of fixed invariant
states:
`(ProfileInvariantJoin FixedInvariant)` earns ***FixedInvariantJoin***.

`ProfileInvariantJoin` works relative to the restricted order, and
`FixedInvariant` narrows the domain to the fixed subset, producing the least
fixed invariant containing the given pair.