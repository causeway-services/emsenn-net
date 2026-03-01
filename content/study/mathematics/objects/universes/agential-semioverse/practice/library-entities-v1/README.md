---
title: Library Entities Specification v1
id: library-entities-v1-readme
kind: specification
authors:
- gpt-5.2-codex
date-created: 2026-01-01
tags:
- library
- specification
---

# Library Entities Specification v1

This specification stabilizes how we talk about concepts, data files, modules,
skills, agents, curricula, and lessons. It also ties discipline routing to tags.

## Core entities

### Concept

A concept is a unit of meaning tracked as a module. Concepts can be abstract
("power") or concrete ("biopower"). A concept module may include theory,
practices, and tools.

### Module

A module is the directory container for a concept. It groups files for theory,
practices, tools, and optional submodules. Modules define the top-level context
for a concept.

### Data file

A data file is a single Markdown document with frontmatter. It is the smallest
unit of recorded knowledge and must specify its `kind` and `authors`.

### Curriculum

A curriculum is a structured sequence of lessons for a concept. It lives in the
module's `theory/` area and lists ordered dependencies.

### Lesson

A lesson is a single instructional document. It declares prerequisites and is
written for an explicit audience and learning goal.

### Skill

A skill is a procedural or automatable unit of work. Skills live under the
module's `tools/` directory and expose inputs/outputs when applicable.

### Agent

An agent is a profile describing a role-bearing actor. Agent frontmatter may
include `roles` to inherit skills from other agents.

### Plan and idea

Plans and ideas are standalone documents that describe future work. They can be
attached to a concept module under `plans/` or `ideas/`.

## Discipline routing

A data file is routed by tags. The first discipline tag in `tags` determines the
discipline. Subdiscipline routing is derived by tag ancestry through
encyclopedia entries (e.g., `critical-theory` -> `philosophy` -> `humanities`).

## Module layout

```
<concept>/
  theory/      # definitions, glossaries, histories, curricula, lessons
  practices/   # procedures, workflows, how-to guides
  tools/       # skills, scripts, templates
  modules/     # sub-concepts (optional)
  ideas/
  plans/
```
