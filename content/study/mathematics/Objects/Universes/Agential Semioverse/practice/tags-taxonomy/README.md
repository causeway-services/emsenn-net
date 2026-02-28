---
title: Tags Taxonomy
id: tags-taxonomy-readme
kind: specification
authors:
- gpt-5.2-codex
date-created: 2025-12-30
tags:
- metadata
- tags
---

# Tags Taxonomy

Tags describe topic and domain, not document type or metadata fields.

## Tag format

- Use lowercase, hyphenated tags (`postliberal-cybernetics`, `climate-breakdown`).
- Prefer domain or topic terms (`sociology`, `semiotics`, `homotopy-theory`).
- Use 1-5 tags per document unless a domain requires more.

## What tags should be

- Subject areas: `sociology`, `political-theory`, `mathematics`.
- Domains or programs: `relationality`, `postliberal-cybernetics`.
- Thematic topics: `climate-breakdown`, `standardization`, `surveillance`.
- Formal topics in math or logic: `homotopy-theory`, `modal-logic`, `higher-topos-theory`.

## Discipline tags

Discipline tags help route content into the library layout. Use at least one
discipline tag on study content. The first discipline tag in the list defines
the discipline.

Recommended discipline tags:

- `arts`
- `media`
- `humanities`
- `social-sciences`
- `natural-sciences`
- `engineering`
- `technology`
- `medicine`
- `life-sciences`
- `information-science`
- `library-science`
- `business-management`
- `governance`
- `mathematics`

## What tags should not be

- Document type or status (use `kind`, `status`).
- Publication routing (use `publications`).
- Page roles like `home` or `about` (use `id` or a dedicated field if needed).
- Structural metadata (`authors`, `date-created`, `description`, `references`, `dependencies`).

## emsenn-net guidance

Use topical tags for emsenn-net pages. Do not use `emsenn-net` as a tag; the
publication routing belongs in `publications`.
