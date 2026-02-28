---

name: identify-gap
kind: skill
description: Use this skill to identify a gap in the library.
id: identify-gap-skill
skill_spec_version: "1"
summary: Detect missing content or skills in the library and report gaps.
inputs:
  - name: scope
    type: string
    description: Area to inspect (e.g., content or skills)
    required: false
    enum: ["content", "skills", "unspecified"]
    default: "unspecified"
outputs:
  - name: gaps
    type: array
    description: List of identified gaps
runtime:
  invocation: inference
  tool: human
---

- If you're identifying missing content, use the `$identify-content-gap` skill.
- If you're identifying missing skills, use the `$identify-skill-gap` skill.
