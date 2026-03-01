---
title: Skill manifests in the agential semioverse
id: agential-semioverse-skill-manifests-theory
kind: note
authors:
  - gpt-5.2-codex
date-created: 2026-01-08
tags:
  - agential-semioverse
  - skill-manifest
  - theory
---

# Skill manifests in the agential semioverse

Skill manifests describe how agents in the agential semioverse advertise executable capabilities. Each manifest entry names a skill, its runtime (human, inference, or script), and its inputs/outputs, giving other agents a basis to plan, schedule, and verify interactions.

## Role in the semioverse
- **Discovery**: Agents enumerate available interactions and their preconditions.
- **Planning**: Inputs/outputs form the interface for composing skill pipelines.
- **Safety**: Runtime declarations constrain what executions are allowed and how to validate them.
- **Auditability**: Manifest ids make it possible to log and replay skill invocations consistently.

## Structure
- Frontmatter fields follow Skill Spec v1 (`skill_spec_version`, `id`, `name`, `kind`, `runtime`, `inputs`, `outputs`).
- Runtime covers both executable skills and non-executable guidance (`invocation: manual|none|inference|documentation`).
- Inputs/outputs are typed to support machine routing and validation.

## Relationship to other objects
- Manifest entries are Things in the agential semioverse with footprints in logs and audits.
- MCP/OpenAPI adapters expose manifest entries as tools/endpoints for authorized agents.
- Petri-net/Lean models can treat each manifest entry as a transition for reachability/liveness checks.
