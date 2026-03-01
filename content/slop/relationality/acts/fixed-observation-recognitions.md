---
title: "Recognizing fixed Observation"
aliases:
  - "Recognizing fixed Observation"
  - "recognizing fixed observation"
act: FixedObservationRecognitions
slug: fixed-observation-recognitions
top: ProfileObservationRecognitions
bottom: FixedProfileRecognitions
summary: >-
  Further restrict the profile’s observation recognitions to the fixed subset
  by composing `ProfileObservationRecognitions` with `FixedProfileRecognitions`.
tags:
  - act---

[ProfileObservationRecognitions](profile-observation-recognitions.md) gathers
the observation witnesses permitted by the active profile, while
[FixedProfileRecognitions](fixed-profile-recognitions.md) further restricts
them to the fixed subset.  Composing them,
`(ProfileObservationRecognitions FixedProfileRecognitions)` earns
***FixedObservationRecognitions***.

The profile observation recognitions already respect the flow–nucleus filter,
and `FixedProfileRecognitions` tightens the admissible contexts to the fixed
geometry, so only fixed observations remain.


{{ act_info(page.meta) }}

{{ act_nav(page.meta) }}
