---
title: Lev ClaimGate Digging Status — 2026-06-28
created: 2026-06-28
updated: 2026-06-28
type: status-capture
status: active-blocker-map
claim_ceiling: thread/user-pasted audit capture plus limited Hermes disk checks; not merged code; not full repo proof; not release certification
source_repo: /Users/joshuaeisenhart/GitHub/lev
related:
  - projects/leviathan-current/lev-claimgate-ratchet-memory-harness-plan-2026-06-25
  - projects/leviathan-current/codex-redteam-targets-2026-06-28
  - hermes-current/fresh-thread-continuity-2026-06-28
---

# Lev ClaimGate Digging Status — 2026-06-28

## Purpose

Preserve the current Lev/ClaimGate audit-and-build state so the work is not lost across Hermes/Claude/Codex thread boundaries.

This page captures the latest user-pasted handoff and Hermes-thread summary. It is a blocker/status map, not a proof that the repo is fixed.

## Current bottom line

The tranche is useful but **not land-ready**.

The live work has shifted from broad audit to bounded implementation and verification. More audit councils should not be launched merely to look busy; the known bottleneck is now building, testing, and landing separated slices.

2026-06-28 update: the notary/falsifier backing receipt is de-risked, but the legacy-path guard now has a real policy fork. `core/poly` has live `@lev-os/daemon` / `@lev-os/sdlc` coupling, so greenlighting the guard requires the owner decision: either those packages are deprecated and `core/poly` must migrate, or the guard's forbidden package list is stale.

Later 2026-06-28 Codex build update: ClaimGate source-bound evidence context has reportedly moved from producer-authored input into host-owned run options, Wizard now supplies that host context, and FlowMind harness output was tightened toward semantic `data.output` only. Hermes spot-check supports the orchestration slice, but **does not support the pasted claim that harness session-runner tests are green**: rerunning the focused harness session-runner test from `core/harness` produced `20 passed / 2 failed`, blocked by SDLC schema path resolution.

Late 2026-06-28 red-team/update: the red-team swarm reportedly broke 16/24 attacks, which collapse to three root causes: caller-minted trust/execution tokens at boundaries, path-string-only carrier provenance, and missing freshness/anti-replay. The highest-consequence reported hole was host-trust laundering via `--host-trusted-evidence-ref` into graph mutation. A later Codex build then reportedly added host execution witnesses, rejected external consume-supplied engine digests unless `--real-engines` host-rebuilds them, blocked raw trusted refs at the CLI boundary, hardened graph runtime root resolution, and fixed source-pack freshness. Hermes spot-check supports several of these improvements, but the Lev worktree remains dirty (`212` status lines) and many key ClaimGate/ratchet files are still untracked, so this is **stronger local evidence, not landed/canonical state**.

Codex target packet: [[projects/leviathan-current/codex-redteam-targets-2026-06-28]] preserves the volatile Claude scratchpad `codex_redteam_targets.md` as a durable build packet: 16 broke-through attacks grouped under the three roots, plus the held internal guards that must not regress. Use it as Codex's actionable target set after reading this status page.

## 2026-06-28 red-team roots and patch state

Reported red-team roots:

1. **Boundary trust-token forgery** — producer/caller could mint proof, trusted refs, ok-flags, object bindings, or projections that gates accepted without a host-issued/execution anchor.
2. **Carrier provenance laundering** — path-string checks blocked narrow Codex-Ratchet path spellings but not content copied to a neutral path, case/slash variants, or `file:` refs into reference material.
3. **Replay/freshness gap** — captured digest/witness or seed families could replay without nonce/session/seen-digest enforcement.

Highest-consequence reported hole:

- A22/A23: caller-supplied host-trust laundering. The pasted collapse says a producer could pass its own receipt ref through `--host-trusted-evidence-ref`, satisfy source-bound gates, and reach `recordClaimGateGraphPatchExecution` with `graphMutationApplied: true`.

Pasted Codex patch report says:

- `LevEngineSubstrateDigest` now requires a host execution witness.
- `real-three-engine-envelope.ts` builds that witness.
- External `lev-wizard-ratchet consume` rejects caller-supplied engine digests unless `--real-engines` is used so the host rebuilds evidence.
- `claim-gate-loop` raw trusted evidence refs are disabled at the CLI boundary.
- Graph runtime root resolution fails closed unless `LEV_PROJECT_ROOT` / `LEV_ROOT` points at a real Lev root.
- The Julia R0 probe writes results to a host temp output path rather than into the source carrier.
- The source-pack freshness check uses a monotonic `verifiedAtMs` against observed source mtime.

Hermes spot-check after paste:

- Read required Lev planning/validation surfaces: `.lev/validation-gates.yaml` and `dna/graph.yaml`.
- `/Users/joshuaeisenhart/GitHub/lev` exists; `git status --short | wc -l` returned `212`.
- Key files named in the patch are visible on disk, but many are still untracked from git's point of view: `core/graph/src/contracts/projection-binding.ts`, `core/graph/src/probes/lev-native-r0-probe.ts`, `core/graph/src/probes/skill-source-pack-runner.ts`, `core/orchestration/src/handlers/claim-gate-loop.ts`, `core/orchestration/src/handlers/lev-wizard-ratchet.ts`, `core/orchestration/src/proof/claim-gate-loop.ts`, `core/orchestration/src/proof/lev-wizard-ratchet.ts`, and `core/orchestration/src/proof/real-three-engine-envelope.ts`.
- `core/graph/src/__tests__/projection-binding.test.ts` now has regression tests rejecting a self-consistent engine digest without a host execution witness and rejecting a stale witness.
- `core/orchestration/src/handlers/lev-wizard-ratchet.ts` rejects external consume inputs that supply `levEngineSubstrateDigest` without `--real-engines`, then host-builds `threeEngineEnvelope`, `levEngineSubstrateDigest`, and `levEngineSubstrateExecutionWitness` when `--real-engines` is present.
- `core/orchestration/src/handlers/claim-gate-loop.ts` has a raw trusted evidence ref disabled response at the CLI boundary. The underlying proof helper still recognizes trusted refs by regex plus set membership, so future review should verify all non-CLI/programmatic paths can only receive host-issued refs.
- `pnpm --filter @lev-os/graph test` returned `356 pass / 0 fail` after retrying without unsupported `--runInBand`; note this includes stale `dist/__tests__` discovery, but it was green in this run.
- Focused orchestration rerun `pnpm --dir core/orchestration exec vitest run src/handlers/claim-gate-loop.test.ts src/handlers/lev-wizard-ratchet.test.ts src/proof/lev-wizard-ratchet.test.ts` returned `3 files passed`, `41 tests passed`, exit `0`.
- Real-engine demo command `pnpm --dir core/orchestration exec lev orchestration lev-wizard-ratchet demo --real-engines --real-source-evidence --real-skills --json` returned exit `0`; the output included `threeEngineOk: true`, `formalSkillRuntimeDebt: 0`, `failurePackets: []`, `graphAdmission.graphMutationApplied: false`, and `steeringAdmission.status: "host_consumed"`.

Current support level:

- **Locally stronger / observed:** graph tests pass, focused ClaimGate/Wizard tests pass, the real-engine demo exits `0`, and source shows host witness and external-digest rejection logic.
- **Still not landed/canonical:** dirty worktree with many untracked load-bearing files; graph mutation remains proposal-only (`graphMutationApplied: false`); the self-audit/runtime-autonomy ceiling from the pasted report remains open; non-CLI trusted-ref paths still need a fresh adversarial check.
- **Do not promote:** not final ratchet, not release proof, not durable graph mutation/autonomous self-improvement.

## Checked or reported green in the thread

Reported from the latest Hermes digging pass, not freshly rerun by this page:

- `pnpm --dir core/orchestration exec vitest run` reported `49 files passed`, `705 tests passed`, exit `0`.
- `pnpm --dir core/orchestration run typecheck` reported exit `0`.
- `pnpm --dir core/graph run typecheck` reported exit `0`.
- Direct source test for `src/__tests__/skill-source-pack-runner.test.ts` reported `5 pass`, `0 fail`.

Caveat: before editing or landing, re-run these from the live repo and record exact output.

Additional Codex-pasted build report on 2026-06-28:

- `sourceBoundEvidenceContext` moved out of producer-authored `ClaimGateCouncilWaveInput` and into host/run options in `core/orchestration/src/proof/claim-gate-loop.ts`.
- `core/orchestration/src/proof/lev-wizard-ratchet.ts` now supplies that context as host-owned call context.
- `core/orchestration/src/proof/claim-gate-loop.test.ts` adds regression coverage for rejecting producer-authored source-bound context.
- `core/harness/src/execution/session-runner.ts` attempts to pass only semantic `data.output` back to FlowMind rather than the full harness receipt envelope.
- Codex reported no OpenRouter or external model API calls; it used internal Codex subagents, local Hermes/Claude files, Lev tests, and Lev CLI runs.

Hermes spot-check after the paste:

- `git status --short | wc -l` in `/Users/joshuaeisenhart/GitHub/lev` returned `204`, so the repo is still far from land-clean.
- The three orchestration files named above are currently untracked from git's point of view, while `core/harness/src/execution/session-runner.ts` and `core/harness/src/__tests__/session-runner.test.ts` are modified.
- Search/read checks found the host-only violation path in `claim-gate-loop.ts`, the Wizard host context call in `lev-wizard-ratchet.ts`, and the producer-smuggle regression in `claim-gate-loop.test.ts`.
- Rerun command `pnpm --dir core/orchestration exec vitest run src/proof/claim-gate-loop.test.ts src/proof/lev-wizard-ratchet.test.ts` returned `2 passed`, `62 passed`, exit `0`.
- Rerun command `pnpm --dir core/orchestration run typecheck` returned exit `0`.
- Rerun command `pnpm --dir core/harness run typecheck` returned exit `0`.
- Rerun command `pnpm --dir core/harness exec vitest run src/__tests__/session-runner.test.ts` returned `20 passed / 2 failed`, exit `1`; failures were `converts sdlc/execute into a harness-backed domain prompt` and `blocks sdlc/execute before handler spawn when execution_plan is invalid`. A second rerun with `pnpm --filter @lev-os/harness-sdk exec vitest run src/__tests__/session-runner.test.ts` failed the same way. The immediate error was `SDLC schema not found: schemas/execution-plan.schema.json`; the only matching schema on disk was `/Users/joshuaeisenhart/GitHub/lev/plugins/sdlc/schemas/execution-plan.schema.json`, while the loader searched package-local/core-local paths and `core/harness/plugins/sdlc/...`.

Treat the orchestration host-context slice as locally green under the focused rerun. Treat the FlowMind/harness slice as **not green under Hermes rerun** until schema path resolution is fixed or Codex provides the exact passing command/environment that makes the search path valid.

Second Codex-pasted build report on 2026-06-28:

- Codex again reported clean model usage: no OpenRouter, no `gpt-3.5-turbo`, only local/internal Codex subagents, now closed.
- Codex reported the same source-bound evidence context fix plus a FlowMind/harness semantic-output fix.
- Codex reported broader verification: `claim-gate-loop.test.ts` `51 pass`; focused Wizard/ClaimGate `105 pass`; full `core/orchestration` `707 pass`; orchestration typecheck pass; harness targeted session-runner `22 pass`; harness typecheck pass; affected FlowMind `39 pass`; live route real evidence/skills `exit 0`, `0 failure packets`, `host_consumed`; invalid sim `exit 1`, `18 failure packets`, `host_reviewed_failed`; stale fixture trust alone `exit 1`.

Hermes re-check after the second paste:

- `git status --short | wc -l` still returned `204`; the repo remains far from land-clean.
- Touched files remain `M core/harness/src/__tests__/session-runner.test.ts`, `M core/harness/src/execution/session-runner.ts`, and untracked orchestration proof files.
- `pnpm --dir core/orchestration exec vitest run src/proof/claim-gate-loop.test.ts src/proof/lev-wizard-ratchet.test.ts` returned `2 passed`, `62 passed`, exit `0`.
- `pnpm --dir core/orchestration run typecheck` returned exit `0`.
- `pnpm --dir core/harness run typecheck` returned exit `0`.
- `pnpm --dir core/harness exec vitest run src/__tests__/session-runner.test.ts` still returned `20 passed / 2 failed`, exit `1`, with the same SDLC schema path failure.

Current support level: Codex may have run a different command, environment, or later patch, but this Hermes-visible worktree does **not** support the claim that targeted harness `session-runner` tests pass. Do not promote the harness slice to green without either fixing the schema search path in this tree or preserving Codex's exact passing command/environment as a separate receipt.

## Current blockers and smallest fixes

### 1. Graph package test discovery is polluted by ignored `dist/`

Observed/reported:

```text
pnpm --dir core/graph exec bun test
334 pass
1 fail
exit 1
```

The failing test was reported under:

```text
core/graph/dist/__tests__/skill-source-pack-runner.test.js
```

The source TypeScript test passed. `core/graph/dist/` was reported ignored and untracked, but Bun still discovered its generated tests.

Smallest fix:

- Make graph tests source-only, or explicitly exclude `dist` from Bun test discovery.
- Add a guard that package tests do not discover `dist/__tests__`.
- Clean/rebuild `dist` separately when testing built package outputs.

### 2. Legacy-path guard is red and now has a real policy fork

Reported command:

```text
pnpm run test:guard:legacy-paths
```

Reported result: exit `1`.

Earlier scanner diagnosis said it was likely over-broad. The newer Claude handoff and Hermes spot-check refine that: some hits are exemption-safe, but `core/poly` has real live coupling to the forbidden packages.

Observed from disk in Hermes spot-check:

- `core/poly/package.json` contains `@lev-os/daemon` and `@lev-os/sdlc` workspace dependencies.
- `core/poly/src` has imports from `@lev-os/daemon` / `@lev-os/sdlc`.
- `core/harness` includes `plugins/sdlc` references; Claude reports `session-runner.ts:91` as a real runtime filesystem coupling.
- `core/orchestration` hits are reported as comments, strings, or fixtures rather than live imports.
- the `core/daemon`, `plugins/platforms`, and `plugins/sdlc` packages naming themselves are exemption-safe.

Smallest honest decision:

- If `@lev-os/daemon` and `@lev-os/sdlc` are actually deprecated, migrate `core/poly` off them; this is real implementation work.
- If they are not deprecated, the forbidden-pattern list is stale and should stop banning those package names.
- Do not merely exempt `core/poly`; that would hide a live dependency edge.

### 3. Source-read binding is still incomplete

Needed chain:

```text
SourcePackReadReceipt
→ loadedContextReceipts
→ member/wave sourceRefs
→ evidence_manifest contextContentHashes
```

Current state reported:

- Source-pack intake and hash checks exist.
- `claim-gate-loop.ts` can compare `contextReceiptRefs` and `contextContentHashes` against host context when provided.
- There is still no first-class proof that a specific source record was read before shaping a specific member/wave.

Smallest fix:

- Add a session-scoped `SourcePackReadReceipt` with source pack ID, source record ID, content hash, loader/member/wave ID, session/workstream, and claim ceiling.
- Require `evidence_manifest` to reference those receipts instead of arbitrary context hashes.

### 4. Notary/falsifier gap is narrowed; backing receipt should be GKSL PSD flip, not the one-sided R0 quotient leg

Reported current good checks in `claim-gate-loop.ts`:

- requires `sessionId` for source-bound evidence;
- compares task hash when context exists;
- compares object ref when context exists;
- compares context receipt refs/hashes when context exists;
- compares `threeEngineEnvelopeHash` when context exists.

Hermes spot-check confirms the handler literals are currently static in `core/orchestration/src/handlers/lev-wizard-ratchet.ts`:

```ts
falsifierStatus: 'closed'
openFalsifierCount: 0
```

Claude handoff plus Hermes disk reads refine the backing receipt choice:

- The consumed R0 quotient-refinement leg fires on the real side: `witness_refinement_negation: "unsat"`.
- That R0 quotient-refinement result lacks `open_falsifier_count` and `falsifier_status`, so adding fields there is real work.
- The R0 quotient-refinement leg does **not** show the needed two-sided control counterpart: `packages.control_only` is `[]`.
- The separate R0 distinguishability file has a two-sided relation flip: `cvc5_relation_flip: ["unsat", "sat"]`, but that is not the same consumed quotient-refinement leg.
- The stronger current backing receipt is `sim_op_gksl_lindblad_probe_results.json`, where `gksl_psd_smt_load_bearing` is `bound_to_measured: true`, real PSD verdict is `sat`, control verdict is `unsat`, and the JAX mirror reports real/control min Kossakowski eigenvalues `+0.5 / -0.5`. The preserved norm is a separate metric, not a blocker.

Smallest fix:

- Add `open_falsifier_count` / `falsifier_status` to the consumed leg.
- Derive/justify their values from a verified two-sided host-recomputable flip, currently the GKSL PSD flip: real holds → `0` / `closed`; control breaks → `1` / `open`.
- Do not use the one-sided quotient-refinement UNSAT alone as the backing receipt.
- Keep the negative test where a source-bound falsifier file says `closed / 0` but lacks host envelope/trusted receipt; non-fixture admission must withhold it.

### 5. Persistence/hydration path remains a high-priority blocker

Claude's pasted handoff states:

- persistence fix at `runtime.ts:171` is first;
- relative path should become absolute or environment-anchored;
- an absolute path was verified to make hydration work.

This page has not freshly verified the file or rerun hydration. Treat this as a high-priority handoff claim that must be checked directly before editing.

### 6. Worktree is too dirty for one broad landing

Reported worktree size: `216` status lines.

Smallest fix:

Split work into separate landing slices:

1. persistence/hydration path;
2. graph test discovery and `dist` hygiene;
3. legacy guard scoping;
4. duplicate package script keys;
5. current ClaimGate source-bound session/context checks;
6. real `SourcePackReadReceipt` binding;
7. falsifier/notary trusted-receipt hardening;
8. Wizard/model-lane/WaveGraph tranche.

Do not commit the whole dirty state as one ratchet patch.

### 7. Duplicate root package script keys create false-green risk

Reported orchestration test warning:

```text
Duplicate key "test:pentagon"
Duplicate key "test:pentagon:gate"
```

Smallest fix:

- Rename or remove duplicate script entries.
- Add a duplicate-key guard for package JSON if absent.

## Blocked/partial worker receipts

A four-worker audit fan-out did not produce usable full summaries:

- Wizard Ratchet newest files: API usage limit before summary.
- ClaimGate source-bound evidence/notary bypass audit: connection error.
- Graph persistence/runtime and legacy guard audit: API usage limit before summary.
- Model-lane collapse and WaveGraph edge contract audit: connection error.

These are route/blocker receipts, not conclusions.

## Model availability note

Hermes itself was still able to answer in the current session. A status check on 2026-06-28 showed the active provider/model as OpenAI Codex / `gpt-5.5`, with OpenRouter, Gemini, and xAI keys configured, while several other providers were not configured or not logged in. The failed worker summaries above look like Claude/OpenRouter quota/connection failures, not proof that all models are unavailable.

For genuinely multimodel councils, the handoff says OpenRouter top-up may be needed.

## Current implementation order

Best current order:

1. Check live repo status and active external writers before editing.
2. Fix persistence/hydration path if `runtime.ts:171` still has the relative-path issue.
3. Fix graph test discovery / stale ignored `dist` pollution.
4. Resolve the legacy-path policy fork: deprecated `daemon`/`sdlc` means migrate `core/poly`; not deprecated means change the forbidden-pattern list.
5. Clean duplicate root package script keys.
6. Land current ClaimGate source-bound session/context checks as a small slice.
7. Add real `SourcePackReadReceipt` binding.
8. Strengthen falsifier/notary trusted-receipt rule using the verified GKSL PSD flip, not the one-sided R0 quotient-refinement leg.

## Claim ceiling

Status capture and next-action router only. This page does not prove the repo, does not land code, and does not certify release readiness.

Related:

- [[projects/leviathan-current/lev-claimgate-ratchet-memory-harness-plan-2026-06-25]]
- [[hermes-current/fresh-thread-continuity-2026-06-28]]
- [[projects/leviathan-current/research-ratchet-deep-patch-plan-2026-06-21]]
- [[projects/leviathan-current/proof-backed-status-dashboard]]
