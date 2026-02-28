---

name: use-markdown-templates
description: Use the repository's Jinja2 templates to generate Markdown files with
  correct frontmatter. Use when creating new docs or curricula.
kind: agent-skill
skill-kind: writing
authors:
- gpt-5.2-codex
date-created: 2025-12-26
id: use-markdown-templates-skill
---

- Choose a template from [/mathematics/objects/agential-semioverse/tools/markdown-templates/templates](/mathematics/objects/agential-semioverse/tools/markdown-templates/templates).
- Create a YAML context file with the required fields.
- Render the template:  
  `python library/mathematics/objects/agential-semioverse/tools/markdown-templates/scripts/render-template.py --template <name> --context <context.yml> --output <file.md>`
- Review the output and fill in any placeholder sections.
