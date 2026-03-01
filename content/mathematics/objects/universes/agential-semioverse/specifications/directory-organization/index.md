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

## Creating a New Discipline Module

1. Create the directory at the appropriate level in `content/`.
2. Add an `index.md` with at minimum `title:` and `date-created:` frontmatter.
3. Describe the discipline in one or two sentences in the index body.
4. Create only the subfolders that have content — do not create empty placeholder directories.
5. If you introduce a special-case subfolder, document it in the table above.
