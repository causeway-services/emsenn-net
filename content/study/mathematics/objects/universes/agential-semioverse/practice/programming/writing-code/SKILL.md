---

name: writing-code
description: How to produce well-formed code. Use whenever you must write code.
id: writing-code-skill
kind: skill
skill_spec_version: "1"
summary: Guidance for producing well-formed code.
inputs:
  - name: language
    type: string
    description: Target language
    required: false
  - name: style
    type: string
    description: Optional style guide or constraints
    required: false
outputs:
  - name: guidelines
    type: string
    description: Guidance text
runtime:
  invocation: inference
  tool: human
---

- Minimal content per file
  - I.e., in Python, Write one exportable function or dataclass per file.
