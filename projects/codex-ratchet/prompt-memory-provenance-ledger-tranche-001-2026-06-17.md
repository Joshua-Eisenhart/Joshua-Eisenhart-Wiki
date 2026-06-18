---
title: Prompt Memory Provenance Ledger Tranche 001
type: provenance-ledger
created: 2026-06-17
updated: 2026-06-17
tags: [codex-ratchet, memory, provenance, claude, codex, hermes, cocoindex, research]
status: active-ledger-tranche
claim_ceiling: source-processing-provenance-and-research-routing-only
promotion_allowed: false
formal_admission_allowed: false
sources:
  - projects/codex-ratchet/memory-source-coverage-matrix-2026-06-17.md
  - projects/codex-ratchet/prompt-memory-intention-formalization-router-2026-06-17.md
  - projects/codex-ratchet/prompt-memory-first-research-tranche-2026-06-17.md
parent_child_audit: mass-source-class-parent-audit-2026-06-17
cross_model_pressure: mixture-of-agents-2026-06-17
raw_memory_policy: "No raw private memory dumps. Use opaque source IDs, redacted paraphrases, source split, research lane, and claim ceiling."
---

# Prompt Memory Provenance Ledger Tranche 001 — 2026-06-17

## Purpose

This is the first bounded provenance ledger for processing Claude, Hermes, Codex app, codex1, and codex2 memory/source stores into the wiki.

It is downstream of:

- [[projects/codex-ratchet/memory-source-coverage-matrix-2026-06-17]]
- [[projects/codex-ratchet/prompt-memory-intention-formalization-router-2026-06-17]]
- [[projects/codex-ratchet/prompt-memory-first-research-tranche-2026-06-17]]

It does **not** complete the memory estate. It starts the ledger process with safe, high-signal rows and explicit deferrals.

## Method receipt

This tranche used a mass parent/child pattern:

- one coverage pass created a source-class matrix and redacted candidate inventory;
- eight source-class parent auditors reviewed Claude CR, Claude Desktop CR, codex1 memory, codex1 sessions, codex2 memory, codex2 sessions, app-support storage, and research/CocoIndex/wiki-skill integration;
- a cross-model pressure pass checked which rows/categories should be included, excluded, deferred, or quarantined;
- the controller wrote this markdown ledger only after those receipts returned.

No child wrote wiki files. No raw memory JSON/JSONL was copied into the wiki.

## Global claim ceiling

Maximum status for every row here:

```text
source-processing / provenance-ledger / research-comparator routing only
promotion_allowed=false
formal_admission_allowed=false
```

This ledger does not admit `M(C)`, QIT-engine, Axis0, bridge physics, cosmology, dark-sector claims, consciousness theory, final ToE, or canon status.

## Row schema

| Field | Meaning |
|---|---|
| `ledger_id` | stable row ID inside this tranche |
| `source_class` | source estate class, not a private path |
| `opaque_source_id` | hashed/private source pointer from the processing pass |
| `speaker/provenance` | owner / assistant / mixed / unknown |
| `safe window` | redacted paraphrase, not raw private memory |
| `owner-kernel candidate` | possible owner-intention signal |
| `uncertainty/correction` | live fork, owner correction, or unresolved status |
| `assistant-elaboration risk` | what may be generated synthesis or stale operational state |
| `target wiki route` | where a later page/patch may land |
| `research comparator lane` | external/local research lanes that discipline wording |
| `falsifier / guard` | what would kill or demote the row |
| `claim ceiling` | maximum allowed status |
| `privacy status` | how private/unsafe the source was judged |

## Ledger rows

### PM-001 — Primary object vs proxy promotion

| Field | Value |
|---|---|
| source_class | `claude_project_memory_desktop_cr` |
| opaque_source_id | `claude_project_memory_desktop_cr:dad8b709bcf2` |
| speaker/provenance | mixed; owner correction preserved through Claude memory |
| safe window | Redacted paraphrase: the primary object is a finite retrocausal possibility-field style receiver, not Axis0, entropy, PEPS, density, or forward dynamics; proxies must stay typed as adapters/readouts. |
| owner-kernel candidate | Object-preservation outranks proxy convenience. |
| uncertainty/correction | Exact formal carrier and later readouts remain test-dependent. |
| assistant-elaboration risk | Specific ladder language and validator mapping may be Claude-generated. |
| target wiki route | `current-decisive-frame-loader`, `prompt-memory-intention-formalization-router`, future primary-object ledger. |
| research comparator lane | operational probabilistic theories; path-integral/retrocausal comparators; probe-bound readout discipline. |
| falsifier / guard | If a proxy is claimed as object without a finite carrier/control/receipt, demote to generated synthesis. |
| claim ceiling | object-preservation routing only; no physics/Axis0/QIT admission. |
| privacy status | medium; private source, paraphrase only. |

### PM-002 — Purgatory/graveyard as working space

| Field | Value |
|---|---|
| source_class | `claude_project_memory_desktop_cr` |
| opaque_source_id | `claude_project_memory_desktop_cr:434b1ae417a7` |
| speaker/provenance | mixed; owner correction preserved through Claude memory |
| safe window | Redacted paraphrase: “graveyard” should behave more like purgatory/workspace; negative rows are not dead forever, but remain blocked until a new constraint/result changes status. |
| owner-kernel candidate | Negative evidence carves boundaries and preserves future options. |
| uncertainty/correction | Rename and implementation status are not fully propagated. |
| assistant-elaboration risk | Tool-role and v3/v4 implementation details require repo checks. |
| target wiki route | `current-toe-contender-graveyard-workspace-2026-06-07`; future purgatory status patch. |
| research comparator lane | viability kernels; basin stability; quality diversity / novelty search; evolutionary epistemology. |
| falsifier / guard | If no new gate/result/receipt exists, a graveyard row cannot resurrect. |
| claim ceiling | workspace-method candidate only; no model admission. |
| privacy status | medium; paraphrase only. |

### PM-003 — Narrow deterministic seat-certifier vs soft model ordering

| Field | Value |
|---|---|
| source_class | `claude_project_memory_desktop_cr` |
| opaque_source_id | `claude_project_memory_desktop_cr:94da49cf9166` |
| speaker/provenance | mixed; owner correction preserved through Claude context |
| safe window | Redacted paraphrase: deterministic/Python gates should certify whether evidence really ran; priority, rescue ordering, and interpretation choice remain soft, plural, and model-judged. |
| owner-kernel candidate | Strictness belongs at the evidence-seat layer, not at the exploration/value-ordering layer. |
| uncertainty/correction | Likelihood-first ordering is useful but imperfect; it must not become rigid law. |
| assistant-elaboration risk | Any detailed gate architecture is a proposal unless implemented and verified. |
| target wiki route | `deterministic-llm-harness-design-and-audit-2026-06-15`; future engine-authenticity seat-certifier page. |
| research comparator lane | reproducible computation; evidence attestation; ensemble judgment; N-version review. |
| falsifier / guard | If a claimed strict gate cannot rerun/recompute the artifact, it is not a seat-certifier. |
| claim ceiling | method/control surface only. |
| privacy status | medium-high; some source rows unsafe-private; paraphrase only. |

### PM-004 — Fake A/B/C decisions and anti-collapse fanout

| Field | Value |
|---|---|
| source_class | `codex1_memory` |
| opaque_source_id | `codex1_memory:8af5c63b1bef` |
| speaker/provenance | mixed; owner correction plus assistant receipt |
| safe window | Redacted paraphrase: pre-shaped A/B/C choices can be fake decisions; when options are not mutually exclusive, run wide divergent fanout rather than forcing the owner to prune before exploration. |
| owner-kernel candidate | Exploration should preserve plural live readings; do not collapse into menus that only look like choices. |
| uncertainty/correction | Some model outputs may be malformed/empty and must be counted literally, not smoothed. |
| assistant-elaboration risk | Panel synthesis can become over-polished architecture unless tied to receipt quality. |
| target wiki route | this ledger; prompt-memory router; Hermes follow-up menu style surfaces. |
| research comparator lane | ensemble critique; adversarial audit; divergent search / quality diversity. |
| falsifier / guard | If alternatives are genuinely exclusive by evidence, a choice can be real; otherwise fake-choice wording must be removed. |
| claim ceiling | audit-method receipt only. |
| privacy status | low-medium; no raw model outputs. |

### PM-005 — Harness = deterministic gates + wide LLM exploration

| Field | Value |
|---|---|
| source_class | `codex1_memory` |
| opaque_source_id | `codex1_memory:5628dcac87b0` |
| speaker/provenance | mixed; owner correction plus Codex memory synthesis |
| safe window | Redacted paraphrase: Wizard, skills, agents, and Python code all belong in the harness; deterministic gates decide admission, while LLMs generate broad candidate exploration through parent/child/model routes. |
| owner-kernel candidate | The harness has two layers: hard evidence gates and soft plural exploration. |
| uncertainty/correction | Terms such as purgatory/priest/most-likely-first may be source-local and need propagation checks. |
| assistant-elaboration risk | Workspace/harness synthesis can overstate corpus support if exact files are not checked. |
| target wiki route | `deterministic-llm-harness-design-and-audit-2026-06-15`; `hermes-current/skills-and-agent-rules`. |
| research comparator lane | formal gatekeeping; audit-chain fixed points; human-in-the-loop formalization. |
| falsifier / guard | If builder/auditor separation disappears, the row fails as harness discipline. |
| claim ceiling | method/harness routing only. |
| privacy status | medium-high; paraphrase only. |

### PM-006 — Codex/CocoIndex retrieval hygiene

| Field | Value |
|---|---|
| source_class | `codex1_memory` |
| opaque_source_id | `codex1_memory:85cdeaa82e4f` |
| speaker/provenance | mixed operational memory |
| safe window | Redacted paraphrase: CocoIndex is a semantic map over wiki/repo surfaces; search hits improve findability but exact files still outrank semantic retrieval. |
| owner-kernel candidate | Retrieval helps agents find context; it is not authority. |
| uncertainty/correction | Daemon, venv, and MCP health are current-state facts and must be rechecked. |
| assistant-elaboration risk | Search hits can be stale, legacy, or wrong if not followed by exact reads. |
| target wiki route | `hermes-current/cocoindex-wiki-mcp-memory-layer`; `cocoindex-and-bloat-cleanup-policy-2026-06-17`. |
| research comparator lane | retrieval-augmented memory; provenance-aware semantic search; source authority ranking. |
| falsifier / guard | If CocoIndex returns a page, still read exact file before load-bearing claims. |
| claim ceiling | operational routing only. |
| privacy status | low; operational setup but still paraphrased. |

### PM-007 — Foundation order: measured, not prescribed

| Field | Value |
|---|---|
| source_class | `codex2_memory` |
| opaque_source_id | `codex2_memory:4a478e3130b2` |
| speaker/provenance | mixed; owner prompt/correction preserved in Codex2 memory |
| safe window | Redacted paraphrase: do actual foundation builds; order should be measured by commutation/compatibility tests, not declared from a top-floor narrative. |
| owner-kernel candidate | Build foundations first; let order witnesses decide sequence claims. |
| uncertainty/correction | Fine-structure, manifold, and physics status remain downstream. |
| assistant-elaboration risk | Artifact lists, job IDs, and workflow preferences may be generated or stale. |
| target wiki route | foundation-intention routing; prompt-memory-first-research-tranche Kernel B. |
| research comparator lane | finite quotient tests; commutation/order theory; CSP/local consistency; term rewriting/confluence. |
| falsifier / guard | If no real order witness exists, no F01/N01 ordering claim can advance. |
| claim ceiling | workflow/source-processing only. |
| privacy status | medium; private paths/job IDs excluded. |

### PM-008 — MSS/MAS and plural minimal survivors

| Field | Value |
|---|---|
| source_class | `codex2_memory` |
| opaque_source_id | `codex2_memory:673563e61a4c` |
| speaker/provenance | mixed; high-signal owner correction through Codex2 memory |
| safe window | Redacted paraphrase: density-matrix over-promotion should be blocked; MSS/MAS are admission/meta-gate language and plural `Min(Surv(C))` matters more than a single weakest winner. |
| owner-kernel candidate | Keep plural least-admissible survivor pressure; density/Hilbert objects are downstream if forced. |
| uncertainty/correction | Smooth manifold and density may appear later under explicit finite carrier/control conditions. |
| assistant-elaboration risk | Detailed sequence and repo-reference reconciliation require exact source checks. |
| target wiki route | `current-v7-campaign-restart-context-2026-06-14`; future foundation-intention ledger. |
| research comparator lane | quotient structures; operational probabilistic theories; preorders/minimal-survivor frameworks. |
| falsifier / guard | If memory lacks bounded owner quote or owner-confirmed paraphrase, this remains candidate wording. |
| claim ceiling | owner-intention/formalization lane only. |
| privacy status | low-medium; paraphrase only. |

### PM-009 — Sidequest boundaries and informal falsifier value

| Field | Value |
|---|---|
| source_class | `codex2_memory` |
| opaque_source_id | `codex2_memory:9e8f62843f82` |
| speaker/provenance | mixed; owner scope boundary plus assistant notes |
| safe window | Redacted paraphrase: informal sidequest lanes can generate falsifiers and hypotheses, but writes and authority must remain fenced; existing legos must be reconciled before matrix inflation. |
| owner-kernel candidate | Sidequest output is useful fuel, not formal evidence. |
| uncertainty/correction | Which legos admit/repair/block remains open. |
| assistant-elaboration risk | Artifact counts and breach details require repo confirmation. |
| target wiki route | prompt-memory ledger; sidequest-boundary process note. |
| research comparator lane | negative-evidence workspaces; quality diversity; provenance governance. |
| falsifier / guard | If sidequest output lacks exact repo evidence, it cannot promote any result. |
| claim ceiling | process/scope and reconciliation routing only. |
| privacy status | medium; paraphrase only. |

### PM-010 — Layer-completion overclaim gate

| Field | Value |
|---|---|
| source_class | `codex2_memory` |
| opaque_source_id | `codex2_memory:8e902e29bf07` |
| speaker/provenance | mixed; owner boundary preserved through memory |
| safe window | Redacted paraphrase: formal-scout/status receipts must not be narrated as full layer completion, G-structure selection, stacking readiness, Axis0/FEP/flux unlock, physics progress, or final manifold admission without gates. |
| owner-kernel candidate | Completion/status language needs explicit gate evidence. |
| uncertainty/correction | Validator-hardening and adjacent artifact coverage remain page-specific. |
| assistant-elaboration risk | Accept-with-repair verdicts may be generated analysis. |
| target wiki route | repo-current-surface-ingest; future layer-completion claim gate ledger. |
| research comparator lane | claim-gating; provenance-aware validation; safety cases for evidence promotion. |
| falsifier / guard | Any row claiming completion without gate receipt is demoted. |
| claim ceiling | enforcement/process receipt only. |
| privacy status | low-medium; private paths excluded. |

### PM-011 — Ring-checkerboard no-probability-smuggling

| Field | Value |
|---|---|
| source_class | `codex2_sessions` |
| opaque_source_id | `codex2_sessions:f57f7f2eecf7` |
| speaker/provenance | mixed; owner directed bounded fixes in a private session |
| safe window | Redacted paraphrase: a ring-checkerboard diagnostic should preserve finite/count support and order-dependence; do not smuggle a normalized Shannon/probability readout into a no-measure count discipline. |
| owner-kernel candidate | Count/support geometry and order witnesses matter before probability/entropy readouts. |
| uncertainty/correction | Result remains scratch diagnostic and needs exact artifact verification. |
| assistant-elaboration risk | Any “fixed/passed” report is session output until repo receipts are read. |
| target wiki route | ring-checkerboard provenance; pre-AI rosetta ring-checkerboard pages. |
| research comparator lane | finite dynamical systems; SCC/basin readouts; noncommuting order witnesses. |
| falsifier / guard | If only Shannon-like readout supports the claim, demote under no-measure discipline. |
| claim ceiling | scratch-diagnostic fix routing only. |
| privacy status | high; session JSONL unsafe-private; paraphrase only. |

### PM-012 — Rung-0 quotient fingerprint floor

| Field | Value |
|---|---|
| source_class | `codex2_sessions` |
| opaque_source_id | `codex2_sessions:f5668543b612` |
| speaker/provenance | mixed private session |
| safe window | Redacted paraphrase: Rung-0 quotient/fingerprint floor needs could-fail flip controls, multi-engine agreement, and validators; hardcoded success or tautology must fail honestly. |
| owner-kernel candidate | Foundation sims require real falsifiers and multi-engine checks. |
| uncertainty/correction | Even passed local checks would remain scratch foundation diagnostics. |
| assistant-elaboration risk | Assistant reported passes must be independently read/rerun before citation. |
| target wiki route | v7 foundation sim provenance ledger; root distinguishability rebuild pages. |
| research comparator lane | operational equivalence; finite quotient/probe formalization; SMT/CSP controls. |
| falsifier / guard | Tautology guard or bidirectional flip failure kills the claim. |
| claim ceiling | scratch_diagnostic only. |
| privacy status | high; paraphrase only. |

### PM-013 — Forced vs installed carrier must be measured

| Field | Value |
|---|---|
| source_class | `codex2_sessions` |
| opaque_source_id | `codex2_sessions:b2f3be0a9c66` |
| speaker/provenance | mixed private session |
| safe window | Redacted paraphrase: forced-vs-installed carrier status must come from a real free-variable existence search bound to measured readouts, not from hand-typed verdicts or rank fields. |
| owner-kernel candidate | Carrier status is tested by constraints and readouts, not labels. |
| uncertainty/correction | Complete and incomplete probe families may diverge. |
| assistant-elaboration risk | Solver witness reports need exact result verification. |
| target wiki route | carrier forced/installed comparison provenance ledger. |
| research comparator lane | state compatibility; tomography-like completion; SMT existence search. |
| falsifier / guard | If reproduce ON/OFF does not differ under the declared fixture, demote. |
| claim ceiling | scratch_diagnostic carrier comparison only. |
| privacy status | high; paraphrase only. |

### PM-014 — Codex1 sessions: high-signal but unsafe-private

| Field | Value |
|---|---|
| source_class | `codex1_sessions` |
| opaque_source_id | `codex1_sessions:4d1d1f7e5e63` |
| speaker/provenance | mixed private session |
| safe window | Redacted paraphrase: owner framing emphasizes primitive `~`, probe-relative identity, density downstream, entropy/readout typing, purgatory, and anti-collapse; session content is too private for raw quotation. |
| owner-kernel candidate | The conceptual cluster is high-signal and should guide future ledger targets. |
| uncertainty/correction | Treat as pattern-class until exact safe quote windows are owner-confirmed. |
| assistant-elaboration risk | Assistant’s same-carrier geometry interpretation may itself be an over-fixation. |
| target wiki route | prompt-memory router/tranche; future owner-confirmed quote ledger. |
| research comparator lane | operationalism; distinguishability; contextuality; quality diversity. |
| falsifier / guard | No bounded owner quote or owner-confirmed paraphrase means no owner-kernel promotion. |
| claim ceiling | owner-intention routing only. |
| privacy status | high; unsafe-private; paraphrase only. |

### PM-015 — App support storage is deferred, not processed

| Field | Value |
|---|---|
| source_class | `codex_app_support` / `openai_chat_support` / `openai_atlas_support` |
| opaque_source_id | app-support coverage group |
| speaker/provenance | unknown/mixed app storage |
| safe window | Coverage-only: app support directories include conversation/task stores, browser/app state, telemetry, bundled resources, and databases. They need a schema-aware extractor before any semantic memory claim. |
| owner-kernel candidate | none admitted in this tranche. |
| uncertainty/correction | OpenAI Chat/Codex task stores may be high-signal, but cannot be interpreted by generic text scan. |
| assistant-elaboration risk | Generic candidate extraction over-selected bundled/browser resources. |
| target wiki route | future app-support source coverage ledger/extractor. |
| research comparator lane | private app-store extraction; digital forensics provenance; privacy filtering. |
| falsifier / guard | If no schema split exists, no row may become owner memory. |
| claim ceiling | coverage-only pending extractor. |
| privacy status | very high; do not quote. |

## Deferred/quarantined categories

| Category | Status | Reason |
|---|---|---|
| Raw session JSON/JSONL | excluded | unsafe-private; no raw dump allowed |
| Codex app/OpenAI app storage | coverage-only | requires schema-aware extractor and privacy review |
| GCM session result claims | quarantine | need exact repo receipts/reruns before result claims |
| Underdefined formal constructs | hypothesis register only | names like MSS/MAS, Min(Surv(C)), carrier admissibility need page-level definitions and controls |
| Model agreement | audit signal only | agreement does not promote memory-derived claims |

## Required falsifiers for future rows

- If no bounded owner quote or owner-confirmed paraphrase exists, the row cannot be an owner-kernel row.
- If the source is assistant-generated or mixed, mark assistant-elaboration risk.
- If no probe/equivalence relation is named, probe-relative identity language is fog.
- If no order witness exists, F01/N01 sequence claims cannot advance.
- If confluence/coherence erases a bracketing/order difference, no order/bracketing evidence remains.
- If no dynamics/perturbation/return condition exists, no basin/attractor claim is allowed.
- If no new gate/result exists, a graveyard row cannot resurrect.
- If cross-field parallel lacks finite carrier/control/receipt, it remains genealogy only.
- If model agreement is the only support, it is audit signal only.

## Next tranches

1. Claude CR focused ledger: owner corrections and foundation/admission language.
2. Claude Desktop focused ledger: purgatory, seat-certifier, primary-object/proxy, Wizard execution.
3. Codex1 memory ledger: harness/fake-choice/CocoIndex/operator-correction rows.
4. Codex1/Codex2 session cluster ledgers: unsafe-private by default; group by object family and require exact repo receipts for result claims.
5. App-support extractor: schema-aware inventory before any content-level ledger.
