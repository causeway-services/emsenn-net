---

name: summarize-sample
description: Summarize a dataset with basic descriptive statistics. Use when
  reporting on sample data.
kind: skill
skill-kind: analysis
authors:
- gpt-5.2-codex
date-created: 2026-01-01
id: summarize-sample-skill
tags:
- statistics
- mathematics
runtime:
  invocation: inference
  tool: llm
inputs:
  - name: data
    type: array
    description: Sample data (numeric or categorical)
    required: false
outputs:
  - name: summary
    type: string
    description: Descriptive stats (count, central tendency, spread, outliers)
dependencies:
- /mathematics/statistics/curricula/lesson-3-descriptive-statistics.md
- /mathematics/statistics/terms/index.md
---

# Summarize Sample

- Identify the variable and its units.
- Report mean, median, and a spread measure.
- Note sample size and any missing values.
- Record anomalies or outliers for follow-up.
