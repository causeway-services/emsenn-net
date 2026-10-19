---
title: Fixed Fiber Category
act: FixedFiberCategory
slug: fixed-fiber-category
top: FiberCategory
bottom: FixedProfileRecognitions
summary: >-
  Restrict the fibre categories further to fixed recognitions by composing
  `FiberCategory` with `FixedProfileRecognitions`.
tags:
  - act
date-created: 2025-04-01T00:00:00
---
# Fixed Fiber Category

Over each fixed context we have the general fibre categories encoded by
[FiberCategory](fiber-category.md).  Intersecting them with
[FixedProfileRecognitions](fixed-profile-recognitions.md) restricts the
judgements to the fixed profile:
`(FiberCategory FixedProfileRecognitions)` earns
***FixedFiberCategory***.