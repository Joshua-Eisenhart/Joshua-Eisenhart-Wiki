---
type: concept
created: 2026-05-18
updated: 2026-05-18
tags: [simulation, tools, max-stack, z3, topology, noncommutation, evidence]
sources:
  - /tmp/max_stack_probe_variants_read_20260518.json
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/sim_max_stack_5tool_constraint_admissibility.py
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/sim_max_stack_gtower_ratchet_6tools.py
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/sim_max_stack_6tool_gtower_ratchet.py
---

# Max-Stack Probe Variants Status Router

## Purpose
This page routes the related max-stack probe variants that sit near [[multi-tool-constraint-manifold-packet-router]].

It keeps two things separate:
- source/probe claims visible in the Python files;
- current result status, which was not found for these variants in this tranche.

Read artifact:
- `/tmp/max_stack_probe_variants_read_20260518.json`

## Variants inspected

| Probe | Kernel | Tool stack | Source claim ceiling | Result status found |
|---|---|---|---|---|
| `sim_max_stack_5tool_constraint_admissibility.py` | distinguishability constraint manifold; admitted/excluded `(p,q)` states; topology, Pareto, clustering over admitted cloud | Hypothesis, Z3, GUDHI, pymoo, datasketch | source claims all 5 tools load-bearing | no matching result JSON found |
| `sim_max_stack_gtower_ratchet_6tools.py` | G-tower noncommutative ratchet; GL(n)→O(n)→SO(n)→SU(n); reversed-order witness excluded | Clifford/numpy, Sympy, Z3, e3nn, RIBS, Optuna | source claims canonical | no matching result JSON found |
| `sim_max_stack_6tool_gtower_ratchet.py` | rotor noncommutation; BCH commutator; Z3 UNSAT for forced commutativity; SO(3) equivariance; archive and optimization | Clifford, Sympy, Z3, e3nn, RIBS, Optuna | source claims canonical / all 6 load-bearing | no matching result JSON found |

## Interpretation
These files are high-value source/probe surfaces because they show concrete multi-tool role separation.

They are not, by this page alone, current rerun-backed result surfaces.

The clean claim is:
- the repo contains max-stack probe designs for constraint manifolds and G-tower noncommutation;
- their source text states explicit positive, negative, and boundary tests;
- no matching result JSON was found in the current search tranche;
- therefore the wiki should route them as source/probe candidates until rerun evidence or result artifacts are found.

## Why they matter
The variants cover two important families.

### Constraint-manifold family
This supports:
- [[hypothesis-z3-property-guard-router]]
- [[topology-carrier-tool-lane]]
- [[mass-sim-generator-wide-exploration-support]]

It is the pattern:
- generate candidate states;
- formally exclude illegal states;
- read topology over survivors;
- optimize tradeoffs;
- cluster candidate families.

### G-tower / noncommutation family
This supports:
- noncommutation as a root constraint;
- BCH/commutator as symbolic obstruction;
- Z3 as a formal impossibility check;
- equivariance as a preservation check;
- archive/optimization tools as search and coverage surfaces.

It is the pattern:
- order matters;
- reversed order cannot be silently swapped;
- identity/near-identity cases are boundary/negative controls;
- noncommutation should be measured, symbolized, formally checked, and searched.

## Overclaim fences
Do not say:
- source `classification: canonical` equals current canonical result;
- all tools are load-bearing unless the result manifest confirms it;
- no result JSON means the source is false;
- multi-tool design equals current evidence completion.

Safer language:
- source/probe variant;
- design-level tool stack;
- result status not found in this tranche;
- rerun or result-location required before promotion.

## Next admissible work
1. Locate any hidden/noncanonical output directories for these probes.
2. If missing, run the smallest admissible probe under the current runner contract.
3. Record classification, result path, tool manifest, and tool integration depth.
4. Patch this router with verified result status only after that evidence exists.

## Related pages
- [[multi-tool-constraint-manifold-packet-router]]
- [[hypothesis-z3-property-guard-router]]
- [[repo-tool-use-router]]
- [[topology-carrier-tool-lane]]
- [[sim-math-geometry-result-surface-router]]
- [[negative-sims-and-kill-tests-support]]
