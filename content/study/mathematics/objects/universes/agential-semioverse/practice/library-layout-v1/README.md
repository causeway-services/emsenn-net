---
title: Library Layout Specification v1
id: library-layout-v1-readme
kind: specification
authors:
- gpt-5.2-codex
date-created: 2026-01-01
tags:
- library
- organization
- specification
---

# Library Layout Specification v1

This specification defines how library content is laid out using frontmatter
(`kind`, `tags`, and optional routing fields).

## Terms

- **discipline**: the top-level academic or practice domain (e.g., philosophy).
- **subdiscipline**: a narrower domain inside a discipline (e.g., critical-theory).
- **concept**: the subject of a module (e.g., biopower, discourse).
- **module**: a concept directory that can include theory, practices, and tools.

## Routing inputs

Use these frontmatter fields when present:

- `kind` (required)
- `tags` (required for routing study content)
- `concept` (optional override)
- `roles` (agents only; list of role identifiers)

## Top-level layout

### Disciplines

Primary study content is organized by discipline:

```
/library/<discipline>/<subdiscipline>/<concept>/
```

Examples:

- `/library/philosophy/critical-theory/power/biopower/`
- `/library/philosophy/critical-theory/discourse/`

Discipline tags are listed in [Tags taxonomy](/mathematics/objects/agential-semioverse/practice/tags-taxonomy/README.md).

### Applications

Applications and spaces live under `/library/applications/`:

```
/library/applications/spaces/<space>/<agent>/
```

### Mathematics

Mathematical structures and objects live under `/library/mathematics/`:

```
/library/mathematics/objects/<object>/`
```

### Encyclopedia

Encyclopedia entries live under `/library/encyclopedia/` with category folders:

```
/library/encyclopedia/who/
/library/encyclopedia/theories/
/library/encyclopedia/events/
```

### Ideas and plans

General ideas and plans live under `/library/ideas/` and `/library/plans/`.
Concept-specific ideas and plans should live under the concept module:

```
/library/<discipline>/<subdiscipline>/<concept>/ideas/
/library/<discipline>/<subdiscipline>/<concept>/plans/
```

## Module layout

Each concept module may include the following subdirectories:

```
<concept>/
  theory/      # definitions, glossaries, histories, curricula, lessons
  practices/   # procedures, workflows, how-to guides
  tools/       # skills, scripts, templates
  modules/     # sub-concepts (optional)
```

### Kind-to-directory mapping

- `readme`, `glossary`, `history`, `genealogy`, `specification`, `curriculum`,
  `lesson` -> `theory/`
- `procedure`, `how-to`, `practice` -> `practices/`
- `skill`, `agent-skill` -> `tools/` (with a skill directory per skill)

## Tag-based routing

### Discipline tags

The first tag that is a discipline tag defines the discipline. Discipline tags
are listed in [Tags taxonomy](/mathematics/objects/agential-semioverse/practice/tags-taxonomy/README.md).

### Subdiscipline chains

Subdiscipline routing is determined by tag ancestry. If a tag has an
encyclopedia entry, the tags on that entry define its parent discipline or
subdiscipline. This allows paths like:

```
critical-theory -> philosophy -> humanities
```

which yields:

```
/library/philosophy/critical-theory/<concept>/
```

- Use `tags` to identify the discipline and subdiscipline.
- If multiple discipline tags appear, the first one wins.
- Use `concept` when the concept name differs from the directory name.

## Agents and roles

Agents should live under `/library/applications/spaces/<space>/<agent>/` and
include a `roles` list in frontmatter. Roles point to the agent-role definition
(e.g., `roles: [semioverse-agent]`).

## Compatibility

Existing legacy paths (e.g., `/library/study/` or `/library/agents/`) should be
migrated to the above layout over time. New content should follow this
specification.
