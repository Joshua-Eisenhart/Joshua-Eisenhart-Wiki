---
title: IGT Atom Result Audit
created: 2026-04-15
updated: 2026-05-21
type: concept
tags: [igt, simulation, audit, results, routing]
sources:
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/sim_igt_atom_1_carrier.py
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/sim_igt_atom_2_structure.py
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/sim_igt_atom_3_reduction.py
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/sim_igt_atom_4_admissibility.py
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/sim_igt_atom_5_distinguishability.py
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/sim_igt_atom_6_chirality.py
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/sim_igt_atom_7_coupling.py
missing_result_receipts:
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_igt_atom_1_carrier_results.json
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_igt_atom_2_structure_results.json
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_igt_atom_3_reduction_results.json
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_igt_atom_4_admissibility_results.json
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_igt_atom_5_distinguishability_results.json
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_igt_atom_6_chirality_results.json
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_igt_atom_7_coupling_results.json
framing: source_present_result_missing_snapshot
---

# IGT Atom Result Audit

## Role in the live wiki cluster
- Strongest use: compact source-facing audit for the IGT atom chain and its nearest follow-on artifact names.
- Weak use: front-door doctrine page, substitute for a local rerun, or proof that any IGT lane is `canonical by process`.
- Authority boundary: this page is now a source-present/result-missing snapshot. It preserves the atom-chain shape, but the old exact result JSON names are missing in this checkout and do not promote any sim above source-present until relinked or rerun.

## Audit scope
This pass directly read:
- the atom-chain sim files `sim_igt_atom_1_carrier.py` through `sim_igt_atom_7_coupling.py`
- a small adjacent follow-on set: `sim_igt_win_lose_atomic`, `sim_igt_nested_WIN_LOSE_attractor`, `igt_deep_nested_win_lose_irreducibility`, `sim_igt_yin_yang_ansatz`, `sim_igt_nested_yin_yang_IGT_equivalence`, and `sim_igt_two_pattern_uniqueness`

No local rerun was performed in this audit. The old matching result receipt names in `system_v4/probes/a2_state/sim_results/` were not found at their cited paths. The safe status label here is therefore source-present / result-link-missing.

## Atom-chain artifact inventory

| Atom | Sim file | What the sim claims to cover | Old result artifact name | Current receipt status | Safe status label |
|---|---|---|---|---|---|
| 1 | `sim_igt_atom_1_carrier.py` | 4-element carrier set `{win,lose} x {WIN,LOSE}` | `sim_igt_atom_1_carrier_results.json` | missing at old exact path | source-present |
| 2 | `sim_igt_atom_2_structure.py` | Hamming-1 4-ring / yin-yang square structure | `sim_igt_atom_2_structure_results.json` | missing at old exact path | source-present |
| 3 | `sim_igt_atom_3_reduction.py` | lossy 2-to-1 inner/outer reductions | `sim_igt_atom_3_reduction_results.json` | missing at old exact path | source-present |
| 4 | `sim_igt_atom_4_admissibility.py` | long-run admissibility filter on the outer axis | `sim_igt_atom_4_admissibility_results.json` | missing at old exact path | source-present |
| 5 | `sim_igt_atom_5_distinguishability.py` | partial probes collapse some pairs; only full probe separates all four | `sim_igt_atom_5_distinguishability_results.json` | missing at old exact path | source-present |
| 6 | `sim_igt_atom_6_chirality.py` | two ring orientations and chirality / handedness split | `sim_igt_atom_6_chirality_results.json` | missing at old exact path | source-present |
| 7 | `sim_igt_atom_7_coupling.py` | 16-state product space and 4-state admissible sub-ring under coupling | `sim_igt_atom_7_coupling_results.json` | missing at old exact path | source-present |

## What this audit safely shows
- The IGT atom chain is not merely planned; all seven atom sim files exist on disk.
- The queue shorthand had drifted: the actual atom series is `carrier`, `structure`, `reduction`, `admissibility`, `distinguishability`, `chirality`, `coupling`, not the older placeholder names.
- The old matching result JSON names are missing in this checkout, so prior aggregate pass-field claims must not be reused without exact receipt recovery.
- The strongest honest next move is receipt recovery or rerun/validation on the atom chain, not more symbolic notes.

## Adjacent follow-on artifacts

| Follow-on lane | Old result artifact name | Current receipt status | Safe status label |
|---|---|---|---|
| atomic win/lose round | `sim_igt_win_lose_atomic_results.json` | not re-linked in this pass | result-link-unverified |
| nested WIN/LOSE attractor | `sim_igt_nested_WIN_LOSE_attractor_results.json` | not re-linked in this pass | result-link-unverified |
| deep nested irreducibility | `igt_deep_nested_win_lose_irreducibility_results.json` | not re-linked in this pass | result-link-unverified |
| minimal yin/yang ansatz | `sim_igt_yin_yang_ansatz_results.json` | not re-linked in this pass | result-link-unverified |
| nested yin/yang equivalence | `sim_igt_nested_yin_yang_IGT_equivalence_results.json` | not re-linked in this pass | result-link-unverified |
| two-pattern uniqueness | `sim_igt_two_pattern_uniqueness_results.json` | not re-linked in this pass | result-link-unverified |

## Honesty fence
- This page does not claim any of the above sims `pass local rerun` in the current session.
- It does not claim that any missing or prior result file labeled `canonical` is therefore `canonical by process`.
- It does not claim convergence between the IGT lane and QIT engine doctrine. It only preserves the source-chain shape and old result names until exact current receipts are recovered.

## Practical interpretation
The biggest wiki gap in this lane is now source/result separation: the atom-chain source files are present, the old result names are recorded, and the exact current receipts still need recovery or rerun before artifact-side pass fields can be used.

## Next bounded follow-up
Run the seven-atom chain under the repo interpreter from `Makefile`:
- `/Users/joshuaeisenhart/.local/share/codex-ratchet/envs/main/bin/python3`

Then update this page from source-present/result-missing status to rerun-backed status labels where earned.

## Related pages
- [[igt-to-qit-engine-genealogy]]
- [[taijitu-probe-reconciliation-card]]
- [[jungian-functions-and-igt-explicit-math-geometry-map]]
- [[axis-and-entropy-reference]]
