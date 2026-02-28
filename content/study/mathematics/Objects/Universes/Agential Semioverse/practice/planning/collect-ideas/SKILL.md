---

name: collect-ideas
kind: skill
description: Collect idea headers from IDEAS.md for planning. Use when converting
  ideas into PLANS items.
id: collect-ideas-skill
skill_spec_version: "1"
skill_kind: planning
summary: Extract idea headings from IDEAS.md for downstream planning.
inputs:
  - name: ideas_path
    type: path
    description: Path to IDEAS.md
    required: false
    default: IDEAS.md
outputs:
  - name: ideas
    type: array
    description: List of idea titles/headings
runtime:
  invocation: inference
  tool: human
---

# Collect Ideas

## When to use this skill

Use this skill when you need to list idea headers and their locations in IDEAS.md.

## What you require

You must have access to the IDEAS.md file.

## What to do

- Parse IDEAS.md headings.
- Emit a JSON list of idea titles with line numbers.
