---

name: create-skill
description: Create a new skill for doing a unit of work. Use when you want to normalize
  a process for future iterations.
kind: skill
skill_kind: programming
status: intuition
version: 0.1.0
authors:
- emsenn
id: create-skill-skill
skill_spec_version: "1"
summary: Create a new SKILL.md with required frontmatter and process steps.
runtime:
  invocation: manual
  tool: human
inputs:
  - name: skill_name
    type: string
    description: Canonical name for the new skill directory and frontmatter
    required: true
  - name: domain_path
    type: string
    description: Domain/subdomain path under library/ (e.g., mathematics/objects/agential-semioverse/tools)
    required: true
outputs:
  - name: skill_path
    type: path
    description: Created skill directory path
---

- Decide on a unique `skill-name`.
- Make a new directory under `/library/{domain}/[subdomain/]{skill-name}/`
  - e.g. `/library/mathematics/objects/agential-semioverse/tools/{skill-name}/`
- Create, in that directory, a `SKILL.md`
  - This file must begin with YAML frontmatter delimiters (---)
  - The first key must be `name: {skill-name}`
  - The second key must be `description: {What work occurs when skill is applied.} Use when {list of activating goals}.`
  - The third key must be `kind: skill`
  - There should be a `skill-kind:` that is one of: assisting, programming, researching, writing.
  - There may be other keys:
    - `authors:` should be a list of the Agent IDs of whoever authored the skills.
    - `date-created:` should be the `YYYY-MM-DD` the skill was created on.
  - The keys should be closed with A YAML delimter (---)
  - The body of this file must include a step-by-step process for enacting the named skill.
    - This process may be formatted as nested lists, as this file is.
  - There may be other nuances to making skills not documented here.
- Once you've made a skill, you might want to use the `$install-skills` skill to make sure it's installed.
  
