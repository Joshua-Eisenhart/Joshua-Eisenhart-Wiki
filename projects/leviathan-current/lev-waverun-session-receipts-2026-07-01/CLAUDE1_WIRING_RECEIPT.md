---
title: Claude 1 — cross-process secret WIRED (2 of the chain-crossing ledgers)
author: Claude 1 (claude-opus-4-8)
created: 2026-06-30
type: claude1-wiring-receipt
claim_ceiling: passes_local_rerun_not_canonical; orchestration 800/800; uncommitted; graph-patch ledger still pending
status: superseded
superseded_by: "current wave/canon receipts"
reason: "references patch/waverun artifact"
---

# Claude 1 — cross-process secret wiring

## Bottom line

Executed punch-list item #1. The cross-process trust gap is now closed for the two
chain-crossing ledgers. Orchestration suite 800/800, my wired files typecheck clean, and
the persisted host secret was created live on disk.

## What changed

1. **Module redesigned host-scoped** (`core/orchestration/src/proof/host-trust-secret.ts`).
   The sealed secret now lives at `~/.local/share/lev/host-trust-root-secret` (XDG,
   0600, in a 0700 dir), NOT under a project root. Reason: persisting under the
   caller-controllable `LEV_PROJECT_ROOT` would re-open the redirection attack the audit
   confirmed closed (an attacker redirecting the root to a dir they own could read the
   sealed secret and forge MACs). Host-scoping closes it — redirecting the root moves a
   ledger PATH but never the secret. The gitignore prereq is now moot (secret is not in
   the repo). API: `deriveHostTrustDomainKey(domain)`; `LEV_HOST_TRUST_SECRET_PATH`
   override for tests. Module tests 8/8 (incl a redirection-resistance test + a real
   OS child-process MAC-reproduction proof).

2. **Wired host-trust + wave-run-consume** (`core/orchestration/src/handlers/claim-gate-loop.ts`,
   `hostTrustMac`, domain `host-trust`). Removed the per-process `randomBytes(32)`;
   updated the stale comment.

3. **Wired host-graph-event-trust** (`core/orchestration/src/proof/claim-gate-loop.ts:1227`,
   domain `host-graph-event-trust`). Removed the per-process secret.

## What I deliberately did NOT wire (and why)

**Host-witness stays per-process** (`core/orchestration/src/proof/claim-gate-steering-run.ts`).
Wiring it FLIPPED two tests: "a host witness issued by another process is not replayable
into this process" and "blocks replaying a host-issued witness ledger from another
process." Those tests show the witness's anti-replay is implemented BY process-secret
isolation, not by a nonce/spent guard — so cross-process witness validation is a replay
violation by design, not the bug. I reverted the witness wiring and added a comment
documenting the distinction. Key lesson: not all 5 ledgers want cross-process durability —
only the chain-crossing tokens (host-consume, graph-event-trust) that the recursive loop
and apply chain carry across CLI invocations; execution-attestation tokens (witness) stay
process-local for anti-replay.

## Verification (real output)

- `pnpm --dir core/orchestration exec vitest run src/proof/host-trust-secret.test.ts` -> 8/8.
- `pnpm --filter @lev-os/orchestration test` -> 53 files, **800 tests pass, 0 fail**.
- `pnpm --filter @lev-os/orchestration typecheck` -> ONE error, in
  `real-three-engine-envelope.ts:419` (`inheritEnv` not on `MechanicalProbeExecutedNegativeControlRequest`)
  — a file I never touched, mtime 16:19 (Codex's concurrent edit). None of my wired files
  have type errors.
- Live: `~/.local/share/lev/host-trust-root-secret` created during the run — 32 bytes,
  `-rw-------`, outside the repo.

## Still to do (item #1 not fully complete)

- **graph-patch apply authority** (`core/graph/src/handlers/graph-patch.ts`,
  `HOST_GRAPH_PATCH_PROCESS_SECRET`). `core/graph` does NOT depend on `@lev-os/orchestration`
  (the dep runs the other way), so it cannot import this module. Relocate the module to a
  shared package both depend on — `@lev-os/config` is the right home (`@lev-os/domain` is
  no-I/O; my module does fs). Then wire graph-patch + update the 2 orchestration imports.
- Persist the graph-patch single-use spend set (`spentClaimGateGraphApplyAuthorityNonces`)
  to a ledger file — currently in-memory, does not survive a restart (audit + inventory
  flagged).
- Blocker on doing the above cleanly: Codex's `inheritEnv` typecheck break in
  `real-three-engine-envelope.ts` should clear first, and Codex is actively editing that
  package — a cross-package change is best made once their edit settles.

## Ceiling

`passes local rerun`, not canonical, uncommitted, branch-local. A fresh-context auditor
should confirm: the witness-stays-per-process reasoning is correct (cross-process witness
really is replay, not a needed chain token), and the host-scoped secret location genuinely
closes the redirection attack for the two wired ledgers.
