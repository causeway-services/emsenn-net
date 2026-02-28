---
title: Library API Glossary
id: library-api-glossary
kind: glossary
authors:
- gpt-5.2-codex
date-created: 2025-12-31
tags:
- api
- programming
---

# Library API Glossary

## skill execution

A call to `POST /api/v1/skills/{skill_id}/execute` with a validated input payload.

## inputs

The JSON object passed to a Skill under the `inputs` key.

## outputs

The structured result returned by a Skill, including effect details.

## resource

A library item exposed via MCP as `library://<path>`.
