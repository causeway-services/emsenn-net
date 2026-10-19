---
title: Ordering Profile Invariants
act: ProfileInvariantOrder
slug: profile-invariant-order
top: OrderRecognition
bottom: ProfileInvariant
summary: >-
  Restrict the recognition order to profile-invariant states by composing
  `OrderRecognition` with `ProfileInvariant`.
tags:
  - act
date-created: 2025-04-01T00:00:00
---
# Ordering Profile Invariants

`OrderRecognition = (RecognizeContext Recognition)` records when one recognition
subsumes another.  [ProfileInvariant](profile-invariant.md) picks out the
flow-fixed physics states that lie in the active profile.  Composing them,
`(OrderRecognition ProfileInvariant)` earns
***ProfileInvariantOrder***.

This restricts the ambient order to the profile-invariant states.