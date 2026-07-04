---
title: Thread B packet — CR→Lev steering projection tamper gap
created: 2026-06-30
type: sendable-thread-b-finding-prompt
status: current
claim_ceiling: Hermes verified Thread A ledger and negative-control JSON artifacts on disk; this packet is a repro/fix target, not proof that the patch has landed.
---

# Thread B packet — CR→Lev steering projection tamper gap

Paste this to Claude Thread B / Lev patch worker.

```text
Thread A stood up the CR sim/result -> Lev produce -> Lev consume --no-write loop and found a live over-accept gap. This is now your Thread B patch target after the WaveRun seed-gate audit/closure.

Do not run broad CR sims. Do not edit CR source. Use Thread A artifacts as repro fixtures only.

Repo:
/Users/joshuaeisenhart/GitHub/lev

Thread A ledger:
/tmp/claude-burn-2026-06-29/cr-lev-sim-run-fresh/LEDGER.md

Clean host-consumed example:
/tmp/claude-burn-2026-06-29/cr-lev-sim-run-fresh/01-finite-density/consume-stdout.json

Negative controls:
/tmp/claude-burn-2026-06-29/cr-lev-sim-run-fresh/_negative_controls/nc1-consume.json
/tmp/claude-burn-2026-06-29/cr-lev-sim-run-fresh/_negative_controls/nc2b-consume.json
/tmp/claude-burn-2026-06-29/cr-lev-sim-run-fresh/_negative_controls/tampered-forge-pass-rundir/

Observed current behavior:

1. Clean row:
   - CR result hash fresh-bound: `7521bff4e3c3904cc6cddb0713ad5ec8c704e7f493c11c7996072d8c2ba5a3a8`
   - consume returned `ok:true`, `status:host_consumed`, `projectedVerdict:pass`, `recomputedVerdict:pass`, `findings:[]`.

2. NC1 obligation flip:
   - Thread A changed one exec-spec obligation (`claimgate.falsifier`) to `failed`.
   - produce verdict became `fail`.
   - consume returned `status:host_reviewed_failed`, `recomputedVerdict:fail`.
   - This proves consume is responsive to obligation status, not blind echo.

3. NC2 forge-pass:
   - Thread A copied the genuinely failed NC1 projection.
   - Then edited projection files under `tampered-forge-pass-rundir` so `fail/failed` became `pass/passed` in:
     - `eval-job-output.json`
     - `eval-job.json`
     - `proof-spec.json`
     - `boundary.json`
   - Running `lev orchestration claimgate-steering consume <tampered-forge-pass-rundir> --json --no-write` returned:
     - `ok:true`
     - `status:host_consumed`
     - `projectedVerdict:pass`
     - `recomputedVerdict:pass`
     - `findings:[]`
   - This is the defect: consume recomputes from tamperable projection files but does not detect post-produce projection mutation.

Bounded reading:
- The CR input/result hash is present and bound.
- The produced projection itself is not sealed against post-produce edits, or consume is not checking that seal.
- `host_consumed` currently means “well-formed projection recomputed to pass from current files,” not “projection is authentic/tamper-proof.”

Patch target:
Find the ClaimGate steering producer/consumer path, likely around:
- `core/orchestration/src/proof/claim-gate-steering-produce.ts`
- the corresponding consumer/handler for `lev orchestration claimgate-steering consume`
- any host witness/context files such as `.lev/context/claim-gate-steering-host-witnesses.jsonl`

Required behavior:
- produce must emit or append a host-sealed projection digest/witness that binds the produced projection files as written;
- consume must recompute projection file hashes and compare to the producer/host witness before accepting `host_consumed`;
- if projection files were changed after produce, consume must return a blocked/tamper finding, not `host_consumed`;
- `--no-write` must still enforce the seal check if a witness exists, or explicitly report `host_witness_absent`/`projection_unsealed` instead of `host_consumed`.

Required tests:
1. clean produced projection consumes as `host_consumed` when witness/hash seal matches;
2. obligation flip still fails normally;
3. post-produce tamper of `eval-job-output.json` blocks with a finding like `claimgate_steering.projection_digest_mismatch`;
4. post-produce tamper of `proof-spec.json` blocks;
5. post-produce tamper of `boundary.json` blocks;
6. missing host witness does not silently upgrade to `host_consumed` for newly produced sealed-mode runs;
7. `--no-write` mode enforces the same verification, without writing new receipts except allowed no-write output.

After patch, rerun:
- targeted ClaimGate steering produce/consume tests;
- `pnpm --filter @lev-os/orchestration test -- claim-gate-wave-runner` if touched surfaces affect WaveRun;
- `pnpm --filter @lev-os/orchestration typecheck`.

Then rerun Thread A’s NC2 fixture or reproduce it with a new temp projection and prove the forged pass is blocked.

Write receipt:
/tmp/claude-burn-2026-06-29/lev-wave-run-loop/THREAD_B_STEERING_PROJECTION_SEAL_RECEIPT.md

Do not claim canonical. Claim ceiling is `passes local rerun; uncommitted until integrated`.
```

## Hermes verification notes

Hermes directly read:

- `/tmp/claude-burn-2026-06-29/cr-lev-sim-run-fresh/LEDGER.md`
- `/tmp/claude-burn-2026-06-29/cr-lev-sim-run-fresh/01-finite-density/consume-stdout.json`
- `/tmp/claude-burn-2026-06-29/cr-lev-sim-run-fresh/_negative_controls/nc1-consume.json`
- `/tmp/claude-burn-2026-06-29/cr-lev-sim-run-fresh/_negative_controls/nc2b-consume.json`

Observed NC2 status in JSON:

```json
{
  "ok": true,
  "status": "host_consumed",
  "projectedVerdict": "pass",
  "recomputedVerdict": "pass",
  "findings": []
}
```

Do not save this as durable memory. It belongs in this receipt/prompt and, once fixed, in the relevant skill/procedure as a negative-control pattern.

## Addendum — Thread A mass-audit corrections (2026-06-30, after Hermes's verification pass)

Hermes verified the single 01-finite-density row plus NC1/NC2b — that verification is correct as far as it goes. A separate fresh-context mass audit ran afterward, independently reproducing all 7 envelope rows and sweeping for more forgery patterns. Two findings change the patch scope; a third is unrelated to Lev and noted only so it isn't lost.

### 1. Root cause is broader than "post-produce tampering" — widen the patch target

Two new attacks beyond NC2, both **accepted** by `consume`:

- a `claimgate.hashes` obligation whose `evidenceRefs` sha256 points at a completely unrelated file — accepted.
- a doctored CR result file (`all_pass:false`, failing its own internal checks) whose hash truthfully matches the doctored file — accepted.

Cause, confirmed by reading `claim-gate-steering-run.ts`: `consume` never opens or hashes the file an obligation's `evidenceRefs` cites. It only checks that its own 5 internal projection files (`run.json`, `proof-spec.json`, `eval-job.json`, `eval-job-output.json`, `boundary.json`) are present and well-formed. So the bug is not only "projection edited after produce" — an `evidenceRefs` hash that never matched its cited file in the first place also sails through.

Add to **Required behavior**: consume must dereference and re-hash the file(s) each obligation's `evidenceRefs` cites, not only the 5 internal projection files, before accepting `host_consumed`.

Add to **Required tests**:
8. an obligation whose `evidenceRefs` sha256 does not match the file it cites is blocked, independent of whether the projection files themselves were edited;
9. a doctored evidence file with a self-consistent (truthfully matching) hash but failing internal content is blocked.

One attack — dropping 2 of 14 required obligations from the exec-spec — was correctly **blocked**: produce is fail-open on missing names, but consume independently re-derives the required-gate set and fails closed. That part of the design works; leave it as-is.

### 2. The ledger is not 7/7 confirmed — do not treat the batch as reliable repro fixtures

Independent reproduction of the 6-envelope batch (separate from the finite-density row Hermes checked) found:

- `01-finite-density`, `r4-mc-profile`, `r4-nonassoc-disc` — reproduce credibly as host_consumed, each with its own caveat (mc-profile is a self-attested echo of the validator boolean; nonassoc-disc wrote no durable receipt under `--no-write`).
- `r4-spinor-holonomy` — **not** host_consumed. That row's own `run.json` says `live_lev_consumed:false`; no consume artifact exists in its directory. The host_consumed values originally reported for it belong to a different run's saved file.
- `r5-weyl-chirality` — **not** host_consumed, fabricated. No consume output file exists, no trace of the claimed receipt ID anywhere, and `boundary.json` says `live_lev_consumed:false`.
- `clifford-spinor-carrier` — **not** host_consumed. No evidence the `lev` CLI was invoked at all: zero hits in Lev's event logs, identical synthetic timestamps and `elapsedMs:1` padding across all 5 produce files.
- `r5-hopf` — unverified; the audit hit a rate limit before re-deriving this row. Do not cite it as confirmed in either direction.

This is a Thread-A-side batch-script reliability defect (`batch_thread_a.py`), not a Lev bug. Flagging it here only so Thread B doesn't treat the full original ledger as 7 independently-confirmed repro fixtures — use `01-finite-density` as the trustworthy one; the NC1/NC2 artifacts Hermes cited are unaffected by this.

### 3. Unrelated to Lev — noted for provenance only

The same audit pass found the CR tree at `/Users/joshuaeisenhart/Desktop/Codex Ratchet` was wrongly characterized as stale earlier in Thread A. It holds ~1,000 dirty entries of real unmerged work. Not a Thread B concern; not actioned here.
