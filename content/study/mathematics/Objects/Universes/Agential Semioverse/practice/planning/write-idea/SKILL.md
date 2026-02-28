---

skill_spec_version: "1"
id: write-idea-skill
name: write-idea
summary: Write a single idea as a standalone Markdown document with frontmatter and clear motivation.
description: Write a single idea as a standalone Markdown document with frontmatter and clear motivation. Use when recording a new idea.
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
    description: Idea template path
    required: false
    default: mathematics/objects/agential-semioverse/tools/markdown-templates/templates/idea.md.j2
outputs:
  - name: idea_path
    type: path
    description: Where the idea was written
---

- Use the idea template: `mathematics/objects/agential-semioverse/tools/markdown-templates/templates/idea.md.j2`.
- Fill in title, summary, motivation, and potential next steps.
- Place the idea file under [/library/ideas/](/library/ideas/) unless a specific subfolder is needed.
- Add `dependencies` or `references` when the idea relies on other files.
- Add an index entry to [/IDEAS.md](/IDEAS.md) using
  [/mathematics/objects/agential-semioverse/practice/planning/create-idea/SKILL.md](/mathematics/objects/agential-semioverse/practice/planning/create-idea/SKILL.md).
