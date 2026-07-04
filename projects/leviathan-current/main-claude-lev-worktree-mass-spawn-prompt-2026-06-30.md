---
title: Main Claude Lev worktree mass-spawn prompt
created: 2026-06-30
type: sendable-claude-worktree-controller-prompt
status: current
authority: owner-greenlit isolated worktree patch; do not edit Codex live tree
claim_ceiling: controller prompt only; not proof, not admission
---

# Main Claude Lev worktree mass-spawn prompt — 2026-06-30

Paste this to the main Claude thread.

```text
You have the missing greenlight now: isolated worktree patch by you is authorized. Do not ask the owner again whether to use a worktree. Do not edit Codex's live tree.

Live tree Codex owns, read-only only:
`/Users/joshuaeisenhart/GitHub/lev`

Integration worktree for you:
`/tmp/lev-mass-wt`  (macOS path may show as `/private/tmp/lev-mass-wt`)
branch: `lev-mass-patch-20260630`
base: `f9185635334f`

If `/tmp/lev-mass-wt` already exists and is clean, use it. If it is missing, create it from committed `f9185635334f`; do not copy Codex's dirty tree.

Parent ledger:
`/tmp/claude-burn-2026-06-29/lev-mass-parent-ledger.md`

Lane receipts:
`/tmp/claude-burn-2026-06-29/lev-mass/<lane-id>.md`

Patch files:
`/tmp/claude-burn-2026-06-29/lev-mass/patches/<lane-id>.patch`

## Core correction

The job is not to ask for another decision. The job is to mass-spawn bounded patch lanes in isolated worktrees, then integrate them serially into `/tmp/lev-mass-wt`.

Do not run another 14-wide fanout. Use bounded concurrency: max 4 implementation workers at once, plus at most 2 read-only verifier/spec workers. Rate-limit failures are already observed.

## Worktree architecture

Use **per-lane worktrees** for true mass editing without conflicts:

- integration worktree: `/tmp/lev-mass-wt`
- lane worktrees under: `/tmp/lev-mass-lanes/<lane-id>`
- each lane branch: `lev-mass/<lane-id>-20260630`

Create lane worktrees from the same base:

```bash
git -C /Users/joshuaeisenhart/GitHub/lev worktree add -b lev-mass/a22c-root-20260630 /tmp/lev-mass-lanes/a22c-root f9185635334f
git -C /Users/joshuaeisenhart/GitHub/lev worktree add -b lev-mass/rerun-path-20260630 /tmp/lev-mass-lanes/rerun-path f9185635334f
git -C /Users/joshuaeisenhart/GitHub/lev worktree add -b lev-mass/key-normalization-20260630 /tmp/lev-mass-lanes/key-normalization f9185635334f
git -C /Users/joshuaeisenhart/GitHub/lev worktree add -b lev-mass/evidence-context-20260630 /tmp/lev-mass-lanes/evidence-context f9185635334f
```

Do not create branches that already exist; if a worktree exists, inspect it and continue or create a new suffix.

Each implementation lane edits only its own lane worktree and writes a patch:

```bash
git -C /tmp/lev-mass-lanes/<lane-id> diff -- <allowed files> > /tmp/claude-burn-2026-06-29/lev-mass/patches/<lane-id>.patch
```

Parent applies patches one at a time to `/tmp/lev-mass-wt`, runs targeted tests after each apply, and records conflicts in the ledger. Do not stage or commit.

## Wave 0 — parent setup, no code edits

Do this first in the parent thread:

1. Verify `/tmp/lev-mass-wt` exists and is clean.
2. Verify it is on branch `lev-mass-patch-20260630` at `f9185635334f` unless already patched by you.
3. Create directories:
   - `/tmp/claude-burn-2026-06-29/lev-mass/`
   - `/tmp/claude-burn-2026-06-29/lev-mass/patches/`
   - `/tmp/lev-mass-lanes/`
4. Update parent ledger with current state.
5. Spawn Wave 1 lanes.

## Wave 1 — independent root-trust and hygiene fixes

Spawn these lanes with bounded concurrency. Each lane must write receipt + patch.

### Lane 1: `a22c-root`

Worktree: `/tmp/lev-mass-lanes/a22c-root`

Goal: close same-process host-trusted-evidence ref root redirection.

Files likely:
- `core/orchestration/src/handlers/claim-gate-loop.ts`
- `core/orchestration/src/handlers/claim-gate-loop.test.ts`
- possibly `core/orchestration/src/proof/claim-gate-redteam-targets.test.ts`

Requirements:
- Do not relitigate steering host witness MAC; it exists.
- Distinguish raw JSON ledger forgery, same-process issue/root redirection, graph-event trust A23b.
- Make host-trust issuance host-internal/token-gated or otherwise inaccessible to producer authority.
- Pin/validate trust root against canonical host root; no caller-settable env root as proof authority.
- Add regression: same-process imported caller cannot redirect root + issue trust + pass `--host-trusted-evidence-ref`.
- Preserve legitimate host-issued trust path.

Acceptance command:
```bash
pnpm --filter @lev-os/orchestration test -- src/handlers/claim-gate-loop.test.ts src/proof/claim-gate-redteam-targets.test.ts
pnpm --filter @lev-os/orchestration typecheck
```

### Lane 2: `rerun-path`

Worktree: `/tmp/lev-mass-lanes/rerun-path`

Goal: fix `rerun_commands` path ownership.

Files likely:
- `core/orchestration/src/proof/claim-gate-steering-run.ts`
- `core/orchestration/src/proof/claim-gate-steering-run.test.ts`
- possibly `core/orchestration/src/handlers/claimgate-steering.test.ts`

Requirements:
- Add regression where `boundary.target_files = ["/etc/hosts"]` blocks.
- Fix `hostCheckoutPathExists` so absolute paths outside canonical Lev checkout/run roots fail.
- Block traversal escapes.
- Preserve legitimate in-repo/fixture target files.
- Prefer hash-binding to `sourceFileHashes` if feasible in this lane; otherwise record as follow-up.

Acceptance command:
```bash
pnpm --filter @lev-os/orchestration test -- src/proof/claim-gate-steering-run.test.ts src/handlers/claimgate-steering.test.ts
pnpm --filter @lev-os/orchestration typecheck
```

### Lane 3: `key-normalization`

Worktree: `/tmp/lev-mass-lanes/key-normalization`

Goal: fix exact-string authority-key scan.

Files likely:
- `core/orchestration/src/proof/claim-gate-steering-run.ts`
- `core/orchestration/src/proof/claim-gate-steering-run.test.ts`

Requirements:
- Verify value normalization exists; do not claim value path is the bug.
- Normalize/reject suspicious keys before `Set.has` checks.
- Cover case, leading/trailing space, zero-width, and homoglyph variants.
- Keep error codes debuggable with raw offending key or a safe escaped form.
- Avoid breaking benign non-authority keys.

Acceptance command:
```bash
pnpm --filter @lev-os/orchestration test -- src/proof/claim-gate-steering-run.test.ts src/proof/claim-gate-redteam-targets.test.ts
pnpm --filter @lev-os/orchestration typecheck
```

### Lane 4: `evidence-context`

Worktree: `/tmp/lev-mass-lanes/evidence-context`

Goal: stop producer-vs-producer evidence-manifest context from conferring host trust.

Files likely:
- `core/orchestration/src/proof/claim-gate-loop.ts`
- `core/orchestration/src/proof/claim-gate-loop.test.ts`
- `core/orchestration/src/proof/lev-wizard-ratchet.ts`
- `core/orchestration/src/proof/lev-wizard-ratchet.test.ts`

Requirements:
- Determine if the fix belongs in council-wave loop, steering-run consumer, or Wizard route. Do not patch the wrong seam blindly.
- Add regression using forged evidence file + forged context. Expected withheld/blocked when route claims host-bound evidence.
- Introduce host-attested context path: token-gated, HMAC-signed, or host-store-derived.
- Public caller-supplied context must be advisory only or rejected for host-bound gates.
- Preserve fixture behavior with explicit ceiling if full host context is absent.

Acceptance command:
```bash
pnpm --filter @lev-os/orchestration test -- src/proof/claim-gate-loop.test.ts src/proof/lev-wizard-ratchet.test.ts
pnpm --filter @lev-os/orchestration typecheck
```

## Wave 1 integration

After the first four lanes return patches:

1. Parent reads all four receipts.
2. Parent applies patches one at a time into `/tmp/lev-mass-wt`.
3. After each patch:
   - run that lane's targeted tests;
   - if conflict, spawn a `conflict-fixer-<lane>` worker in the integration worktree only for that conflict;
   - update ledger.
4. Do not proceed to Wave 2 until Wave 1 integrated tests pass.

## Wave 2 — seed and Wizard recursive path

Only after Wave 1 integration is green, spawn these.

### Lane 5: `seed-integrity`

Goal: host-anchor `nextRunSeed` and replay ledger.

Files likely:
- `core/orchestration/src/proof/lev-wizard-ratchet.ts`
- `core/orchestration/src/proof/lev-wizard-ratchet.test.ts`
- `core/orchestration/src/handlers/lev-wizard-ratchet.ts`
- `core/orchestration/src/handlers/lev-wizard-ratchet.test.ts`

Requirements:
- Add forged previousResult/nextRunSeed self-consistency rejection.
- Add replay bypass via `LEV_PROJECT_ROOT`/`LEV_ROOT` root-redirection rejection.
- HMAC/sign seed facts or bind seed to host-issued previous-run receipt store.
- Legitimate earned seed can be consumed once and replay blocks.

### Lane 6: `wizard-host-consumed`

Goal: make Wizard steering enter a real host-verifiable path rather than fixture-only custom-gate failure.

Files likely:
- `core/orchestration/src/proof/lev-wizard-ratchet.ts`
- `core/orchestration/src/proof/lev-wizard-ratchet.test.ts`
- `core/orchestration/src/proof/claim-gate-steering-run.ts`
- `core/orchestration/src/proof/claim-gate-steering-run.test.ts`
- `core/orchestration/src/handlers/lev-wizard-ratchet.ts`

Design choice:
- Option A: register host-owned internal verifiers for `wizard_sim_engine_probe`, `wizard_council_wave_loop`, `wizard_graph_patch_proposal_review`.
- Option B: make Wizard steering emit the existing 14 standard ClaimGate internal gates backed by host-verifiable evidence.

Acceptance:
```bash
./core/poly/bin/lev orchestration lev-wizard-ratchet demo --real-engines --real-source-evidence --real-skills --json --out /tmp/lev-wizard-real-path-wave1.json
./core/poly/bin/lev orchestration lev-wizard-ratchet seed /tmp/lev-wizard-real-path-wave1.json --json --out /tmp/lev-wizard-real-path-wave2.json
```

Accept either real `host_consumed + nextRunSeed + wave2` or a new precise blocker that is not the old unregistered `wizard_*` gate seam.

## Wave 3 — graph-sink / positive boundary and final verifier

### Lane 7: `graph-sink-upstream-signing`

Goal: address graph-sink finding: upstream result/admission receipts are keyless sha256; host-sign upstream receipts before graph mutation authority.

Files likely:
- `core/orchestration/src/proof/claim-gate-loop.ts`
- `core/orchestration/src/proof/claim-gate-loop.test.ts`
- `core/orchestration/src/handlers/claim-gate-loop.ts`
- graph patch execution tests as needed

Acceptance:
- Producer-forged upstream result/admission receipts cannot lead to `graphMutationApplied=true`.
- Host-signed upstream path still allows legitimate graph mutation.

### Lane 8: `positive-boundary-ceiling`

Goal: lift or explicitly preserve the `host_consumed` ceiling.

Problem statement:
`host_consumed` currently certifies projection hygiene / adapter_partial, not sim re-execution. `rerun_commands` path fix helps but may not equal full sim rerun.

Task:
- Decide what extra host-executed proof is required for `host_consumed` to mean ratchet-relevant execution.
- Add tests/labels so projection hygiene cannot be misreported as sim execution.
- If full sim re-exec is out of scope, make the ceiling explicit in CLI/result fields.

## Final verification in integration worktree

Run in `/tmp/lev-mass-wt` after integrated patches:

```bash
pnpm --filter @lev-os/orchestration test -- src/proof/claim-gate-redteam-targets.test.ts src/proof/claim-gate-loop.test.ts src/handlers/claim-gate-loop.test.ts src/handlers/claimgate-steering.test.ts src/proof/claim-gate-steering-run.test.ts src/proof/lev-wizard-ratchet.test.ts src/handlers/lev-wizard-ratchet.test.ts
pnpm --filter @lev-os/graph test -- src/__tests__/claim-gate-redteam-targets.test.ts
pnpm --filter @lev-os/orchestration typecheck
pnpm --filter @lev-os/graph typecheck
pnpm --filter @lev-os/orchestration build
git diff --check
```

Then live CLI smoke:

```bash
./core/poly/bin/lev orchestration claimgate-steering --help
./core/poly/bin/lev orchestration lev-wizard-ratchet --help
./core/poly/bin/lev orchestration lev-wizard-ratchet demo --real-source-evidence --json --out /tmp/lev-wizard-post-mass-demo.json
```

## Output required from main Claude

Final answer must include:

```text
Worktree used:
Parent ledger path:
Lane worktrees created:
Workers spawned:
Per-lane receipts:
Patches integrated:
Tests run with exit codes:
Live CLI result:
Remaining blockers:
Patch split / files changed:
No stage/commit/push/rebase/clean/reset confirmation:
```

Do not say done/canonical/landed.
```
