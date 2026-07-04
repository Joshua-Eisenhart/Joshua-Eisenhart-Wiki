---
title: Main Claude Wave 1a correction prompt
created: 2026-06-30
type: sendable-correction-prompt
status: current
claim_ceiling: Hermes verified ledger/receipts/worktree state; this prompt corrects workflow shape and next actions.
---

# Main Claude Wave 1a correction prompt — 2026-06-30

Paste this to main Claude.

```text
STOP. You are not running the requested mass workflow yet.

Hermes verified the current state:

- `/tmp/claude-burn-2026-06-29/lev-mass-parent-ledger.md` contains only Wave 1a planning.
- `/tmp/lev-mass-lanes/` has no lane worktrees.
- `/tmp/lev-mass-wt` now has untracked source files directly in the integration worktree:
  - `core/orchestration/src/handlers/claim-gate-loop.ts`
  - `core/orchestration/src/proof/claim-gate-loop.ts`
  - `core/orchestration/src/proof/claim-gate-host-trust-anchor.ts`
- Wave 1a wrote the integration worktree directly and materialized files from `d755e7a9b`, rather than using per-lane worktrees and patches.
- The adversarial verifier refuted the keystone as incomplete: A22c host-trust consume lane rejected forged refs, but graph-event trust was still forgeable in that worktree path.

This is useful work, but it is not the mass patch architecture requested.

## Immediate correction

Do not continue by editing `/tmp/lev-mass-wt` directly.

First, preserve the Wave 1a state as a failed/partial patch artifact:

1. Write:
   `/tmp/claude-burn-2026-06-29/lev-mass/wave1a-status.md`

It must say:
- builder result: A22c consume-lane patched
- verifier result: REFUTED / relocated still forgeable through graph-event ledger
- current integration worktree dirty state: three untracked files
- baseline mismatch: A22c target code was not in f918 baseline, materialized from `d755e7a9b`
- decision: do not build more lanes on this partial keystone until it is either integrated from the right base or reset into a proper lane worktree

2. Create the per-lane worktree structure now:
   `/tmp/lev-mass-lanes/a22c-root`
   `/tmp/lev-mass-lanes/rerun-path`
   `/tmp/lev-mass-lanes/key-normalization`
   `/tmp/lev-mass-lanes/evidence-context`

3. Each lane must be a separate git worktree and branch. Do not write lane edits directly to `/tmp/lev-mass-wt`.

4. Spawn at least these four workers now, bounded concurrency max 4:

- `a22c-root-and-graph-event-unified`
  - Goal: one unified host-trust primitive that covers both host-trusted evidence refs and graph-event trust, not one ledger only.
  - Must include legitimate host-issued path; not just rejection.
  - Must produce patch: `/tmp/claude-burn-2026-06-29/lev-mass/patches/a22c-root-and-graph-event-unified.patch`
  - Receipt: `/tmp/claude-burn-2026-06-29/lev-mass/a22c-root-and-graph-event-unified.md`

- `rerun-path`
  - Goal: block `/etc/hosts` and traversal; preserve in-root target files.
  - Patch + receipt.

- `key-normalization`
  - Goal: key normalization / suspicious-key rejection. Value normalization already exists.
  - Patch + receipt.

- `evidence-context`
  - Goal: host-attested evidence manifest context, not producer-vs-producer.
  - Patch + receipt.

5. Parent applies patches serially into `/tmp/lev-mass-wt` only after each lane writes patch + receipt.

6. Do not proceed to seed/Wizard Wave 2 until Wave 1 patches are integrated and targeted tests pass.

## Important base warning

The f918 committed baseline does not contain the A22c target code. You must decide and state the patch base:

- If the target is Codex's dirty live tree, you cannot patch it directly; you need Codex to apply or export that slice.
- If the target is a prior branch/commit like `d755e7a9b`, create the lane worktree from that branch/commit and state it.
- If you materialize files into f918 as untracked files, classify that as a transplant patch, not a clean branch patch.

Do not hide the base mismatch.

## Output after this correction

Reply with:
- wave1a-status path
- lane worktrees created
- workers spawned
- receipt paths expected
- whether `/tmp/lev-mass-wt` was reset clean or preserved dirty as partial evidence

Do not say done/canonical/landed.
```
