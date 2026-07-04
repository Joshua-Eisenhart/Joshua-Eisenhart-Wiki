---
title: Three-thread deeper audit send packet
created: 2026-06-30
type: sendable-audit
status: current-controller-packet
claim_ceiling: Read-only Hermes audit of visible repos and receipt files; sendable steering packet only, not admission, not landed proof.
---

# Three-thread deeper audit send packet — 2026-06-30

Paste this to the relevant Claude/Codex threads as a grounded controller audit.

## Global verdict

The three lanes are not equivalent.

1. **Lev lane did real continuous work** and produced receipts, tests, builds, forge probes, and source mutations. It now needs consolidation and gap-closing, not more spawning.
2. **Active Codex Ratchet lane did not run**: no `/tmp/claude-burn-2026-06-29/cr-active` receipt dir and no Claude process with cwd `/Users/joshuaeisenhart/Codex-Ratchet` was observed.
3. **Desktop CR lane partially ran** and produced useful quarantine receipts, but one receipt repeats a root-confusion error and the final consolidator is missing.

Support level: observed by Hermes from git state, process cwd, receipt dirs, and selected receipt reads on 2026-06-30. Counts may move while Codex/Claude are active.

---

## Thread 1 — Lev ClaimGate / `lev-wizard-ratchet`

### Observed state

```text
root: /Users/joshuaeisenhart/GitHub/lev
branch: claimgate-steering-bridge-lock
HEAD: f9185635334f
porcelain status: M=139 D=4 ??=80 total=223
receipt dir: /tmp/claude-burn-2026-06-29/lev
receipt count observed: 62 files
```

Tracked deletes currently visible in Lev:

```text
D apps/nextjs/src/app/_components/posts.tsx
D core/event-bus/analytics/lev-learn/.venv/.gitignore
D core/harness/tests/system-prompt-wiring.test.ts
D core/poly/bridge/orchestrator/.gitignore
```

Do not stage or clean these until the patch slices are separated.

### Receipts inspected

```text
/tmp/claude-burn-2026-06-29/lev/minimal-command-runner.md
/tmp/claude-burn-2026-06-29/lev/host-proof-execution-audit.md
/tmp/claude-burn-2026-06-29/lev/handler-fail-closed-audit.md
/tmp/claude-burn-2026-06-29/lev/clean-build-dist-audit.md
/tmp/claude-burn-2026-06-29/lev/lev-wizard-ratchet-claim-gate-link.md
/tmp/claude-burn-2026-06-29/lev/graph-side-trust-audit.md
/tmp/claude-burn-2026-06-29/lev/redteam-test-map.md
/tmp/claude-burn-2026-06-29/lev/cli-e2e-forge-plan.md
/tmp/claude-burn-2026-06-29/lev/forgery-A22-trusted-ref.md
/tmp/claude-burn-2026-06-29/lev/forgery-A3-digest.md
/tmp/claude-burn-2026-06-29/lev/demo-full-result.json
```

### What is genuinely better

Receipts report:

```text
pnpm --filter @lev-os/orchestration typecheck: exit 0
pnpm --filter @lev-os/orchestration test: 51 files, 760 tests passed
pnpm --filter @lev-os/orchestration build: exit 0
7 targeted orchestration files: 129 tests passed
```

`clean-build-dist-audit.md` reports:

- `core/orchestration/package.json` has `prebuild: node scripts/clean-build.mjs`.
- `clean-build.mjs` removes `dist`, `tsconfig.tsbuildinfo`, and `tsconfig.build.tsbuildinfo` before `tsc`.
- fresh dist after build contains `hostWitnessMac` and matches source MAC lines.

`handler-fail-closed-audit.md` reports:

- single `claimgate-steering consume` no longer falls back to plain consume on witness error;
- witness error returns `CLAIMGATE_STEERING_WITNESS_FAILED`;
- empty batch root fails closed.

`host-proof-execution-audit.md` reports:

- host witness now includes `executeHostProofObligations(...)`;
- non-internal obligations fail with explicit “No host-owned proof obligation runner...” reason;
- 14 internal gates are host-evaluated and do not trust `obligation.actualResult`;
- `host_consumed` now requires host MAC witness plus host proof execution verdict pass.

### Important caveat: the happy path is now real, so label it correctly

`cli-e2e-forge-plan.md` actually produced a full 14-gate run and consumed it:

```text
status: host_consumed
projectedVerdict: pass
recomputedVerdict: pass
liveLevConsumed: true
receipt.id: rcpt-df475157009894b0
```

That is not automatically a vulnerability. The worker says this is the intended happy path: a `produce` run with all 14 internal gates passes because the host re-evaluates the gates and signs the witness.

The red-team question is now narrower:

```text
Are any of the 14 internal gates tautological, host-hardcoded, or ledger-forgeable?
```

Do not keep calling the whole gate “forgeable” if the remaining problem is specific gate content.

### Remaining Lev blockers / risks

#### 1. A15 falsifier hardcode remains open

`lev-wizard-ratchet-claim-gate-link.md` reports two unconditional `closed` sites:

```text
core/orchestration/src/proof/lev-wizard-ratchet.ts line ~1543
falsifierStatus: 'closed'
openFalsifierCount: 0

core/orchestration/src/handlers/lev-wizard-ratchet.ts line ~325
falsifierStatus: 'closed'
openFalsifierCount: 0
```

This makes the host/evidence falsifier cross-check tautological in practice. The route can only compare `closed` to `closed`; it cannot catch a producer lying about open falsifiers. This is now higher priority than older generic “self-issued witness” language.

Required fix/test:

```text
Host context must be able to represent open falsifiers.
Add a test where host context says open_falsifier_count > 0 and source evidence says closed.
Expected: ClaimGate withholds / blocks, not host-consumes.
```

#### 2. Batch witness-throw fallthrough is narrowly safe but untested

`handler-fail-closed-audit.md` reports a batch worker catch/fallthrough:

```text
claim-gate-steering-run.ts ~1501–1510
if witness issuance throws, batch falls through to plain consume
```

Current analysis says this still blocks because no witness exists, but it is not directly tested.

Required regression:

```text
batch fallthrough from witness-throw on pass/pass run remains host_blocked, not host_consumed
```

#### 3. Host trust ledger integrity is still open

`graph-side-trust-audit.md` reports A22 direct caller-minted refs are closed, but host trust ledger integrity remains weak:

```text
hostIssuedTrustRefs() trusts any JSONL line with a ref field.
No MAC/signature on claim-gate-host-trust.jsonl.
If attacker can write the host trust ledger path, they can mint trust entries.
```

Required next decision:

```text
Either sign/MAC ledger entries, or explicitly reduce the threat model to filesystem-host-root integrity and test that callers cannot choose the host trust root.
```

#### 4. `lev-wizard-ratchet` still does not earn `nextRunSeed` in fixture mode

`demo-full-result.json` has:

```text
claimCeiling: fixture_or_dry_run_until_live_model_and_engine_receipts
receipt.id: rcpt-e1543176d465f9e2
```

`lev-wizard-ratchet-claim-gate-link.md` says fixture tests assert steering stays `host_blocked`; `nextRunSeed` requires `host_consumed` and is unreachable without live host execution.

This may be correct, but it must be stated as a ceiling, not a failure hidden behind green tests.

#### 5. Red-team map has naming/accounting gaps

`redteam-test-map.md` reports tracked coverage for 20 of 24 named rows and `stillNeedsDedicatedAttackImplementation: []`, but also says `A1`, `A13`, `A17`, and `A21` have no labeled regression anywhere under `src/`.

Required action:

```text
Resolve whether A1/A13/A17/A21 are intentionally out of scope or missing from the harness. Do not claim literal A1–A24 coverage until this is reconciled.
```

#### 6. Scope expanded into harness runner changes

Observed modified files include:

```text
M core/harness/src/providers/codex.ts
M core/harness/src/providers/__tests__/codex.test.ts
M core/harness/src/execution/runner.ts
M core/harness/src/execution/runner.semantic-ops.test.ts
```

These may be useful, but they are a separate patch from ClaimGate hardening.

### Lev required next response

Paste this into the Lev thread:

```text
Deeper audit says: stop expanding and consolidate.

You have real receipts, but the work must now be split into patch slices.

Produce one consolidation receipt with these sections:

1. ClaimGate steering hardening slice
   - files changed
   - exact tests/build run
   - whether single consume is fail-closed
   - whether clean build/dist is source-current
   - red-team results

2. Remaining required tests/fixes before calling ClaimGate closed
   - A15 open-falsifier host context vs source-closed evidence
   - batch witness-throw fallthrough must remain host_blocked
   - host trust ledger integrity/MAC or explicit threat-model test
   - A1/A13/A17/A21 coverage reconciliation

3. `lev-wizard-ratchet` ceiling
   - explain why fixture route remains `fixture_or_dry_run_until_live_model_and_engine_receipts`
   - state whether `nextRunSeed` is blocked by design until live host execution
   - do not call model lanes gate-bearing if they are advisory only

4. Harness runner patch slice
   - list codex provider / runner files changed
   - why they are in scope or separate
   - test results
   - whether this can land separately

5. Dirty/unrelated worktree state
   - include tracked deletes
   - include untracked test files
   - no staging, no commits, no push

Do not spawn more workers. Do not summarize as “closed.” The next deliverable is a patch-slice consolidation receipt.
```

---

## Thread 2 — Active Codex Ratchet readiness lane

### Observed state

```text
root: /Users/joshuaeisenhart/Codex-Ratchet
branch: session/r0-three-engine-probes
HEAD: 82fe601855c9
porcelain status: M=34 D=0 ??=3 total=37
receipt dir: /tmp/claude-burn-2026-06-29/cr-active
receipt dir exists: false
Claude process cwd in this root: none observed
```

### Verdict

This lane did not run. No worker receipts, no matrix, no consolidator.

The dirty repo still contains the known CR artifacts:

- many `system_v5/julia_carrier/*_results.json`;
- two `system_v5/legos/results/*`;
- three formal-scout result JSONs;
- untracked `system_v5/ops/formal_scouts/audits/`.

Hermes previously parsed the dirty JSONs and saw mostly `scratch_diagnostic` / `formal_scout` / `promotion_allowed=false`. But the assigned Claude readiness matrix is still absent.

### Active CR required next response

Paste this into the Active CR thread:

```text
Audit says this lane did not run. There is no `/tmp/claude-burn-2026-06-29/cr-active` receipt dir and no observed Claude process in `/Users/joshuaeisenhart/Codex-Ratchet`.

Start with the first worker only; do not summarize and stop.

Repository: `/Users/joshuaeisenhart/Codex-Ratchet`.

Create the directory:
`/tmp/claude-burn-2026-06-29/cr-active/`

Write the first receipt:
`/tmp/claude-burn-2026-06-29/cr-active/dirty-result-matrix.md`

Task:
Parse all dirty JSON result/audit files from `git status --short` and produce a table:

- path
- classification
- all_pass
- promotion_allowed
- formal_admission_allowed
- blockers
- source path if present
- claim ceiling
- candidate for later Lev pilot: yes/no
- reason

Rules:
- no repo edits
- no canonical/admitted/ready labels
- use only: scratch_diagnostic, formal_scout, lego, candidate, needs_rerun, blocked, unknown
- after writing this first receipt, immediately launch `g2-su3-gap-audit`

Do not ask what to do. The assigned work is the matrix.
```

---

## Thread 3 — Desktop Codex Ratchet quarantine lane

### Observed state

```text
root: /Users/joshuaeisenhart/Desktop/Codex Ratchet
branch: main...origin/main [behind 1]
HEAD: f68da8e74c52
porcelain status: M=64 D=0 ??=942 total=1006
receipt dir: /tmp/claude-burn-2026-06-29/cr-desktop
receipt count observed: 10
```

Correction: an earlier quick status-shape script reported `D=8`, but exact porcelain status shows `D=0`. The `deleted-files-risk-audit.md` receipt is right: no tracked working-tree deletes were found. The huge deletion count against origin is a behind-origin diff illusion.

### Useful receipts produced

```text
DRIFT_STOP_RECEIPT.md
dirty-tree-area-map.md
generated-index-audit.md
formal-scout-source-audit.md
tests-validator-audit.md
visualizer-and-test-jax-audit.md
claude-worktree-audit.md
deleted-files-risk-audit.md
discard-quarantine-top50.md
import-candidate-top20.md
git-status-raw.txt
```

### Useful findings

`dirty-tree-area-map.md` reports:

```text
1006 dirty entries
942 untracked
64 modified
663 .py
240 .json
86 .md
707 entries under system_v5/ops/formal_scouts
```

`generated-index-audit.md` reports:

- three evidence indexes are generated outputs, not admission;
- `formal_scout_readiness_index.json` grew from 404 to 830 results and now shows many validator failures / missing READMEs;
- `sim_inventory_index.json` changed schema from broad historical linked count to tighter evidence-linked count;
- two lego result JSONs changed only elapsed timing fields;
- no promotion claims.

`deleted-files-risk-audit.md` reports:

- no dangerous accidental deletions;
- local branch is behind origin by one squash-sync commit;
- files absent relative to origin are not deleted locally; they are not yet pulled.

`discard-quarantine-top50.md` reports:

- root-level untracked JAX results are mostly historical run artifacts;
- some Julia `layers/*.jl` should be held for audit, not discarded blindly;
- no immediate import candidates from that discard scan.

### Important error

`import-candidate-top20.md` begins with a false root statement:

```text
This repo IS the active CR (~/Codex-Ratchet).
```

That is false. The root is:

```text
/Users/joshuaeisenhart/Desktop/Codex Ratchet
```

It is not:

```text
/Users/joshuaeisenhart/Codex-Ratchet
```

So its import-candidate recommendations must be rechecked against active CR before use.

### Missing receipt

The planned final receipt is still missing:

```text
/tmp/claude-burn-2026-06-29/cr-desktop/desktop-receipt-consolidator.md
```

### Desktop required next response

Paste this into the Desktop CR thread:

```text
Deeper audit says the Desktop quarantine lane produced useful receipts but is not closed.

Two required corrections now:

1. Root-confusion correction
Write:
`/tmp/claude-burn-2026-06-29/cr-desktop/root-confusion-correction.md`

It must quote and correct this false line from `import-candidate-top20.md`:
“This repo IS the active CR (~/Codex-Ratchet).”

Correct statement:
“This root is `/Users/joshuaeisenhart/Desktop/Codex Ratchet`. It is not `/Users/joshuaeisenhart/Codex-Ratchet`. Any import recommendation must be rechecked against active CR before use.”

2. Final consolidator
Write:
`/tmp/claude-burn-2026-06-29/cr-desktop/desktop-receipt-consolidator.md`

It must contain exactly three sections:

- import candidates
- hold/quarantine
- discard-later candidates

For each path include:
- exact path
- support level
- reason
- must recheck in active CR? yes/no

Use the receipts already produced. Do not launch new sim campaigns. Do not stage, commit, push, clean, reset, or mutate source.
```

---

## Cross-thread priority order

1. **Active CR must start.** It is the only lane with zero receipts.
2. **Lev must consolidate.** It has the most progress and the most mutation risk.
3. **Desktop CR must correct/consolidate.** It has useful quarantine work but one root-confusion error.

## Do not allow these claims yet

```text
Lev ClaimGate closed.
Lev route is live autonomous council recursion.
CR sims are ready/admitted/canonical.
Desktop CR is active CR.
Desktop import candidates are safe to import without rechecking active CR.
A1-A24 are literally all covered.
Host trust ledger is cryptographically sealed.
```

## Safe current claims

```text
Lev branch has passing local orchestration receipts and a cleaner ClaimGate witness/build path, but remains dirty and not landed.
Active CR has dirty formal-scout/scratch diagnostic evidence but no current Claude readiness matrix.
Desktop CR has useful quarantine receipts, but must correct root confusion and produce a final consolidator.
```
