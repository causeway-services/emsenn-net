---
title: "Reading and writing rule texts"
aliases:
  - "Reading and writing rule texts"
id: card-games-lesson-reading-writing-rule-texts
kind: lesson
authors:
- gpt-5.2-codex
date-created: 2026-03-01T00:00:00
tags:
- card-games
dependencies:
- /study/card-games/terms/index.md
---

Audience: readers transitioning from players to teachers, editors, or designers.

Learning goal: produce rule text that is unambiguous, testable, and teachable.

A strong rule document is executable prose. A reader should be able to set up,
play, and score a full round without asking for missing steps. To do that,
separate descriptive background from procedural requirements.

A practical rule-text order:

1. Components and player counts.
2. Setup.
3. Turn structure and legal actions.
4. Resolution rules for conflicts and edge cases.
5. Scoring and end conditions.
6. Optional variants.

Prefer explicit verbs over implied intention. "Draw one card" is clearer than
"refresh your hand." Define overloaded terms once and link to local definitions
such as [[games/card-games/terms/trick|trick]] or
[[games/card-games/terms/trump|trump]].

Edge-case policy should also be explicit. Specify what happens for ties,
impossible moves, exhausted draw piles, and illegal plays discovered late. If a
rule can be interpreted two ways by careful readers, rewrite it before testing.

Playtesting for rule text is different from playtesting for balance. Ask new
readers to run the game from the document alone while you observe where they
pause, diverge, or invent filler rules. Those moments reveal missing
preconditions or undefined transitions.

Finally, maintain versioned revisions. Label rule updates and summarize what
changed between versions. This protects analysis notes from drift and makes it
possible to compare strategy claims against the correct rule set.

Check for understanding: rewrite one ambiguous rule from memory into a version
that includes actor, action, constraint, and timing.
