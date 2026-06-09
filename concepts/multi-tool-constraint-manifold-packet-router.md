---
type: concept
created: 2026-05-18
updated: 2026-05-18
tags: [simulation, tools, constraint-manifold, z3, topology, optimization, evidence]
sources:
  - /tmp/max_stack_constraint_manifold_5tools_read_20260518.json
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/sim_max_stack_constraint_manifold_5tools.py
---

# Multi-Tool Constraint Manifold Packet Router

## Purpose
This page routes `sim_max_stack_constraint_manifold_5tools.py` into the wiki as a multi-tool constraint-manifold packet.

The useful kernel:

A constraint manifold claim becomes stronger when separate tools perform separate jobs: generated search, formal admission/exclusion, topology over survivors, optimization over tradeoffs, and family clustering.

## Source surface
Read artifact:
- `/tmp/max_stack_constraint_manifold_5tools_read_20260518.json`

Repo file:
- `system_v4/probes/sim_max_stack_constraint_manifold_5tools.py`

## Claim shape
The source claims that a distinguishability-constraint manifold admits a structured population of probe states that:
- survive Z3 checks per individual constraint;
- form a point cloud with non-trivial persistent homology;
- trade off topological complexity and constraint cost;
- cluster into candidate Rosetta families.

## Tool-role split
The packet is useful because each tool has a different job.

| Tool / lane | Intended role | Claim support |
|---|---|---|
| Hypothesis-style generation | creates candidate state pressure | wide exploration, not proof |
| Z3 | admits/excludes states under constraint encoding | formal local gate |
| GUDHI / Vietoris-Rips | checks topology of admitted point cloud | topology witness, if data supports it |
| pymoo / NSGA-II | searches Pareto tradeoffs | optimization witness, not theorem |
| datasketch / LSH | clusters survivor families | family-routing signal |

## Relation to current wiki lanes
- [[hypothesis-z3-property-guard-router]] covers the smaller two-tool ladder.
- [[topology-carrier-tool-lane]] covers topology witnesses and their fences.
- [[repo-tool-use-router]] keeps mention/call/supportive/load-bearing/canonical status separate.
- [[sim-math-geometry-result-surface-router]] routes result surfaces without promoting them.
- [[mass-sim-generator-wide-exploration-support]] provides the generation/ledger discipline.

## Overclaim fences
Do not say:
- five tools means canonical truth;
- persistent homology alone proves the manifold;
- Pareto fronts prove physical relevance;
- clustering proves semantic families;
- Z3 admission over one encoding proves the whole system.

Safer language:
- multi-tool packet;
- constraint-manifold candidate surface;
- topology witness over admitted cloud;
- Pareto tradeoff witness;
- Rosetta-candidate family routing;
- load-bearing only where the tool changes admission, exclusion, topology, optimization, or clustering.

## Claim ceiling
This router should preserve the source as a packet-level evidence surface, not promote it by prose.

Before stronger language, require:
- current rerun status;
- result JSON path;
- tool manifest depth;
- classification field;
- divergence log if classical baseline;
- exact role for each used tool;
- whether all five tools remained load-bearing or some fell to supportive.


## 2026-05-18 result-status addendum
Search artifact:
- `/tmp/max_stack_constraint_manifold_result_search_20260518.json`

Observed state:
- source probe found: `system_v4/probes/sim_max_stack_constraint_manifold_5tools.py`
- matching result JSON: not found in the result search
- related max-stack probe files found, but no verified result artifact for this exact packet was located in this tranche

Status implication:
- this page remains a source/probe router, not a result-promotion page;
- the claim ceiling stays at “packet exists / source inspected” until a result JSON is located or the probe is rerun under the current runner contract;
- do not use the page to claim canonical status or pass status.

Next admissible step:
- rerun or locate the exact result artifact for `sim_max_stack_constraint_manifold_5tools.py`;
- record classification, tool manifest, tool integration depth, divergence log, and result path;
- then patch this page with the verified result status.

## MMM sentences
- A tool is load-bearing only where removing it changes the admissible shape.
- Z3 draws local gates; topology reads the survivor cloud.
- Pareto fronts are tradeoff witnesses, not destiny.
- Clusters route families; they do not name essences.
- Five tools are useful only if they disagree in useful ways.

## Next verification target
Inspect the actual result artifact for this sim, if present, and create a result-status addendum with:
- classification;
- pass/fail status;
- tool integration depth;
- tool manifest roles;
- output/result path;
- any downgrade from canonical to supportive.

## Related pages
- [[max-stack-probe-variants-status-router]]
- [[hypothesis-z3-property-guard-router]]
- [[property-fuzz-metamorphic-testing-support]]
- [[repo-tool-use-router]]
- [[topology-carrier-tool-lane]]
- [[sim-math-geometry-result-surface-router]]
- [[mass-sim-generator-wide-exploration-support]]
- [[negative-sims-and-kill-tests-support]]
