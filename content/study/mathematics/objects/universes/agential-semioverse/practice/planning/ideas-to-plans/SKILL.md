---

name: ideas-to-plans
kind: skill
description: Translate IDEAS.md entries into PLANS.md items. Use when planning and
  prioritizing work.
id: ideas-to-plans-skill
skill_spec_version: "1"
skill_kind: planning
summary: Convert idea headers into plan items with inline metadata.
inputs:
  - name: ideas_path
    type: path
    description: Path to IDEAS.md
    required: false
    default: IDEAS.md
  - name: plans_path
    type: path
    description: Path to PLANS.md
    required: false
    default: PLANS.md
outputs:
  - name: updated_plans_path
    type: path
    description: Path to PLANS.md after updates
runtime:
  invocation: inference
  tool: human
---

# Ideas To PLANS

## When to use this skill

Use this skill when you need to convert ideas into well-formed PLANS items.

## What you require

You must have access to IDEAS.md and PLANS.md.

## What to do

- Read idea headings from IDEAS.md.
- Append PLANS items with required inline fields to PLANS.md.
- Do not overwrite existing PLANS items.
