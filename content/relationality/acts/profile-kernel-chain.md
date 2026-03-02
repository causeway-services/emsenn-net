---
title: Profile Kernel Chain
act: ProfileKernelChain
slug: profile-kernel-chain
top: ProfileKernelStep
bottom: TraceProfile
summary: >-
  Build the kernel chain across profiles by letting `ProfileKernelStep` witness
  `TraceProfile`.
tags:
  - act
date-created: 2025-04-01T00:00:00
---
# Profile Kernel Chain

A kernel chain repeatedly applies the observation kernel across layers.  Having
a profile-step kernel ([ProfileKernelStep](profile-kernel-step.md)), we obtain
the profile chain by iterating the chain recogniser `TraceProfile`.  Letting the
step witness the trace,
`(ProfileKernelStep TraceProfile)`, earns ***ProfileKernelChain***.

`TraceProfile = (CompleteTrace ProfileRecognitions)` projects traces through the
profile recognitions, and `ProfileKernelStep` updates one profile to the next.
Their composition yields the recognitional chain that threads updates through
the trace of profiles.