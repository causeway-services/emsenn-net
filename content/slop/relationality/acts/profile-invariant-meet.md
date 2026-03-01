---
title: "Meeting Profile invariants"
aliases:
  - "Meeting Profile invariants"
  - "meeting profile invariants"
act: ProfileInvariantMeet
slug: profile-invariant-meet
top: MeetRecognition
bottom: ProfileInvariant
summary: >-
  Restrict the meet operation to profile-invariant states by composing
  `MeetRecognition` with `ProfileInvariant`.
tags:
  - act
---

`MeetRecognition = (OrderRecognition Entry)` captures greatest lower bounds.
Restricting it to [ProfileInvariant](profile-invariant.md) states gives the meet
operation on profile invariants:
`(MeetRecognition ProfileInvariant)` earns
***ProfileInvariantMeet***.


{{ act_info(page.meta) }}

{{ act_nav(page.meta) }}
