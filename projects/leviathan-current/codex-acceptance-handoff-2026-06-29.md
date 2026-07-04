# Lev ClaimGate seam-layer hardening + CR-workload acceptance pilot — Codex handoff (2026-06-29)

## Frame
NOT a Codex Ratchet integration project. This is Lev gate-hardening, with Codex Ratchet as the hard workload that tests whether Lev admits only real evidence. Goal: Lev rejects forged sim/proof receipts and admits ONLY host-issued, content-bound, fresh evidence.

## Audit status — why the current patch is NOT done
The 3-root patch was audited two ways (white-box code-read + black-box 24-attack rerun; both converge). It hardens the CLI front door (A8 case-fold now holds; A2 holds on production call sites) but is SOFT at every importable/consume/witness seam beneath. 19/24 attacks still break. A22 (host-trust) is untouched. The gates are proof-only — not wired into executeTask/dispatchInstruction.
DO NOT land or canonicalize the current patch — it relocates the holes, it does not close them. The deliverable is the seam-layer fix below.

## Unified root
The gate surface is a CONSISTENCY CHECKER, not an evidence verifier — the attacker authors both sides of every cross-reference, so internal consistency proves nothing. The fix is ONE primitive at the SEAM layer: a host-side, non-attacker-controllable root of trust (recompute-from-bytes / re-execute-the-obligation / signed nonce / real spawned engine).

## Step 1 — seam-layer fix (ELIMINATE the anchor; do not guard the call site)
1. Host-owned evidence only: producer/caller input must not supply source-bound context, trusted refs, ok-flags, projections, object bindings, or engine digests as authority.
2. A2: REMOVE `allowEmbeddedNegativeControl` from the exported API (mechanical-probe-runner.ts:128, 479-480). Locking call sites is not enough.
3. A23: make `hostGraphEventTrustIssued` (proof/claim-gate-loop.ts:522, 4105) a host-issued SIGNED token, not a caller-supplied boolean any direct importer sets true.
4. A1: recompute `sourceRefBoundToCommand` (commandBindsSourceRef); do not trust the stored field.
5. A10: content-hash ALL THREE engine lanes vs a host-pinned allowlist — JAX/PyTorch (real-three-engine-envelope.ts:141-198) have no expectedSourceHash; only Julia does.
6. A22 (BIGGEST, UNTOUCHED): `isTrustedReceiptEvidenceRef` (claim-gate-loop.ts:1543) — caller-minted `--host-trusted-evidence-ref` must not confer trust (it is regex + Set.has() with no host issuance/existence check today).
7. A3/A14: consume (claim-gate-steering-run.ts:619-620) must call validateLevEngineSubstrateDigest; a forged digest in boundary.json must not reach host_consumed.
8. A6/A18: freshness/anti-replay — bind evidence to session/nonce/mtime/content (seen-digest rule).
9. WIRE the gates (runMechanicalProbeLane / recordClaimGateGraphPatchExecution / produceClaimGateSteeringRun) into executeTask/dispatchInstruction — they are proof-only now.

## Step 2 — CR→Lev acceptance pilot (the goal-test; doubles as the gate-fix acceptance)
Input: one real CR sim result JSON (or CR-shaped fixture) + its validator command + source/content hash + bounded source files. ONE bounded sim, NOT the whole M(C) program.
Lev must:
1. ingest it as an evidence/source pack;
2. admit it ONLY via host-issued, content-bound, fresh evidence (host re-runs or re-hashes; artifact shape is not evidence);
3. emit a graph proposal;
4. apply graph mutation only after host-consumed admission, into a SANDBOXED test graph/event store (NOT production);
5. write a rerunnable event/receipt.
Negative controls that MUST reject: A3 forged digest in boundary.json; A22 caller-minted `--host-trusted-evidence-ref`; A6 stale/replayed evidence; A10 path-laundered/copied carrier.
PASS = real bounded receipt admitted + all four forgeries rejected + mutation replayable in the test graph + no setup error counted as pass/reject.

## Do not
Broaden into CR integration; run the whole M(C) program; treat artifact shape as evidence; call the patch done from prose; mutate production graph/state for the pilot.

## Deliverable — one landable receipt
changed files; tests added (the 24 attacks + the pilot); exact commands + outputs; attack IDs closed/open; dirty/untracked state; remaining non-CLI/programmatic trust paths; whether land-ready or local-evidence-only.

## ROUND-3 VERDICT (2026-06-29) — STOP the CLI whack-a-mole; fix the ROOT at the validator layer
3 red-team rounds: 16 broke → 19 → 17. Flat, because it is NOT N bugs — it is ONE root cause with ~17 surfaces: Lev's validators are pure structural-consistency functions with NO execution anchor and NO cryptographic secret (all hashes are sha256 over attacker-reachable content; the witness schema has no nonce/session/MAC). substrate digest, probe receipt, carrier guard, seed gate, manifest hash, skill dispatch, trusted refs, witness ledger ALL fall to the same missing anchor.
DUAL-LAYER (both true): the CLI is meaningfully hardened (old --host-trusted-evidence-ref blocked; forged digest in boundary.json AND nested eval-job.json metadata caught by deep scan; allowEmbeddedNegativeControl dead-code; A4/A5/A7 internal checks hold) — BUT any direct importer of the validators gets a structural-consistency rubber stamp (A1/A2/A21/A24), and the new env-var witness-root is a CLI-reachable break (A3 above).
THE FIX (one change, closes all 17): a MAC/signature with a key OUTSIDE caller control, or a real execution anchor the producer can't reproduce, applied at the CONTRACT/VALIDATOR layer where validateLevEngineSubstrateDigest / validateMechanicalProbeRunReceipt / validateHostExecutionWitness live — NOT another CLI guard. Each round of CLI guards just relocates the forgery to the next door.

## NEW FINDING (2026-06-29, verified by running) — the witness gate relocated, not closed
The host-witness round was audited live. The witness is now REQUIRED (control: no witness → host_blocked, good — closes A12/A14 "bare projection passes"). BUT it is FORGEABLE:
- `buildClaimGateHostExecutionWitnessForRun` (claim-gate-steering-run.ts:496) is EXPORTED and builds a valid witness from the run dir alone — NO host secret.
- consume reads the witness from a ledger at `LEV_CLAIMGATE_HOST_WITNESS_ROOT` (line 225) — a CALLER-SETTABLE path.
- `validateHostExecutionWitness` (558) only checks the witness fields equal the producer-authored projection (runId, IDs, pass/pass, source hashes) — all producer-derivable.
PROVEN: build a witness with the exported builder for a clean pass/pass projection, plant it in a ledger at an attacker-controlled `LEV_CLAIMGATE_HOST_WITNESS_ROOT`, run consume → `host_consumed`, ok:true, 0 findings. Control without the planted witness → `host_blocked`. Same relocation as `--host-trusted-evidence-ref`: producer mints the host's own attestation.
WITNESS FIX (the real one): the witness needs a secret the producer can't reproduce — sign it with a key outside caller/CLI control, OR issue it in-process bound to a host-issued session nonce, AND make the ledger root non-caller-settable. "Build-from-projection + read-from-a-settable-file" has no secret. The witness's own ceiling `host_execution_witness_not_transferable_authority` is correct — so STOP using it as transferable authority until it is signed/host-custody.

Full red-team detail + premortem: `codex-redteam-targets-2026-06-28.md` (POST-FIX AUDIT section in the source scratch copy).
