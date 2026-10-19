---
title: Entropy Measure
act: EntropyMeasure
slug: entropy-measure
top: ProfileEntropyMeasure
bottom: EntropySeed
summary: >-
  Collapse entropy seeds using the profile entropy machinery by composing
  `ProfileEntropyMeasure` with `EntropySeed`.
tags:
  - act
date-created: 2025-04-01T00:00:00
---
# Entropy Measure

[ProfileEntropyMeasure](profile-entropy-measure.md) already collapses entropy
seeds using the profile nucleus.  Supplying the entropy seed,
`(ProfileEntropyMeasure EntropySeed)` earns
***EntropyMeasure***,
giving the fixed entropy measure.