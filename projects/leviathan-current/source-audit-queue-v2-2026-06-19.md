---
title: Leviathan Source Audit Queue V2
type: audit-queue
status: proposed-next-pass
claim_ceiling: work queue; not completed proof
---

# Leviathan Source Audit Queue V2

## Purpose

This queue tells the next Codex/Hermes pass exactly where to push beyond the current wiki.

## Highest-priority repo checks

1. Fresh clone snapshot: record remote, commit SHA, clean status.
2. `pnpm install` result.
3. `pnpm run build:poly` result.
4. default `lev pentagon run/gate --project .` result.
5. named `pentagon-sdk-poly-binding` result.
6. `pnpm --filter @lev-os/testing test` result.
7. targeted event-dispatch tests after package import fixes.
8. search for child-process `process.env` pass-through and classify severity.
9. `core/context-graph`, `core/graph-algorithms`, `core/reconciler`, `core/world-model` source status.
10. plugin posture reconciliation.

## Highest-priority attribution checks

1. Inspect `josh-flowmind-spec.zip` only with explicit approval and classify source ownership before citation.
2. Locate source evidence for the original Wizard idea from JP if available.
3. Build a Wizard lineage ledger separating original idea, packet mechanics, MMM, taskcards, route truth, adapters, and conformance.
4. Check `docs/design/proposal-flowmind-system.md` and `proposal-flowmind-ratchet.md` directly in current repo after a fresh clone.
5. Re-check `docs/NORTH_STAR.md` Josh attribution lines in current snapshot.

## Highest-priority wiki cleanup

1. Link owner correction from read-first/index.
2. Add no-ratchet-from-leviathan policy.
3. Add delusion audit.
4. Add Wizard origin note.
5. Patch stale local-checkout language in older packet pages.
6. Add claim-linter patterns for forbidden attribution reversals.
