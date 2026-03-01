---

skill_spec_version: "1"
id: install-skills-skill
name: install-skills
summary: Install skills from the library into the agent runtime.
description: Install skills from the library where agents will see them. Use after changing skills.
kind: skill
skill_kind: programming
authors:
- gpt-5.2-codex
- emsenn
runtime:
  entrypoint: install_skills.py
  language: python
  invocation: cli
inputs: []
outputs:
  - name: status
    type: string
    description: Result of installation
---

## Process

- Run the `install_skills.py` script
- Address every error and warning:
  - Either present them to your operator, or, if capable, fix them yourself.
- If there are no errors, then the skills should be installed.
