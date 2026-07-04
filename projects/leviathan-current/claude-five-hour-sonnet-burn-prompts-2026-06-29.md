---
title: Claude five-hour Sonnet burn prompts for Lev / CR / Desktop CR
created: 2026-06-29
type: prompt-pack
status: working-controller-packet
claim_ceiling: Prompt/control packet only; not execution evidence, not admission, not proof that Claude ran the work.
---

# Claude five-hour Sonnet burn prompts — 2026-06-29

## Current verified anchors from Hermes

- Lev root: `/Users/joshuaeisenhart/GitHub/lev`, branch `claimgate-steering-bridge-lock`, HEAD `f9185635334f`, dirty count `219`, status shape `M=137 D=4 ??=78`.
- Lev ClaimGate has moved: `core/orchestration/src/handlers/claimgate-steering.ts` now returns `CLAIMGATE_STEERING_WITNESS_FAILED` on witnessed consume error instead of falling back to plain consume; `core/orchestration/package.json` now has `prebuild: node scripts/clean-build.mjs`; `claim-gate-steering-run.ts` now includes `executeHostProofObligations(...)`. These are observed source changes, not acceptance until tests/red-team rerun.
- Active CR root: `/Users/joshuaeisenhart/Codex-Ratchet`, branch `session/r0-three-engine-probes`, HEAD `82fe601855c9`, dirty count `37`, mostly scratch/formal scout result JSONs plus the Weyl terrain source-alignment audit.
- Desktop CR root: `/Users/joshuaeisenhart/Desktop/Codex Ratchet`, branch `main...origin/main [behind 1]`, HEAD `f68da8e74c52`, dirty count `1006`, status shape `M=56 D=8 ??=942`. Desktop is receipt/quarantine only.
- Do not conflate the three roots.
- Do not drift to old standalone `~/wiki/wizard`. For Lev work, the relevant apparatus is Lev's `lev-wizard-ratchet` + ClaimGate.

## Emergency drift-stop prompt

Paste this into any Claude thread that starts reading old Wizard/Hermes packets or asking what to do instead of working.

```text
STOP. You are drifting.

The object is not the old standalone `~/wiki/wizard` apparatus, not Hermes Wizard v4.3, and not your own Claude Workflow fanout. The object is the updated wizard-inspired system being built into Lev:

- `/Users/joshuaeisenhart/GitHub/lev`
- `lev orchestration lev-wizard-ratchet`
- ClaimGate steering gates
- model-lane/council-wave ratchet artifacts in Lev source
- source/dist runtime truth
- receipts from real Lev commands or direct source/test audits

Do not ask me what to run. The next work is already clear: use Lev's own apparatus and current ClaimGate code as the target, and produce receipts. Do not read `~/wiki/wizard` unless explicitly asked for historical comparison.

Immediate action:
1. Write a short `DRIFT_STOP_RECEIPT` in your answer: wrong object read, corrected object, roots, and non-goals.
2. Continue into the assigned task packet below without another clarification question.
3. If you cannot run Lev, perform a source/test audit and state exactly which command was blocked.
4. Do not call anything done/canonical/admitted without exact file/test/command evidence.
```

## Universal parent-controller rule for all Claude threads

Every parent thread should paste this at the top before spawning Sonnet workers.

```text
Run mode: five-hour Sonnet-high burn, but not flat drift.

Use Sonnet high workers aggressively on independent packets. Do not spawn many workers on the same uncertainty. Do not run old Wizard/Hermes packets. Do not stop after reading.

Control law:
- Parent keeps a worker ledger.
- Spawn up to 6 Sonnet-high workers at once for independent read-only or scratch-only packets.
- Each worker gets one bounded packet, one receipt path, and a timeout.
- When a worker returns, verify its receipt path exists, mark `ok/error/blocked`, and immediately launch the next queued packet until the time budget is exhausted or the queue is empty.
- Git/index/staging/commits/pushes are forbidden.
- Shared repo files are not edited by workers. Receipts go under `/tmp/claude-burn-2026-06-29/<thread>/<worker-id>.md` unless a task explicitly says scratch copy.
- Started workers are not progress. Completed receipts and command outputs are progress.
- If a packet is blocked, write the blocker and move to the next packet.
- Final parent output must include: ledger table, receipts produced, verified commands, unresolved gaps, top 5 next actions.
```

---

# Thread 1 — Lev ClaimGate / `lev-wizard-ratchet` hardening audit

Use in the Lev/Codex/Claude thread rooted at `/Users/joshuaeisenhart/GitHub/lev`.

## Parent prompt

```text
Repository: `/Users/joshuaeisenhart/GitHub/lev`.

Mission: Use a Sonnet-high worker burn to audit the current Lev ClaimGate + `lev-wizard-ratchet` hardening work after the latest Codex changes. This is not Codex Ratchet integration and not old Wizard work. The target apparatus is Lev itself.

Current Hermes-observed state:
- branch `claimgate-steering-bridge-lock`, HEAD `f9185635334f`, dirty count around 219.
- `claimgate-steering.ts` appears to fail closed now on witnessed consume error.
- `package.json` has `prebuild: node scripts/clean-build.mjs`.
- `claim-gate-steering-run.ts` now includes `executeHostProofObligations(...)` and host witness MAC code.
- These are source observations only. You must verify with commands and red-team behavior.

Do not broaden. Do not stage/commit/push. Do not rebase. Do not read old `~/wiki/wizard`. Use Lev source and Lev commands.

Spawn up to 6 Sonnet-high child workers at a time, then roll forward until all packets below have receipts. Each child writes `/tmp/claude-burn-2026-06-29/lev/<worker-id>.md`.

Worker queue:
1. `handler-fail-closed-audit` — inspect `core/orchestration/src/handlers/claimgate-steering.ts`; prove whether single consume and batch consume are fail-closed; cite lines; propose missing tests.
2. `host-proof-execution-audit` — inspect `core/orchestration/src/proof/claim-gate-steering-run.ts`; decide whether `executeHostProofObligations` prevents host-signing a merely producer-consistent projection; cite exact accepted/rejected obligations.
3. `clean-build-dist-audit` — inspect `core/orchestration/package.json`, `scripts/clean-build.mjs`, tsconfig, and fresh dist status; determine whether build now cleans before tsc and whether dist is source-current after build.
4. `redteam-test-map` — map A3/A3b/A3c/A6/A6b/A15/A19/A22/A22b/A23/A24 tests to files and line ranges; list gaps.
5. `cli-e2e-forge-plan` — produce exact commands to create/consume forged steering runs through the CLI after build; include expected `host_blocked` vs `host_consumed` and receipt paths.
6. `lev-wizard-ratchet-claim-gate-link` — inspect `core/orchestration/src/proof/lev-wizard-ratchet.ts`, handler, and tests; map how `lev-wizard-ratchet` produces/consumes ClaimGate evidence and where model-lane/council receipts enter.
7. `dirty-patch-isolation` — list narrow files belonging to ClaimGate hardening vs unrelated dirty files; recommend landable patch slices without staging.
8. `graph-side-trust-audit` — inspect `core/graph/src/__tests__/claim-gate-redteam-targets.test.ts` and graph trust code; classify graph forged-event/trusted-ref protections.
9. `minimal-command-runner` — run only safe verification commands if no writer is active: `pnpm --filter @lev-os/orchestration typecheck`, targeted tests, and build. If writer is active or commands would conflict, produce exact deferred command plan.
10. `apparatus-route-truth` — inspect actual `lev orchestration lev-wizard-ratchet --help`, `self-audit`, `demo`, `seed` surfaces; report what can be run now and what is blocked by ClaimGate state.

Parent synthesis after workers:
- Verify a sample of receipts by reading files/lines or running commands.
- Produce a ranked fix/verify list:
  1. must fix before red-team rerun;
  2. must test before claiming closed;
  3. safe to defer;
  4. unrelated dirty state.
- If tests pass, still say `branch-local, dirty, not landed`.
```

## Child receipt format

```text
# <worker-id>
root:
files read:
commands run:
observed facts:
claim ceiling:
pass/fail/open:
exact blockers:
recommended next action:
```

---

# Thread 2 — Active Codex Ratchet readiness matrix for later Lev admission

Use in the active CR thread rooted at `/Users/joshuaeisenhart/Codex-Ratchet`.

## Parent prompt

```text
Repository: `/Users/joshuaeisenhart/Codex-Ratchet`.

Mission: Build a controller-readable readiness matrix for using Codex Ratchet outputs as later workloads for upgraded Lev. Do not promote any CR sim. Do not mutate repo source. Do not run old Wizard. This is prework for Lev admission after ClaimGate stabilizes.

Current Hermes-observed state:
- branch `session/r0-three-engine-probes`, HEAD `82fe601855c9`, dirty count `37`.
- Dirty JSONs are mostly `system_v5/julia_carrier/*_results.json`, two `system_v5/legos/results/*`, three formal-scout result JSONs, and `system_v5/ops/formal_scouts/audits/`.
- Most dirty JSONs are `scratch_diagnostic` or `formal_scout` with `promotion_allowed=false`.
- Weyl terrain source-alignment audit exists here, not in Desktop CR, and has high-severity source-native operating-space findings.

Spawn up to 8 Sonnet-high read-only workers at a time. Each writes `/tmp/claude-burn-2026-06-29/cr-active/<worker-id>.md`. Keep launching next workers until the queue is done or time ends.

Worker queue:
1. `dirty-result-matrix` — parse all 34 dirty JSON result/audit files and produce CSV/Markdown matrix: path, classification, all_pass, promotion_allowed, formal_admission_allowed, blockers, source path, candidate for Lev pilot yes/no.
2. `g2-su3-gap-audit` — audit `foundation_foundation_r5_g2_su3_reduction_jax.py` and result; determine exact blind-dimension and sharp-control gaps; do not promote.
3. `weyl-terrain-incident-triage` — audit `weyl_terrain_source_alignment_audit.json`; summarize categories of source-native operating-space missingness and choose repair lanes.
4. `julia-carrier-cluster-audit` — group dirty `system_v5/julia_carrier/*` results by object family; identify which are scratch feedstock vs candidate pilot inputs.
5. `formal-scout-blocker-audit` — inspect the three dirty formal-scout result JSONs; extract blockers like missing dependency paths and classify fixability.
6. `lego-result-audit` — audit the two dirty `system_v5/legos/results/*`; decide whether they are valid lego evidence or just feedstock.
7. `pilot-selection-top10` — choose top 10 candidate workloads for later Lev admission, but only from artifacts with clear source/result paths and explicit claim ceilings.
8. `negative-control-inventory` — for each top candidate, identify positive, negative, boundary, and demotion conditions required before Lev pilot.
9. `lev-input-sketches` — draft 3 possible `lev-wizard-ratchet` input sketches for future use. Mark them sketches only; do not claim runnable unless command-checked.
10. `matrix-consolidator` — merge receipts into one readiness matrix and next-wave plan.

Rules:
- No repo edits except optional receipt files under `/tmp`.
- No `canonical`, `admitted`, or `ready` labels. Use `candidate`, `formal_scout`, `scratch_diagnostic`, `needs_rerun`, `blocked`.
- If a worker finishes early, launch the next queued worker. Do not stop after reading.

Parent synthesis:
- Produce `CR_READY_FOR_LEV_MATRIX` with top 10 candidates, top 10 blockers, and top 5 next waves.
```

---

# Thread 3 — Desktop CR dirty-tree quarantine and import/discard map

Use in the Desktop Claude thread rooted at `/Users/joshuaeisenhart/Desktop/Codex Ratchet`.

## Parent prompt

```text
Repository: `/Users/joshuaeisenhart/Desktop/Codex Ratchet`.

Mission: Quarantine and classify the dirty Desktop CR tree so it stops drifting. This is not the active CR authority root. This is not a place to expand work. It is a receipt/triage/import-discard surface.

Current Hermes-observed state:
- branch `main...origin/main [behind 1]`, HEAD `f68da8e74c52`.
- dirty count `1006`, status shape `M=56 D=8 ??=942`.
- massive generated evidence/index diff under `system_v5/evidence` and `system_v5/legos/results`.
- `.claude/worktrees/*` exist; do not assume worktree freshness means main tree changes are admitted.
- The Weyl terrain audit file cited earlier was not found in Desktop path; it exists in `/Users/joshuaeisenhart/Codex-Ratchet`.

Do not read old `~/wiki/wizard`. Do not run new sim campaigns. Do not stage/commit/push/rebase/clean/reset. Do not mutate source. Receipts only under `/tmp/claude-burn-2026-06-29/cr-desktop/<worker-id>.md`.

Spawn up to 8 Sonnet-high read-only workers at a time. Continue launching until the queue is done or time ends.

Worker queue:
1. `dirty-tree-area-map` — summarize all 1006 dirty entries by area, extension, likely generated/source/doc/test/visualizer categories.
2. `generated-index-audit` — inspect `system_v5/evidence/*index*.json` diffs; decide if generated-only, stale, or candidate evidence; no promotion.
3. `formal-scout-source-audit` — sample/classify untracked `system_v5/ops/formal_scouts/*.py` by family; identify likely duplicates vs unique candidate material.
4. `tests-validator-audit` — inspect dirty `system_v5/tests/*` and validator scripts; list potentially useful tests to port to active CR or Lev.
5. `visualizer-and-test-jax-audit` — classify `visualizer/*` and `test_jax_*.py` untracked files as discard/quarantine/import-candidate.
6. `claude-worktree-audit` — for each `.claude/worktrees/*`, capture branch, HEAD, status, and intentional deltas if any.
7. `deleted-files-risk-audit` — list the 8 deleted tracked files and assess whether they are dangerous accidental deletions.
8. `import-candidate-top20` — choose at most 20 files worth considering for active CR import, with reasons and blockers.
9. `discard-quarantine-top50` — choose generated/copied/stale files safe to quarantine/ignore later, without deleting now.
10. `desktop-receipt-consolidator` — merge all receipts into a single import/discard/hold manifest.

Parent synthesis:
- Output three lists only: `import candidates`, `hold/quarantine`, `discard-later candidates`.
- Include exact paths and support level.
- Do not claim any Desktop artifact is admitted or canonical.
```

---

# Optional fourth thread — pure Claude mass-burn coordinator

Use only if a separate Claude thread is available to coordinate, not edit.

```text
You are the five-hour Sonnet burn coordinator. Do not do repo work directly. Track the three parent threads:
1. Lev ClaimGate audit: `/Users/joshuaeisenhart/GitHub/lev`.
2. Active CR readiness matrix: `/Users/joshuaeisenhart/Codex-Ratchet`.
3. Desktop CR quarantine: `/Users/joshuaeisenhart/Desktop/Codex Ratchet`.

Every 20 minutes, ask each parent for its ledger and receipt paths. Produce a consolidated board:
- queued
- running
- ok
- blocked
- rerouted
- stale/drifted
- receipts produced
- next worker to launch

If any thread drifts to old Wizard/Hermes packets, immediately send the emergency drift-stop prompt.

Do not synthesize scientific claims. Your job is throughput and route truth.
```
