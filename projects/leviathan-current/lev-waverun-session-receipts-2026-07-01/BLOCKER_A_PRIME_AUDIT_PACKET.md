---
title: Blocker A-prime audit packet (for Codex to implement; Claude to audit)
author: Claude 1 (claude-opus-4-8) — audit only, no implementation
created: 2026-06-30
branch: patch/waverun-engine-gates-20260630
head_at_audit: 50d2e64f3
claim_ceiling: analysis packet, not a fix; no repo edits made
status: superseded
superseded_by: "current wave/canon receipts"
reason: "references patch/waverun artifact"
---

# Blocker A-prime — audit packet

Blocker A (forged obligation hashes on `createRealThreeEngineObligationRunner`) is CLOSED at HEAD `50d2e64f3`. This packet is the SIBLING gap on the OTHER runner. No implementation here — Codex owns `claim-gate-wave-runner.ts`.

## 1. Exact vulnerable path

**Function:** `wizardThreeEngineObligationRunner` — `core/orchestration/src/proof/lev-wizard-ratchet.ts:1640-1692`. This is the `threeEngineRunner` the wizard wires in at `lev-wizard-ratchet.ts:2426`, i.e. the runner behind `lev orchestration lev-wizard-ratchet demo --real-engines`.

**Current validation behavior (lines 1645-1691):** the runner returns `ok: true` and builds `derivedProjection` from `input.levEngineSubstrateDigest` when, and only when:
- `threeEngineValidation.ok && engineSubstrateValidation.ok` (self-consistency of the envelope/digest OBJECTS), and
- `input.levEngineSubstrateDigest` is present.

It then calls `buildGraphSubstrateDerivedProjection({ digest: input.levEngineSubstrateDigest, ... })` (line 1672-1677) and returns the projection. It NEVER calls `validateRealRunnerObligationBindings` and NEVER binds the obligation's declared `sourceHashes`/`inputHash`/`sourceRefs` to any host-executed receipt.

**Contrast — the good runner:** `createRealThreeEngineObligationRunner` (`claim-gate-wave-runner.ts:1204`), graph-substrate branch (`:1219-1251`), (a) calls `buildEngineSubstrateDigest()` — a real host execution — then (b) calls `validateRealRunnerObligationBindings({ obligation, receipts: hostEngineReceiptsFromSubstrateDigest(artifacts.digest) })` (`:1221-1224`) and fails closed on any finding. That binding (`claim-gate-wave-runner.ts:301-333`) diffs the obligation's declared `sourceRefs`/`sourceHashes`/`inputHash` against the host-executed lane receipts, and `real-three-engine-envelope.ts` disk-anchors those receipts via `readFileSync` of the Lev-owned carrier scripts against expected source hashes.

**Why projection-binding self-consistency is insufficient:** `threeEngineValidation`/`engineSubstrateValidation` are `EnvelopeValidationResult`s from the `projection-binding.ts` validators (`~:562-877`). They check the digest/envelope object is internally coherent (hashes match their own contents, witness receipts present) — but contain NO `readFileSync`/`spawnSync`. A digest whose internal hashes are self-consistent over FABRICATED numbers passes them. And the digest arrives as `input.levEngineSubstrateDigest` — trusted as provided. So the wizard runner's trust rests on "the caller handed me a self-consistent digest," not "this digest came from executing the real Lev-owned carriers." Same trust-shape as the original Blocker A, different runner.

**Not CLI-exploitable today (state it, don't hide it):** on the `demo` path the digest is genuinely host-executed — `handlers/lev-wizard-ratchet.ts:471` sets `levEngineSubstrateDigest: engineArtifacts.digest`, and there is no CLI flag to inject a raw digest. So this is a STRUCTURAL gap in the gate, not a live CLI exploit. It matters because the gate would accept a forged digest if one reached this runner via any non-demo caller (library call, future flag, a different producer).

## 2. Minimal failing test

**Where:** `core/orchestration/src/proof/lev-wizard-ratchet.test.ts` (co-located with the runner).

**Fixture shape:** construct the runner via `wizardThreeEngineObligationRunner(input, threeEngineValidation, engineSubstrateValidation)` where:
- `input.levEngineSubstrateDigest` = a SELF-CONSISTENT but FORGED digest: internal hashes correct (so `engineSubstrateValidation.ok === true`), but the graphInvariants are fabricated (e.g. `juliaAlgebraicConnectivity: 999`) and its lane receipts carry `sourceHash`es that do NOT match the real carrier script bytes on disk.
- the obligation's declared `sourceHashes`/`inputHash` set to match the forged digest's receipts (so a naive declared-vs-digest check would pass) — this is what forces the fix to disk-anchor, not just self-bind.

**Expected fail condition (asserts the DESIRED post-fix behavior — currently fails/red because the code lets it through):**
- runner returns `ok: false` with a finding that the digest's source hashes do not match the on-disk Lev-owned carrier scripts (or that no host-execution receipt anchors the digest), and
- the projection is NOT built.

**What currently passes but should not:** the forged self-consistent digest above currently yields `ok: true` + a derived projection (connectivity 999) — verify by running the fixture against HEAD before the fix and showing `ok: true`.

**Positive control (must keep passing):** the real `demo --real-engines` digest (from a genuine execution) still yields `ok: true` and a projection with the real invariants `2 / [6,4,6,4] / [2,2,2,2]`.

## 3. Minimal patch design

Reuse the EXISTING disk-anchored machinery — do not invent a parallel trust mechanism.

- **Export** `validateRealRunnerObligationBindings` (`claim-gate-wave-runner.ts:301`) and `hostEngineReceiptsFromSubstrateDigest` (`:260`) — currently module-private — so the wizard runner can reuse them.
- In `wizardThreeEngineObligationRunner`, before building the projection, add the same binding + anchoring the good runner has. Two levels; do BOTH:
  - **Binding (necessary):** destructure `{ obligation, obligationHash }` (the callback currently takes only `obligationHash`), and call `validateRealRunnerObligationBindings({ obligation, receipts: hostEngineReceiptsFromSubstrateDigest(input.levEngineSubstrateDigest) })`; return `ok: false` on any finding.
  - **Disk-anchor (the actual A-prime fix):** verify the digest's lane `sourceHash`es equal `readFileSync`+sha256 of the real Lev-owned carrier scripts, reusing the expected-source-hash check already in `real-three-engine-envelope.ts` (the same mechanism `resolveEngineCarrierForRuntime` / the `LEV_NATIVE_*_SOURCE_SHA256` pins use). This is what makes a fabricated-but-self-consistent digest fail. Binding alone does not (a forger can match declared hashes to their own forged receipts).
- Tradeoff to decide (Codex's call): disk-anchoring the SOURCE hashes proves the digest names the real scripts but not that the numbers were actually computed by them; the only thing that anchors the OUTPUT is re-execution (`buildEngineSubstrateDigest()`), which the `demo` path already does upstream at `handlers/lev-wizard-ratchet.ts:471`. Preferred path: thread the host-execution receipts already produced at :471 into the runner and bind against THOSE, rather than re-executing inside the runner.
- **Constraints (do not violate):** keep the projection non-authoritative — `promotionAllowed`/`graphMutationApplied`/`memoryPromotionApplied` stay hardcoded `false` (do not touch `validateDerivedProjection`); NO graph-apply changes; NO new architecture slice.

## 4. File ownership

**Must be edited (Codex-owned hot files — Codex implements, or transfers ownership first):**
- `core/orchestration/src/proof/claim-gate-wave-runner.ts` — export the two binding helpers.
- `core/orchestration/src/proof/lev-wizard-ratchet.ts` — the runner change.
- `core/orchestration/src/proof/lev-wizard-ratchet.test.ts` — the new failing test (+ positive control).
- possibly `core/orchestration/src/handlers/lev-wizard-ratchet.ts` — if threading host receipts from :471.

**Must NOT be edited by this work:** the graph-apply bridge (`consumeClaimGateGraphPatchProposal`/`buildClaimGateGraphPatchApplyPlan`/`recordClaimGateGraphPatchExecution`), `validateDerivedProjection`/the fence flags, the trust ledgers, and the unrelated Claude uncommitted work (graph-event-trust wiring in `proof/claim-gate-loop.ts`, the skill-loader fix in `core/graph`, the a22 test-isolation fix in `claim-gate-redteam-targets.test.ts`).

**Requires Codex to stop first:** YES. `claim-gate-wave-runner.ts` is the active hot seam Codex is editing; a third parallel patch here risks silently dropping the fix. Recommended sequence: Codex implements from this packet → Claude 1 audits in fresh context (forge a self-consistent digest, run the runner, confirm block; confirm real demo still passes; confirm fence flags unchanged; run orchestration targeted tests + typecheck + build).

## Also worth folding into the same Codex pass (from the audit)
- `graphStateScope !== 'not_scoped'` is rejected outright rather than validated in the `50d2e64f3` fix — a coverage gap, additive to close.
- `1c899f776` is a vacuous/mislabeled commit (pure reindent, zero new assertions) — do not count it as coverage.
