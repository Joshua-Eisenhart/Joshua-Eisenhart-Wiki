---
title: Wizard Voice Preservation Audit v3.3
created: 2026-04-29
updated: 2026-04-29
type: audit
tags: [wizard, audit, voices, followup, output-contract]
framing: current
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# Wizard Voice Preservation Audit v3.3

## Scope

Audited active wiki surfaces:

- `AGENTS.md`
- `01-wizard-general.md`
- `03-followups-and-compositions.md`
- `05-validation-gates.md`
- `validation/WIZARD_OUTPUT_SMOKE_TEST_v3_3.md`

## Findings

### Finding 1: Voice collapse was under-specified

The previous contract said voices and wave results should appear when useful, but it did not require each visible voice to preserve a distinct contribution. That allowed an output to claim a voice wave while summarizing all voices into one paragraph.

Status: fixed by adding the Voice Preservation Contract and Voice Preservation Gate.

### Finding 2: Follow-up could drift into route bookkeeping

The follow-up system correctly had Make, Scout, and Audit/Improve waves, but the visible menu rule did not explicitly reject internal diagnostic prompts as the default. That allowed follow-up options like receipt inspection, contradiction ledgers, and route proof to crowd out useful next prompts.

Status: fixed by adding the Useful Prompt Rule and follow-up fail patterns.

### Finding 3: Header truth could dominate the body

The header already required subagent and wave counts, but the docs did not say strongly enough that header truth must stay compact and the body must remain useful content.

Status: fixed by adding the rule that route truth belongs in the header and compact Results boundary, while the body carries useful judgment.

### Finding 4: Collapse testing existed but was too broad

`WIZARD_OUTPUT_SMOKE_TEST_v3_3.md` checked general output shape, but it did not directly fail no-voice and broken-follow-up outputs.

Status: fixed by adding `WIZARD_VOICE_FOLLOWUP_COLLAPSE_TEST_v3_3.md`.

## Current Acceptance Rule

A Full Wizard answer is not accepted if it reads like a log, if voices are removable labels, or if follow-up is mostly orchestration/debug work. The desired artifact is a readable answer shaped by real routes, with route truth compactly carried in the header.
