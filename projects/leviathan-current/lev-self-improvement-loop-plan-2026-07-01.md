---
title: Lev self-improvement loop — honest architecture + measurable program
created: 2026-07-01
type: program-plan
status: current
claim_ceiling: grounded in code (fresh-context 4-lens map + synthesis, cited); nothing earned/canon
supersedes_intent: owner goal "Lev running, uses CR sims/wiki/wizard as resource to improve itself, proven by running sims better"
---

# Lev self-improvement loop — the honest program

Grounded map (workflow wf_1863b637-258, 4 parallel readers + synthesis, all cited to file:line; key claims re-verified by direct read).

## Bottom line
The loop is real, replay-guarded, self-verifying — but it ratchets over GRAPH FACTS, not over Lev's own capability. **Lev does not improve Lev today.** What this session did is the honest reading: **codex/human improves Lev THROUGH Lev's gates** (edit TS → build → a wave exercises it → asserts a receipt fact). The wave's output is always the receipt-fact, never the capability.

## The real loop today (one wave, end to end)
1. Council build — makeDemoInput builds the SAME fixed council every wave; claimCeiling hard-pinned to 'fixture_or_dry_run_until_live_model_and_engine_receipts' (handlers/lev-wizard-ratchet.ts:634-672).
2. Engine probe (the one live, content-bearing part) — --real-engines shells out to Julia/JAX/PyTorch via spawnSync, pinned source hashes + executed negative control (real-three-engine-envelope.ts:185-266; mechanical-probe-runner.ts:184). A CR sim can BE the probe via cr_sim_packet_v0 (real-three-engine-envelope.ts:717-767).
3. ClaimGate — deterministic wave; gate check derived from real envelope validation (gate = code, claim-gate-wave-runner.ts:2413-2427).
4. Steering — recompute verdict; seed earned only if projected==recomputed==pass (lev-wizard-ratchet.ts:1833-1841).
5. Graph patch — HMAC single-spend apply authority → graph.process(event) → persisted graph_event_id; loop re-queries event store + entity state to self-verify (graph-patch.ts:254-296; lev-wizard-ratchet.ts:919-960). Only facts written: engine_obligation_receipt entity + has_engine_obligation_result claim.
6. Seed chain — next-run seed carries receipt IDs + content hashes, validated vs prior, anti-replay ledger.

WIRED-LIVE: real 3-engine subprocess exec; real graph mutation + self-verify; host-gated apply authority; deterministic steering recompute; seed chaining + anti-replay; model lanes pinned advisory-only (cannot gate).
FIXTURE/STUB: default (non-real-engines) envelope uses placeholder hashes; every wave = same council/task; model lanes didn't run; formal-skill dispatch is a loader receipt not execution; CR sim consumed by HASH not content.
ABSENT: wiki ingestion (wiki is BLOCKLISTED as a runtime carrier by design, real-three-engine-envelope.ts:37); any wave writing Lev's own skills/config/code; any field representing "better".

## The honest gap (autonomous "Lev improves Lev" needs, none exist)
- Data-driven registry: obligation kinds are hardcoded TS union literals matched by kind==='literal' (claim-gate-wave-runner.ts:44,254-269). Adding cr_sim_packet_v0 was a source edit + rebuild, not a wave output. Compositor vocabulary is node/edge/claim only — no op writes a skill/gate/carrier/obligation-kind.
- Capability-bearing seed: next-run seed chains IDENTITY only (ceiling accepted_survivor_seed_not_autonomous_execution); cannot carry code/capability.
- A "better" primitive: pass today = string-presence + passing negative control (authenticity binary). No baseline/delta/tolerance/betterThan anywhere.
VERDICT: registry + capability-seed are a DISTRACTION and against doctrine (gates are code; LLMs never gate; not_autonomous_code_mutation is the deliberate governor). The "better" primitive is the one worth building and needs NO autonomy.

## The metric + baseline (VERIFIED by direct read 2026-07-01)
Metric: # onboarded cr_sim_packet_v0 sims whose ENVELOPE records a COMPUTED cross-engine parity {agree, maxAbsDiff, tolerance} lifted from real lane/controller outputs and hashed into the receipt.
BASELINE = 0/3 at the receipt level. divergence:{juliaAuthoritative:true, maxDivergence:0} is HARDCODED at real-three-engine-envelope.ts:322,765,964 — a fake zero hashed into every receipt. Controllers DO compute agreement (coratchet artifact has real parity+parity_tolerance; ring-checkerboard gates integer equality but doesn't surface it; fingerprint is 2-engine SMT polarity) but that number is never lifted into the hashed envelope.
Companion baselines: 3 sims onboarded, 2 on canonical cr_sim_packet_v0 path, 0 promoted above fixture, 3 of ~725 corpus candidates.

## Turn 1 (IN PROGRESS, codex build bsiibqmsq): computed parity gate
Replace hardcoded maxDivergence:0 with a COMPUTED {agree,maxAbsDiff,tolerance} read from the controller/lane artifacts via a manifest parityReport spec, hashed into the envelope. Anti-by-construction guard: a declared parity that can't be read or disagrees FAILS the envelope. Load-bearing test: agreeField=false → envelope fails. Moves metric 0/3 → ≥2/3 (coratchet numeric + ring-checkerboard integer); fingerprint stays honest smt_polarity/computed:false.

## Sequencing (each turn a measurable iteration)
- Turn 2 — betterThan gate: deterministic gate reads two receipts for same simPacketId, admits an "improvement" claim only if parity strictly beats prior + negative control still passes. Metric: first sim with a recorded improvement delta (0→1). First receipt that can say "ran better", pure code.
- Turn 3 — migrate coratchet to canonical packet + onboard a 4th corpus sim with full 3-engine + parity tolerance. Metric: canonical onboards 2→4.
- Turn 4 — feed parity into steering by CONTENT not hash: computed agree/delta selects/rejects a candidate claim (like buildGraphSubstrateDerivedProjection carries real graphInvariants but graphMutationApplied:false). First claim whose acceptance is driven by a sim NUMBER.
- Turn 5 — close smallest formal-skill dispatch debt: wire ONE admitted skill with valid execution_profile to actually RUN its procedure (drives formalSkillRuntimeDebt down 1). Dispatched formal skills 0→1.
HELD OUT (doctrine): autonomous-registry (wave writes new capability) stays OUT until turns 2-5 land and a genuine need survives that evidence.

Files: real-three-engine-envelope.ts, claim-gate-wave-runner.ts, lev-wizard-ratchet.ts (proof+handlers), graph-patch.ts, the carriers under core/orchestration/src/probes/lev-sim-engine-carrier/.
