---

title: Outdated Math and Geometry Ladder
created: 2026-04-07
updated: 2026-04-08
type: concept
tags: [reference, research, planning]
sources:
  - raw/articles/system-v5-reference-docs/outdated-math-and-geometry-ladder.md
framing: legacy
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# Outdated Math and Geometry Ladder

## Overview
- Here’s the cleanest current table I can give you.
- **Math And Geometry Ladder**
- | Layer | Object / Math | Used Now? | Status In Repo | Main Surfaces |
- |---|---|---:|---|---|
- | 0 | root constraints `F01_FINITUDE`, `N01_NONCOMMUTATION` | Yes | doctrine / admission layer, not a direct sim object | [CONSTRAINT_GEOMETRY_AXIS0_SEPARATION.md](/Users/joshuaeisenhart/Desktop/Codex%20Ratchet/system_v4/docs/CONSTRAINT_GEOMETRY_AXIS0_SEPARATION.md) |
- | 1 | admissible finite QIT math | Yes | live working basis | [AXIS_0_1_2_QIT_MATH.md](/Users/joshuaeisenhart/Desktop/Codex%20Ratchet/system_v4/docs/AXIS_0_1_2_QIT_MATH.md), [AXIS_3_4_5_6_QIT_MATH.md](/Users/joshuaeisenhart/Desktop/Codex%20Ratchet/system_v4/docs/AXIS_3_4_5_6_QIT_MATH.md) |
- | 2 | complex Hilbert space / spinor state space | Yes | live working basis | [hopf_manifold.py](/Users/joshuaeisenhart/Desktop/Codex%20Ratchet/system_v4/probes/hopf_manifold.py) |
- | 3 | density matrices `rho`, bipartite `rho_AB` candidates | Yes | heavily used; final Ax0 bridge target still open | [geometric_operators.py](/Users/joshuaeisenhart/Desktop/Codex%20Ratchet/system_v4/probes/geometric_operators.py), [axis0_xi_strict_bakeoff_sim.py](/Users/joshuaeisenhart/Desktop/Codex%20Ratchet/system_v4/probes/axis0_xi_strict_bakeoff_sim.py) |
- | 4 | Pauli matrices / SU(2) / Bloch machinery | Yes | live and foundational | [hopf_manifold.py](/Users/joshuaeisenhart/Desktop/Codex%20Ratchet/system_v4/probes/hopf_manifold.py), [engine_core.py](/Users/joshuaeisenhart/Desktop/Codex%20Ratchet/system_v4/probes/engine_core.py) |
- | 5 | `S^3 = SU(2)` carrier | Yes | strongly simulated | [sim_L0_s3_valid.py](/Users/joshuaeisenhart/Desktop/Codex%20Ratchet/system_v4/probes/sim_L0_s3_valid.py) |

## Related pages
- [[constraint-surface-and-process]]
- [[model-math-geometry-sim-plan]]
- [[system-architecture-reference]]
