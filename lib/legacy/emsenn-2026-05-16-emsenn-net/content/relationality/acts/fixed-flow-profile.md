---
title: Fixed Flow Profile
act: FixedFlowProfile
slug: fixed-flow-profile
top: ShuffleFlow
bottom: FixedProfileRecognitions
summary: >-
  Restrict the shuffle flow to the fixed-profile recognitions by letting
  `ShuffleFlow` witness `FixedProfileRecognitions`.
tags:
  - act
date-created: 2025-04-01T00:00:00
---
# Fixed Flow Profile

`FlowProfile = (Flow ProfileRecognitions)` restricts the global flow to a given
profile.  To specialize this to the fixed-profile recognitions we let
[ShuffleFlow](shuffle-flow.md) witness
[FixedProfileRecognitions](fixed-profile-recognitions.md):
`(ShuffleFlow FixedProfileRecognitions)` earns
***FixedFlowProfile***.

`ShuffleFlow` evolves admissible trace-shuffle classes along evaluation
contexts, and `FixedProfileRecognitions` picks out recognitions stabilized by
the same dynamics and fixed shape.  The composition restricts the shuffle
flow to this profile, yielding a dynamics where every state evolves according to
that trace structure while preserving the fixed shape.