---
title: Lev-lane packet — --real-engines runner is R0-locked; generalization spec
created: 2026-06-30
type: sendable-lev-lane-blocker-and-spec
status: current
claim_ceiling: >
  Lev-lane blocker/spec only. NOT implementation. NOT CR admission evidence.
  NOT a claim that Lev currently mechanically verifies R1-R3. This packet preserves a
  finding and hands a generalization spec to the Lev lane; it changes nothing on disk.
---

# Lev-lane packet — Leviathan `--real-engines` runner is R0-locked

Paste this to the Lev-lane / Leviathan patch worker. Not for the CR scaled-ratchet lane.

Provenance: found by the CR-lane carrier-override integration probe (workflow `wf_b6f41da9-2e6`, 2026-06-30). Two fresh-context probes built relocatable carrier adapters outside both trees and drove `lev orchestration lev-wizard-ratchet demo --json --real-engines` with `LEV_SIM_ENGINE_CARRIER` set. Both returned `RUNNER_IS_R0_LOCKED`.

## 1. Verdict

- `RUNNER_IS_R0_LOCKED`.
- Lev `--real-engines` verifies its own pinned R0 mirror only.
- CR rungs (R0 included as CR's actual bytes, and R1-R3) currently get Lev **bookkeeping**, not byte-exact mechanical Lev admission.
- The `LEV_SIM_ENGINE_CARRIER` override cannot point Lev at CR sims: both probes threw at carrier resolution before any engine spawned.

## 2. Evidence

- Carrier-root guard: `resolveEngineCarrierForRuntime()` in `core/orchestration/src/proof/real-three-engine-envelope.ts` (lines ~74-95) throws synchronously if the override path is outside the Lev-owned root. Exact error: `LEV_SIM_ENGINE_CARRIER points outside the Lev-owned runtime carrier root (.../lev-sim-engine-carrier/r0-quotient); copied or path-laundered carriers are not runtime authority.` Exit 1, no output file, no `threeEngineReceiptManifest`, no `runtimeCarrier`.
- Source-hash pin: `validateLevNativeR0QuotientProbeReceipt()` in `core/orchestration/src/proof/lev-native-r0-probe.ts` pins `receipt.sourceHash` to `sha256:00a678ce…a785f6a3` (Lev's own mirror). A second, independent guard: even if the carrier-root guard were bypassed, this pin rejects CR's bytes.
- Hash distinction: CR's actual R0 Julia file (`~/Codex-Ratchet/system_v5/julia_carrier/foundation_r0_probe_quotient_refinement_julia.jl`) hashes `sha256:7104a9b0…fe935af8`. Lev's mirror pins `00a678ce…a785f6a3`. Different files; the pin is mirror-only.
- R1 probe: never reached `buildRealThreeEngineEnvelope()`; `runMechanicalProbeLane` never fired; no subprocess launched; `r1-out.json` never created. Failed at the same R0-locked carrier root. The downstream semantic checks (`juliaPinnedR0Receipt`, `jaxPrimaryR0QuotientRefinement`, `pytorch…QuotientRefinement`, the `duplicate_Z_does_not_refine` control) are all R0-specific, so R1 could not pass them even if resolution were reached.

## 3. Truth labels (use these, do not inflate)

- Fleet re-run + adversary (fresh-context Claude agents re-executing the sim and hunting by-construction) = the ACTUAL current admission gate for CR rungs. R0-R3 stand at `passes local rerun` on this basis.
- `claimgate-steering produce/consume` = bookkeeping only. It over-accepts per the ATTACK-1 / evidenceRefs gap (consume never re-hashes or re-runs the underlying result JSON; see `thread-b-steering-projection-seal-finding-2026-06-30.md`). A `host_consumed` there is not mechanical admission.
- `lev-wizard-ratchet --real-engines` = valid mechanical builder-blind receipt for the Lev-owned R0 mirror ONLY. It is not a receipt over any CR rung's actual bytes.

## 4. Generalization spec (make the rung data, not code)

Required for Lev to mechanically verify arbitrary rungs:

- Parameterized carrier subroot: a rung id selects a Lev-owned carrier subdirectory, instead of the hardcoded `r0-quotient` root literal in `resolveEngineCarrierForRuntime()`.
- Per-rung `sourceHash`: expected source hash read from a per-rung manifest, not the single R0 literal in `validateLevNativeR0QuotientProbeReceipt()`.
- Per-rung semantic checks: keyed by rung id, so R1 (F01 finitude) validates its own invariants (quotient refinement + order-gap witnesses) rather than R0 quotient-refinement checks.
- Carrier-declared negative control: each rung's carrier declares an input it MUST reject, so the gate proves it can fail, not just pass. (R0's is `duplicate_Z_does_not_refine`.)
- Explicit byte/source anchoring kept intact: keep the carrier-root and source-hash guards; only make their expected values rung-parameterized. Bytes for each rung must still be Lev-owned and pinned.
- No CR-as-runtime-library shortcut: do NOT resolve the override to the live CR tree. Lev owns the carrier; sync it deliberately, hash-pin it.
- No memory / spinor / projection / graph-patch as proof: the mechanical receipt is the engine execution over pinned bytes, nothing softer.

## 5. Next owner and gate

- Owner: Lev lane, not the CR scaled-ratchet lane.
- Do NOT implement while the CR scaled ratchet is active; no contention.
- After the runner is generalized, a later audit must prove R1/R2/R3 with REAL engine receipts (per-rung pinned bytes, per-rung semantic checks, negative control that actually fails) BEFORE any rung is called "Lev-admitted." Until then, R0-R3 are `passes local rerun` via fleet re-run, with Lev as bookkeeping.

## Do-not list

- Do not edit Lev source or CR source from this packet.
- Do not claim canonical. Claim ceiling: `Lev-lane blocker/spec; not implementation; not CR admission evidence`.
