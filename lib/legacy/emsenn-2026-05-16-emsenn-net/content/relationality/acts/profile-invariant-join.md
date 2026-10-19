---
title: Joining Profile Invariants
act: ProfileInvariantJoin
slug: profile-invariant-join
top: JoinRecognition
bottom: ProfileInvariant
summary: >-
  Restrict the join operation to profile-invariant states by composing
  `JoinRecognition` with `ProfileInvariant`.
tags:
  - act
date-created: 2025-04-01T00:00:00
---
# Joining Profile Invariants

`JoinRecognition = (OrderRecognition ContextualizeTrace)` captures least upper
bounds.  Restricting it to [ProfileInvariant](profile-invariant.md) gives the
join on profile invariants:
`(JoinRecognition ProfileInvariant)` earns
***ProfileInvariantJoin***.