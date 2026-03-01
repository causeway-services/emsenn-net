---

name: check-emsenns-latest-logs
kind: skill
description: Check emsenn's most recent log entry or N most recent log entries by
  filename date order; use when asked for the latest log(s), recent log summary, or
  to inspect emsenn log entries.
id: check-emsenns-latest-logs-skill
skill_spec_version: "1"
summary: Return the most recent N log entries for emsenn.
inputs:
  - name: count
    type: integer
    description: Number of log entries to return
    required: false
    default: 1
outputs:
  - name: logs
    type: array
    description: List of log entry paths/content
runtime:
  invocation: inference
  tool: human
---

# Check Emsenn's Latest Logs

## Workflow

- Locate log entries in [/agents/emsenn/content/log/](/agents/emsenn/content/log/).
- Select the latest entries by filename date (YYYYMMDD prefix).
- Default to 1 entry when N is not provided.
- For `--compact`, output only the YAML frontmatter if present.
- Otherwise, output full log entries.

## Script

Use `scripts/check_logs.py` for deterministic selection and output.

Examples:

```bash
python scripts/check_logs.py
python scripts/check_logs.py --count 3
python scripts/check_logs.py --compact
python scripts/check_logs.py --count 2 --compact
```
