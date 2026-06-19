---
title: Codex Ratchet Cross-Issue Finite Test Backlog
created: 2026-06-19
type: backlog
status: imported_from_chat_deepening
claim_ceiling: planning and source-processing only; no sim admission, no layer completion, no M(C) admission, no QIT-engine admission, no Axis0, no bridge, no physics
promotion_allowed: false
formal_admission_allowed: false
tags: [codex-ratchet, finite-tests, backlog, source-processing, physics-model, spinor-network]
sources:
  - projects/codex-ratchet/cross-issue-deepening-intake-2026-06-19
  - Joshua-Eisenhart-Wiki/projects/codex-ratchet/actual-physics-docs-processing-map-2026-06-06.md
  - Joshua-Eisenhart-Wiki/projects/codex-ratchet/physics-model-unique-claim-atlas-2026-06-06.md
  - Joshua-Eisenhart-Wiki/projects/codex-ratchet/owner-physics-claims-source-extract-2026-06-06.md
  - Joshua-Eisenhart-Wiki/projects/codex-ratchet/geometric-constraint-manifold-spinor-carrier-source-extract-2026-06-06.md
---

# Codex Ratchet Cross-Issue Finite Test Backlog — 2026-06-19

This backlog turns the cross-issue source-processing pass into finite test targets. It is not an execution record and does not claim anything was run.

## Status labels for this page

Use only these planning labels:

| Label | Meaning |
|---|---|
| `source_extract_needed` | quote/window extraction is missing or too thin |
| `finite_object_needed` | source claim needs exact finite carrier/support/probe object |
| `control_design_needed` | falsifiers are not yet explicit enough |
| `sim_target_ready` | finite object + controls are clear enough to become a sim target |
| `blocked_by_prior_layer` | depends on earlier `M(C)`, spinor, density/probe, cut, or loop receipt |
| `graveyard_deflator` | build as anti-overclaim / baseline / falsifier row |

No row here means `canonical`, `admitted`, or `passes local rerun`.

## Highest-priority source extraction rows

| Priority | Row | Why it matters | Status |
|---:|---|---|---|
| 1 | Sequential universe / dark-sector memory | actual-physics map names Tranche D as next correct work | `source_extract_needed` |
| 2 | Six-bit / two-trigram engine | prevents flattening engine to two spinors or generic noncommutation | `source_extract_needed` |
| 3 | Axis 1 bath legality + Axis 2 chart lens | required for Szilard-class legality rather than label overlay | `source_extract_needed` |
| 4 | S3/Hopf global chirality vs local-defect geometry | explains why S3/Hopf is load-bearing if true | `source_extract_needed` |
| 5 | 8 terrain x 8 operator lattice | prevents undercounting engine state space | `source_extract_needed` |
| 6 | `ijk` probability-time shell | prevents quaternion labels from becoming decorative | `source_extract_needed` |
| 7 | Holodeck projection/error-correction loop | bridges perception/FEP to finite experiment design | `source_extract_needed` |
| 8 | Dark energy / dark matter flow-memory split | converts cosmology prose into role/readout variables | `source_extract_needed` |
| 9 | Gravity as possibility convergence | requires finite shell/screen/no-signal map | `source_extract_needed` |
| 10 | Science method / Leviathan as engine application | cross-domain application only; prevent origin confusion | `source_extract_needed` |

## Sim target cards

### T1 — six-bit / two-trigram Szilard legality map

```yaml
sim_target_id: six_bit_two_trigram_szilard_legality_v0
status: finite_object_needed
claim_ceiling: scratch_diagnostic_only
```

Question:

```text
Does a finite six-bit/two-trigram architecture carry Szilard legality that generic noncommutation does not carry?
```

Finite object:

```text
X = finite engine-state set with:
  topology_trigram in {0,1}^3
  operator_trigram in {0,1}^3
  polarity/order bits as derived readouts or extra variants
```

Positive:

- legal isothermal stroke has bath coupling;
- legal adiabatic stroke has near-zero bath coupling;
- topology and operator trigrams are both read.

Negatives:

- remove Axis 1 bath-gate variable;
- remove Axis 2 chart/lens variable;
- shuffle topology bits while preserving operator bits;
- collapse both trigrams into one sign bit.

Pass ceiling:

```text
finite legality discriminator only; no QIT-engine or physics claim.
```

### T2 — Axis 1/2 Szilard legality witness

```yaml
sim_target_id: axis12_szilard_legality_witness_v0
status: control_design_needed
claim_ceiling: scratch_diagnostic_only
```

Question:

```text
Can Axis 1/2 be represented as finite legality maps that distinguish legal and illegal thermodynamic labels?
```

Finite object:

```text
stroke = {isothermal_reset, adiabatic_unitary, free_reset, fake_adiabatic_entropy_import}
bath_gate = {off, weak, on}
chart_lens = {closed_lagrangian, open_eulerian}
work_memory_register = finite counter/state
```

Controls:

- free reset without erasure cost must fail;
- adiabatic label with entropy import/export must fail;
- chart swap should change representation but not erase conserved legality criteria;
- label shuffle fails if legality is label-only.

Blocked consumers:

- Axis0;
- full IGT/QIT engine;
- physics/cosmology.

### T3 — Type 1/2 three-factor orientation split

```yaml
sim_target_id: type12_three_factor_engine_orientation_v0
status: finite_object_needed
claim_ceiling: scratch_diagnostic_only
```

Question:

```text
Can the model separate left/right spinor type, two stacked Szilard cycle directions, and inner/outer impedance role?
```

Finite object:

```text
engine_type in {type1, type2}
cycle_direction in {deductive, inductive} or source-native names
impedance_role in {inner_major, outer_minor}
```

Controls:

- collapse engine type only;
- collapse cycle direction only;
- collapse impedance role only;
- test whether each collapse kills a distinct readout.

Pass ceiling:

```text
factor-separation fixture only.
```

### T4 — S3/Hopf versus local-defect carrier discriminator

```yaml
sim_target_id: s3_hopf_global_chirality_vs_local_defect_v0
status: blocked_by_prior_layer
claim_ceiling: scratch_diagnostic_only
blocked_by: finite spinor carrier / Hopf readout exact object
```

Question:

```text
Does the S3/Hopf carrier preserve global chirality that local-defect carriers cannot preserve under the same left/right Weyl transport witness?
```

Finite object:

- finite discretized Hopf/fiber support;
- local-defect carrier variant;
- left/right Weyl transport witness;
- same density/probe readout for both.

Controls:

- density-only quotient erases chirality;
- local-defect carrier fails global consistency;
- label-shuffled left/right fails;
- path reversal changes sign as expected.

### T5 — sequential universe inherited memory toy

```yaml
sim_target_id: sequential_universe_inherited_memory_v0
status: source_extract_needed
claim_ceiling: source_to_sim_target_only
```

Question:

```text
Does structured inherited information improve finite daughter-state stability under constraints, compared with no/random/scrambled inheritance?
```

Finite object:

```text
U_n = finite spinor-network state
I_n = inherited memory channel / correlation structure
U_{n+1} = ratchet_update(U_n, I_n, constraints)
stability = finite viability / survival / constraint-satisfaction readout
```

Controls:

- no inheritance;
- random inheritance;
- same scalar entropy but scrambled correlations;
- cyclic update instead of sequential update;
- no entanglement;
- no order sensitivity.

Pass ceiling:

```text
finite inherited-memory role diagnostic only; no dark matter or cosmology claim.
```

### T6 — dark-sector flow-memory split

```yaml
sim_target_id: dark_sector_flow_memory_role_split_v0
status: source_extract_needed
claim_ceiling: scratch_diagnostic_only
```

Question:

```text
Can finite readouts separate expansion/possibility-growth role from inherited memory/anchoring role?
```

Finite object:

```text
flow_readout
memory_preservation_readout
stability_viability_readout
no_signal_flag
```

Controls:

- same scalar entropy with memory destroyed;
- memory retained but flow randomized;
- no-signal violation fails;
- role labels shuffled.

### T7 — gravity possibility-convergence shell gradient

```yaml
sim_target_id: gravity_possibility_convergence_shell_gradient_v0
status: blocked_by_prior_layer
claim_ceiling: source_to_sim_target_only
blocked_by: finite spinor-network shell/cut object
```

Question:

```text
Can a nested finite shell/screen family produce a gradient over distinguishability/cut information without signal transfer?
```

Finite object:

```text
shell_index
finite spinor-network cut
profile = distinguishability / coherent-info / admissibility score
gradient = finite difference over shell_index
```

Controls:

- same scalar / scrambled gradient;
- local-unitary control;
- no-signal check;
- shell index label shuffle;
- flat profile negative.

Pass ceiling:

```text
finite shell-gradient fixture only; no gravity claim.
```

### T8 — `ijk` probability-time shell

```yaml
sim_target_id: ijk_probability_time_shell_v0
status: finite_object_needed
claim_ceiling: scratch_diagnostic_only
```

Question:

```text
Can the `i/j/k` language be made into finite shell variables and probability-vector readouts instead of decorative quaternion terms?
```

Finite object:

```text
i = shell index or entropy-capacity scalar
j = probability vector family over continuations
k = second probability vector family over continuations
present = constrained quotient over j/k futures
```

Controls:

- scramble j/k while preserving i;
- collapse j/k into one vector;
- same probability scalar but different continuation structure;
- branch ontology versus convergence quotient.

### T9 — holodeck projection/error-correction loop

```yaml
sim_target_id: holodeck_projection_error_correction_loop_v0
status: finite_object_needed
claim_ceiling: scratch_diagnostic_only
```

Question:

```text
Can a finite predictive projection loop preserve the distinction among latent state, projection, probe error, update, and compression/hash readout?
```

Finite object:

```text
latent spinor-network or finite-state carrier
projection surface
probe/camera readout
error map
update rule
compression/hash readout
```

Controls:

- random projection;
- no feedback;
- same compression without geometry;
- no-probe;
- same visual projection with different latent state.

### T10 — terrain/operator 64-state lattice extraction

```yaml
sim_target_id: terrain_operator_64_state_lattice_v0
status: source_extract_needed
claim_ceiling: source_to_sim_target_only
```

Question:

```text
Can the 8 terrain x 8 operator lattice be represented as separable finite axes instead of one blended chart?
```

Finite object:

```text
terrain_id in 0..7
operator_id in 0..7
stage_id in 0..15
suboperator_id in 0..3
native_operator_for_stage
all_operator_actions_per_stage
```

Controls:

- terrain-only collapse;
- operator-only collapse;
- native-operator shuffle;
- stage/suboperator mismatch;
- same 64 count but different adjacency.

Pass ceiling:

```text
state-lattice extraction fixture only.
```

### T11 — many-futures convergence versus branching

```yaml
sim_target_id: many_futures_convergence_not_branching_v0
status: finite_object_needed
claim_ceiling: scratch_diagnostic_only
```

Question:

```text
Can a finite continuation set converge into one present-state quotient under viability/constraint weights without becoming a many-worlds branch ontology?
```

Finite object:

```text
continuation_set F
weight / viability / constraint map w: F -> finite score
present quotient q(F,w)
history ledger H
```

Controls:

- random future weights;
- uniform weights;
- branching ontology retains all futures as equally real;
- same selected present but different erased residuals.

### T12 — science method / Leviathan engine application

```yaml
sim_target_id: science_method_engine_application_v0
status: source_extract_needed
claim_ceiling: cross_domain_routing_only
```

Question:

```text
Can deductive/inductive topology be represented as finite operator-policy loops without claiming Codex Ratchet derives from Leviathan?
```

Finite object:

```text
deductive loop
inductive loop
observer/scientist state
experiment/probe state
receipt ledger
policy update
```

Controls:

- observer outside experiment;
- no receipt ledger;
- inductive/deductive labels shuffled;
- Leviathan-origin overclaim rejected.

## Graveyard / deflator rows to keep active

| Deflator | What it prevents |
|---|---|
| Low-rank SVD baseline | prevents held-out transfer from being miscalled carrier evidence |
| Context-indexed quotient caveat | prevents contextuality from being miscalled `rho` uniqueness |
| Density-only quotient control | prevents spinor/Hopf/chirality information from being silently erased |
| Static-predicate commuting control | prevents ratchet from being miscalled when update is only static filtering |
| Same-scalar scrambled-memory control | prevents dark-sector memory from reducing to scalar entropy |
| Same-count different-adjacency control | prevents 64-state lattice from being count tautology |
| Label shuffle | prevents axis/terrain/type names from carrying evidence alone |
| No-signal fence | prevents gravity/retrocausality language from implying information transfer |

## Front-door patch candidate

```markdown
- [[projects/codex-ratchet/cross-issue-finite-test-backlog-2026-06-19]] — finite-test backlog extracted from the cross-issue deepening pass: six-bit/two-trigram engine, Axis 1/2 Szilard legality, Type 1/2 factor split, S3/Hopf global chirality, sequential-universe inherited memory, dark-sector flow/memory split, gravity shell gradient, `ijk` probability-time shell, holodeck loop, 64-state terrain/operator lattice, and many-futures convergence; planning only, no promotion.
```
