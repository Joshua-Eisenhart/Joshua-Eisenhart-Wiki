---
title: Codex audit + A22b/A22c regression fix
author: Claude 1 (claude-opus-4-8)
created: 2026-06-30
type: audit + fix receipt
claim_ceiling: passes_local_rerun; orchestration 805/805, typecheck 0; a22 fix + graph-event wiring + skill-loader uncommitted, host-trust committed
status: superseded
superseded_by: "current wave/canon receipts"
reason: "references patch/waverun artifact"
---

# Audit of Codex recent work + A22b/A22c regression fix

## Audit findings (5-lens Sonnet workflow, adversarially verified)

- **Blocker A STILL OPEN.** Codex's "source-bound matching" fixed `obligationHash` binding + host-supplied envelope/digest-context matching — real, value-coupled. It did NOT anchor the obligation's own `sourceHashes`/`graphStateHash`/`inputHash`: the real runner (`createRealThreeEngineObligationRunner`) calls `buildEnvelopeAndDigest()` with zero args, so those fields never reach it. Two agents independently forged all three hashes and got `status: passed` under `--real-engines`. Fix path: thread the declared hashes into `buildRealThreeEngineEnvelopeAndDigest` and compare vs `realpathSync`+sha256 of the actual carrier scripts, fail closed. In Codex's active file — coordinate.
- **Replay guards:** host-consume `HOST_CONSUME_REF_ALREADY_SPENT` = CONFIRMED-REAL (persisted JSONL, cross-process blocked live). graph-apply `CLAIMGATE_APPLY_PLAN_AUTHORITY_SPENT` = in-memory `Set`, per-process secret, NOT wired — cross-process double-spend trap; fixing the MAC alone would reopen it, so persist the spend-set together with any secret wiring.
- **Graph-apply authority MAC + carrier resolution:** CONFIRMED-REAL (not forgeable; Lev-owned-only, denylist + realpath allowlist + hash-pinned scripts).

## Codex reconciliation

Codex/owner committed my host-trust work as `bfc36727a fix(claim-gate): persist host trust root outside project state` (my host-scoped redesign). 6 recent commits including `4244bac03` (fixed the `inheritEnv` typecheck break). My graph-event-trust wiring + skill-loader fix remain clean uncommitted working-tree (no conflict).

## A22b/A22c regression — diagnosed and fixed

The audit reported orchestration 801/2 (A22b, A22c failing) and blamed generic "test isolation." Precise root cause: **my committed persisted-secret change surfaced a pre-existing orphaned-env-var bug.** The redteam tests set `LEV_CLAIMGATE_HOST_TRUST_ROOT` to isolate, but that var is read by ZERO production code — `claimGateProjectRoot()` reads only `LEV_PROJECT_ROOT`/`LEV_ROOT`; the caller-settable-root var was deliberately removed as the round-4 forgery vector. So the tests fell through to the real repo root and polluted `.lev/context/claim-gate-host-trust.jsonl` with test refs (`rcpt-object-bound`, etc.). Under the old per-process secret those stale refs never validated across runs; my persisted secret makes them validate, so A22b sees the ref as host-issued and its "should be disabled" assertion fails.

**Fix (test-only — deliberately does NOT re-add the removed env var):** `makeTempRoot` in `claim-gate-redteam-targets.test.ts` now creates Lev markers (`dna/graph.yaml`, `.lev/validation-gates.yaml`), and the 4 sites use the production-honored `LEV_PROJECT_ROOT`. Deleted the polluted ledger (backed up in scratchpad). Verified: moving the ledger aside made the suite 18/18; the isolation fix makes it durable — the tests now read their own temp ledger, never the real one.

## Verification

- `pnpm --filter @lev-os/orchestration test` -> 53 files, **805 pass, 0 fail** (was 801/2).
- `pnpm --filter @lev-os/orchestration typecheck` -> exit 0, 0 errors.

## Still open (not this turn)

- Blocker A (obligation hash anchoring) — Codex's file, coordinate.
- graph-patch cross-process wiring + persist the spend set (core/graph, needs the secret module relocated to `@lev-os/config`).
- The same orphaned-env-var isolation bug likely affects `core/harness` cdo-triple50 (audit flagged "same family") — separate package, not fixed here.
