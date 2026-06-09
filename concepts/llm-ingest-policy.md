---
title: LLM Ingest Policy
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
---

# LLM Ingest Policy

## Role in the live wiki cluster
- Strongest use: controller-facing retrieval and downranking policy after the entry surfaces have already established current vs legacy boundaries.
- Weak use: first-stop front door note for humans/agents entering the wiki cold.
- Authority boundary: second-layer retrieval doctrine for concept/wiki loading behavior; it should be applied after `hermes-current/` and project entry notes, not instead of them.

## Recommended reading order
1. `hermes-current/read-first.md`
2. the rest of the active `hermes-current/` spine
3. relevant project `read-first.md`
4. [[current-canonical-spine]] or [[harness-boot-pack]] when the task needs concept-level harness doctrine
5. this page when the task specifically needs retrieval order, exclusion rules, contradiction handling, or controller-side loading discipline

Rules for how an LLM should retrieve, prioritize, and interpret wiki content. This is the controller-facing instruction set that turns the wiki from a knowledge base into a reasoning scaffold.

## Retrieval Order

When an LLM loads wiki context, load in this order:

### Tier 1 — Always Load (binding)

These pages shape all reasoning. Load first, treat as binding.

1. `hermes-current/read-first.md` plus the needed `hermes-current/` spine notes — live front door
2. relevant project `read-first.md` note when the task is project-bound
3. [[nominalist-translation-rules]] — 7 mandatory translation rules
4. [[llm-bias-inversion-rules]] — 6 mandatory inversions
5. [[harness-bias-inversions]] — controller-facing enforcement view of the 6 inversions
6. [[llm-controller-contract]] — status labels and hard stops
7. [[enforcement-and-process-rules]] — the 13 rules
8. [[hermes-memory-and-wiki-roles]] — where stable facts should live: durable memory vs session recall vs wiki vs repo artifacts

### Tier 2 — Load on Topic Match

Load when the query touches this domain.

| Domain | Load these pages |
|---|---|
| Geometry | [[geometry-ingredient-map]], [[density-matrix-mathematics]], [[hopf-fibration-mathematics]], [[clifford-algebra-qit]] |
| Constraints/cascade | [[constraint-surface-and-process]], [[constraint-surface-translated]], [[pytorch-ratchet-build-plan]] |
| Evidence/results | [[probe-doc-result-map]], [[docs-vs-sims-gap-audit]] |
| Bridge/seam | [[qit-engine-geometry-entropy-bridge]], [[migration-registry]] |
| Controller enforcement | [[llm-research-gap-matrix]], [[llm-research-enforcement-validator]], [[actual-lego-registry]], [[tooling-status]] |
| Active repo authority | [[current-authoritative-stack-index]], [[axis0-current-doctrine-state-card]], [[thread-b-stack-audit]] |
| Philosophy/nominalism | [[nominalism-in-this-system]], [[anti-reification-and-nominalism-reference]], [[operationalism-and-measurement-reference]] |
| LLM bias | [[llm-ontology-smuggling-reference]], [[llm-bias-and-failure-modes-reference]] |
| Translation | [[translation-methodology-reference]], [[process-and-systems-thinking-reference]], [[research-support-bibliography]] |
| Concept-level harness doctrine | [[current-canonical-spine]], [[harness-boot-pack]] |

### Tier 3 — Available but Never Load by Default

These are for deep dives only. Do not load into harness context.

- Source-notes indexes (too large, low signal per page)
- Legacy/speculative pages
- Digest pages (summaries of other pages)
- Archived files in `_archive/`

## Exclude Rules

| Pattern | Action | Reason |
|---|---|---|
| `*copy*` filename | Exclude | Duplicate of canonical page |
| `*outdated*` filename | Exclude | Superseded content |
| `_archive/` path | Exclude | Archived, not current |
| `legacy` in tags | Downrank | Low authority |
| `digest` in tags | Downrank | Summary of other pages |
| `framing: legacy` | Downrank | Older framing |
| No `classification` field in result JSON | Flag as legacy | Pre-template result |

## Contradiction Handling

When two wiki pages make conflicting claims:

1. Check dates — newer generally supersedes older
2. Check framing — `current` supersedes `legacy`
3. If both current and both recent: flag the contradiction, do not resolve
4. Add `contradictions: [page-name]` to frontmatter of both pages
5. Do NOT silently overwrite one with the other

**Why:** Contradictions between constraint shells are signal. L4 kills what L3 preserves — that is the system working, not a problem.

## Status Label Enforcement

When describing any sim result or system state, use ONLY these 4 terms:

| Term | When to use |
|---|---|
| `exists` | File on disk |
| `runs` | Executes without error |
| `passes local rerun` | Fresh run confirms expected tests pass |
| `canonical by process` | Passes local rerun + SIM_TEMPLATE + tool manifest + classification |

**Banned:** "verified", "confirmed", "validated", "complete", "passes all criteria", "survives", "winner."

## Translation Checkpoint

Before generating any response about this system:

1. Did I name the constraint set? (catches universal smuggling)
2. Did I name the probe? (catches essentialist smuggling)
3. Did I use selection language? (catches causal smuggling)
4. Did I enumerate rather than summarize? (catches compression smuggling)
5. Did I describe processes, not substances? (catches substance smuggling)

If any check fails, rewrite before outputting.

## Loading Priority for Specific Query Types

| Query type | Primary load | Secondary load |
|---|---|---|
| "What is the system?" | canonical-spine, constraint-surface | geometry-ingredient-map |
| "What works?" | probe-doc-result-map, migration-registry | phase7 results |
| "What's broken?" | docs-vs-sims-gap-audit, battery-index | negative battery results |
| "How should I describe this?" | nominalist-translation-rules, llm-bias-inversion-rules | translation-methodology |
| "What's the geometry?" | geometry-ingredient-map, density-matrix-mathematics | hopf-fibration, clifford |
| "What's the plan?" | pytorch-ratchet-build-plan, shell-local-to-coupled-program | migration-registry |
| "What's the evidence?" | probe-doc-result-map, enforcement-and-process-rules | falsification-sim-designs |

## Related Pages

- [[wiki-as-harness-architecture]] — the 4-layer architecture this policy implements
- [[current-canonical-spine]] — second-layer harness doctrine, not the entry front door
- [[nominalist-translation-rules]] — the translation rules this enforces
- [[llm-bias-inversion-rules]] — the inversions this enforces
- [[harness-bias-inversions]] — controller-facing operational checklist for the same inversions
- [[harness-translated-companion]] — proof-of-method page showing the translation stack on one canonical source pair
- [[research-support-bibliography]] — the support cluster for translation framing
- [[hermes-memory-and-wiki-roles]] — storage/routing split for memory-facing controller work
- [[llm-controller-contract]] — the execution contract
- [[llm-research-gap-matrix]] — controller-side gap bookkeeping
- [[llm-research-enforcement-validator]] — closeout and matrix validation surface
- [[current-authoritative-stack-index]] — repo-current owner stack mirror
- [[docs-framing-map]] — provenance labeling system
- [[probe-doc-result-map]] — the evidence bridge
