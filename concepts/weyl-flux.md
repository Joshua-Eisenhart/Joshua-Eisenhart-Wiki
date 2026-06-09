---
title: Weyl Flux
created: 2026-04-07
updated: 2026-04-14
type: concept
tags: [reference, research, geometry, chirality, transport]
sources:
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v5/docs/plans/sim_backlog_matrix.md
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v5/docs/17_actual_lego_registry.md
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v5/docs/CONSTRAINT_ON_DISTINGUISHABILITY_FULL_MATH.md
framing: current
---

# Weyl Flux

## Definition
`Flux` in this system is not a primitive object.
It is an open derived candidate family that may or may not appear once enough of the geometry/chirality/operator manifold is running together.

That means the right question is not “what is flux?” in isolation.
The right question is: which stagewise change surfaces, transport currents, chirality differentials, or cut-state currents survive enough of the lower manifold to deserve the name flux.

## Why flux is not early
The current repo/process docs are explicit that flux should not be treated as a first local lego beside Hopf geometry or carrier admission.

In the live backlog this appears explicitly as `flux_candidate_family` with state `derived/open only` and the instruction to defer it until transport + chirality + delta surfaces are real.

The reason is structural:
- a left/right Weyl split by itself is too thin
- Pauli/operator action on that split may be necessary
- nested Hopf torus placement matters
- loop/transport grammar matters
- additional coexistence of manifold layers may be required before a real current-like object appears

So flux belongs later than shell-local geometry.
It should only be tested after enough of the manifold layers are real and running on each other.

## Dependency chain
The raw source page already gave the right shape. In current wiki/controller language the practical chain is:

1. root admissibility
2. admissible domain `M(C)`
3. finite carrier `H = C^2`
4. spinor carrier `S^3`
5. Hopf projection `S^3 -> S^2`
6. nested Hopf torus stratification
7. left/right Weyl split
8. density extraction `rho_L`, `rho_R`
9. loop grammar `gamma_f`, `gamma_b`
10. stagewise engine/operator evolution
11. raw stagewise deltas
12. chirality differential
13. transport / phase / entropic / coupling current candidates
14. candidate flux family
15. negatives and placement decision

The important point is that flux appears only after stagewise deltas and current candidates, not before them.

## Candidate family rather than single object
The raw source identifies several possible current-like branches. In cleaned current framing they are still best treated as a family:
- geometric/transport current
- chirality-separation current
- Bloch-differential current
- entropic current
- phase/winding current
- cut-state / coupling current
- later axis-internal or cross-axis current

The system should not prematurely collapse these into one “true flux” object.

## Relevance to this system
This matters because the geometry-manifold lane is the spine of the build.
If flux is promoted too early, the controller will start reading any change surface as if it were a lawful engine-level quantity. That would violate the current admissibility discipline.

Flux is therefore a test of whether the system can:
- keep lower layers explicit
- derive candidate current families honestly
- use negatives to reject fake transport stories
- avoid renaming generic change as a deeper object

## Current best placement
Current best placement is:
- on the dynamic geometry/manifold layer, below axes/readouts
- later than local geometry
- later than local Weyl extraction
- later than local Pauli/operator admission
- likely after at least some coexistence of manifold layers
- still pre-axis only if a derived candidate survives the required dependency and negative chain

2026-06-09 owner correction: flux should not be treated as `Axis 3` itself. Axis 3 may read loop/transport orientation, but flux is a geometry/current candidate on the dynamic constraint manifold. The manifold should not be framed as static: it expands, compresses, folds, warps, and reindexes; flux belongs to that dynamic geometry if it survives.

2026-06-09 curvature-member test in flight:

```text
/Users/joshuaeisenhart/Codex-Ratchet/system_v6/sims/flux_emergence_discriminator/
```

This bounded packet tests the Hopf-curvature member of the flux candidate family:

```math
A = d\phi + \cos(2\eta)d\chi
```

```math
F=dA=-2\sin(2\eta)d\eta\wedge d\chi
```

Working implication: within one fixed torus shell (`eta` constant), the curvature restricts away; one shell gives holonomy, not flux. Flux needs inter-shell/nested-Hopf structure:

```math
\Phi(\eta_1,\eta_2)=2\pi(\cos 2\eta_1-\cos 2\eta_2)
```

Expected ablations for that candidate:

```text
bare spinor: no bundle / no connection -> no F
single shell: holonomy exists, flux absent/undefined
nested shells: inter-shell flux exists
ratchet scramble: pairwise flux pattern order-sensitive; total Chern invariant order-indifferent
```

Ceiling: this tests only the curvature member's emergence conditions. Flux remains an open candidate family until the result/audit lands and until other current candidates are compared.

Repo-current status translation:
- treat flux as `candidate-family` language, not a normalized local lego
- do not use flux wording to skip over `weyl_chirality_pair`, `chiral_density_bookkeeping`, `pauli_generator_basis`, `left_right_asymmetry`, `fiber_loop_law`, `base_loop_law`, or `composition_order_noncommutation`

So flux is better treated as a later manifold-coexistence/emergence candidate than as an early shell-local lego.

## Negatives required
Any serious flux candidate should be pressure-tested by at least:
- removing chirality
- swapping loop law / destroying fiber-base distinction
- flattening transport geometry
- collapsing seat distinctions on the nested tori
- removing operator action that the candidate supposedly depends on
- checking whether the quantity only appears after joint/cut coupling

If a “flux” quantity survives none of those, it should not be promoted.

## Relation to engine language
Flux is tempting because engine language naturally suggests current, flow, transport, and asymmetry.
But in this system, engine language must remain downstream of admissibility.

So a lawful engine current should emerge from:
- admissible states
- admissible transforms
- admissible loops
- admissible chirality/operator structure

not from metaphorical talk about motion.

## Relation to the CS framing
In CS/developer terms, flux should be thought of as a derived runtime observable or current family, not a primitive state field.

That means:
- it is downstream of the state model
- downstream of legal transforms
- downstream of loop semantics
- and possibly downstream of multi-layer coexistence

So it is closer to an earned telemetry family over a constrained runtime than to a built-in variable.

## Open questions
- Does any pre-joint candidate survive before `rho_AB`, or is meaningful flux only honest after some coupled cut-state layer?
- Which candidate branch is actually load-bearing: chirality differential, Bloch current, phase current, entropic current, or cut current?
- Does flux require Pauli action on Weyl spinors as part of the minimal honest chain?
- Does flux only become honest once multiple geometry layers run on each other rather than in isolation?

## Related pages
- [[sim-build-spine-and-wiki-maintenance]]
- [[pre-axies-math-and-geometry-work-out]]
- [[constraint-on-distinguishability-full-math]]
- [[axis-and-entropy-reference]]
- [[engine-math-reference]]
- [[terrain-laws-and-loop-geometry]]
- [[current-geometry-spine-status]]
- [[pauli-on-weyl-loop-interaction]]
- [[controller-state-transition-model]]
- [[qit-engine-dev-framing]]
