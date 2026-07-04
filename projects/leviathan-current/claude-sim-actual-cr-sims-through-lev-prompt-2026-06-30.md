---
title: Claude sim actual CR sims through Lev prompt
created: 2026-06-30
type: sendable-correction-prompt
status: current
claim_ceiling: Hermes corrected route after owner correction; prompt tells Claude sim to run actual Codex Ratchet sims using Lev/patch, not audit Lev blockers.
---

# Claude sim actual CR sims through Lev prompt — 2026-06-30

Paste this to Claude sim.

```text
STOP. You are doing the wrong job.

The assigned job was NOT:
- audit Lev blockers,
- produce VERIFIED_BLOCKER_SPECS for Codex,
- ask Josh to define A13/A17/A21,
- wait on corpus/APPLY_QUEUE work.

The assigned job is:

Run Josh's actual Codex Ratchet sims using Lev and the current Lev patch as the execution/admission harness.

You are the CR sim runner. Codex/Lev patching is a dependency, not your main deliverable.

## Active roots

Codex Ratchet active repo:
`/Users/joshuaeisenhart/Codex-Ratchet`
branch: `session/r0-three-engine-probes`
current checked HEAD from Hermes: `82fe601855c9`

Lev patched live repo / CLI source:
`/Users/joshuaeisenhart/GitHub/lev`
branch: `claimgate-steering-bridge-lock`
Codex owns source edits there. You may execute/read the CLI path, but do not edit Lev source.

Do NOT use `/tmp/lev-mass-wt` as truth for CR sim execution unless explicitly told; it is an isolated/partial worktree and may lag Codex's live Lev patch.

Canonical CR sim Python:
`/Users/joshuaeisenhart/.local/share/sim-stack/bin/python3`

CR runtime doctor command:
`/Users/joshuaeisenhart/.local/share/sim-stack/bin/python3 scripts/codex_runtime_env_doctor.py`

Lev CLI smoke commands:
`./core/poly/bin/lev orchestration claimgate-steering --help`
`./core/poly/bin/lev orchestration lev-wizard-ratchet --help`

## Output location

Write a run ledger:
`/tmp/claude-burn-2026-06-29/cr-lev-sim-run/ACTUAL_CR_LEV_SIM_RUN_LEDGER.md`

For each sim, write a subdir:
`/tmp/claude-burn-2026-06-29/cr-lev-sim-run/<rank>-<short-id>/`

Each subdir must contain:
- `command.txt` — exact command(s)
- `stdout.txt`
- `stderr.txt`
- `result-copy.json` or path pointer to the fresh result JSON
- `codex-sim-runner-receipt.json` if `scripts/codex_sim_runner.py` is used
- `lev-claimgate-produce.json` if Lev produce is used
- `lev-claimgate-consume.json` if Lev consume is used
- `classification.md` with status labels

Status labels must be exact:
`exists`, `runs`, `passes local rerun`, `lev-produced`, `lev-consumed`, `host_blocked`, `failed`, `blocked`.

Do not say `admitted`, `canonical`, or `done` unless a current checked gate actually says that.

## Required pilot queue

Use the active CR readiness matrix as source:
`/tmp/claude-burn-2026-06-29/cr-active/CR_READY_FOR_LEV_MATRIX.md`

Run the top pilot set fresh. Start with these 10 unless one is blocked by missing command shape:

1. `system_v5/legos/finite_density_matrix_carrier_trace_psd_pytorch_sympy_z3.py`
2. `system_v5/legos/density_operator_cptp_amplitude_damping_trace_psd_pytorch_sympy_z3.py`
3. `system_v7/sims/probe_quotient_fingerprint_floor_v1/probe_quotient_fingerprint_floor_v1_jax.py` plus its Julia peer if required by existing runner/admission packet
4. `system_v5/legos/weyl_spinor_chirality_hamiltonian_sign_expectation_clifford_pytorch_z3.py`
5. `system_v5/legos/pauli_clifford_commutator_representation_gap_clifford_sympy_z3.py`
6. `system_v5/legos/signed_conditional_and_coherent_information_negative_entropy_pytorch_sympy_z3.py`
7. `system_v5/legos/coherent_information_parameter_gradient_two_qubit_mixture_pytorch_autograd_z3.py`
8. `system_v5/legos/spectral_entropy_family_density_state_pytorch_sympy_z3.py`
9. `system_v5/legos/two_point_spectral_triple_dirac_commutator_distance_pytorch_sympy_z3.py`
10. `system_v5/ops/formal_scouts/sim_rosetta_igt_qit_four_element_structure_probe.py`

If a listed sim needs a repo-local runner rather than direct Python, use that runner, but record the command. Do not replace the pilot set with a Lev blocker audit.

## Execution method

### Step 0 — preflight

Run in CR:
`/Users/joshuaeisenhart/.local/share/sim-stack/bin/python3 scripts/codex_runtime_env_doctor.py`

Run in Lev:
`./core/poly/bin/lev orchestration claimgate-steering --help`
`./core/poly/bin/lev orchestration lev-wizard-ratchet --help`

Record outputs in the ledger. If either preflight fails, report the exact blocker and still run any CR sims that do not depend on that failing component.

### Step 1 — run actual CR sims

Use bounded concurrency, max 3 sim jobs at once. These are real sim reruns, not read-only source audits.

Preferred wrapper for single Python sims:

`/Users/joshuaeisenhart/.local/share/sim-stack/bin/python3 scripts/codex_sim_runner.py --sim-path <sim-path> --python /Users/joshuaeisenhart/.local/share/sim-stack/bin/python3 --receipt-dir /tmp/claude-burn-2026-06-29/cr-lev-sim-run/<rank>-<short-id> --timeout 300 --stage-claim scratch_diagnostic --formal-stage pilot_rerun --tool-target lev_pilot`

If `codex_sim_runner.py` is not appropriate for a specific sim, run the sim directly with the canonical Python and record why.

For the v7 three-engine candidate, run the existing JAX + Julia legs or the repo's existing three-engine runner if present. Validate with:
`/Users/joshuaeisenhart/.local/share/sim-stack/bin/python3 scripts/validate_three_engine_sim_result.py <result-json>`

For formal scout #10, validate with:
`/Users/joshuaeisenhart/.local/share/sim-stack/bin/python3 system_v5/ops/formal_scouts/validate_formal_scout_results.py <result-json>`

### Step 2 — pass sim outputs through Lev/patch

For each sim that produces a fresh result/receipt, attempt a Lev ClaimGate projection/consume path. The point is to test the CR sim as a Lev workload, not to patch Lev.

Use Lev CLI from:
`/Users/joshuaeisenhart/GitHub/lev`

Create an exec-spec JSON per sim under the sim's run subdir. It must cite:
- CR sim path
- result JSON path / receipt path
- sha256 of result JSON if easy to compute
- claim ceiling (`scratch_diagnostic` / `candidate`, not canonical)
- obligations that were actually checked, not fake ones

Then run:
`./core/poly/bin/lev orchestration claimgate-steering produce <exec-spec.json> --out /tmp/claude-burn-2026-06-29/cr-lev-sim-run/lev-runs --json`

Then run:
`./core/poly/bin/lev orchestration claimgate-steering consume <produced-run-dir> --json --no-write`

If Lev returns `host_blocked`, that is still a valid result. Record the finding codes. Do not smooth it into failure or success.

If current Lev cannot consume CR sim paths because the patch does not yet support host context or target-file binding, write that as the exact Lev/patch blocker while preserving the CR sim rerun result.

### Step 3 — ledger and summary

The final ledger must answer:

1. Which CR sims actually ran?
2. Which produced fresh result JSONs or receipts?
3. Which passed their local CR validators?
4. Which were successfully wrapped by Lev produce?
5. Which were consumed by Lev, and with what status (`host_consumed`, `host_blocked`, etc.)?
6. Which Lev/patch seams blocked actual CR sim ingestion?
7. Which sims should Codex patch/run next?

## Do not do these

- Do not produce more Lev blocker specs instead of running CR sims.
- Do not ask Josh to define A13/A17/A21 before running the actual pilot sims.
- Do not wait for the corpus proposal wave.
- Do not edit Lev source.
- Do not edit CR source unless the sim itself writes result files as part of the run; if it does, copy before/after and label the dirty delta.
- Do not claim admission/canonical status.

## Final response format

Return:

`Actual CR sims run:`
- list rank, sim path, command, exit code, result path, local status

`Lev/patch harness result:`
- per sim: produced? consumed? status? finding codes?

`Artifacts:`
- ledger path and subdir paths

`Blocked:`
- exact missing runtime/Lev patch blocker, if any

`Next:`
- the smallest next real sim wave or exact Lev patch needed to ingest the sim outputs
```
