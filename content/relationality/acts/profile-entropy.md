---
title: Profile Entropy
act: ProfileEntropy
slug: profile-entropy
top: TraceProfile
bottom: ProfileEntropyMeasure
summary: >-
  Propagate the profile entropy measure across the trace by composing
  `TraceProfile` with `ProfileEntropyMeasure`.
tags:
  - act
date-created: 2025-04-01T00:00:00
---
# Profile Entropy

To obtain the entropy of a full profile we propagate the entropy measure across
the trace of recognitions inside that profile.
[TraceProfile](trace-profile.md) records the trace structure, so letting it
witness [ProfileEntropyMeasure](profile-entropy-measure.md),
`(TraceProfile ProfileEntropyMeasure)`, earns
***ProfileEntropy***.