---
title: "Channel Capacity and Coding"
aliases:
  - "Channel Capacity and Coding"
id: channel-capacity-and-coding
kind: lesson
authors:
- gpt-5.2-codex
date-created: 2025-12-30
description: How channels limit information and how codes approach capacity.
tags:
- information-theory
- study
dependencies:
- /information/curricula/mutual-information.md
---


## Assumed audience

- Reading level: technical.
- Background: entropy and mutual information.
- Goal: understand capacity and why codes matter.

## Channel capacity

The capacity of a channel is the maximum information rate that can be sent with
arbitrarily low error.

## The core formula

Capacity is the maximum of mutual information over input distributions:

\[
C = \max_{p(x)} I(X;Y).
\]

## Coding intuition

- Error-correcting codes add redundancy.
- Good codes approach capacity without exceeding it.

## Why this matters

Capacity defines a hard limit for communication systems and data storage.
