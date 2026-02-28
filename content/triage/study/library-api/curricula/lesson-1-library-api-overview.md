---
title: Library API Overview
id: library-api-lesson-overview
kind: lesson
authors:
- gpt-5.2-codex
date-created: 2025-12-31
tags:
- api
- programming
---

# Library API Overview

The engine exposes Skills over HTTP and MCP. Every action is a Skill execution;
there is no separate library server.

## HTTP surface

- `GET /api/v1/skills` to list skills.
- `GET /api/v1/skills/{skill_id}` for skill metadata.
- `POST /api/v1/skills/{skill_id}/execute` with `{ "inputs": { ... } }`.

## MCP surface

- `/mcp` exposes Skills as tools and library resources as `library://` URIs.

## Example: read a file

- Execute the `read-file` Skill with `{ "path": "study/example.md" }`.
