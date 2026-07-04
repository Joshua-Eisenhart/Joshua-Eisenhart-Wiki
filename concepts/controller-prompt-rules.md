---
title: Controller Prompt Rules
created: 2026-04-09
updated: 2026-04-16
type: concept
tags: [harness, system, canonical, architecture, language]
sources:
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/CLAUDE.md
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v5/docs/ENFORCEMENT_AND_PROCESS_RULES.md
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v5/docs/LLM_CONTROLLER_CONTRACT.md
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/skills/llm_research_enforcement_validator.py
framing: current
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# Controller Prompt Rules

## Role in the live wiki cluster
- Strongest use: bounded controller/delegation rule page for lane selection, worker prompt shape, claim reporting, and closeout gates.
- Weak use: broad system-summary page or replacement for the repo-current controller authority docs themselves.
- Authority boundary: wiki bridge page that mirrors and operationalizes controller behavior; when a claim depends on exact repo-current contract wording, the repo docs still outrank this summary.

## Recommended reading order
1. `hermes-current/read-first.md`
2. the rest of the `hermes-current/` spine and the relevant project front door
3. repo-current controller docs (`CLAUDE.md`, `system_v5/docs/ENFORCEMENT_AND_PROCESS_RULES.md`, `system_v5/docs/LLM_CONTROLLER_CONTRACT.md`) when the task touches live controller truth
4. [[harness-boot-pack]] / [[llm-ingest-policy]] for second-layer harness loading discipline
5. this page when the task specifically involves delegation, worker closeout review, or controller-side claim reporting

Derived from [[llm-ingest-policy]], [[nominalist-translation-rules]], and [[llm-bias-inversion-rules]]. This page mirrors the repo-current controller contract and validator path for the bounded tasks where a wiki-side operational summary is actually useful.

## Lane Selection Rules

### Which lane to run

| Situation | Lane | Why |
|---|---|---|
| New sim needed | Worker | Bounded task, one cell, one closeout |
| Status report needed | Controller | Consolidation, overclaim check |
| Translation needed | Controller | Must apply harness rules |
| Gap analysis needed | Controller | Must read probe-doc-result-map |
| Archive cleanup needed | Controller | Must verify no inbound links |

### Bounded task format

Every worker prompt must contain:
1. **Read order**: which files to read first
2. **Guardrails**: template compliance, tool manifest, non-empty reasons
3. **Allowed claims**: what this worker may conclude (bounded)
4. **Required verification**: what must be run before reporting success
5. **Stop rules**: when to stop and report back

### Consolidation pass (after every worker)

After every worker completes:
1. Check for overclaim (worker says "all pass" → verify specific criteria)
2. Check for stale doc edits (worker edited a doc → verify code gate was met)
3. Check for schema drift (worker used non-template format → flag)
4. Run the controller-side validator when a worker returns a research closeout or gap-matrix edit: `system_v4/skills/llm_research_enforcement_validator.py`

## Claim Reporting Rules

### Status vocabulary (4 only)

- `exists`
- `runs`
- `passes local rerun`
- `canonical by process`

Never use: verified, confirmed, validated, complete, passes all criteria, survives, winner.

### Claim → Evidence table (required before any summary)

| Claim | Source file | Result path | Criteria checked | Status label |
|---|---|---|---|---|
| (every claim) | (file) | (JSON) | (C1/C2/C3/C4) | (one of 4 public labels) |

No broad summary without this table.

### Tool enforcement

| Claim type | Required tool | Cross-check |
|---|---|---|
| Impossibility | z3 (UNSAT) | cvc5 |
| Shell metrics | geomstats | numpy baseline |
| Multi-way interaction | XGI | rustworkx |
| Cell complex | TopoNetX | GUDHI |
| Geometric algebra | clifford | numpy roundtrip |
| Gradient flow | PyTorch | finite difference |

If a tool is `used: false`, it cannot be `load_bearing`.

## Translation Rules (apply before every output)

### The 7 mandatory translations

1. Object → Survivor
2. Creation → Selection
3. Essence → Probe-relative
4. Causation → Constraint coupling
5. Truth → Admissibility
6. Identity → Distinguishability class
7. Universal → Context-bound

### The 6 bias inversions

1. Reification → Constraint survival
2. Narrative smoothing → Contradiction preservation
3. Forward causation → Constraint selection
4. Universal framing → Context-bound
5. Object-first → Relation-first
6. Compression → Expansion

Operational checklist source: [[harness-bias-inversions]]

### Pre-flight check (5 questions)

1. Named constraint set?
2. Named probe?
3. Used selection language?
4. Enumerated rather than summarized?
5. Described processes, not substances?

## Gate Rules

1. No E (emergence) claim without A-D cells for that family
2. No "phase complete" from subset coverage
3. No "layer verified" from local-only sims
4. No registry/doc edit until code/result gate satisfied
5. No controller acceptance of a research closeout without validator pass and evidence paths when the closeout uses the enforcement schema
6. Batch workers: 5-10 files max per batch

## Retrieval Order for Controller

When the controller needs to assess system state:

1. [[current-authoritative-stack-index]] — repo-current owner surfaces and routing
2. [[probe-doc-result-map]] — what evidence exists
3. [[docs-vs-sims-gap-audit]] — what's missing
4. [[migration-registry]] — per-family status
5. [[llm-research-gap-matrix]] — controller-side gap bookkeeping
6. [[tool-manifest-audit]] — template compliance
7. [[llm-research-enforcement-validator]] — closeout acceptance contract

For autonomous wiki work, pair this page with [[wiki-automation-contract]] so lane selection and reporting rules stay subordinate to ordered tranche execution rather than salience-first page picking.

## Related Pages

- [[harness-boot-pack]] — the minimum read order
- [[llm-ingest-policy]] — full retrieval and exclusion rules
- [[nominalist-translation-rules]] — the 7 rules
- [[llm-bias-inversion-rules]] — the 6 inversions
- [[harness-bias-inversions]] — controller-facing operational checklist for the six inversions
- [[harness-translated-companion]] — proof-of-method translation companion page
- [[research-support-bibliography]] — support cluster for harness framing
- [[llm-controller-contract]] — the execution contract
- [[llm-research-gap-matrix]] — controller-side gap bookkeeping
- [[llm-research-enforcement-validator]] — validator and closeout schema summary
- [[current-authoritative-stack-index]] — repo-current owner stack mirror
- [[enforcement-and-process-rules]] — the 13 rules
