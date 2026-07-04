# Thread B — WaveRun V0 host-consume seed gate — fresh-context adversarial audit

Repo: `/Users/joshuaeisenhart/GitHub/lev`, branch `claimgate-steering-bridge-lock` (dirty/untracked tree, audited on-disk state as instructed).

Files audited (both untracked/new on this branch per `git status`):
- `core/orchestration/src/proof/claim-gate-wave-runner.ts`
- `core/orchestration/src/proof/claim-gate-wave-runner.test.ts`

## Overall verdict: ISSUES-FOUND

The host-consume gate is real (not pure by-construction theatre) for the four cases the shipped test actually exercises, and the deterministic-gate layer underneath it is genuinely separate (independently file-backed, hash-checked evidence, not a string-presence check). But the gate has one concrete, reproduced defect: `receiptRef` is checked only for `length === 0`, not for whitespace-only content. A whitespace-only `receiptRef` is treated as a valid bound receipt and a next-run seed is emitted carrying that whitespace string as `hostConsumeReceiptRef`. The shipped test suite does not cover this case, so it never caught it.

---

## 1. Does `makeNextRunSeed` require `hostConsume.status === 'host_consumed'`?

CONFIRMED. `core/orchestration/src/proof/claim-gate-wave-runner.ts:318-325`:

```ts
if (
  !hostConsume
  || hostConsume.status !== 'host_consumed'
  || typeof hostConsume.receiptRef !== 'string'
  || hostConsume.receiptRef.length === 0
) {
  return null;
}
```

The second disjunct (`hostConsume.status !== 'host_consumed'`) is a direct, unambiguous status check. Any status other than `'host_consumed'` (`'adapter_projection_only'`, `'host_blocked'`, `'absent'` — the full `ClaimGateWaveRunHostConsumeStatus` union at line 74-78) short-circuits to `null`.

## 2. Does it require a non-empty `receiptRef` (typeof string && length > 0)?

CONFIRMED, but the non-emptiness check is weaker than "non-empty" in the meaningful sense — it is `length === 0`, not a trim-aware check. Same lines, third/fourth disjuncts:

```ts
|| typeof hostConsume.receiptRef !== 'string'
|| hostConsume.receiptRef.length === 0
```

`typeof !== 'string'` rejects `undefined`/non-string. `.length === 0` rejects the empty string. It does **not** reject whitespace-only strings (`"   "`, `"\t"`, `"\n"`) — see defect in answer 5.

## 3. THE KEY CHECK — do negative cases fail for the host-consume reason, not an unrelated gate failure?

CONFIRMED for all four cases in the shipped test (`claim-gate-wave-runner.test.ts:511-564`). Verified independently by reading the test and by re-running it:

| Case | `result.status` | `result.acceptedClaimIds` | `result.nextRunSeed` |
|---|---|---|---|
| `host_consumed` + real receiptRef (positive control) | `'passed'` | `['HOST_CONSUME_BRANCH']` | non-null, populated |
| `host_consumed` + no receiptRef | `'passed'` | `['HOST_CONSUME_BRANCH']` | `null` |
| `adapter_projection_only` | `'passed'` | `['HOST_CONSUME_BRANCH']` | `null` |
| `undefined` (absent) | `'passed'` | `['HOST_CONSUME_BRANCH']` | `null` |

In every negative case `status === 'passed'` and `acceptedClaimIds` is non-empty — i.e. the deterministic ClaimGate layer (the `object_binding` / `evidence_manifest` / `falsifier` gate checks) genuinely accepted the claim. The only thing that differs between rows is `nextRunSeed`. This means the test is not vacuous: it isolates the host-consume gate as the sole suppressor of the seed in the negative rows.

Supporting evidence that the deterministic-gate layer is not rigged to trivially pass: `passingGateChecks()` (test file lines 99-109) writes real JSON files to a tmpdir via `writeSourceBoundGateEvidence` (lines 73-97) and returns `evidenceRefs: [file:<path>, sha256:<hash-of-file-body>]`. These are consumed by `runClaimGateCouncilWaveLoopWithHostTrustedEvidence` in `claim-gate-loop.ts`, which is a separate, independently-imported module — not re-implemented in the wave-runner test. The wave-runner module itself contains no shortcut that marks a claim accepted regardless of gate content; `runClaimGateWaveRun` derives `acceptedClaimIds` from `finalResult.graphPatchProposal.acceptedClaimIds` (`claim-gate-wave-runner.ts:467`), which is a pass-through of whatever the underlying loop function decided.

I additionally forced a real negative on the deterministic-gate side (adversarial probe, not in the shipped suite — see answer 5 / Section "Independent adversarial probe") by setting a gate check to `status: 'fail'`: the result was `status: 'blocked'`, `acceptedClaimIds: []`, confirming the deterministic gate path is a live, content-sensitive code path, not a constant.

## 4. Is `status: 'passed'` + `nextRunSeed: null` coherent, and is host-consume kept separate from the gate verdict?

CONFIRMED as designed; flagged as a footgun risk.

`runClaimGateWaveRun` computes `blocked` independently of `hostConsume` (`claim-gate-wave-runner.ts:470-475`):

```ts
const blocked = (
  !finalResult
  || withheldClaimIds.length > 0
  || finalResult.failurePackets.length > 0
  || repairFindings.some((finding) => finding.severity === 'error')
);
const status: ClaimGateWaveRunResult['status'] = blocked ? 'blocked' : repaired ? 'passed_after_repair' : 'passed';
```

`hostConsume` never appears in this expression. `nextRunSeed` is computed on a separate line (`469`) via `makeNextRunSeed(...)`, which is the only place `hostConsume` is read. So the design is: deterministic ClaimGate verdict (`status`) and host-consume-bound seed emission (`nextRunSeed`) are two independent obligations, exactly as the inline comment at lines 313-317 states.

Is this the right design, or a footgun? Both readings survive and should not be collapsed:

- **Defensible reading**: `status: 'passed'` answers "did the deterministic, locally-checkable gates accept this claim", which is true regardless of whether a host happened to consume the run. `nextRunSeed: null` separately answers "is there a host-bound chain-forward artifact", which legitimately requires an external fact (host consumption) the wave-runner cannot manufacture. Conflating the two would force every unconsumed-but-locally-valid run to read as "blocked," which is a different and arguably false claim (the claim itself is not what's blocked — only its continuation is withheld).
- **Footgun reading**: any caller that only checks `result.status === 'passed'` (a very natural single-field check) will read this as full success and may not realize a continuation chain was silently withheld. The two-condition contract is undocumented at the type level — `ClaimGateWaveRunResult.status` carries no information that a seed was withheld. A caller has to know to also check `nextRunSeed !== null`.

This is a genuine design tension, not a bug. Flagging it rather than resolving it for the owner.

## 5. Is the gate by-construction? Adversarial input search.

Read the full condition (lines 318-325) and tested each branch directly against the real, compiled function (not a re-implementation) via an out-of-repo adversarial vitest probe (see "Independent adversarial probe" below).

**a. `hostConsume.receiptRef` is whitespace-only, `status: 'host_consumed'`.**

DEFECT CONFIRMED. `"   ".length === 3 !== 0`, so the fourth disjunct is false, the guard does not return `null`, and a seed is emitted with `hostConsumeReceiptRef: "   "`. Reproduced directly:

```json
{
  "status": "passed",
  "acceptedClaimIds": ["WHITESPACE_RECEIPT_BRANCH"],
  "nextRunSeed": {
    "kind": "ClaimGateWaveRunNextRunSeed",
    "claimCeiling": "accepted_survivor_seed_not_autonomous_execution",
    "sessionId": "adversarial-probe-session",
    "sourceReceiptId": "rcpt-0311fcdf70b7bbe6",
    "acceptedClaimIds": ["WHITESPACE_RECEIPT_BRANCH"],
    "hostConsumeReceiptRef": "   "
  }
}
```

Defect location: `core/orchestration/src/proof/claim-gate-wave-runner.ts:322` — `hostConsume.receiptRef.length === 0` should be `hostConsume.receiptRef.trim().length === 0` (or equivalent) to match the stated intent ("non-empty `receiptRef`... is load-bearing", per the test's own inline comment at `claim-gate-wave-runner.test.ts:544`). This is a real, exploitable gap: a host adapter that passes through an uninitialized/placeholder whitespace string (a plausible bug class — e.g. a template default or a stripped field that degrades to spaces) would silently satisfy the gate.

**b. `status: 'host_consumed'` but `acceptedClaimIds` is empty (all claims withheld).**

NOT REPRODUCIBLE as a leak — correctly blocked, but for a reason upstream of `makeNextRunSeed`, not because of the host-consume check itself. `makeNextRunSeed`'s first guard (line 310) independently requires `acceptedClaimIds.length > 0` and `withheldClaimIds.length === 0` and `failurePackets.length === 0`:

```ts
const acceptedClaimIds = result.graphPatchProposal.acceptedClaimIds;
if (acceptedClaimIds.length === 0 || result.graphPatchProposal.withheldClaimIds.length > 0 || result.failurePackets.length > 0) {
  return null;
}
```

Reproduced by forcing a failing gate check (`status: 'fail'` on `object_binding`): result was `status: 'blocked'`, `acceptedClaimIds: []`, `withheldClaimIds: ['WITHHELD_BRANCH']`, `nextRunSeed: null`. Correct behavior, and notably this guard is checked *before* the host-consume guard, so it is doing real, independent work — the host-consume gate is not the only thing standing between an unresolved claim and a seed.

**c. `status: 'host_blocked'` with a `receiptRef` present.**

NOT REPRODUCIBLE as a leak. `'host_blocked' !== 'host_consumed'` trips the second disjunct regardless of `receiptRef`. Reproduced: `status: 'passed'` (deterministic gates still pass — correctly independent per answer 4), `nextRunSeed: null`. Correct.

**d. A withheld claim coexisting with otherwise-accepted claims.**

Not separately re-tested beyond (b): the same first guard (`withheldClaimIds.length > 0`) covers this — any nonzero withheld count anywhere in the result blocks the seed regardless of host-consume status. This is an all-or-nothing seed gate at the wave level, not per-claim; that is a scope note, not a defect, since `ClaimGateWaveRunNextRunSeed.acceptedClaimIds` is a single list for the whole run.

**Conclusion on by-construction:** the gate is NOT fully by-construction — three of four adversarial branches (status mismatch, empty acceptedClaimIds, withheld claims) behave correctly and are independent, content-sensitive checks, not props. But the `receiptRef` non-emptiness check is incomplete: it is a presence/length check, not a content-validity check, and a whitespace-only value passes it. That is the kind of "string-presence check, not real content check" pattern the project's own binding doctrine (`feedback_my_own_builds_hit_byconstruction_and_presence_checks`) explicitly warns about.

## 6. Do the tests inspect result JSON fields, not prose?

CONFIRMED. Every assertion in the target test (`claim-gate-wave-runner.test.ts:539-560`) reads structured result fields: `consumed.status`, `consumed.acceptedClaimIds`, `consumed.nextRunSeed?.acceptedClaimIds`, `consumed.nextRunSeed?.hostConsumeReceiptRef`, `consumedNoReceipt.nextRunSeed`, `adapterOnly.nextRunSeed`, `absent.nextRunSeed`. No assertion touches a free-text/prose field, an LLM judge output, or a label string outside the typed result shape. This matches the project's "gates are code, never prose" doctrine.

---

## Independent execution (run by this auditor, not relayed from the builder)

```
cd /Users/joshuaeisenhart/GitHub/lev/core/orchestration
npx vitest run claim-gate-wave-runner
```
Result: **Test Files 1 passed (1)**, **Tests 9 passed (9)**, exit 0.

(Note: `pnpm --filter @lev-os/orchestration test -- claim-gate-wave-runner` as given in the task, run first, ran the FULL suite — 52 files / 782 tests, all passed — because `--` before the filter caused pnpm/vitest argument handling to not scope to the named file in this repo's script wiring. Re-ran scoped directly with `npx vitest run claim-gate-wave-runner` inside the package to get an honest single-file count.)

```
cd /Users/joshuaeisenhart/GitHub/lev
pnpm --filter @lev-os/orchestration typecheck
```
Result: `tsc --noEmit` completed with **exit 0**, no diagnostics printed.

## Independent adversarial probe (by-construction check)

Per the task's "optionally probe by-construction directly" instruction, I wrote a throwaway vitest spec at `/tmp/claude-burn-2026-06-29/lev-wave-run-loop/adversarial-seed-gate-probe.test.ts` (kept outside the repo) that imports the real `runClaimGateWaveRun` and feeds it three adversarial inputs not covered by the shipped test: whitespace-only `receiptRef`, `host_consumed` with all claims withheld, and `host_blocked` with a receiptRef present.

Vitest's `include` glob in `core/orchestration/vitest.config.ts` is rooted at `src/**/*.test.ts`, so an external file is not picked up by path matching even when passed explicitly, and a standalone `vitest.config.ts` outside the repo cannot resolve `vitest/config` (no local `node_modules`). To get a real run against the compiled module graph (not a hand-rolled re-implementation), I temporarily copied the same spec into `core/orchestration/src/__adversarial_probe_tmp__/` (untracked, never staged), ran it with `npx vitest run <path>`, captured output, then deleted the directory immediately after. `git status` confirms no trace remains (`src/proof/claim-gate-wave-runner.ts` and `.test.ts` show as the only untracked files in `core/orchestration/src/proof/`, consistent with the dirty branch state noted at task start — no `__adversarial_probe_tmp__` artifact left behind).

Results: the whitespace-receiptRef probe reproduced a real seed leak (see answer 5a). The other two probes confirmed correct blocking behavior.

## Concrete defect summary

| # | File:line | Defect | Severity |
|---|---|---|---|
| 1 | `core/orchestration/src/proof/claim-gate-wave-runner.ts:322` | `hostConsume.receiptRef.length === 0` accepts whitespace-only strings as a valid bound receipt; should be a trimmed/content check | Medium — gate is the stated security/provenance boundary ("receiptRef is load-bearing" per the test's own comment); a whitespace placeholder slipping through silently mints a seed |
| 2 | `core/orchestration/src/proof/claim-gate-wave-runner.test.ts:511-564` | No test case for whitespace-only `receiptRef`, `host_blocked` status, or `host_consumed`+empty-acceptedClaimIds — the shipped suite did not catch defect #1 | Low/process — coverage gap, not a runtime defect itself |

No other defects found. The status/seed separation (answer 4) is a design choice worth the owner's explicit sign-off, not a defect.
