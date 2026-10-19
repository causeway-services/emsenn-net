---
title: Entropy
act: Entropy
slug: entropy
top: ProfileEntropy
bottom: EntropyMeasure
summary: >-
  Propagate the entropy measure using the profile entropy machinery by
  composing `ProfileEntropy` with `EntropyMeasure`.
tags:
  - act
date-created: 2025-04-01T00:00:00
---
# Entropy

[ProfileEntropy](profile-entropy.md) already propagates any profile entropy
measure across the trace of recognitions.  Supplying the entropy measure,
`(ProfileEntropy EntropyMeasure)`, earns ***Entropy***,
recording the full-profile entropy under the flow–measure evolution.