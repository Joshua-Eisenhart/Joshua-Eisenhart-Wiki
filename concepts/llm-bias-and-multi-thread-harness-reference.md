---
title: LLM Bias And Multi Thread Harness Reference
created: 2026-04-07
updated: 2026-04-08
type: summary
tags: [reference, research, formal]
sources:
  - raw/articles/new-docs/archive_hermes_overlaps/LLM_BIAS_AND_MULTI_THREAD_HARNESS_REFERENCE.md
framing: legacy
priming: false
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# LLM Bias and Multi-Thread Harness: Formal Reference

## Overview
Records major LLM failure modes relevant to a boot-time harness that must preserve multiple narratives, resist flattening, and keep outputs aligned to the user's system grammar.

## Key Failure Modes

### 1) Smoothing / Flattening
Model compresses distinctions into safe average, erasing edges and exceptions. Mitigations: keep raw notes separate from summaries, require distinct alternatives, preserve exceptions explicitly, ask contrastive questions.

### 2) Narrative Collapse
Multiple plausible narratives forced into one canonical narrative too early. Mitigations: keep parallel branches open until explicit merge point, maintain hypothesis labels, use "do not resolve yet" state.

### 3) Sycophancy
Model agrees with user even when claim is uncertain or wrong. Mitigations: prioritize correctness over agreement, require evidence, add adversarial/challenger pass.

### 4) Summary Bias
Abstractive summaries erase uncertainty and exceptions. Mitigations: use extractive notes before summaries, keep separate exceptions/unresolved section, make summary subordinate to full notes.

### 5) Overconfident Closure
Model ends with neat answer before evidence is sufficient. Mitigations: require explicit uncertainty flags, separate "what I know" from "what I conclude," add "what would kill this" section.

### 6) Anchoring
Model latches onto first plausible interpretation and filters everything through it. Mitigations: present multiple interpretations simultaneously, test against the most different alternative first.

### 7) Genre Conformity
Model produces output that "looks like" the expected format even when content doesn't match. Mitigations: validate content before formatting, use non-standard formats for unusual content.

## Harness Implications
The boot prompts in [[boot-prompt-templates]] are designed to counteract these specific failure modes. A1 boot counters sycophancy and smoothing. B boot counters narrative collapse and anchoring. A0 boot counters overconfident closure and genre conformity.

## Related pages
- [[boot-prompt-templates]]
- [[agent-workflow-and-boot-architecture]]
- [[audit-platonic-residue-and-gaps]]
- [[llm-bias-and-failure-modes-reference]]
