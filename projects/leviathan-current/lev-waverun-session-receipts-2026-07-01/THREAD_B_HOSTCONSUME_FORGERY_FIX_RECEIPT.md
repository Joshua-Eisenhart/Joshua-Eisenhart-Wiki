---
title: Thread B — WaveRun hostConsume forgery fix
author: Claude Thread B (claude-opus-4-8 / claude-sonnet-5 audit)
created: 2026-06-30
type: thread-b-patch-receipt
claim_ceiling: passes_local_rerun_not_canonical; independently fresh-context audited; uncommitted branch-local change
status: superseded
superseded_by: "current wave/canon receipts"
reason: "references patch/waverun artifact"
---

# Thread B — WaveRun hostConsume forgery fix

## Bottom line

A mass adversarial audit (5-lens workflow) found that `ClaimGateWaveRunInput.hostConsume`
had zero cryptographic anchoring — a fifth instance of the caller-trust-forgery root this
codebase has already fixed four times elsewhere. Confirmed live: a forged `receiptRef`
invented in a JSON file minted a real `nextRunSeed` through the actual `wave-run` CLI
handler. Both this and a smaller Unicode-whitespace bypass are now fixed and independently
re-verified by a fresh-context auditor who ran live exploits against the fix itself.

## How it was found

Live CLI work this session ran `lev orchestration claim-gate-loop wave-run` with a
self-invented `hostConsume.receiptRef` and got `status:'passed'` with a seed — at the time
read as proof the gate worked. The mass audit's `mutation_bypass` lens proved this was
itself an exploit: the CLI's `wave-run` subcommand reads arbitrary JSON and passes
`hostConsume` straight into `runClaimGateWaveRun` with no validation, unlike the sibling
`consume` subcommand, which validates `--host-trusted-evidence-ref` flags against a
host-issued HMAC-signed ledger first.

## What was patched

### Fix 1 — Unicode visible-content check (defense in depth)
File: `core/orchestration/src/proof/claim-gate-wave-runner.ts`, `makeNextRunSeed`.

`receiptRef = hostConsume?.receiptRef?.replace(/\p{Cf}/gu, '').trim()` — strips Unicode
"Format" category characters (zero-width space/joiner/non-joiner, BOM, soft hyphen, word
joiner) before the truthiness check, closing the audit's reproduced U+200B bypass.

Residual (non-blocking) gap found by the verification auditor: U+3164 (HANGUL FILLER) and
U+2800 (BRAILLE PATTERN BLANK) are category Lo/So, not Cf, and survive the strip. Not a
security bypass — the load-bearing check (Fix 2) still requires an exact-string match
against an HMAC-signed ledger entry, which these characters do not satisfy by accident.
Worth tightening later; not urgent.

### Fix 2 — Host-issued, MAC-signed consume ledger (the real fix)
File: `core/orchestration/src/handlers/claim-gate-loop.ts`.

Mirrors the existing `HOST_TRUST_PROCESS_SECRET` / `hostTrustMac` / `validHostTrustedEvidenceEntry`
/ `hostIssuedTrustRefs` pattern exactly, scoped to wave-run host-consume:

- `ClaimGateWaveRunHostConsumeRefEntry` — ledger entry shape (kind, claimCeiling, authority,
  receiptRef, nonce, issuedAt, payloadHash, mac).
- `waveRunHostConsumeLedgerPath()` — `.lev/context/claim-gate-wave-run-host-consume.jsonl`
  under the Lev project root.
- `issueClaimGateWaveRunHostConsumeRef(receiptRef, root)` — exported; the ONLY way to mint
  a valid entry. HMAC-signs with the same per-process `HOST_TRUST_PROCESS_SECRET`. Never
  called by the `wave-run` subcommand on the caller's behalf — confirmed by trace and grep,
  its only call site outside its own definition is the test file.
- `validWaveRunHostConsumeRefEntry(value)` / `hostIssuedWaveRunConsumeRefs()` — validates
  and reads the ledger via `timingSafeEqual`-checked MAC comparison.
- `callerSuppliedWaveRunHostConsumeResponse` — the rejection response, `error_code:
  'CALLER_SUPPLIED_HOST_CONSUME_DISABLED'`.

`wave-run` subcommand: if `input.hostConsume?.receiptRef` is a non-empty string, it must
be present in `hostIssuedWaveRunConsumeRefs()` or the request is rejected BEFORE
`runClaimGateWaveRun` is ever called. No artifact is written on rejection.

## Tests added

- `core/orchestration/src/proof/claim-gate-wave-runner.test.ts`: zero-width-space
  receiptRef case added to the existing host-consume test (still no seed).
- `core/orchestration/src/handlers/claim-gate-loop.test.ts`: two new tests —
  `blocks a wave-run hostConsume.receiptRef the host never issued, even when deterministic
  gates pass` (forged ref -> `CALLER_SUPPLIED_HOST_CONSUME_DISABLED`, no output file at
  all) and `accepts a wave-run hostConsume.receiptRef the host actually issued and emits a
  real next-run seed` (calls `issueClaimGateWaveRunHostConsumeRef` first, then succeeds).

## Verification (commands + real output)

- `pnpm --dir core/orchestration exec vitest run src/proof/claim-gate-wave-runner.test.ts
  src/handlers/claim-gate-loop.test.ts` -> 2 files, 26 tests, all passed.
- `pnpm --filter @lev-os/orchestration typecheck` -> exit 0.
- Live, through the real CLI binary (`lev orchestration claim-gate-loop wave-run`):
  - The earlier self-invented `hostConsume.receiptRef` now correctly rejected with
    `CALLER_SUPPLIED_HOST_CONSUME_DISABLED`.
  - A single-process script that calls `issueClaimGateWaveRunHostConsumeRef` then the real
    `handler(['wave-run', ...])` in the same process: `status:'passed'`, real `nextRunSeed`
    with the issued `receiptRef`.
- INDEPENDENT fresh-context audit (Sonnet, did not write this code) re-verified both fixes
  by running live exploits against them: hand-tampered a ledger line with a fabricated MAC
  and got it correctly rejected (`hostIssuedWaveRunConsumeRefs` filters it out); confirmed
  `issueClaimGateWaveRunHostConsumeRef`'s only call site is the test file; reasoned through
  and confirmed an `LEV_PROJECT_ROOT`-redirection attack buys an attacker nothing (they can
  choose where the ledger is read from, not compute a valid MAC without the in-process
  secret). Verdict: CONFIRMED FIXED.

## Known limitation (pre-existing pattern, not introduced by this fix)

`HOST_TRUST_PROCESS_SECRET` is `randomBytes(32)` generated fresh per process, never
persisted. This means a ledger entry issued by one process cannot be validated by a
different process invocation (e.g. two separate `lev` CLI calls from a shell) — only
within a single long-lived process. This exactly matches the existing `hostTrust` ledger's
lifecycle (same variable, same design), so it is not a regression. It does mean: real
production use of wave-run host-consume requires either an in-process caller (a long-lived
host/daemon that both performs the consume and calls `runClaimGateWaveRun` itself) or a
not-yet-built mechanism to bridge trust across process restarts — the same open question
the pre-existing host-trust ledger already has. Flagging for whoever next builds the real
host-execution bridge; not fixed here as it is a broader architectural question beyond this
patch's scope.

## Ceiling / what is NOT claimed

- `passes local rerun`, NOT canonical, NOT committed (untracked, branch-local).
- The other 4 lenses of the original mass audit (engine-obligation gate, repair-binding
  gate, prose-gate/test-quality, wiring-reachability) were not retrieved — the workflow's
  synthesis was truncated in delivery and the raw transcript was not force-read (explicit
  overflow guard). This receipt covers only the `mutation_bypass` lens finding and its fix.
