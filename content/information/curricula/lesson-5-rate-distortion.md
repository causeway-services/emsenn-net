---
title: "Rate-Distortion and Lossy compression"
aliases:
  - "Rate-Distortion and Lossy compression"
id: rate-distortion-and-lossy-compression
kind: lesson
authors:
- gpt-5.2-codex
date-created: 2025-12-30
description: The tradeoff between compression rate and distortion.
tags:
- information-theory
- study
dependencies:
- /information/curricula/lesson-2-entropy-and-surprise.md
---


## Assumed audience

- Reading level: technical.
- Background: entropy and probability.
- Goal: understand rate-distortion tradeoffs.

## Core idea

Lossy compression accepts distortion in exchange for smaller bit rates.
Rate-distortion theory quantifies the best possible tradeoff.

## Rate-distortion function

The function $R(D)$ gives the minimum rate needed to achieve expected

\[
E[d(X, \hat{X})] \le D.
\]

## Why this matters

This is the theoretical limit behind audio, image, and video compression.
