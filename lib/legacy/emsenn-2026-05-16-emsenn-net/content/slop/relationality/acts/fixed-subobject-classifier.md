---
title: "Fixed subobject classifier"
aliases:
  - "Fixed subobject classifier"
  - "fixed subobject classifier"
act: FixedSubobjectClassifier
slug: fixed-subobject-classifier
top: ProfileSubobjectClassifier
bottom: FixedProfileRecognitions
summary: >-
  Restrict the profile’s truth object to fixed recognitions by composing
  `ProfileSubobjectClassifier` with `FixedProfileRecognitions`.
tags:
  - act
---

The profile already carries an internal truth object via
[ProfileSubobjectClassifier](profile-subobject-classifier.md).  To reason purely
inside the fixed profile we restrict that classifier to
[FixedProfileRecognitions](fixed-profile-recognitions.md):
`(ProfileSubobjectClassifier FixedProfileRecognitions)` earns
***FixedSubobjectClassifier***.


{{ act_info(page.meta) }}

{{ act_nav(page.meta) }}
