---

name: lint-plans
kind: skill
description: Validate PLANS.md items for required inline fields. Use when checking
  PLANS hygiene.
id: lint-plans-skill
skill_spec_version: "1"
skill_kind: planning
summary: Check PLANS.md for required inline fields and formatting.
inputs:
  - name: plans_path
    type: path
    description: Path to PLANS.md
    required: false
    default: PLANS.md
outputs:
  - name: issues
    type: array
    description: List of lint findings
runtime:
  invocation: inference
  tool: human
---

# Lint PLANS

## When to use this skill

Use this skill when you need to validate PLANS items for required inline fields.

## What you require

You must have access to the target PLANS.md file.

## What to do

- Ensure each checklist item includes `roles` and `goals` inline fields.
- Report missing fields and exit non-zero on failure.
