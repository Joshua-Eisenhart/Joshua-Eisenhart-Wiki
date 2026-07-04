---
title: Harness Boot Pack
created: 2026-04-09
updated: 2026-04-15
type: concept
tags: [harness, system, canonical, architecture, language]
sources:
  - /Users/joshuaeisenhart/wiki/hermes-current/read-first.md
  - /Users/joshuaeisenhart/wiki/hermes-current/skills-and-agent-rules.md
  - /Users/joshuaeisenhart/wiki/hermes-current/wiki-harness-progress-and-audit.md
  - /Users/joshuaeisenhart/wiki/concepts/current-canonical-spine.md
framing: current
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# Harness Boot Pack

## Role in the live wiki cluster
- Strongest use: minimal second-layer boot sequence once the `hermes-current/` front door and relevant project front door are already loaded.
- Weak use: replacement for `hermes-current/read-first.md` or a license to skip current/provenance notes.
- Authority boundary: execution-oriented concept page for controller lanes; it compresses second-layer harness loading but does not define the primary human/agent entrypoint.

## Recommended reading order
1. `hermes-current/read-first.md`
2. the rest of the `hermes-current/` spine needed for identity, intentions, rules, and provenance
3. relevant project `read-first.md` note when the task is project-bound
4. this page for a compact controller boot sequence into authority, translation, grounding, evidence, and memory-placement surfaces
5. the deeper page named in the matching section below when a specific lane needs more than the compact boot

The minimum viable second-layer boot for any LLM lane working on this system after the `hermes-current/` front door and relevant project front door are already loaded. Everything else is on-demand.

## Boot Sequence (read in order)

### 1. Entry and doctrine — what loads first versus second

- `hermes-current/read-first.md` plus the needed `hermes-current/` spine notes — live front door
- relevant project `read-first.md` note — task-local front door
- [[current-canonical-spine]] — compact concept-level harness spine after the front door
- [[llm-controller-contract]] — 4 status labels, hard stops, lane separation

### 2. Rules — how to think

- [[nominalist-translation-rules]] — 7 mandatory translation rules
- [[llm-bias-inversion-rules]] — 6 mandatory inversions
- [[harness-bias-inversions]] — controller-facing enforcement checklist for the same six inversions
- [[enforcement-and-process-rules]] — 13 rules, coupling program order

### 3. Grounding — what is real

- [[constraint-surface-and-process]] or [[constraint-surface-translated]] — M(C), F01, N01
- [[geometry-ingredient-map]] — carrier, constraint, bridge geometry

### 4. Evidence — how to check

- [[probe-doc-result-map]] — concept → probe → result → status
- [[llm-ingest-policy]] — retrieval order, exclude rules, translation checkpoints

### 5. Memory placement — where facts should live

- [[hermes-memory-and-wiki-roles]] — user memory vs session recall vs wiki vs repo-artifact split

## After Boot (load on demand)

| Query type | Load |
|---|---|
| Geometry | density-matrix-mathematics, hopf-fibration-mathematics, clifford-algebra-qit |
| Constraints | pytorch-ratchet-build-plan, migration-registry |
| Philosophy | nominalism-in-this-system, anti-reification-and-nominalism-reference |
| Smuggling check | llm-ontology-smuggling-reference |
| Translation | translation-methodology-reference |
| Gap tracking | docs-vs-sims-gap-audit |

## Never Load by Default

- Source-notes indexes
- Legacy/speculative pages
- Digest pages
- Archived files in `_archive/`

## Pre-Flight Check (run before every output)

1. Did I name the constraint set?
2. Did I name the probe?
3. Did I use selection language?
4. Did I enumerate rather than summarize?
5. Did I describe processes, not substances?

If any answer is no, rewrite.

## Status Labels (4 only)

- `exists` — file on disk
- `runs` — executes without error
- `passes local rerun` — fresh run confirms expected tests pass
- `canonical by process` — passes local rerun + SIM_TEMPLATE + tool manifest + classification

Banned: verified, confirmed, validated, complete, passes all criteria, survives, winner.

## Related Pages

- [[wiki-as-harness-architecture]] — the 4-layer architecture
- [[llm-ingest-policy]] — full ingest policy with retrieval tiers
- [[controller-prompt-rules]] — prompt rules derived from this boot pack
- [[harness-bias-inversions]] — operational inversion checklist for controller lanes
- [[harness-translated-companion]] — proof-of-method translation companion page
- [[research-support-bibliography]] — support cluster for process and translation framing
- [[hermes-memory-and-wiki-roles]] — basic storage/routing rule for durable memory vs wiki vs artifacts
