---
title: Irrational Commutation
act: IrrationalCommutation
slug: irrational-commutation
top: IrrationalModality
bottom: CollapseShuffle
summary: >-
  Ensure irrational modalities commute with shuffle collapse by composing them
  with `CollapseShuffle`.
tags:
  - act
date-created: 2025-04-01T00:00:00
---
# Irrational Commutation

For a modality indexed by an irrational α to behave coherently, it must commute
with the nucleus under admissible reordering collapse.  We enforce this via
`(IrrationalModality CollapseShuffle)`, earning
***IrrationalCommutation***.

`CollapseShuffle` identifies recognitions that differ only by reorderings, and
`IrrationalModality` scales the space of reorderings while preserving
their structure.  The composition asserts that irrational scaling preserves
collapse-equivalence.