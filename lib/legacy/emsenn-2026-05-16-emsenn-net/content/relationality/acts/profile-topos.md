---
title: Profile Topos
act: ProfileTopos
slug: profile-topos
top: FixedFiniteLimits
bottom: FixedExponential
summary: >-
  Package finite limits, exponentials, and the subobject classifier into a
  topos-like structure on the fixed profile.
tags:
  - act
date-created: 2025-04-01T00:00:00
---
# Profile Topos

Combining finite limits, exponentials, and a subobject classifier gives a
topos-like structure.  We package these components in a single act:
`(FixedFiniteLimits FixedExponential FixedSubobjectClassifier)` earns
***ProfileTopos***.

`FixedFiniteLimits` gives the limits, `FixedExponential` gives exponentials,
and `FixedSubobjectClassifier` gives the classifier Ω, satisfying the structural
requirements of a Heyting topos internal to the fixed profile.