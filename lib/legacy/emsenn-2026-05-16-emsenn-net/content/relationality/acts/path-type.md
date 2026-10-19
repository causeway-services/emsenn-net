---
title: Path Type
act: PathType
slug: path-type
top: FlowProfile
bottom: RecognizeContext
summary: >-
  Define profile paths by letting the default flow witness context recognitions.
tags:
  - act
date-created: 2025-04-01T00:00:00
---
# Path Type

Paths in homotopy type theory correspond to maps from the unit interval.  In the
profile setting, the base flow generates canonical time evolution, so we define
paths by composing the flow with context recognition:
`(FlowProfile RecognizeContext)` earns
***PathType***.