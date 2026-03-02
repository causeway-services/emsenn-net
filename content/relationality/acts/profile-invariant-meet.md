---
title: Meeting Profile Invariants
act: ProfileInvariantMeet
slug: profile-invariant-meet
top: MeetRecognition
bottom: ProfileInvariant
summary: >-
  Restrict the meet operation to profile-invariant states by composing
  `MeetRecognition` with `ProfileInvariant`.
tags:
  - act
date-created: 2025-04-01T00:00:00
---
# Meeting Profile Invariants

`MeetRecognition = (OrderRecognition Entry)` captures greatest lower bounds.
Restricting it to [ProfileInvariant](profile-invariant.md) states gives the meet
operation on profile invariants:
`(MeetRecognition ProfileInvariant)` earns
***ProfileInvariantMeet***.