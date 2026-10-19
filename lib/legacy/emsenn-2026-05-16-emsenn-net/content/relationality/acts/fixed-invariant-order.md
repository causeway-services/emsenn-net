---
title: Ordering Fixed Invariant
act: FixedInvariantOrder
slug: fixed-invariant-order
top: ProfileInvariantOrder
bottom: FixedInvariant
summary: >-
  Restrict the invariant order further to fixed states by composing
  `ProfileInvariantOrder` with `FixedInvariant`.
tags:
  - act
date-created: 2025-04-01T00:00:00
---
# Ordering Fixed Invariant

`ProfileInvariantOrder = (OrderRecognition ProfileInvariant)` already restricts
the recognition order to profile invariants.  [FixedInvariant](fixed-invariant.md)
further limits us to the fixed-invariant physics states.  Composing them,
`(ProfileInvariantOrder FixedInvariant)` earns
***FixedInvariantOrder***.

`FixedInvariant` is a collection of recognitions that are both flow-fixed and
fixed-profile-stable.  Restricting the profile order along these recognitions
yields the partial order underlying the fixed statespace geometry.