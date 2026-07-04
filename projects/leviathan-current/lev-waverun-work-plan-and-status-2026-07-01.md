---
title: Lev WaveRun / ClaimGate — work plan and status (audit-corrected)
created: 2026-07-01
branch: patch/waverun-engine-gates-20260630
type: master-status-and-plan
supersedes: prior scattered status; see session receipts subdir for evidence
status: superseded
superseded_by: "current canon-gated branch state"
reason: "references claimgate branch"
---

# Lev WaveRun / ClaimGate — work plan and status

Master status + forward plan for the ClaimGate/WaveRun patch, corrected by Claude audit against Codex's self-authored plan. Evidence receipts preserved in `./lev-waverun-session-receipts-2026-07-01/`.

## Current state (as of 2026-07-01)

- Branch: `patch/waverun-engine-gates-20260630`. Latest key commit: `408267f51 fix(wizard): require host-built engine substrate authority` (closes Blocker A-prime).
- The recursive-loop spine is REAL and live-verified: `lev orchestration lev-wizard-ratchet loop --waves N --real-engines --real-skills --real-source-evidence` runs a bounded multi-wave loop, graph-applies survivors, feeds the next-run seed, blocks replay, append-only, real Julia/JAX/PyTorch subprocesses. Verified by two independent agents (items 12/13).
- Cross-process trust: the 2 chain-crossing tokens (host-trust incl wave-run-consume; host-graph-event-trust) are wired to a persisted host-scoped secret (`bfc36727a`) with persisted anti-replay. The witness + graph-apply authority are per-process BY DESIGN (in-process attestations, `not_transferable`) — correctly NOT cross-process.
- Working tree is heavily dirty (~190 files, mixed authorship) — includes 11 uncommitted plugin fixes (below). "Assembly branch" cleanliness is undercut by this; isolate ClaimGate-relevant files when committing.

## Trust-spine status (the load-bearing part)

| Item | Status | Note |
|---|---|---|
| ClaimGate host trust spine (MAC/root, A22 symbol gating, replay) | Strong, branch-local | Needs red-team rerun as a durable suite; classify importable API seams |
| Blocker A (forged obligation sourceHashes on general runner) | CLOSED | `50d2e64f3` validateRealRunnerObligationBindings; forged hash blocks |
| Blocker A-PRIME (wizard runner accepted forged self-consistent digest) | CLOSED at `408267f51`, VERIFIED; residual-1 CLOSED at `92f6535eb`; nonce/replay CLOSED at `e83974175` | Fresh live-repro: independently-forged digest blocked (projection-only, 18 failure packets, no seed); NOT by-construction (test fails 1/23 when fix reverted). Residual-1 (`test_fixture_only`+`NODE_ENV=test` string authority) is structurally pinned: the public string option was removed and fixture authority requires the explicit symbol-keyed `LEV_WIZARD_TEST_FIXTURE_ENGINE_AUTHORITY` capability in tests. Same-process replay-of-real-evidence is now hardened: each real Lev engine substrate digest carries `execution.runId`, `execution.nonce`, and `execution.issuedAt`; host witnesses bind run id + nonce; the Wizard runner consumes host-built digest authority once, so caller-provided or replayed digests are projection-only. Verified by graph/orchestration tests, typecheck/build, and an unstubbed real-engine loop rerun. |
| Cross-process secret (host-trust, graph-event-trust) | DONE | persisted host-scoped XDG secret; both have persisted anti-replay |
| graphStateScope != not_scoped | Coverage gap | rejected outright rather than validated — additive fix |
| ENGINES-NO-CI | OPEN — next build | Real Julia/JAX/PyTorch path proven only by live reproduction; every checked-in test STUBS the digest builder; none of 10 CI workflows runs the orchestration proof suite. |

## Forward plan (corrected sequencing — trust before features)

Consensus of Claude audit + Codex cross-model council: **close the trust seam, then add automated coverage, THEN enrich the loop.**

1. Close trust before features — A-prime DONE + VERIFIED (`408267f51`); residual-1 symbol pin DONE (`92f6535eb`); nonce/run-id freshness + single-use host-built digest authority DONE (`e83974175`). Remaining: fold these into the durable red-team suite for forged digest / stale source hash / external digest injection / serialized host-built digest replay.
2. **Real-engine CI backstop** — DRAFTED + locally-verified + bug-fixed (Claude). Files: `.github/workflows/real-engines.yml` (workflow_dispatch + weekly cron, preflight-gated graceful skip, no LLM/API keys) + `tooling/scripts/real-engines-preflight.sh`. Grounded: env overrides `LEV_JULIA_BIN` + `LEV_PY`; julia 1.12.6; python deps jax 0.10.2 / jaxlib 0.10.2 / torch 2.12.1 / quimb 1.14.0 / geomstats 2.8.0 / numpy 2.3.5 / numba 0.65.1; real-engine tests = `lev-wizard-ratchet.test.ts` "real-evidence loop" (unstubbed; local dry-run 2 passed / 101s / real engines). Fixed the `LEV_JULIA_BIN: julia` ENOENT bug (engine spawns julia with empty child env → needs absolute path from `setup-julia` bindir). STILL GH-Actions-push-UNVERIFIED: julia `Pkg.instantiate()` of a heavy manifest (ITensors/DifferentialEquations/Yao/Z3) on ubuntu, pip jax/torch linux wheels, total wall-clock. EXTERNAL FLEET FINDING (deepseek+grok+gemini): opt-in-only CI is insufficient (opt-in risks neglect) → ALSO add a MANDATORY cheap job on every push running the orchestration proof/handler suite (existing stubs + the A-prime regression tests), so a stub-regression is caught always while the heavy real-engine spawn stays opt-in/cron.
3. FixedPoint / progress law — `LoopProgressReceipt`; hash admitted graph state + accepted claim IDs + obligation hashes + seed refs; halt when a wave passes but produces no new admitted state; fixed-point halt applies no extra graph patch. (Codex build; files: handlers/lev-wizard-ratchet.ts + .test.ts.)
4. Formalize councils as executable profiles — CouncilMemberProfile V0 (role, allowedObligationKinds, allowedTools, outputSchema, forbiddenClaims, requiredEvidence, claimCeiling, repairBudget, profileHash). LLMs propose branch packets only; schema-checked.
5. Expand engine obligation kinds one at a time with negative controls — Julia (semantic/exact graph checks), JAX (batch/counterexample/projection), PyTorch (tensor/autograd/falsifier). Engines emit receipts, never proof authority.
6. Wire graph + memory carefully — engine result -> graph-op proposal -> ClaimGate admission -> graph apply -> event receipt -> next seed. Spinor/memory stays derived read-model until explicit promotion gates.
7. Run one CR-style bounded sim packet through Lev as host-executed evidence (forged/stale/path-laundered variants must reject), then scale to a corpus runner. Then gradual identity merge.

### DO NOT do (audit corrections held)
- Do NOT harden the graph-apply authority to cross-process — it is in-process BY DESIGN (`not_transferable`, issued+consumed atomically in `apply-graph-patch`); only revisit if a serialized apply-plan flow is intentionally supported (owner decision).
- Do NOT count `1c899f776` as test coverage — it is a vacuous reindent (52 ins/52 del, zero assertions).
- Do NOT build FixedPoint/councils/memory/corpus (steps 3-7) on top of the engine gate until the real-engine CI backstop (step 2) exists.

## Plugin punch-list (separate track, 11 fixed + verified, UNCOMMITTED)

Fixed and verified against the live tree, isolated to their own plugins: browser, flowmind (fixture path), mastra (test script), autoresearch (env-configurable model), slate (vitest alias), discourse-graph (handler export + barrel), bench (list regex), autowiki (already fixed), system-dashboard (whitespace generator), sentinel (test script), auth-sniffer (vitest run).
- REJECTED: storage (fabricated root cause — test passes on HEAD).
- DEFERRED: claw-router (needs shared-lockfile install + incomplete — also needs @x402/*, @solana/kit), watchdog (fiddly node --test glob + a live agent-smoke test).

## Model routing (fleet allocation)

- BULK / breadth workflow lenses: haiku (Claude cheap tier) + `codex exec` (Spark / gpt-5.5-low) shelled out for mechanical bulk.
- SUBSTANCE / adversarial verify / synthesis: sonnet.
- CROSS-CHECK, sparing: OpenRouter Chinese (deepseek/qwen/glm via curl, OPENROUTER_API_KEY in env) + xAI secondary (XAI_API_KEY in ~/.zshrc) — NOT grok-4.3-main as workhorse; reserve for security-critical closures.
- Workflow tool caveat: `agent()` spawns Claude only (opus/sonnet/haiku/fable); external fleet reached via agent Bash shell-out or direct Bash cross-check.

## Evidence receipts (preserved from ephemeral /tmp)

In `./lev-waverun-session-receipts-2026-07-01/`: BLOCKER_A_PRIME_AUDIT_PACKET, SYSTEM_INVENTORY (complete 28+ system inventory), massaudit_synthesis, CLAUDE1_CROSS_PROCESS_TRUST_RECEIPT, CLAUDE1_WIRING_RECEIPT, CODEX_AUDIT_AND_A22_FIX, THREAD_B_{SEED_GATE_RECEIPT, SEED_GATE_FRESH_AUDIT, HOSTCONSUME_FORGERY_FIX_RECEIPT}.

## Pilot log — Lev runs CR sims (foundations-up, no skip to Axis0)

- **2026-07-01 PILOT A — DONE + verified-by-Claude.** CR Rung-0 sim `probe_quotient_fingerprint_floor_v1` (julia+jax, z3 flip) brought into Lev as a HOST-OWNED carrier (`core/orchestration/src/probes/lev-sim-engine-carrier/cr-fingerprint-floor-v1/`, guard respected — not run from the CR path), wired as engine obligation `cr_fingerprint_floor_v1` (`julia_jax_required`) in claim-gate-wave-runner.ts + real-three-engine-envelope.ts, run through WaveRun → receipt `passed`, obligation `passed`, source hashes bind. Claude independently re-ran the julia lane: `ok:True`, z3 `full_P unsat` / `erased_P sat`, `flip_confirmed`. FIRST proof of "Lev runs a CR sim on real engines through a code gate." Caveats: UNCOMMITTED; run via a node script against dist, not the full `lev … wave-run` CLI; pytorch unscoped for this floor. (codex built; Claude verified.)
- **PILOT B (running).** Co-ratchet floor `entropy_geometry_coratchet_floor_v0` (exact-python oracle, not gated-clean) → port to 3 engines as host-owned carrier `cr-coratchet-floor-v0`, wire obligation `cr_coratchet_floor_v0`, build the CO-RATCHET LOCK gate: geometry `{n,edges,components}` vs entropy/operator `T5_order_AB_vs_BA` co-vary under constraints, 1e-10 engine-vs-oracle parity, negative control that breaks the lock must reject. The entropy⇄geometry co-ratchet tested as a probe result. Owner confirms the "locked" science criterion.
- **2026-07-01 PILOT B — DONE + verified-by-Claude (co-ratchet lock is load-bearing).** Co-ratchet floor `entropy_geometry_coratchet_floor_v0` ported into Lev as host-owned carrier `cr-coratchet-floor-v0` (exact-python oracle + julia + jax lanes), obligation `cr_coratchet_floor_v0` (`julia_jax_required`; pytorch scoped out — no autograd observable). WaveRun run 664279 `passed` (earlier runs 481843/622572 correctly BLOCKED by the host-binding gate on envelope-hash mismatch — good sign the trust binding fires; codex iterated to green). Claude re-ran the julia lane primary + negative control: gate is value-coupled (`all_pass = negative_control ? !lock : lock`); primary locks, erase-T5 control (`erase_state_dependent_order_readout`, keeps geometry, removes T5) BREAKS the lock → the entropy⇄geometry co-ratchet tested as a real probe result, not by-construction. OWNER SCIENCE CALL PENDING: codex's proposed "locked" criterion = exact/julia/jax agree 1e-10 on geometry {n,edges,components}+capacity/block AND T5 ≥1 state-dependent noncommuting AB/BA pair AND AB_capacity≠BA_capacity AND geometry changes across the active carve chain. Uncommitted. (codex built; Claude verified the flip.)
