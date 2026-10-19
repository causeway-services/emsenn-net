---
title: Seeding Profile Entropy
act: ProfileEntropySeed
slug: profile-entropy-seed
top: ProfileKernelStep
bottom: ProfileReach
summary: >-
  Seed an entropy measure by comparing profile kernel updates against reachable
  states via `ProfileKernelStep` witnessing `ProfileReach`.
tags:
  - act
date-created: 2025-04-01T00:00:00
---
# Seeding Profile Entropy

Entropy measures the “spread” of a state under transitions.  We seed profile
entropy by observing the divergence between a state and its profile kernel
successor.  Letting [ProfileKernelStep](profile-kernel-step.md) witness
[ProfileReach](profile-reach.md),
`(ProfileKernelStep ProfileReach)`, earns
***ProfileEntropySeed***.