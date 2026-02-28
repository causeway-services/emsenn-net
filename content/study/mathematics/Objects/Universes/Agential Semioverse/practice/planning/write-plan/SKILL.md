---

skill_spec_version: "1"
id: write-plan-skill
name: write-plan
summary: Write a plan as a standalone Markdown document with explicit steps and risks.
description: Write a plan as a standalone Markdown document with explicit steps and risks. Use when an idea is approved for execution.
kind: skill
skill_kind: planning
authors:
  - gpt-5.2-codex
date-created: 2025-12-26
runtime:
  invocation: manual
  tool: human
inputs:
  - name: template_path
    type: path
    description: Plan template path
    required: false
    default: plans/templates/plan.md.j2
outputs:
  - name: plan_path
    type: path
    description: Where the plan was written
---

- Use the plan template: [plan template](/mathematics/objects/agential-semioverse/tools/markdown-templates/templates/plan.md.j2).
- Define the goal, steps, deliverables, and risks.
- Place the plan file under [/plans/](/plans/) unless a specific subfolder is needed.
- Add `dependencies` or `references` when the plan relies on other files.
