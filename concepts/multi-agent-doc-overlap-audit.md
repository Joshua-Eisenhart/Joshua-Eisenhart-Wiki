---
title: Multi Agent Doc Overlap Audit
created: 2026-04-07
updated: 2026-04-08
type: summary
tags: [reference, research, audit, multi-agent]
sources:
  - raw/articles/new-docs/archive_old/MULTI_AGENT_DOC_OVERLAP_AUDIT.md
framing: legacy
priming: false
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# Multi-Agent Doc Overlap Audit

## Overview
Audits where Opus and Hermes agree/diverge on overlapping docs. Date: 2026-04-05. The multi-agent overlap pattern is itself evidence.

## Distinguishability Docs
Opus: DISTINGUISHABILITY_FORMAL_REFERENCE.md (339 lines). Hermes: CONSTRAINT_ON_DISTINGUISHABILITY_FORMAL_REFERENCE.md (180 lines).

### Where They AGREE
Both list: trace distance, operational equivalence, coarse-graining, DPI, Blackwell order, Helstrom bound. Both correctly note DPI as the linchpin. Both note identity as derived from distinguishability (Leibniz PII).

### Where They DIVERGE
Opus includes: fidelity, Holevo bound, Spekkens contextuality, PBR theorem, Fisher info, resource theory, quantum Stein's lemma. Hermes includes: pseudometric, superselection rules, fit/mismatch framing per concept.

### Signal
Both agents independently identified the same core formal concepts. DPI as linchpin emerged independently. Hermes's lighter doc is better for quick reference. Opus's heavier doc is better for formal depth.

## LLM Bias Docs
Opus: LLM_BIAS_AND_FAILURE_MODES_REFERENCE.md (203 lines). Hermes: LLM_BIAS_AND_MULTI_THREAD_HARNESS_REFERENCE.md (135 lines).

### Where They AGREE
Both list: sycophancy, hallucination/smoothing, narrative collapse, summary bias, overconfident closure. Both identify next-token prediction as compression objective.

### Where They DIVERGE
Opus: 18 paper citations, formal definitions, RLHF details, context window causes. Hermes: multi-thread harness mitigations, merge gates, provenance, "do not resolve yet" as explicit state -- more operational.

## Key Finding
Where both agents converge independently = high-confidence concepts. Where they diverge = complementary perspectives (depth vs operations). Neither is sufficient alone. The divergence IS the information.

## Related pages
- [[constraint-on-distinguishability-formal-reference]]
- [[llm-bias-and-multi-thread-harness-reference]]
- [[llm-bias-and-failure-modes-reference]]
