---
title: Claude Thread B WaveRun correction
created: 2026-06-30
type: sendable-correction-prompt
status: current
claim_ceiling: Hermes read current Lev wave-runner files and ran targeted orchestration test; this is routing/build guidance, not admission.
---

# Claude Thread B WaveRun correction — 2026-06-30

Paste this to Claude Thread B.

```text
Stop looping on the role question. You are Thread B: Leviathan patch worker.

Hermes checked the current state at 2026-06-30 12:52–12:53 PDT:

- `core/orchestration/src/proof/claim-gate-wave-runner.ts` exists and is untracked.
- `core/orchestration/src/proof/claim-gate-wave-runner.test.ts` exists and is untracked.
- mtimes were 12:40:11 and 12:42:52; no fresh write was observed during the check.
- the `node` process holding the file open is TypeScript tsserver / LSP read-only, not proof of an active writer.
- targeted test command passed:
  `pnpm --filter @lev-os/orchestration test -- claim-gate-wave-runner`
  result: 52 test files passed, 780 tests passed.

But Hermes also read the files and found the important gap:

- The seed/host-consume gate is not enforced yet.
- `ClaimGateWaveRunInput` defines `hostConsume`, but `makeNextRunSeed(...)` ignores it.
- The required test `wave_run_seed_not_emitted_without_host_consumed` is still missing in substance.
- Current tests allow `nextRunSeed` when deterministic gates pass even if there is no host-consumed receipt.

So your next job is not to ask whether you are builder or auditor. Your next job is the missing patch:

1. Add the missing test: seed is not emitted unless hostConsume.status === `host_consumed` and a receiptRef exists.
2. Update WaveRun implementation so `nextRunSeed` is emitted only when:
   - final deterministic gates pass,
   - no withheld claims,
   - no failure packets,
   - no repair findings,
   - and `hostConsume.status === 'host_consumed'` with a receiptRef.
3. Preserve the ceiling: seed is `accepted_survivor_seed_not_autonomous_execution`.
4. Add/adjust a positive test proving seed emits when host-consumed is supplied.
5. Rerun:
   `pnpm --filter @lev-os/orchestration test -- claim-gate-wave-runner`
   `pnpm --filter @lev-os/orchestration typecheck`
6. Write receipt:
   `/tmp/claude-burn-2026-06-29/lev-wave-run-loop/THREAD_B_SEED_GATE_RECEIPT.md`

If you still believe a live Codex process is actively writing these exact files, do not stall. Instead write a patch file and receipt without touching the live files:

`/tmp/claude-burn-2026-06-29/lev-wave-run-loop/thread-b-seed-gate.patch`

But do not treat the TypeScript LSP having the file open as evidence of a writer.

Do not run broad CR sims. Do not audit Lev blockers. Do not ask the role question again. Patch the missing host-consume seed gate or emit the patch file if you prove an active writer.
```
