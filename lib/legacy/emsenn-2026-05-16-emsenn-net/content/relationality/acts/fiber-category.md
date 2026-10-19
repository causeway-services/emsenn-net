---
title: Fiber Category
act: FiberCategory
slug: fiber-category
top: JudgeProfile
bottom: ProfileRecognitions
summary: >-
  Package the judgemental data of the active profile as the fibres by letting
  `JudgeProfile` witness `ProfileRecognitions`.
tags:
  - act
date-created: 2025-04-01T00:00:00
---
# Fiber Category

Every profile context carries the recognised terms, types, and judgements
assembled by [JudgeProfile](judge-profile.md).  Restricting that structure to
the active [ProfileRecognitions](profile-recognitions.md) yields the fibre
categories of our indexed semantics:
`(JudgeProfile ProfileRecognitions)` earns
***FiberCategory***.