---
title: Directory Organization Specification
date-created: 2026-03-01T00:00:00
authors:
  - emsenn
tags:
  - specification
  - agential-semioverse
  - repository
---

# Directory Organization Specification

This specification defines the standard directory structure for discipline modules in the Agential Semioverse Repository (ASR). It applies to any directory that represents a discipline or subdiscipline in the vault.

## Standard Subfolders

The following subfolders are recognized within a discipline module. Not every discipline will have all of them; create only those that have content.

### `disciplines/`

Formal subdisciplines that are themselves organized as full discipline modules. Use this when a subdiscipline has enough content and internal structure to warrant its own `topics/`, `terms/`, `curricula/`, etc.

### `concepts/`

Notes on individual concepts within the discipline. Each note covers one concept and its relations. Use when the content is specifically concept-defining rather than topical.

### `schools/`

Named theoretical traditions, movements, or frameworks that the discipline studies or that operate within it. Examples: marxism under sociology, foucauldianism under critical theory.

### `topics/`

Areas of inquiry within the discipline. Topics may themselves contain nested `concepts/`, `terms/`, `curricula/`, and other recognized subfolders. Topics are broader than concepts and narrower than disciplines.

### `terms/`

Glossary entries and term definitions. Each file defines a term. May exist at the discipline level or inside a topic.

### `text/`

Papers, essays, reading notes, and other texts. Use for content that is primarily a document or artifact rather than a structured note on a concept or topic.

### `curricula/`

Learning sequences: ordered lessons, reading lists, or pathways through the discipline's material.

---

## Cross-Cutting Subfolders

These subfolders may appear in any module, including topics, schools, and disciplines, without being listed above. They follow standard naming regardless of where they appear.

### `history/`

Notes on the historical development of the parent module's subject. May appear in a discipline, topic, or school. Not categorized as a topic itself — it is a recognized structural companion to any module.

---

## Special Cases

Some disciplines have domain-specific subfolders that do not fit the standard set. These are valid and should be documented here when introduced.

| Discipline | Special Folder | Purpose |
|---|---|---|
| `mathematics/` | `objects/` | Mathematical objects (numbers, sets, topoi, universes, etc.) |
| `linguistics/` | `languages/` | Language-specific research notes (e.g., `languages/eng/`) |

When introducing a new special-case folder, add a row to this table and briefly note the rationale in the discipline's `index.md`.

---

## Mapping to ASR Concepts

In the Agential Semioverse Repository, each discipline module is a **Thing**. Its directory is the **thing handle**. Its `index.md`, internal links, and frontmatter constitute its **interaction surface**. The **footprint** of a discipline module is the semantic closure of that surface within the vault's state.

The standard subfolders create predictable interaction surfaces: an agent or reader looking for terms knows to look in `terms/`, for learning sequences in `curricula/`, for primary texts in `text/`. This predictability is what makes the vault machine-readable as an ASR.

Subfolders that are recognized but not present in a given module represent gaps in the interaction surface — candidates for the `close-semioverse-gap` skill.

---

## Creating a New Discipline Directory

1. Create the directory at the appropriate level in `content/`.
2. Add an `index.md` with the following frontmatter:
   - `title:` — the human-readable page name Quartz will display (e.g., "Ecological Topics", not just "Topics")
   - `date-created:` — ISO 8601
   - `aliases:` — at minimum two: one matching the title exactly, one lowercase (e.g., "Ecological Topics" and "ecological topics"). Add others as useful for Obsidian navigation.
   - `description:` — optional but useful for semantic web crawlers; one sentence describing what the directory contains.
3. The `index.md` body should be brief — one or two sentences at most. Do not list specific files or pages; the static site generator handles navigation. Do not write page listings or detailed summaries of current content, as these go stale and mislead about the directory's scope.
4. Create only subfolders that have content — do not create empty placeholder directories.
5. If you introduce a special-case subfolder, document it in the table above.

## index.md Anti-Patterns

The following patterns should not appear in `index.md` files:

- **Page listings** — bullet lists of links to files within the same directory. The SSG generates navigation; hardcoded listings go stale.
- **Content summaries as scope** — describing only the pages that currently exist gives a false picture of the directory's purpose. Describe what the directory *is for*, not what happens to be in it.
- **"Module"** — directories are directories or folders, not modules. Use the appropriate term.
- **Over-specified frontmatter tags** — tags should reflect the directory's general topic, not list every concept that happens to appear in current content.
