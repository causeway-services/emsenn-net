---
title: Recognizing Fixed Observation
act: FixedObservationRecognitions
slug: fixed-observation-recognitions
top: ProfileObservationRecognitions
bottom: FixedProfileRecognitions
summary: >-
  Further restrict the profile’s observation recognitions to the fixed subset
  by composing `ProfileObservationRecognitions` with `FixedProfileRecognitions`.
tags:
  - act
date-created: 2025-04-01T00:00:00
---
# Recognizing Fixed Observation

[ProfileObservationRecognitions](profile-observation-recognitions.md) gathers
the observation witnesses permitted by the active profile, while
[FixedProfileRecognitions](fixed-profile-recognitions.md) further restricts
them to the fixed subset.  Composing them,
`(ProfileObservationRecognitions FixedProfileRecognitions)` earns
***FixedObservationRecognitions***.

The profile observation recognitions already respect the flow–nucleus filter,
and `FixedProfileRecognitions` tightens the admissible contexts to the fixed
geometry, so only fixed observations remain.