---
title: Lev mass workflow deep audit and patch orders
created: 2026-06-30
type: sendable-controller-packet
status: current-after-mass-spawn-orders
claim_ceiling: Hermes read/write-current audit of visible roots, receipt dirs, selected source files, and local targeted tests; not landed proof; not canonical.
---

# Lev mass workflow deep audit and patch orders — 2026-06-30

Use this after the mass-spawn orders. It corrects the previous problem: this is not a one-shot audit prompt. It is a mass workflow controller packet for Claude terminals to spawn, build, verify, and keep rolling by receipts.

## Current observed runtime state

Hermes snapshot time: `2026-06-30 01:15 PDT`.

### Live process/cwd truth

Observed live high-signal agent processes:

```text
Codex resume PID 31322/31323 cwd=/Users/joshuaeisenhart/GitHub/lev
Claude Code PID 33870 cwd=/Users/joshuaeisenhart/Desktop/Codex Ratchet
Claude Code PID 83546 cwd=/Users/joshuaeisenhart/Desktop/Codex Ratchet
Claude Code PID 70323 cwd=/Users/joshuaeisenhart/Desktop/Codex Ratchet/.claude/worktrees/naughty-napier-32aee7
Claude Code PID 70336 cwd=/Users/joshuaeisenhart/Desktop/Codex Ratchet/.claude/worktrees/laughing-ramanujan-63d54f
```

Observed caveat: no Claude Code process cwd was observed directly in `/Users/joshuaeisenhart/Codex-Ratchet`; active CR receipts exist anyway, so judge by receipt files, not cwd alone.

### Receipt dirs now exist

```text
/tmp/claude-burn-2026-06-29/lev          md_count=21 all_file_count=94
/tmp/claude-burn-2026-06-29/lev-census   md_count=7  all_file_count=36
/tmp/claude-burn-2026-06-29/cr-active    md_count=10 all_file_count=10
/tmp/claude-burn-2026-06-29/cr-desktop   md_count=13 all_file_count=14
```

Mass work did happen by receipt output. What is not proven from process state alone is how many Claude child workers were spawned inside each terminal. For that, require parent ledgers in the next wave.

---

## Root states

### Lev

```text
root: /Users/joshuaeisenhart/GitHub/lev
branch: claimgate-steering-bridge-lock
HEAD: f9185635334f
status shape: M=139 D=4 ??=80 total=223
```

Visible tracked deletes:

```text
D apps/nextjs/src/app/_components/posts.tsx
D core/event-bus/analytics/lev-learn/.venv/.gitignore
D core/harness/tests/system-prompt-wiring.test.ts
D core/poly/bridge/orchestrator/.gitignore
```

### Active Codex Ratchet

```text
root: /Users/joshuaeisenhart/Codex-Ratchet
branch: session/r0-three-engine-probes
HEAD: 82fe601855c9
status shape: M=34 D=0 ??=3 total=37
```

### Desktop Codex Ratchet

```text
root: /Users/joshuaeisenhart/Desktop/Codex Ratchet
branch: main...origin/main [behind 1]
HEAD: f68da8e74c52
status shape: M=64 D=0 ??=942 total=1006
```

Corrected fact: Desktop has `D=0` in current porcelain status. Prior `D=8` was a bad status-shape artifact / diff-vs-origin confusion.

---

## Hermes verification run after the mass-spawn output

Hermes locally ran the current Lev targeted tests against the visible tree.

```text
pnpm --filter @lev-os/orchestration test -- \
  src/handlers/claim-gate-loop.test.ts \
  src/proof/claim-gate-redteam-targets.test.ts \
  src/proof/lev-wizard-ratchet.test.ts \
  src/handlers/lev-wizard-ratchet.test.ts \
  src/handlers/claimgate-steering.test.ts

Result: exit 0
Test Files: 51 passed
Tests: 766 passed
```

```text
pnpm --filter @lev-os/graph test -- src/__tests__/claim-gate-redteam-targets.test.ts

Result: exit 0
7 pass, 0 fail
```

```text
pnpm --filter @lev-os/orchestration typecheck
Result: exit 0

pnpm --filter @lev-os/graph typecheck
Result: exit 0
```

```text
git diff --check -- selected ClaimGate/Wizard/graph/harness touched files
Result: exit 0
```

Support level: current visible tree, local rerun. Not CI. Not landed. Dirty tree may continue moving while Codex is active.

---

## Lev: what improved

From `codex-consolidation-receipt.md` and current source/tests:

1. ClaimGate steering has stronger host witness machinery:
   - process-local HMAC witness;
   - host proof execution evidence;
   - pass/pass projection without host proof evidence blocks;
   - batch witness-throw fallthrough regression reportedly added.

2. Orchestration clean build path exists:
   - `prebuild: node scripts/clean-build.mjs`;
   - clean dist before `tsc`.

3. Host trust ledger raw JSON lines are no longer accepted:
   - current `handlers/claim-gate-loop.ts` uses `ClaimGateHostTrustedEvidenceRef` with `payloadHash` and HMAC.

4. A15 hardcoded Wizard falsifier status was partly fixed:
   - handler accepts `--host-falsifier-status` and `--host-open-falsifier-count`;
   - proof path has `hostFalsifierState` plumbing;
   - tests around open-falsifier withholding now pass.

5. A1 graph red-team coverage now exists and passes:
   - graph test rejects self-attested `sourceRefBoundToCommand` when command args do not execute that source.

6. Harness runner patch slice exists:
   - Codex JSONL start-only events no longer count as success;
   - unsupported Codex models surface errors;
   - direct subprocess Codex route by default;
   - `--verifier` gates single-run receipts.

---

## Lev: open blockers that still matter

Do not call the full Lev path working until these are closed or deliberately scoped out.

### Blocker 1 — A22c same-process host-trust issuance remains forgeable by root redirection

Current source has HMAC on host trust ledger entries. That closes raw ledger JSON forgery. It does **not** close same-process issue + caller-controlled root.

Current source facts:

```text
handlers/claim-gate-loop.ts:196-201
claimGateProjectRoot() = LEV_CLAIMGATE_HOST_TRUST_ROOT ?? LEV_PROJECT_ROOT ?? LEV_ROOT ?? cwd()
hostTrustLedgerPath() uses that root

handlers/claim-gate-loop.ts:204
export function issueClaimGateHostTrustedEvidenceRefs(refs, root = claimGateProjectRoot())
```

`lev-census/host-trust-ledger-a22c.md` reports a live probe:

```text
Scenario A: no ledger -> CALLER_SUPPLIED_HOST_TRUST_DISABLED
Scenario B: same-process issue into attacker LEV_CLAIMGATE_HOST_TRUST_ROOT -> acceptedClaimIds ["forged-claim-live-a22c"]
Scenario C: same-process issue via LEV_PROJECT_ROOT fallback -> acceptedClaimIds ["forged-claim-live-a22c"]
```

Current classification:

```text
cross-process raw ledger forgery: blocked
same-process public issuer + caller-settable root: open / producer-forgeable
```

Required fix direction:

- remove public issuer authority from untrusted callers;
- make issuance require a module-private issuer token or a host-only handler path;
- pin host trust root to a canonical host root captured before user/projection/env influence;
- do not let `LEV_CLAIMGATE_HOST_TRUST_ROOT`, `LEV_PROJECT_ROOT`, or `LEV_ROOT` be proof authority unless separately host-attested;
- add regression: same-process imported caller cannot call the issuer or redirect the root and then pass `--host-trusted-evidence-ref`.

### Blocker 2 — `rerun_commands` accepts any existing host file

Current source:

```text
claim-gate-steering-run.ts:711-746
rerun_commands reads boundary.target_files and calls hostCheckoutPathExists()

hostCheckoutPathExists(path, runDir):
  if (existsSync(path)) return true
  then ancestor-walk existsSync(join(cursor, path))
```

`lev-census/rerun-commands-existsSync.md` live probe:

```text
boundary.target_files = ["/etc/hosts"]
ok: true
status: host_consumed
findings: 0
```

Current classification:

```text
producer-forgeable path-presence gate
```

Required fix direction:

- resolve target path under a canonical Lev checkout root;
- reject absolute paths outside that root;
- reject ancestor-walk paths outside root;
- ideally require target file hashes to match `sourceFileHashes` / boundary hash entries.

### Blocker 3 — source-forbidden field scan is exact-key only

`lev-census/source-forbidden-fieldscan-a3-variants.md` reports:

```text
20 variants tested
14 caught
6 bypassed:
  LevEngineSubstrateDigest
  LEVENGINESUBSTRATEDIGEST
  levEngineSubstrateDigеst  # Cyrillic e
  " levEngineSubstrateDigest"
  "levEngineSubstrateDigest "
  "lev​EngineSubstrateDigest" # zero-width space
```

This does not prove those variant keys are currently read as real host authority. It does prove the forbidden-field scanner is exact-string only, so it can miss smuggled authority-shaped fields.

Required fix direction:

- canonicalise JSON keys before forbidden-set checks;
- reject suspicious unicode/zero-width/trim/case variants;
- apply same normalisation to `SOURCE_FORBIDDEN_PROOF_AUTHORITY_FIELDS` and `EXPLICIT_AUTHORITY_PROJECTION_FIELDS`;
- add variants as tests.

### Blocker 4 — evidence-manifest comparison remains producer-vs-producer in the Wizard route

`lev-census/evidence-manifest-hashes.md` reports the `evidence_manifest` gate can accept a claim where the producer wrote both:

- the `file:` evidence blob and its `sha256:` ref;
- the `sourceBoundEvidenceContext` values that the gate compares against.

Current code shape:

```text
sourceBoundEvidenceContextForInput(input) derives contextReceiptRefs, contextContentHashes, threeEngineEnvelopeHash, engineSubstrateDigestHash from producer-authored LevWizardRatchetRunInput.
runClaimGateCouncilWaveLoop options accept sourceBoundEvidenceContext as a plain field.
```

Current classification:

```text
self-consistency check unless the context is host-issued / host-attested
```

Required fix direction:

- distinguish public `sourceBoundEvidenceContext` from host-attested context;
- make the trusted context path token-gated or HMAC-signed;
- host must recompute from host-owned receipt store or previous host-issued run records, not just from producer input.

### Blocker 5 — Wizard seed integrity / replay remains producer-document anchored

Current source:

```text
buildAcceptedSurvivorNextRunSeed() hashes seedFacts from previousResult fields.
createSeededLevWizardRatchetInput() validates intra-document consistency against previousResult.
```

`lev-census/seed-integrity-a16-a18.md` reports:

- A16: nextRunSeed content hash has no host secret / HMAC / nonce;
- A18: seed consumption ledger path uses env-root resolution and can be redirected.

Current classification:

```text
producer-forgeable if the producer authors the whole previousResult document
```

Required fix direction:

- HMAC/sign nextRunSeed with a host-only secret;
- verify seed against a host-issued previous-run ledger/receipt store;
- pin replay ledger root to canonical host root;
- add tests for forged previousResult and env-root replay bypass.

### Blocker 6 — Wizard route still does not reach real `host_consumed` / `nextRunSeed`

Earlier `lev-wizard-ratchet-falsifier-refutation-worker.md` proved the old path blocked because Wizard obligations were not registered internal ClaimGate gates:

```text
wizard_sim_engine_probe
wizard_council_wave_loop
wizard_graph_patch_proposal_review
```

Current source search still shows:

```text
REQUIRED_INTERNAL_CLAIMGATE_GATES = 14 generic gates only
if (!requiredGates.has(gateName)) return No Lev-owned internal ClaimGate verifier...
Wizard obligations still produced as claimgate.wizard_* obligations
```

A15 falsifier hardcode was improved, but this is a different seam.

Required design choice:

Option A — register real host-owned internal verifiers for:

```text
wizard_sim_engine_probe
wizard_council_wave_loop
wizard_graph_patch_proposal_review
```

Option B — make Wizard steering produce the existing 14 generic ClaimGate internal gates instead of custom `wizard_*` gates.

Acceptance:

```text
lev orchestration lev-wizard-ratchet demo --real-engines --real-source-evidence --real-skills --json --out <file>
```

must produce either:

- a deliberate `host_blocked` with named remaining blockers, or
- `host_consumed` for a genuinely host-verified path and then a valid `nextRunSeed`.

No more “fixture/dry-run green” as a substitute.

### Blocker 7 — attack-id accounting is still not literal A1–A24 closure

Current source now says:

```text
explicitGraphSuiteCoverage = ['A1', 'A2', 'A4', 'A5', 'A8', 'A9', 'A11']
stillNeedsDedicatedAttackImplementation = []
untraceableClaimedAttackIds = ['A13', 'A17', 'A21']
```

Safe claim:

```text
A1 is now covered in graph tests.
A13/A17/A21 remain untraceable claimed attack IDs, not closed attack implementations.
```

---

## Active CR: current state after mass-spawn

The active CR lane now ran and produced the missing matrix.

Key receipt:

```text
/tmp/claude-burn-2026-06-29/cr-active/CR_READY_FOR_LEV_MATRIX.md
```

Safe summary:

- Every row remains fenced: `promotion_allowed=false`, `formal_admission_allowed=false`.
- The matrix keeps two live readings of top candidate:
  - lego stack / atomic gate strength;
  - v7 sim / result-schema ingestibility.
- Highest-leverage next wave is fresh rerun of pilot set in active CR.

Top candidates named in the matrix include:

```text
finite_density_matrix_carrier_trace_psd_pytorch_sympy_z3
amplitude_damping CPTP density operator lego
probe_quotient_fingerprint_floor_v1
weyl_spinor_chirality_hamiltonian_sign_expectation_clifford_pytorch_z3
pauli_clifford_commutator_representation_gap_clifford_sympy_z3
signed conditional/coherent information negative entropy lego
coherent information parameter gradient two-qubit mixture lego
spectral entropy family density state lego
two-point spectral triple Dirac commutator distance lego
rosetta IGT/QIT four-element formal scout
```

Highest-leverage next CR wave from the matrix:

```text
Re-run the 9 lego candidates and v7 probe_quotient_fingerprint_floor_v1 fresh in active CR.
Upgrade from exists+runs to passes-local-rerun.
```

Do **not** schedule CR into Lev until Lev's ClaimGate/Wizard trust seams above are closed.

---

## Desktop CR: current state after mass-spawn

Desktop lane now corrected itself and consolidated.

Receipts:

```text
/tmp/claude-burn-2026-06-29/cr-desktop/root-confusion-correction.md
/tmp/claude-burn-2026-06-29/cr-desktop/desktop-receipt-consolidator.md
/tmp/claude-burn-2026-06-29/cr-desktop/IMPORT_DISCARD_HOLD_MANIFEST.md
```

Safe summary:

- root confusion corrected;
- Desktop is not active CR;
- `D=0` confirmed;
- 53 import candidates require active-CR recheck;
- hold/quarantine and discard-later lists exist;
- lane is closed for triage.

Do not let Desktop import candidates jump directly into active CR. Diff them first.

---

## What “mass workflow” should mean now

The next Claude terminal work must be **build/fix waves**, not more auditors reading old receipts.

Parent Claude must maintain a real ledger:

```text
queued | running | ok | failed | blocked | superseded | needs-owner
```

Each child worker must have:

```text
worker_id
root
exact files allowed
goal
acceptance command
receipt path
timeout
status
next worker to launch
```

Started workers do not count. Completed receipts plus current Hermes/Codex verification count.

---

## Full Lev patch campaign — mass-spawn parent prompt

Paste this into the Claude terminal that should control the Lev mass workflow. It is intentionally explicit about spawning.

```text
You are the Lev mass-work parent controller.

Root: /Users/joshuaeisenhart/GitHub/lev
Branch: claimgate-steering-bridge-lock
Do not stage, commit, push, rebase, clean, reset, or touch unrelated dirty files.

Mission: get Lev's full Wizard/ClaimGate path working as a real patched system, not a one-shot audit. Use mass spawning through your actual Claude/CCD spawn tools. If your environment exposes `mcp__ccd_session__spawn_task`, use it. If it exposes Claude Code Task/subagent tools instead, use those. Do not merely describe spawning.

Parent ledger path:
/tmp/claude-burn-2026-06-29/lev-mass-parent-ledger.md

Every worker writes exactly one receipt:
/tmp/claude-burn-2026-06-29/lev-mass/<worker-id>.md

Acceptance for every worker receipt:
- files read
- files changed
- commands run with exit codes
- tests added
- result: ok / failed / blocked
- exact remaining risk
- next worker recommendation

Run waves, not flat chaos:
Wave 0: parent census and patch isolation.
Wave 1: independent root-trust fixes.
Wave 2: Wizard path host-consumed / nextRunSeed integration.
Wave 3: package split and verification.
Wave 4: active CR pilot only after Lev passes.

Concurrency:
- Spawn up to 6 workers at once in Wave 1.
- Only spawn workers that touch disjoint files.
- If two workers need the same file, serialize them or put one in audit-only mode.
- Parent must update the ledger after every worker result and immediately launch the next queued worker.

Wave 0 — parent census first, no edits:
1. `dirty-slice-map` — list all currently dirty Lev files grouped by patch slice: ClaimGate, Wizard, harness runner, graph, unrelated. Receipt only.
2. `current-test-baseline` — run current targeted tests/typechecks and record counts. Use existing Hermes outputs as comparison but run locally too.

Wave 1 — root-trust fix workers:
3. `a22c-host-trust-root-fix` — fix same-process host trust ref forgery:
   - make trust issuance host-internal/token-gated or otherwise not public to untrusted callers;
   - pin host trust ledger root to canonical host root, not caller-settable env;
   - add regression for same-process issue+root redirect;
   - acceptance: forged ref not accepted; legitimate host-issued ref still accepted.

4. `rerun-commands-ownership-fix` — fix `/etc/hosts` target_files exploit:
   - reject absolute paths outside canonical Lev checkout;
   - require target_files under host root and/or hash-bound to sourceFileHashes;
   - add regression with `/etc/hosts` expecting host_blocked;
   - acceptance: legitimate target_files still pass.

5. `source-forbidden-key-normalization-fix` — fix A3 forbidden-field variants:
   - normalize or reject case/space/zero-width/homoglyph variants before forbidden-set lookup;
   - add tests for the 6 bypass variants from `lev-census/source-forbidden-fieldscan-a3-variants.md`;
   - acceptance: all variants caught or explicitly rejected as suspicious keys.

6. `evidence-manifest-host-context-fix` — stop producer-vs-producer evidence manifest matching:
   - make trusted sourceBoundEvidenceContext host-issued/token-gated/signed;
   - reject caller-supplied context when route claims host trust;
   - add regression using forged file evidence + forged context expecting withheld/blocked;
   - acceptance: legitimate source evidence still passes.

7. `seed-integrity-replay-fix` — host-anchor nextRunSeed and seed replay ledger:
   - sign/HMAC seed facts or bind to host-issued previous-run receipt store;
   - pin replay ledger root;
   - add tests for forged previousResult and `LEV_PROJECT_ROOT` replay bypass;
   - acceptance: forged seed blocked; legitimate earned seed can be consumed once.

Wave 2 — Wizard full path:
8. `wizard-internal-gates-design` — choose and implement one path:
   - Option A: register host-owned internal gates for `wizard_sim_engine_probe`, `wizard_council_wave_loop`, `wizard_graph_patch_proposal_review`; or
   - Option B: make Wizard steering emit the existing 14 standard ClaimGate internal gates.
   - acceptance: `lev-wizard-ratchet demo --real-engines --real-source-evidence --real-skills` no longer blocks solely because wizard_* gates are unregistered.

9. `wizard-next-run-seed-e2e` — prove the recursive wave:
   - run demo/consume/seed chain in tmp dir;
   - get either a real `host_consumed` + nextRunSeed or a precise blocker that is not the old unregistered-gate blocker;
   - acceptance: wave1 -> seed -> wave2 is mechanically tested, not hand-constructed.

Wave 3 — patch slicing and verification:
10. `claimgate-slice-verifier` — fresh-context audit of workers 3-7. Run targeted tests and attack probes. No implementation unless fixing a failed test.
11. `wizard-slice-verifier` — fresh-context audit of workers 8-9. Run demo/seed chain. No implementation unless fixing a failed test.
12. `harness-runner-slice-verifier` — verify Codex adapter/runner patch remains separate and green.
13. `dist-build-packaging-verifier` — run clean build and dist/source checks.
14. `final-patch-plan` — produce landable patch split with exact file lists and commands.

Wave 4 — only after Wave 3 is green:
15. `active-cr-pilot-rerun-plan` — do not mutate Lev. Read CR matrix and produce fresh rerun commands for the top-10 pilot set in active CR.

Parent rules:
- Do not stop after launching first workers.
- If a worker blocks, write blocker receipt and launch the next independent worker.
- If a worker touches a file another worker needs, mark conflict and serialize.
- If tests fail, do not summarize and stop: spawn a focused fixer worker with the failing command and file list.
- Final parent output must be a ledger with all worker statuses and receipt paths.
```

---

## Short prompt for already-running Claude terminals

Use this if a terminal already has context and you need to redirect it:

```text
STOP reading and summarizing. Switch to mass-work parent mode.

Read:
/Users/joshuaeisenhart/wiki/projects/leviathan-current/lev-mass-workflow-deep-audit-and-patch-orders-2026-06-30.md

Use the “Full Lev patch campaign — mass-spawn parent prompt” section.

You must use your actual spawn/task tools. Do not pretend. Create:
/tmp/claude-burn-2026-06-29/lev-mass-parent-ledger.md

Spawn Wave 0 and Wave 1 workers now. Each child writes one receipt under:
/tmp/claude-burn-2026-06-29/lev-mass/<worker-id>.md

Do not stage/commit/push/rebase/clean/reset. Do not touch unrelated dirty files.
```

---

## Safe claims now

```text
Mass receipt output exists now across Lev, lev-census, active CR, and Desktop CR.
Desktop triage corrected root confusion and closed its consolidator.
Active CR readiness matrix exists and is useful, but all CR candidates remain non-admitted/pre-pilot.
Lev targeted current tests pass locally: orchestration 766, graph redteam 7, typechecks ok.
Lev is still dirty and not landed.
The full Lev/Wizard path is not yet trustworthy until A22c, rerun_commands, source key normalization, evidence-manifest host context, seed integrity, and Wizard steering host-consumed path are fixed and verified.
```

## Unsafe claims

```text
Full Lev path works.
Wizard recursive waves are live.
All A1-A24 are closed.
A22c is closed just because raw JSON ledger forgery is blocked.
`rerun_commands` proves Lev-owned source targets.
Evidence-manifest proves host-owned context.
CR candidates are ready/admitted/canonical.
Desktop CR import candidates can be applied without active-CR diffing.
```
