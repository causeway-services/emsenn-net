---
title: Fixed Exponential
act: FixedExponential
slug: fixed-exponential
top: ProfileExponential
bottom: FixedProfileRecognitions
summary: >-
  Restrict the profile exponentials further to fixed recognitions by composing
  `ProfileExponential` with `FixedProfileRecognitions`.
tags:
  - act
date-created: 2025-04-01T00:00:00
---
# Fixed Exponential

The profile already has internal exponentials via
[ProfileExponential](profile-exponential.md).  To work entirely inside the
fixed profile we restrict those exponentials to
[FixedProfileRecognitions](fixed-profile-recognitions.md):
`(ProfileExponential FixedProfileRecognitions)` earns
***FixedExponential***.