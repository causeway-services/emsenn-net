---
title: Fixed Chain
act: FixedChain
slug: fixed-chain
top: EnsureFixedPoint
bottom: ProfileKernelChain
summary: >-
  Apply the fixed-point construction to the profile kernel chain to obtain its
  stationary profile-level distribution.
tags:
  - act
date-created: 2025-04-01T00:00:00
---
# Fixed Chain

A stationary chain is one whose profile-level transitions stabilise.
`ProfileKernelChain` iterates the kernel update across profiles, so we
apply the fixed-point machinery via [EnsureFixedPoint](ensure-fixed-point.md):
`(EnsureFixedPoint ProfileKernelChain)` earns
***FixedChain***.

`IterativePersistence` ensures that persistent iteration produces a stabilised
profile.  The composite therefore yields the stationary chain: a
profile-level distribution that remains unchanged after any flow–measure
update.