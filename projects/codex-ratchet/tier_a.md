last_updated: 2026-04-17T08:17:04Z

# Tier A

Historical 2026-04-17 Tier A execution note. Runner-DONE and green-gate claims here are dated evidence only, not current repo readiness, maturity, or promotion status.

Status: gate passed
Gate: green

Scope closed in this batch
- cleanup-first guard resolved to green before Tier A authoring
- orphan canonical downgrade applied (80 files) with reason `orphan_no_source_2026-04-17`
- runner smoke probe succeeded
- A4.5 and A4.6 finished and runner-confirmed
- 6 additional pre-approved capability sims authored and enqueued

Cleanup-first / supervisor evidence
- `system_v4/probes/a2_state/sim_results/system_hygiene_supervisor_results.json`
- observed green checkpoint during this run:
  - `overall_green=True`
  - `repair_queue_count=0`
- `ops/sim_runner.sh` was repaired to use the Makefile interpreter instead of `which python3`; this cleared the earlier cvc5 runner mismatch.

A4 integration evidence
- `tool_integration_toponetx_pyg.py` exists
- `tool_integration_cvc5_sympy.py` exists
- queue / runner evidence in `ops/queue_tier_a.txt`:
  - `# DONE ... tool_integration_toponetx_pyg ...`
  - `# DONE ... tool_integration_cvc5_sympy ...`
- A4 set now present and DONE:
  - z3_sympy
  - sympy_pyg
  - pyg_torch
  - clifford_weyl
  - toponetx_pyg
  - cvc5_sympy

Core Tier A capability evidence
- capability probes present and runner-DONE:
  - `tool_capability_z3.py`
  - `tool_capability_cvc5.py`
  - `tool_capability_sympy.py`
  - `tool_capability_pyg.py`
  - `tool_capability_toponetx.py`
  - `tool_capability_clifford.py`
  - `tool_capability_torch.py`

Overnight extension capability evidence
- additional capability probes present and runner-DONE:
  - `tool_capability_gudhi.py`
  - `tool_capability_torch_ga.py`
  - `tool_capability_qutip.py`
  - `tool_capability_pennylane.py`
  - `tool_capability_cirq.py`
  - `tool_capability_networkx.py`

Queue evidence snapshot
From `ops/queue_tier_a.txt`, the following final DONE rows are present for the requested batch:
- `tool_capability_z3`
- `tool_capability_cvc5`
- `tool_capability_sympy`
- `tool_capability_pyg`
- `tool_capability_toponetx`
- `tool_capability_clifford`
- `tool_capability_torch`
- `tool_integration_z3_sympy`
- `tool_integration_sympy_pyg`
- `tool_integration_pyg_torch`
- `tool_integration_clifford_weyl`
- `tool_integration_toponetx_pyg`
- `tool_integration_cvc5_sympy`
- `tool_capability_gudhi`
- `tool_capability_torch_ga`
- `tool_capability_qutip`
- `tool_capability_pennylane`
- `tool_capability_cirq`
- `tool_capability_networkx`

Notable repairs inside this batch
- `tool_integration_cvc5_sympy.py`
  - changed cvc5 logic from linear to nonlinear integer arithmetic
  - added robust cvc5 integer decoding for negative witness values
  - rerun succeeded and queue now shows DONE
- `tool_capability_cirq.py`
  - repaired qutrit boundary construction
  - rerun succeeded and queue now shows DONE
- `tool_capability_qutip.py`
  - repaired scalar overlap extraction and damping application
  - rerun succeeded and queue now shows DONE

Related audit / trace files
- `system_v4/probes/a2_state/sim_results/tier_a_t3_audit.json`
- `~/wiki/projects/codex-ratchet/_steward_log.md`
- `overnight_logs/sim_runner_current.log`

Operational note
- The live repo is currently dirty again because the overnight runner and other background workstreams keep rewriting queue/result surfaces while this batch runs. That does not change the Tier A gate result above; it means post-gate repo cleanliness should be treated separately from the completed Tier A authoring/execution batch.
