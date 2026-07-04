---
title: Hermes Memory and Wiki Roles
created: 2026-04-14
updated: 2026-04-14
type: concept
framing: current
tags: [memory, harness, workflow, controller, wiki]
sources:
  - /Users/joshuaeisenhart/wiki/concepts/current-canonical-spine.md
  - /Users/joshuaeisenhart/wiki/concepts/llm-ingest-policy.md
  - /Users/joshuaeisenhart/wiki/concepts/harness-boot-pack.md
  - /Users/joshuaeisenhart/wiki/concepts/prediction-first-memory-vs-llm-memory.md
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# Hermes Memory and Wiki Roles

## Purpose
This page makes one basic operational split explicit: Hermes memory and the wiki are not the same thing, and they should not be asked to do the same job.

## Role in the live wiki cluster
- strongest use: quick controller-facing rule page for where a fact should live
- weak use: deep theory of memory or holodeck doctrine
- authority boundary: workflow/router page, not a runtime implementation claim

## The short rule
Use the smallest stable surface that preserves the information without creating drift.

## Four different memory surfaces

### 1. User profile memory
Use Hermes durable user memory for:
- stable preferences
- recurring corrections
- communication style
- durable workflow constraints the user repeatedly expects

Good examples:
- preferred status discipline
- bounded-only work habits
- preferred model choice for autonomous maintenance runs

Do not use it for:
- task progress
- one-session outcomes
- large inventories
- project ledgers

### 2. Session recall
Use transcript/session recall for:
- what happened in a prior session
- which tranche was completed
- what was discussed last time
- past debugging context that is useful but not a stable preference

This is where "what were we doing?" should go, not durable memory.

### 3. Wiki pages
Use the wiki for:
- structured project knowledge
- routing and authority order
- concept pages
- ledgers, status summaries, and support surfaces
- anything that should be inspectable and linkable by humans and LLMs

The wiki is the right place for:
- sim family summaries
- geometry packets
- bridge pages
- controller-facing routing surfaces
- public concept relationships

### 4. Raw/source and repo artifacts
Use raw/source docs and repo artifacts for:
- original provenance
- probe files
- result JSONs
- machine-readable evidence

If a claim depends on a result artifact, the artifact outranks the summary page.

## Practical placement rules

| Kind of information | Best home |
|---|---|
| stable user preference | Hermes user memory |
| stable environment fact | Hermes memory |
| prior-session work log | session recall |
| project concept / router / ledger | wiki |
| exact evidence / rerun output | repo artifact |
| legacy source text | raw/source layer |

## Compact-memory writing rule
When a fact really does belong in Hermes durable memory, compress it hard.

Prefer one dense line over several near-duplicates.

Good pattern:
- combine related run preferences into one line
- combine related environment facts into one line
- keep one wiki-location note instead of several overlapping wiki/vault reminders

Examples of good compact forms:
- overnight/autonomous runs: continuous queue, no idle sleep loops, ~5-minute human updates, GPT-5.4 low for wiki maintenance
- wiki surface: primary project wiki is `/Users/joshuaeisenhart/wiki`; use wiki for durable project knowledge, not Hermes memory
- sim process: tools first, micro-legos first, geometry-family coverage broad, classical baselines allowed
- execution prefs: exact bounded order only; sim tools first as classical capability probes before nonclassical/deep geometry work; classical baselines allowed

Anti-pattern:
- multiple separate memory entries that restate the same operational preference in slightly different words

## Anti-drift rules
- do not stuff project ledgers into Hermes durable memory
- do not treat the wiki as a substitute for result artifacts
- do not treat session recall as a canonical authority page
- do not leave stable repeated corrections only in chat history if they belong in durable memory
- do not save temporary task state to memory just because it might be useful once

## Why this matters
When these surfaces collapse into each other, three bad things happen:
1. memory fills with project clutter
2. the wiki becomes stale because facts were only kept in chat
3. summaries drift away from the actual artifacts

The clean workflow is:
- user preference -> memory
- completed conversation context -> session recall
- durable project structure -> wiki
- exact truth/evidence -> repo artifacts

## Relation to prediction-first memory
[[prediction-first-memory-vs-llm-memory]] is about a higher-level memory theory.
This page is simpler: it is the operating rule for where information should be stored today so Hermes and the wiki stay useful.

## Related pages
- [[current-canonical-spine]]
- [[llm-ingest-policy]]
- [[harness-boot-pack]]
- [[controller-state-transition-model]]
- [[prediction-first-memory-vs-llm-memory]]
- [[llm-constraint-harness-wiki]]
- [[current-research-overlays]]
