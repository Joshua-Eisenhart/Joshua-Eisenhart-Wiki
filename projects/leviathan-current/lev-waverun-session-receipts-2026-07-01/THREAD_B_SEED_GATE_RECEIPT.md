---
title: Thread B — WaveRun host-consume seed gate
author: Claude Thread B (claude-opus-4-8)
created: 2026-06-30
type: thread-b-patch-receipt
claim_ceiling: passes_local_rerun_not_canonical; builder receipt, fresh audit still required; uncommitted branch-local change
status: superseded
superseded_by: "current wave/canon receipts"
reason: "references patch/waverun artifact"
---

# Thread B seed-gate receipt — WaveRun V0 host-consume gate

## Bottom line

The WaveRun next-run seed is now gated on a receipt-bound host consume.
`makeNextRunSeed(...)` no longer emits a seed from deterministic-gate pass alone.
Live edit (files stable ~5 min, Codex idle) — not a patch file.

## What was patched

File: `core/orchestration/src/proof/claim-gate-wave-runner.ts`

`makeNextRunSeed(sessionId, result, hostConsume)` now returns a seed only when ALL hold:
- `result.graphPatchProposal.acceptedClaimIds.length > 0`
- `result.graphPatchProposal.withheldClaimIds.length === 0`
- `result.failurePackets.length === 0`
- (repair errors already force `status: blocked` upstream, which is checked at the call site)
- `hostConsume.status === 'host_consumed'`
- `typeof hostConsume.receiptRef === 'string' && hostConsume.receiptRef.length > 0`

On emit, the seed records `hostConsumeReceiptRef: hostConsume.receiptRef` and preserves the
ceiling `accepted_survivor_seed_not_autonomous_execution`. Supporting type added:
`ClaimGateWaveRunHostConsume { status: 'host_consumed'|'adapter_projection_only'|'host_blocked'|'absent'; receiptRef?: string }`
and optional input field `ClaimGateWaveRunInput.hostConsume`.

## Tests added / adjusted

File: `core/orchestration/src/proof/claim-gate-wave-runner.test.ts`

New test `does not emit a next-run seed unless the host actually consumed the run`
(the required `wave_run_seed_not_emitted_without_host_consumed`), value-coupled:
- positive control: `status:'host_consumed'` + `receiptRef` -> seed emitted, `hostConsumeReceiptRef` recorded;
- `status:'host_consumed'` with NO `receiptRef` -> `status:'passed'`, claim accepted, `nextRunSeed === null` (proves receiptRef is load-bearing);
- `status:'adapter_projection_only'` -> accepted but `nextRunSeed === null`;
- `hostConsume` absent -> accepted but `nextRunSeed === null`.

Shared test helper `waveRunInput(...)` now supplies `hostConsume: { status:'host_consumed', receiptRef:'receipt:rcpt-host-consume' }`
so the two pre-existing seed-asserting tests remain valid under the new gate.

## Commands run (exit codes / results)

- `pnpm --filter @lev-os/orchestration test -- claim-gate-wave-runner`
  -> 52 test files passed, 782 tests passed, 0 failed.
- `pnpm --filter @lev-os/orchestration typecheck`
  -> `tsc --noEmit`, exit 0.
- `pnpm --filter @lev-os/orchestration build`
  -> `tsc`, exit 0 (run earlier in the session, pre-receiptRef-tightening; typecheck since clean).

## Co-edit note (honest)

`claim-gate-wave-runner.ts` and `.test.ts` are untracked and were concurrently edited by a
live Codex session during this work (Codex added real-engine-runner imports +
`ClaimGateWaveRunRealEngineRunnerOptions` and an extra real-engine test). The changes are
non-overlapping with this seed-gate patch; the merged on-disk state typechecks and all
orchestration tests pass. Authorship of the file is therefore shared. If the two efforts
need clean separation, that is a coordination decision for the owner.

## Ceiling / what is NOT claimed

- Status: `passes local rerun` (this session). NOT canonical, NOT committed (branch-local,
  untracked on `claimgate-steering-bridge-lock`).
- This is a BUILDER receipt. Per builder != auditor, a fresh-context audit is still required
  before this is trusted: confirm the gate is not by-construction, that the negatives fail for
  the host-consume reason (not an unrelated gate failure), and that `status:'passed'` +
  `nextRunSeed:null` is the correct semantics for "gates passed but host did not consume".
- Host consume is represented as an INPUT condition in V0 (injected, like the three-engine
  runner). WaveRun does not itself perform a live host consume yet.
