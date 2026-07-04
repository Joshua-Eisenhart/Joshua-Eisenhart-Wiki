---
title: Codex Lev big job prompt
created: 2026-06-30
type: sendable-codex-work-packet
status: current-after-a23b
claim_ceiling: Hermes verified selected current tests/build after Codex A23b receipt; this is a work packet, not admission.
---

# Codex Lev big job prompt — 2026-06-30

Paste this to Codex after the A23b report. This is a big implementation job, not another small seam audit.

## Current verified state

Hermes locally checked after the A23b receipt:

```text
root: /Users/joshuaeisenhart/GitHub/lev
branch: claimgate-steering-bridge-lock
HEAD: f9185635334f
status shape: M=139 D=4 ??=80 total=223
```

Hermes reran:

```text
pnpm --filter @lev-os/orchestration test -- \
  src/proof/claim-gate-redteam-targets.test.ts \
  src/proof/claim-gate-loop.test.ts \
  src/handlers/claim-gate-loop.test.ts

Result: exit 0, 51 files passed, 766 tests passed
```

```text
pnpm --filter @lev-os/graph test -- src/__tests__/claim-gate-redteam-targets.test.ts

Result: exit 0, 7 pass, 0 fail
```

```text
pnpm --filter @lev-os/orchestration typecheck
Result: exit 0

pnpm --filter @lev-os/orchestration build
Result: exit 0; prebuild ran clean-build.mjs, then tsc
```

A23b graph-event trust ledger raw forgery appears closed at the tested level. Do not spend the next job re-proving A23b unless a current regression fails.

## Current ceiling

```text
branch-local working-tree real
not landed
not canonical
repo still has 223 dirty entries
ClaimGate/Wizard files include untracked local work
```

No `git add`, `git commit`, `git push`, `git rebase`, `git clean`, `git reset`, or checkout unless explicitly authorized.

---

## Mission

Make the **full Lev Wizard/ClaimGate path** substantially more real.

Do not drift to CR/Desktop. Do not spend the job only summarizing. Do not stop after one green test. This is the large Codex job:

```text
close remaining root-trust seams -> wire Wizard to host-verifiable ClaimGate -> prove a recursive demo/seed path or a precise remaining blocker -> isolate landable patch slices
```

Use the actual Lev apparatus and source. If you can spawn Codex/Spark subagents, use them as bounded verification/fixer lanes. If spawning is unavailable, run the same lanes serially and write the ledger anyway.

Parent ledger:

```text
/tmp/claude-burn-2026-06-29/lev/codex-big-job-ledger.md
```

Per-lane receipts:

```text
/tmp/claude-burn-2026-06-29/lev/codex-big-job/<lane-id>.md
```

Every lane receipt must include:

```text
files read
files changed
red test added or existing failing probe used
green fix
commands run with exit codes
current status: ok / failed / blocked
remaining risk
next lane recommendation
```

---

## Big-job priority order

### Lane 0 — patch-slice census first

Write:

```text
/tmp/claude-burn-2026-06-29/lev/codex-big-job/00-patch-slice-census.md
```

Do not edit. Capture:

- current dirty files grouped into ClaimGate steering, ClaimGate loop, Wizard route, graph redteam, harness runner, dist/build artifacts, unrelated dirty state;
- untracked files that are part of the intended patch;
- tracked deletes that must not be accidentally staged;
- exact current verification baseline.

Acceptance: the receipt names the files Codex is allowed to edit in lanes 1–6.

### Lane 1 — A22c same-process host-trust/root redirection

Problem:

`handlers/claim-gate-loop.ts` now MACs host trust ledger entries, but `issueClaimGateHostTrustedEvidenceRefs(refs, root = claimGateProjectRoot())` is exported and `claimGateProjectRoot()` still uses caller-settable env roots:

```text
LEV_CLAIMGATE_HOST_TRUST_ROOT ?? LEV_PROJECT_ROOT ?? LEV_ROOT ?? cwd()
```

The remaining exploit is not raw JSON forgery. It is same-process host-trust issue into an attacker-controlled root, then using `--host-trusted-evidence-ref` from that root.

Required work:

1. Add a failing test that reproduces same-process issue + root redirection acceptance.
2. Fix by making host trust issuance host-internal/token-gated or otherwise not callable as producer authority.
3. Pin/validate the host trust ledger root to a canonical host root; do not let caller env roots be proof authority.
4. Preserve a legitimate host-issued trust path for real CLI use.

Acceptance:

- forged same-process issue/root-redirected ref is rejected;
- raw JSON forged ledger remains rejected;
- legitimate host-issued trust ref still works;
- targeted tests pass.

### Lane 2 — `rerun_commands` path ownership/hash binding

Problem:

`claim-gate-steering-run.ts` currently accepts any existing file path:

```text
hostCheckoutPathExists(path, runDir): if (existsSync(path)) return true
```

Observed exploit: `boundary.target_files = ["/etc/hosts"]` led to `status=host_consumed` in the census probe.

Required work:

1. Add regression with `/etc/hosts` or another absolute outside-repo path.
2. Fix target file checking so it only accepts files under a canonical Lev checkout/root.
3. Preferably bind target files to source hashes already computed by the host.
4. Preserve legitimate fixture target files.

Acceptance:

- `/etc/hosts` target is `host_blocked`;
- valid in-repo target file remains accepted;
- no path traversal / ancestor-walk outside root;
- tests pass.

### Lane 3 — source forbidden-key normalization

Problem:

`scanAuthorityFieldsDeep` uses exact raw JSON key names. The census found bypasses:

```text
LevEngineSubstrateDigest
LEVENGINESUBSTRATEDIGEST
levEngineSubstrateDigеst  # Cyrillic e
" levEngineSubstrateDigest"
"levEngineSubstrateDigest "
"lev​EngineSubstrateDigest" # zero-width space
```

Required work:

1. Add regression tests for the six bypass variants.
2. Normalize or reject suspicious source keys before checking forbidden/authority fields.
3. Apply the same logic to `SOURCE_FORBIDDEN_PROOF_AUTHORITY_FIELDS` and `EXPLICIT_AUTHORITY_PROJECTION_FIELDS`.
4. Make error codes explicit enough to debug.

Acceptance:

- all six bypass variants produce error findings;
- exact canonical forbidden keys still caught;
- benign ordinary keys remain accepted;
- tests pass.

### Lane 4 — evidence-manifest host context

Problem:

The Wizard route can compare producer-authored evidence files against a `sourceBoundEvidenceContext` derived from producer-authored `LevWizardRatchetRunInput`. That is self-consistency, not host-attested context.

Required work:

1. Add a failing test based on `/tmp/claude-burn-2026-06-29/lev-census/evidence-manifest-hashes.md`:
   - forged evidence file;
   - forged `contextReceiptRefs`, `contextContentHashes`, `threeEngineEnvelopeHash` supplied through options/input;
   - expected withheld/blocked when the route claims host-bound evidence.
2. Introduce a host-attested context path:
   - token-gated, HMAC-signed, or loaded from a host-owned receipt store;
   - public caller-supplied context must be advisory or rejected for host-bound gates.
3. Preserve current fixture behavior with honest ceiling labels if full host context is not available.

Acceptance:

- producer-vs-producer evidence manifest no longer confers gate trust;
- legitimate host-issued context path passes;
- route truth clearly labels advisory/fixture context.

### Lane 5 — seed integrity and replay ledger

Problem:

`buildAcceptedSurvivorNextRunSeed()` hashes facts from `previousResult`; `createSeededLevWizardRatchetInput()` validates intra-document consistency. Replay ledger path is env-root based.

Required work:

1. Add tests for forged previousResult/nextRunSeed self-consistency.
2. Add tests for replay bypass via `LEV_PROJECT_ROOT` / `LEV_ROOT` root redirection.
3. Fix seed issuance/verification with host HMAC or host-issued previous-run receipt ledger.
4. Pin/validate seed replay ledger root.
5. Preserve legitimate once-only seed consumption.

Acceptance:

- forged previousResult seed rejected;
- replay with env-root redirection rejected;
- legitimate earned seed can be consumed once and blocks on second consume;
- tests pass.

### Lane 6 — Wizard steering host-consumed / recursive path

Problem:

`lev-wizard-ratchet` still emits custom obligations:

```text
claimgate.wizard_sim_engine_probe
claimgate.wizard_council_wave_loop
claimgate.wizard_graph_patch_proposal_review
```

But `evaluateInternalClaimGateGate()` only recognizes the 14 generic internal ClaimGate gates. If the custom wizard gates remain unregistered, `host_consumed` / `nextRunSeed` cannot be earned through the real path.

Required design choice:

Choose one and implement:

A. Register host-owned internal verifiers for the three `wizard_*` gates.

or

B. Make Wizard steering emit the existing 14 generic internal ClaimGate gates, backed by host-verifiable evidence.

Acceptance:

Run:

```text
./core/poly/bin/lev orchestration lev-wizard-ratchet demo \
  --real-engines \
  --real-source-evidence \
  --real-skills \
  --json \
  --out /tmp/lev-wizard-real-path-wave1.json
```

Then attempt:

```text
./core/poly/bin/lev orchestration lev-wizard-ratchet seed \
  /tmp/lev-wizard-real-path-wave1.json \
  --json \
  --out /tmp/lev-wizard-real-path-wave2.json
```

Accept either:

- `host_consumed` + nextRunSeed + mechanical wave2 seed path, or
- a precise new blocker that is **not** unregistered wizard internal gates, not producer-vs-producer evidence context, not seed self-consistency.

### Lane 7 — final verifier / patch split

After lanes 1–6, run a fresh verification pass and write:

```text
/tmp/claude-burn-2026-06-29/lev/codex-big-job/07-final-verifier-and-patch-split.md
```

Required commands:

```text
pnpm --filter @lev-os/orchestration test -- src/proof/claim-gate-redteam-targets.test.ts src/proof/claim-gate-loop.test.ts src/handlers/claim-gate-loop.test.ts src/handlers/claimgate-steering.test.ts src/proof/claim-gate-steering-run.test.ts src/proof/lev-wizard-ratchet.test.ts src/handlers/lev-wizard-ratchet.test.ts
pnpm --filter @lev-os/graph test -- src/__tests__/claim-gate-redteam-targets.test.ts
pnpm --filter @lev-os/orchestration typecheck
pnpm --filter @lev-os/graph typecheck
pnpm --filter @lev-os/orchestration build
git diff --check -- <all intentionally touched files>
```

Also run live CLI smoke:

```text
./core/poly/bin/lev orchestration claimgate-steering --help
./core/poly/bin/lev orchestration lev-wizard-ratchet --help
./core/poly/bin/lev orchestration lev-wizard-ratchet demo --real-source-evidence --json --out /tmp/lev-wizard-post-big-job-demo.json
```

Patch split output:

1. ClaimGate root-trust patch files.
2. Wizard route patch files.
3. Graph trust patch files.
4. Harness runner patch files, if still present.
5. Generated dist/build artifacts.
6. Unrelated dirty files to exclude.
7. Untracked files to intentionally include vs ignore.

---

## Rules

- No commit/stage/push/rebase/clean/reset.
- No CR/Desktop broadening.
- Do not reconstruct the old external 24-attack harness unless all current traceable blockers above are closed.
- Do not invent implementations for A13/A17/A21; keep them `untraceableClaimedAttackIds` unless you find their exact durable definitions.
- If a lane cannot finish, write the blocker receipt and continue with another independent lane.
- If a fix conflicts with another lane, serialize and update the ledger.
- Do not claim victory unless the live CLI path is tested.

## Final answer format Codex should return

```text
Big job status: <partial/green/blocked>

Lanes completed:
- <lane-id>: <ok/failed/blocked>, receipt path, tests

Files intentionally changed:
- grouped by patch slice

Commands run:
- exact command -> exit/status/count

Live CLI result:
- claimgate-steering: ...
- lev-wizard-ratchet demo: ...
- seed chain: ...

Remaining blockers:
- precise list

Do not say done/canonical/landed.
```
