---

title: Skill Specification v1
id: skill-spec-v1-readme
kind: specification
authors: [emsenn]
date-created: 2026-01-01
---

# Skill Specification v1

This specification defines the structure for SKILL.md files that describe executable skills in the Emsemioverse library.

## Purpose

Skills are the primary unit of automation in this library. Each skill:

1. Has a well-defined interface (inputs/outputs)
2. Can be discovered and invoked programmatically
3. Supports multiple execution contexts (human, automation, service)
4. Enables composition and chaining

## SKILL.md Structure

A compliant SKILL.md file has YAML frontmatter followed by prose documentation.

### Required Frontmatter Fields

| Field | Type | Description |
|-------|------|-------------|
| `skill_spec_version` | string | Must be `"1"` |
| `id` | string | Unique kebab-case identifier |
| `name` | string | Human-readable name |
| `kind` | string | `skill` or `agent-skill` |
| `authors` | array | List of author identifiers |
| `date-created` | string | YYYY-MM-DD format |

### Optional Frontmatter Fields

| Field | Type | Description |
|-------|------|-------------|
| `summary` | string | One-line description |
| `description` | string | Detailed description |
| `version` | string | Semantic version (default: 0.1.0) |
| `skill_kind` | string | `human`, `automation`, or `service` |
| `runtime` | object | Execution configuration |
| `inputs` | array | Input parameters |
| `outputs` | array | Output values |
| `capabilities` | object | Integration metadata |
| `examples` | array | Usage examples |

### Runtime Configuration

For automation skills, the `runtime` object specifies how to execute:

```yaml
runtime:
  entrypoint: scripts/my-script.py
  language: python
  invocation: cli  # cli | module | function
  env_vars:
    - API_KEY
```

### Input/Output Parameters

Each parameter in `inputs` or `outputs` has:

```yaml
inputs:
  - name: config_path
    description: Path to configuration file
    type: path
    required: true
  - name: dry_run
    description: Preview without making changes
    type: boolean
    required: false
    default: false
```

Supported types: `string`, `integer`, `number`, `boolean`, `array`, `object`, `path`

### Capabilities

The `capabilities` object enables skill discovery and composition:

```yaml
capabilities:
  domains: [publishing, writing]
  consumes: [markdown-file, publication-config]
  provides: [site-directory]
  composable: true
```

## Validation

Use the skill manifest generator to validate SKILL.md files:

```bash
python library/mathematics/objects/agential-semioverse/tools/skill-manifest/scripts/build-skill-manifest.py --validate
```

## Schema

The JSON Schema for validation is at `library/mathematics/objects/agential-semioverse/practice/skill-spec-v1/skill-spec-v1.json`.
