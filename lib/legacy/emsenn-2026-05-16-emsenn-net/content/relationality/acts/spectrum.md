---
title: Spectrum
act: Spectrum
slug: spectrum
top: TraceProfile
bottom: SpectrumMap
summary: >-
  Evaluate the spectral map across the profile trace by composing
  `TraceProfile` with `SpectrumMap`.
tags:
  - act
date-created: 2025-04-01T00:00:00
---
# Spectrum

A full spectrum requires evaluating the spectral map across the trace of a
profile, so we let [TraceProfile](trace-profile.md) witness
[SpectrumMap](spectrum-map.md):
`(TraceProfile SpectrumMap)` earns ***Spectrum***.

`SpectrumMap` contains eigencomponents of the observation kernel, and
`TraceProfile` threads these through all profile recognitions.  Their
composition produces the spectrum of the profile.