---
title: Tri-Engine Rich-Tool Sim Contract Failure and Rebuild 2026-06-07
created: 2026-06-07
type: project-audit-rebuild-router
status: active-rebuild-gate
claim_ceiling: process/tooling correction and rebuild routing only; no sim admission
framing: codex-ratchet
---

# Tri-Engine Rich-Tool Sim Contract Failure and Rebuild 2026-06-07

## Boot rule

Load this before accepting any Codex Ratchet claim that depends on Julia/JAX/PyTorch backend parity, rich tool use, foundation rungs, `M(C)`, carrier/geometry, QIT, Clifford/spinor/Hopf, tensor networks, dynamics, graph/topology, or proof-tool evidence.

Also load the Hermes skill:

```text
codex-ratchet-tri-engine-rich-tool-contract
```

## What failed

The observed failure is not that the earlier scripts were fabricated. The failure is that the scripts used the right engine names while mostly not using the rich package ecosystems that were supposed to make those engines meaningful.

Unsafe promotion pattern:

```text
JAX side: jax + jax.numpy only
Julia side: LinearAlgebra + JSON + Dates only
parity: same hand-rolled algorithm or peer result JSON
```

This is not a proper Julia/JAX rich-tool sim. It is a bare-engine scratch diagnostic unless a separate gate proves otherwise.

## Current checked example

Observed files:

```text
/Users/joshuaeisenhart/Codex-Ratchet/system_v5/ops/formal_scouts/sim_foundation_rung0to3_distinguishability_probe.py
/Users/joshuaeisenhart/Codex-Ratchet/system_v5/julia_carrier/foundation_rung0to3_distinguishability.jl
/Users/joshuaeisenhart/Codex-Ratchet/system_v5/ops/formal_scouts/results/foundation_rung0to3_distinguishability_results.json
/Users/joshuaeisenhart/Codex-Ratchet/system_v5/julia_carrier/foundation_rung0to3_distinguishability_julia_results.json
```

Observed imports:

```text
Python/JAX: jax, jax.numpy
Julia: Dates, JSON, LinearAlgebra
```

Observed result status remains scratch:

```text
classification: scratch_diagnostic
promotion_allowed: false
formal_admission_allowed: false
```

Safe reading: the packet may remain useful as a finite scratch diagnostic, but it is not rich-tool evidence and cannot support admission or strong claims.

## Current package preflight snapshot

Hermes verified `codex2` health on 2026-06-07:

```text
CODEX_OK in about 8 seconds
```

Python/JAX/PyTorch environment checked through:

```text
/Users/joshuaeisenhart/.local/share/codex-ratchet/envs/main/bin/python3
```

Observed installed/importable Python-side packages included:

```text
jax, jax.numpy, jaxopt, lineax, jraph, ott, e3nn_jax, diffrax
torch, torch_geometric, clifford, geomstats, e3nn, functorch
z3, cvc5, sympy, qutip, quimb, cotengra, autoray
toponetx, gudhi, rustworkx, networkx, xgi
numpy, scipy, mpmath
```

Julia environment checked through:

```text
/opt/homebrew/bin/julia --startup-file=no
active_project=/Users/joshuaeisenhart/.julia/environments/v1.12/Project.toml
```

Observed importable Julia packages at this check:

```text
CliffordAlgebras
Z3
JSON
JSON3
```

Observed missing/not importable in that active Julia project at this check:

```text
Grassmann
DifferentialEquations
QuantumClifford
QuantumOptics
ITensorNetworks
ITensors
ITensorMPS
Graphs
TensorOperations
Symbolics
TensorKit
PEPSKit
IntervalArithmetic
Attractors
```

Do not claim these are installed until a fresh preflight imports them successfully.

## Corrected engine contract

### Julia

Julia is the most aligned / authoritative substrate when exact algebra, geometric algebra, spinor/chirality, QIT states/channels, tensor networks, dynamics, or SMT-backed constraints matter.

Julia packages must be package-native and load-bearing. `LinearAlgebra` plus serialization is supportive, not enough.

### JAX

JAX is a primary mirror/dynamics substrate. `jax.numpy` alone is not enough when the claim needs dynamics, QIT, graph, topology, tensor, proof, or package-native structure.

Use relevant JAX/Python tools such as `diffrax`, `jaxopt`, `lineax`, `jraph`, `e3nn_jax`, `ott`, and crossover tools when those match the claim.

### PyTorch

PyTorch can run as an optional third/support substrate and use its installed tools, but it does not replace Julia/JAX. It carries the most NumPy-style substrate contamination, so where engines disagree, Julia is the reference unless a bounded result says otherwise.

Useful PyTorch-side tools include `torch_geometric`, Python `clifford`, `geomstats`, `e3nn`, and `functorch`.

### Crossover tools

`z3`, `cvc5`, `sympy`, `quimb`, `cotengra`, `autoray`, `toponetx`, `gudhi`, `rustworkx`, `networkx`, and `xgi` should be tied to explicit finite objects and claim paths. Decorative imports do not count.

## Rebuild rule

For all prior results that relied on bare JAX/Julia parity:

```text
status: useful scratch / diagnostic only
admission: blocked until rebuilt
required: package-native rich-tool rerun
```

This applies especially to any result used as pressure for:

```text
M(C)
QIT-engine
carrier/geometry
Axis0 / Xi / Phi0
gravity / physics
Standard Model / GR
canonical by process
```

## Result JSON contract for rebuild packets

Each rebuilt packet should include:

```text
engine_contract:
  julia:
    status: ran | blocked | not_scoped
    load_bearing_packages: [...]
    supportive_packages: [...]
    result_path: ...
  jax:
    status: ran | blocked | not_scoped
    load_bearing_packages: [...]
    supportive_packages: [...]
    result_path: ...
  pytorch:
    status: ran | blocked | not_scoped
    load_bearing_packages: [...]
    supportive_packages: [...]
    result_path: ...
package_preflight:
  julia_active_project: ...
  julia_packages_ok: {...}
  python_executable: ...
  python_packages_ok: {...}
substrate_divergence:
  julia_reference: true
  numeric_agreement: ...
  structural_disagreements: [...]
  interpretation: divergence is signal, not just failure
peer_json_rule: peer results may be read only after local computation; never as pass source
```

## Immediate rebuild queue

1. Package capability anchors before claim rebuilding:
   - Julia `CliffordAlgebras` + `Z3` capability packet.
   - JAX `diffrax` / `e3nn_jax` / `jraph` / proof-crossover capability packets as relevant.
   - Optional PyTorch support anchors for `clifford`, `geomstats`, `e3nn`, and `torch_geometric`.
2. Rebuild the division/Clifford/associator onset rung with Julia as reference and JAX/PyTorch as comparison/support.
3. Rebuild the finite path-integral/spinor-holonomy packet using package-native spinor/Hopf/transport tools.
4. Only then resume larger carrier/geometry/QIT-engine packets.

## 2026-06-07 rebuild receipt update

The first strict root/bracketing rebuild tranche now has a durable intake page: [[projects/codex-ratchet/foundation-root-distinguishability-and-associator-rebuild-2026-06-07]].

Safe update:

```text
R0 v2 distinguishability: validator-clean scratch_diagnostic envelope; old R0 v1 thin-SMT split repaired by bound Born-probability Real variables.
R3 associator/non-associativity: validator-clean scratch_diagnostic envelopes for low/medium/high/xhigh; H associator norm 0.0, O associator norm 2.0.
```

This updates the rebuild router, not the admission status. The next admissible discriminator remains `nonassoc_root_vs_carrier_discriminator`: test whether associator sensitivity changes R1/R2 admissibility itself, or only carrier/readout bracketing.

## Claim ceiling

This page is a process/tooling correction and rebuild router. It does not admit any sim, package, carrier, `M(C)`, QIT engine, Axis0, Xi/Phi0, gravity, physics, Standard Model, GR, or canonical status.
