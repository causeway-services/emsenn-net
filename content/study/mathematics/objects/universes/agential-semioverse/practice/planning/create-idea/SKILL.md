---

name: create-idea
kind: skill
description: Add a new Idea. Use when you need to record ideas for future work.
id: create-idea-skill
skill_spec_version: "1"
skill_kind: planning
summary: Append a new idea index entry to IDEAS.md.
inputs:
  - name: title
    type: string
    description: Brief idea title to add as a header
    required: true
  - name: body
    type: string
    description: Optional body text below the header
    required: false
outputs:
  - name: path
    type: string
    description: Path to IDEAS.md
runtime:
  invocation: inference
  tool: human
---

- In `IDEAS.md` add `## {Idea Brief}` followed by a short description.
- Include a link to the idea document under `/library/ideas/` when available.
