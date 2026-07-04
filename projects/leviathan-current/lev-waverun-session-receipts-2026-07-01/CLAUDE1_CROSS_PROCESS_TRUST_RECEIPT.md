---
title: Claude 1 — cross-process host-trust secret (lane deliverable)
author: Claude 1 (claude-opus-4-8)
created: 2026-06-30
type: claude1-lane-receipt
claim_ceiling: passes_local_rerun_not_canonical; new standalone module + tests only; wiring NOT applied (deferred behind Codex Slice A/B collision gate)
status: superseded
superseded_by: "current wave/canon receipts"
reason: "references patch/waverun artifact"
---

# Claude 1 — cross-process trust gap lane

## Bottom line

The four ClaimGate trust ledgers each sign with a per-process `randomBytes(32)` secret,
so no minted trust survives a process boundary -- which makes the recursive WaveRun
"next-seed wave" (seed -> new process -> re-validate prior host consume) impossible. I
built the smallest fix as a NEW standalone module: one persisted, file-sealed root secret
per Lev project root, with domain-separated subkeys. A MAC minted in one process now
validates in another. Proven across a real OS process boundary. Wiring into the existing
ledgers is documented but deliberately NOT applied, to respect the Codex Slice A/B file
boundary.

## Files inspected (read-only)

- `core/orchestration/src/handlers/claim-gate-loop.ts` -- `HOST_TRUST_PROCESS_SECRET = randomBytes(32)` (:75), `hostTrustMac` (:89), `claimGateProjectRoot()` / `hasLevProjectMarkers()` (:204-232), `hostTrustLedgerPath()` (:234), and the wave-run-host-consume ledger I added earlier (reuses `HOST_TRUST_PROCESS_SECRET`).
- `core/orchestration/src/proof/claim-gate-loop.ts` -- `HOST_GRAPH_EVENT_TRUST_PROCESS_SECRET = randomBytes(32)` (:1208), `hostGraphEventTrustMac` (:1226), `issueClaimGateHostGraphEventTrust` (:3021).
- `core/orchestration/src/proof/claim-gate-steering-run.ts` -- `HOST_WITNESS_PROCESS_SECRET = randomBytes(32)` (:32), witness MAC (:629).
- Confirmed by grep: no `process.env.*SECRET`, no file-based secret load, none of the three secrets exported or cross-referenced -- all three are ephemeral and unbridged. The wave-run-consume ledger is a fourth instance of the same per-process pattern.

## Files changed

Two NEW files only. No existing file edited.

- `core/orchestration/src/proof/host-trust-secret.ts` (new module)
- `core/orchestration/src/proof/host-trust-secret.test.ts` (new tests)

## Design decision: persisted sealed key (not signed handoff)

Chose a **persisted shared symmetric root secret** + HMAC-derived per-domain subkeys, because:
- It is the smallest change that makes the EXISTING symmetric `hmac-sha256:<hex>` ledgers cross-process -- each ledger swaps one `randomBytes(32)` constant for one `deriveHostTrustDomainKey(projectRoot, '<domain>')` call; the entry format, `stableStringify`, and `timingSafeEqual` checks are unchanged.
- Domain separation (subkey = `HMAC(root, "lev-host-trust-domain:" + domain)`) keeps the four ledgers cryptographically independent: a signing-surface weakness in one domain does not transfer to another.

Security tradeoff, stated explicitly: persisting the secret moves the posture from "unforgeable
even by the operator within a process" to "unforgeable unless you can read a host-owned 0600
file". That is the correct boundary for the gate's actual job -- stop caller-supplied JSON and
adapter placeholder refs from minting trust, since the secret file is outside the caller's
JSON-input path. It is NOT isolation against the host OS user.

Signed-handoff (asymmetric) alternative, NOT built: persist a sealed private key, sign ledger
entries with it, verify with a published public key, separating "can verify" (any process) from
"can mint" (private-key holder only). Heavier; reserve for if the operator-isolation property is
ever required. The module docstring records this so the next builder has the fork.

## Migration / compat for old in-process-only receipts

- No regression. Anything that validated in-process still validates in-process (same process,
  same loaded secret). Cross-process now ALSO works.
- No data migration: the ledgers are written fresh each run; there is no persisted ledger state
  from a prior ephemeral secret to convert. A ledger entry written under a prior process's
  ephemeral secret simply will not validate after wiring -- but it never validated across
  processes anyway, so nothing that worked before breaks.
- Concurrency: first-writer-wins via `writeFileSync(..., { flag: 'wx' })`; a racing second process
  reads the winner's secret rather than clobbering it. Tested implicitly by the create path.
- GITIGNORE PREREQUISITE (flagged, not done): the runtime secret path
  `.lev/context/.host-trust-root-secret` is currently NOT gitignored (`git check-ignore` returns
  nothing). It MUST be added to `.gitignore` before wiring, or the host secret would be
  committable. My tests never write into the repo (temp dirs only), so there is no pollution now;
  this is a wiring-time prerequisite.

## Tests added

`core/orchestration/src/proof/host-trust-secret.test.ts` -- 7 tests, all passing:
1. creates a 32-byte 0600 secret file on first use;
2. same secret within a process (cache) and after a simulated restart (re-load from file);
3. LOAD-BEARING: a MAC minted "before" a simulated process boundary validates "after", and a
   different project root (different persisted secret) does NOT validate (value-coupled control);
4. REAL cross-process: a separate OS `node` process (spawned via `execFileSync`) reproduces the
   parent's MAC from the same secret file alone -- the actual cross-process property, not a mock;
5. domain separation: same domain -> same key, different domain -> different key;
6. malformed (wrong-length) secret file -> throws;
7. empty domain label -> throws.

Commands (real output):
- `pnpm --dir core/orchestration exec vitest run src/proof/host-trust-secret.test.ts` -> 1 file, 7 tests passed.
- `pnpm --filter @lev-os/orchestration typecheck` -> exit 0 (whole package; the new module does not break the rest of orchestration).

## Proposed wiring (NOT applied -- apply after Codex Slice A/B lands, under collision check)

Each ledger replaces its module-level ephemeral secret with a lazy per-call derived key. Example
for the graph-event ledger in `proof/claim-gate-loop.ts` (Codex's Slice B file -- DO NOT touch
until Slice B lands):
- remove `const HOST_GRAPH_EVENT_TRUST_PROCESS_SECRET = randomBytes(32);`
- in `hostGraphEventTrustMac`, sign with `deriveHostTrustDomainKey(claimGateProjectRoot(), 'host-graph-event-trust')` instead of the constant.
Same shape for `host-trust` and `wave-run-host-consume` (handlers/claim-gate-loop.ts) and
`host-witness` (proof/claim-gate-steering-run.ts), with domain labels `'host-trust'`,
`'wave-run-host-consume'`, `'host-witness'`.

## Collision check against Codex Slice A/B -- CLEAN

- Files I authored: `core/orchestration/src/proof/host-trust-secret.ts` and `...host-trust-secret.test.ts` ONLY (confirmed via `git status --porcelain | grep host-trust-secret`).
- Hard-excluded files I did NOT touch: `claim-gate-wave-runner.ts`, `claim-gate-wave-runner.test.ts`, `proof/index.ts`, `core/graph/src/compositor.ts`, `core/memory/src/session-state-projection.ts`. (Those show as modified/untracked in `git status` from Codex's and earlier work -- NOT from me.)
- `proof/claim-gate-loop.ts` (Codex Slice B): NOT edited. Wiring into it is deferred to the proposal above.
- The new module imports nothing from any Codex-owned file (pure; takes `projectRoot` as a param), so it can be wired in later with zero circular-dependency risk.

## Ceiling / what is NOT claimed

- `passes local rerun`, NOT canonical, NOT committed (untracked, branch-local).
- This delivers the MECHANISM + proof, not the integrated fix. The ledgers still use ephemeral
  secrets until the wiring above is applied (deferred behind the Slice A/B collision gate).
- A fresh-context auditor should confirm: the child-process test genuinely spawns a separate OS
  process (it does -- `execFileSync(process.execPath, ['-e', ...])`); the domain-separation is real
  HKDF-style derivation; and the persisted-secret security tradeoff is acceptable for the intended
  deployment before wiring.
