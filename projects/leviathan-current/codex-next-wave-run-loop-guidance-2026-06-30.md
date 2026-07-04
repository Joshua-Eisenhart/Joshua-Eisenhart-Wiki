---
title: Codex next guidance — executable WaveRun loop
created: 2026-06-30
type: sendable-codex-implementation-prompt
status: current
claim_ceiling: Hermes inspected current Lev surfaces and wrote a next-build packet; Codex must verify exact current source before editing.
---

# Codex next guidance — executable WaveRun loop

Paste this to Codex.

```text
You have the right diagnosis. Now stop widening the audit and build the missing runtime spine.

The next implementation target is NOT:
- another prose summary of Julia/JAX/PyTorch usefulness;
- more static council artifacts;
- another one-off real-engine hardening seam;
- CR sim expansion;
- LLM councils deciding gates.

The next implementation target IS:

Build an executable WaveRun loop where model/council lanes may only propose branch packets, and deterministic host gates decide what survives. The loop must self-repair failed branches through repair-wave packets, then rerun the deterministic gates. Three-engine execution is one deterministic obligation type where scoped; it is not the whole gate system.

## Current source anchors Hermes checked

Lev live tree:
`/Users/joshuaeisenhart/GitHub/lev`
branch: `claimgate-steering-bridge-lock`
HEAD seen by Hermes: `f9185635334f`
status count seen by Hermes: `223` dirty entries

Relevant files exist:
- `core/orchestration/src/proof/claim-gate-loop.ts`
- `core/orchestration/src/proof/real-three-engine-envelope.ts`
- `core/graph/src/probes/mechanical-probe-runner.ts`
- `core/graph/src/contracts/projection-binding.ts`
- `core/orchestration/src/proof/lev-wizard-ratchet.ts`
- `core/harness/src/execution/claim-gate-repair-dispatch.ts`
- `core/harness/src/execution/cdo-triple50.test.ts`

Observed shape:
- `runClaimGateCouncilWaveLoop` already has deterministic loop concepts: waves, failure packets, repair bindings, requeue events, graph patch proposal.
- But part of the current core still has fixture-level pass logic (`passOnWave`, `fixture_truth_gate`, `deterministic_pass_conditions_fixture_level`).
- `real-three-engine-envelope.ts` already executes real Julia/JAX/PyTorch Lev-owned carrier probes with source hashes, negative controls, and `LevEngineSubstrateDigest` validation.
- `claim-gate-repair-dispatch.ts` already builds repair execution requests and expects JSON `ClaimGateCouncilWaveInput` outputs from repair workers.

So do not invent a new architecture. Connect these pieces into a real WaveRun loop.

## Build WaveRun V0

Add the smallest executable object that binds the existing pieces:

`ClaimGateWaveRunInput`
- sessionId
- workstreamId
- maxWaves
- initial `ClaimGateCouncilWaveInput`
- deterministic gate policy
- optional `runRepairDispatch` / injected repair executor
- optional `runThreeEngineEnvelope` / injected three-engine runner

`ClaimGateWaveRunResult`
- waves actually run
- branch/claim statuses
- deterministic gate results
- failure packets
- repair dispatch plans
- repair dispatch execution results
- requeue events
- graph patch proposal
- next-run seed only if deterministic gates and host consume conditions are satisfied
- receipt with claim ceiling: `wave_run_deterministic_gate_loop_not_llm_admission`

Recommended file:
`core/orchestration/src/proof/claim-gate-wave-runner.ts`

Export it from orchestration if needed.

## Gate rule

A claim/branch may pass only if all required gate ids are mechanically satisfied.

Required first gate ids:
- `object_binding`
- `evidence_manifest`
- `falsifier`
- `sim_engine_probe` when scoped

Do not allow these to pass from prose or model agreement. A model lane can only return a proposed `ClaimGateCouncilWaveInput` / branch packet. The host converts that into gate checks and runs deterministic validators.

## Three-engine obligation V0

Do not generalize every branch yet. Use the existing real-engine path as one obligation:

- If a branch declares `sim_engine_probe` with supported object `lev_r0_quotient_refinement`, run or inject `buildRealThreeEngineEnvelope()`.
- Validate the envelope/digest with the existing projection-binding validator.
- Attach envelope hash + substrate digest hash to the claim evidence context.
- If the digest is missing, forged, stale, or carrier path is CR/wiki/reference-owned, block with a finding.
- If branch type is unsupported, return `blocked_unsupported_engine_obligation`; do not silently pass.

This is the narrow real gate that exists. Make it a reusable obligation surface without pretending it gates every CR branch yet.

## Repair loop V0

Use existing pieces instead of handwaving:

1. Run `runClaimGateCouncilWaveLoop` on current wave input.
2. Build `buildClaimGateRepairWavePlan` from failure packets.
3. Build `buildClaimGateRepairDispatchPlan`.
4. Execute repair dispatch only through an injected executor in unit tests first. It must return a JSON `ClaimGateCouncilWaveInput`.
5. Validate the returned repair wave:
   - required claim id matches;
   - `repairOf.failurePacketId` matches;
   - required violated gates are present;
   - no new unrelated claims are smuggled in;
   - claim ceiling remains repair-candidate only.
6. Append the repair wave and rerun deterministic gates.
7. Stop at `maxWaves`; terminal failures are withheld, not patched into graph proposals.

This proves the recursive topology without needing live provider/model availability.

## Tests first / acceptance tests

Add tests before or with implementation. Minimum tests:

1. `llm_prose_cannot_pass_gate`
   - a model/council claim with confident prose but no source-bound evidence is withheld.

2. `failed_branch_requeues_only_itself`
   - one pass + one fail in wave 1;
   - only the failed claim is requeued;
   - accepted graph proposal excludes terminal failed claims.

3. `repair_executor_output_must_bind_failure_packet`
   - injected repair executor returns a repair wave for the wrong claim/failure packet;
   - WaveRun blocks it.

4. `repair_wave_can_flip_after_mechanical_gate`
   - injected repair output supplies the required deterministic evidence;
   - rerun admits the repaired claim under the ceiling.

5. `sim_engine_probe_requires_real_digest`
   - missing/forged three-engine digest blocks.

6. `supported_real_engine_obligation_attaches_digest`
   - injected or real `buildRealThreeEngineEnvelope()` returns a valid envelope;
   - result records envelope hash, substrate digest hash, source hashes, negative controls.

7. `unsupported_engine_obligation_blocks`
   - branch asks for an unsupported sim-engine object;
   - status is blocked, not pass.

8. `wave_run_seed_not_emitted_without_host_consumed`
   - if graph/steering host consume is absent or adapter-only, no next-run seed.

Do not write tests that pass by inspecting model text. Tests should inspect JSON/result fields.

## Commands to run

Use the existing package scripts.

Targeted first:
`pnpm --filter @lev-os/orchestration test -- claim-gate-loop claim-gate-wave-runner`
`pnpm --filter @lev-os/harness-sdk test -- claim-gate-repair-dispatch cdo-triple50`

Then:
`pnpm --filter @lev-os/orchestration typecheck`
`pnpm --filter @lev-os/harness-sdk typecheck`
`pnpm --filter @lev-os/orchestration build`
`pnpm --filter @lev-os/harness-sdk build`

Also rerun the exact `--real-engines` CLI command you used earlier and record it. Do not invent a new command in the report; report the actual command and output.

## Output artifacts

Write a parent receipt:
`/tmp/claude-burn-2026-06-29/lev-wave-run-loop/WAVE_RUN_V0_RECEIPT.md`

Include:
- files changed
- tests added
- commands run with exit codes
- one example WaveRun JSON result path
- whether three-engine obligation ran real or injected
- exact remaining limitations

If you spawn subagents, use bounded workers only. Route Sonnet 5 / newest Sonnet specifically to the subagents if that is available; the parent/controller still owns integration and verification. Do not use Sonnet 5 confidence as a gate result.

Worker A: orchestration WaveRun types + deterministic loop tests.
Worker B: three-engine obligation adapter tests.
Worker C: repair dispatch binding tests.
Worker D: fresh audit after A/B/C land.

Max 3 builder subagents at once, plus one fresh audit after they land. Builder/subagent verdicts are not evidence; parent verifies tests, files, hashes, and ClaimGate outputs.

## Do not overbuild

Do not try to solve all CR sims or all council topologies in this pass. V0 succeeds if it proves:

LLM/council outputs are branch proposals only
→ deterministic host gates classify them
→ failed branches create repair packets
→ repair packets can loop once or more
→ three-engine digest is one real mechanical obligation
→ no next seed / graph mutation occurs from prose or adapter-only output.

## Final report shape

Return exactly:

`Implemented:`
- paths and short description

`Mechanical gates now enforced:`
- list gate ids and what code decides them

`Recursive loop proof:`
- which test shows self-loop repair
- which test shows terminal withhold
- which test shows no LLM-prose admission

`Three-engine obligation:`
- real or injected in tests
- envelope/digest fields checked

`Commands:`
- command + exit code

`Still not done:`
- unsupported branch types
- live provider dispatch if still mocked/injected
- general CR-sim obligation mapping if not built
```
