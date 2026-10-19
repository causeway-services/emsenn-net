---
title: Reindexing
act: Reindexing
slug: reindexing
top: SubstituteReducibility
bottom: IndexBase
summary: >-
  Describe how context morphisms pull back judgements by restricting
  substitution reducibility to the indexed base.
tags:
  - act
date-created: 2025-04-01T00:00:00
---
# Reindexing

Given a morphism of contexts we can transport judgements along it.
`SubstituteReducibility = (BuildReducibleEnvironment JudgeTyping)` shows that
substitution preserves typing and entailment.  Restricting this behaviour to the
indexed base,
`(SubstituteReducibility IndexBase)`, earns
***Reindexing***.