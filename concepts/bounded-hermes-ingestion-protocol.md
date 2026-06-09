---
title: Bounded Hermes Ingestion Protocol
created: 2026-04-07
updated: 2026-04-08
type: summary
tags: [reference, research, system]
sources:
  - raw/articles/new-docs/archive_old/BOUNDED_HERMES_INGESTION_PROTOCOL.md
framing: legacy
priming: false
---

# Bounded Hermes Ingestion Protocol

## Overview
Defines how to feed bounded high-entropy material to Hermes so it helps the system without drowning in mixed layers, stale branches, or narrative smoothing. Superseded by [[agent-workflow-and-boot-architecture]] but preserves pack discipline logic.

## Core Rule
Never ask Hermes to ingest the whole system at once. Always provide: bounded pack, defined role, defined frame, defined output, explicit exclusions. If these are missing, the intake is malformed.

## Why Bounded Ingestion Is Required
Unbounded ingestion causes: mixed layers, stale branch contamination, old-doc overload, graph overload, over-compression, smoothing over unresolved structure, fake closure, loss of tier discipline.

## Pack Structure
Every bounded pack must specify: purpose, role for Hermes, frame, read_order, do_not_read, questions, required_output, promotion_rule.

### Pack sizes
- Small (3-8 files): one narrow subsystem or one immediate audit question
- Medium (8-20 files): one tranche or one architecture problem
- Large (20+ files): only if all in same frame and ordered carefully

## Frame Discipline
Every pack must specify its frame. Examples:
- pre-axis-admission: lower-tier scientific substrate, not Axis construction
- tool-stack-planning: install/use planning, named jobs for tools
- skills-curation: keep/build/patch/retire logic

If wrong frame is used, pack is invalid even if files are good.

## Hermes Roles During Ingestion
Allowed roles: audit reader, bounded synthesizer, tool-role mapper, sim tranche classifier, Hermes-stack planner, skills planner, cleanup planner, reference-repo classifier.

## Promotion Discipline
Reading a pack does not automatically promote contents. A bounded Hermes pass may classify, summarize, identify blockers, map tools to jobs. It may NOT admit laws, promote geometry claims, close open branches, or reclassify diagnostic sims as real evidence.

## Anti-patterns
- Giant mixed packs with multiple frames
- Theory + tools + skills + cleanup all in one prompt
- Packs with no exclusions or no required output
- Packs where Hermes decides the frame itself

## Related pages
- [[agent-workflow-and-boot-architecture]]
- [[boot-prompt-templates]]
- [[stack-authority-and-capability-index]]
