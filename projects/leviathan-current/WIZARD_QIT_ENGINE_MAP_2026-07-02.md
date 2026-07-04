---
title: Wizard QIT Engine Map
created: 2026-07-02
updated: 2026-07-03
type: architecture-spec
status: owner-approved correspondence mapped to implementable Lev harness
claim_ceiling: architecture=implementable-now; IGT/personality/consciousness readings=rosetta candidate only; no CR canon promotion, no benchmark win claimed, no runtime completion proof
tags: [lev, wizard, qit-engine, flowmind, codex-ratchet, gates, benchmark]
sources:
  - ./KERNEL_UPGRADES_LEVIATHAN_2026-07-02.md
  - ./GATE_DOCTRINE_ADMISSIBILITY_NOT_QUALITY.md
  - ./ONE_SYSTEM_THREE_PERSPECTIVES_2026-07-02.md
  - ./MESH_NODE_PROTOCOL_V0_2026-07-02.md
  - /Users/joshuaeisenhart/Codex-Ratchet/system_v5/ops/AXES_TERRAINS_OPERATORS_MANIFOLD_SOURCE_LAYOUT_20260522.md
  - /Users/joshuaeisenhart/Codex-Ratchet/system_v5/ops/AXES_0_6_DEEP_MATH_DEFINITIONS_20260522.md
  - /Users/joshuaeisenhart/Codex-Ratchet/system_v5/ops/QIT_ENGINE_FOUR_OPERATOR_SIGNED_MATH_20260522.md
  - /Users/joshuaeisenhart/Codex-Ratchet/system_v7/sims/qit_surprise_stream_v0
  - /Users/joshuaeisenhart/Codex-Ratchet/system_v7/sims/online_regime_shift_detector_v0
---

# Wizard QIT Engine Map - 2026-07-02

## Purpose

This spec makes the wizard-in-Lev run on the QIT engine structure, not next to it.

The owner-approved correspondence is treated here as an architecture contract:
build a FlowMind-generated wave schedule where wizard voices, loops, councils, and
swarms are parameterized by QIT terrains, operators, chirality passes, surprise
boundaries, EFE next-seed choice, and code gates.

The ceiling is explicit:

- Architecture: implementable now in Lev using FlowMind, the current wizard/waverun
  concepts, sim-witness/evaluator gates, graph/world-model seams, and the G3
  surprise port described in [One System, Three Perspectives](./ONE_SYSTEM_THREE_PERSPECTIVES_2026-07-02.md).
- IGT, personality, and consciousness readings: rosetta candidates only. They
  may name a useful translation layer, but the benchmark below must discriminate
  before they become stronger than labels.
- Gate doctrine: code admits artifacts; LLMs generate, attack, and explain.
  This follows [Gate Doctrine](./GATE_DOCTRINE_ADMISSIBILITY_NOT_QUALITY.md).

## Controlling QIT Facts

The QIT source layout gives the finite carrier and the row grammar:

```text
carrier: finite density/spinor state over C^2
terrains: Se, Ne, Ni, Si, each embedded as fiber and lifted-base path
runtime terrains: Se_f, Si_f, Ne_f, Ni_f, Se_b, Si_b, Ne_b, Ni_b
operators: Ti, Te, Fi, Fe
operator families: dephasing/projection versus unitary rotation
token law: topology x operator-family x precedence
16 ordered tokens: A1 x A2 x A5 x A6
8 paired loop-placement signatures: A3 x A4 x A5 x A6
```

The operator lock is:

```text
Ti = z dephasing / pinching
Te = x dephasing / pinching
Fi = x unitary rotation
Fe = z unitary rotation
```

UP/DOWN, left/right, and plus/minus do not invent new operator formulas. They
name precedence, action side, or closure audit rows over the same four base
maps. Any Lev implementation must carry `operator_formula`, `terrain_id`,
`token_precedence`, `axis6_action_side`, and `closure_type` as separate fields.

## Mapping Matrix

| # | Wizard / Lev object | QIT engine structure | Implementation meaning |
|---:|---|---|---|
| 1 | Eight voices | Eight runtime terrains: `Se_f`, `Si_f`, `Ne_f`, `Ni_f`, `Se_b`, `Si_b`, `Ne_b`, `Ni_b` | A voice is a terrain-parameterized processor slot, SMT-separated by terrain id and path class. It is not a personality entity. |
| 2 | Voice native moves | Two native moves per terrain | Each voice exposes exactly one dephasing/collapse move and one unitary/explore move from its native operator pair. Direct terrains use `Ti`/`Fi`; conjugated terrains use `Te`/`Fe`. |
| 3 | Collapse / critique / decide | Dissipative `Ti`/`Te` dephasing | A dephasing move contracts options toward a fixed algebra, audits coherence, collapses over-broad branches, and records what was killed. |
| 4 | Generate / explore / preserve | Unitary `Fi`/`Fe` rotation | A rotation move preserves spectrum/options while exploring neighboring readings, analogies, and branch variants. |
| 5 | Exactly two moves per voice | Axis 3 section 5.6 plus the 8/16 cardinality correction and Axis 5 family split | The source's Axis 3 to Axis 6 relation forces two non-interchangeable path/chart readouts, and `A3 x A4 x A5 x A6` gives 8 paired signatures rather than 16 token identities. Axis 5 supplies exactly two operator families. The voice therefore gets two native move types, not one blended move and not an unbounded action menu. |
| 6 | One wave | One chirality pass | A wave is one sheet pass, `L` or `R`. In that pass, the sheet can access its 8 terrain voice slots and their 16 native stage attempts. |
| 7 | Dual-wave agreement | Chirality parity gate | A complete L/R pair must compare named observables before any claim crosses the stage boundary. Agreement is parity evidence, not truth by itself. |
| 8 | Deductive/inductive order | Axis 4 `U E U E` / `E U E U` | Deductive waves schedule unitary and dissipative moves as `U,E,U,E`; inductive waves schedule `E,U,E,U`. Composition convention must be explicit. |
| 9 | Full swarm program | 64 schedule, 32 per engine side | The full program expands two engine charts across L/R chirality and the two move families into 64 scheduled move opportunities. This is an engineering schedule convention, not a closure proof. |
| 10 | Replan trigger | Surprise via G3 port plus PH/CUSUM detector | Wave boundaries are driven by `surprise_bits` from `qit_surprise_stream_v0`, consumed through the G3 port, and by `online_regime_shift_detector_v0` Page-Hinkley/CUSUM events. |
| 11 | Next seed | Expected free energy | The next seed is selected by EFE: risk minus epistemic value. The agent-loop sim supplies the action-edge reading; Lev must keep the risk-only ablation visible. |
| 12 | Inter-wave state | Register / spinor memory, capacity edge `k=5` | Between waves, state is a finite register carrying seed, terrain row, move trace, surviving claims, surprise segment, and pointer-candidate hashes. `k=5` is the edge to test, not a license for unbounded memory. |
| 13 | Collapse audit | Einselection | Pointer states are claims that survive all eight terrain voices, both move families, and L/R parity. This is consensus-as-einselection as a concrete audit analogy, fenced from physics or social consensus claims. |
| 14 | Voice order | N01 order-sensitive trajectory | Voice order shapes the trajectory. Gates fix the endpoint. Preserve the [Kernel Upgrades](./KERNEL_UPGRADES_LEVIATHAN_2026-07-02.md) attrition finding: Holevo `chi` through the composed schedule peaked early and went to zero by stage 13; order changed the trajectory, not the admitted endpoint. |
| 15 | Failure modes | Wrong operator family drift | Premature collapse is wrong-axis dephasing: options are killed before the correct terrain/operator row sees them. Endless exploration is all-unitary drift: rotations preserve options without dissipative selection. |

## Voice Slot Contract

Each voice slot is a small processor record:

| Field | Contract |
|---|---|
| `voice_id` | Stable slot id, `V0` through `V7`. |
| `terrain_id` | One of the eight runtime terrains. |
| `topology` | `Se`, `Ne`, `Ni`, or `Si`. |
| `path_class` | `fiber` or `lifted_base`. |
| `frame` | `direct` or `conjugated`. |
| `native_collapse_operator` | `Ti` for direct terrains, `Te` for conjugated terrains. |
| `native_explore_operator` | `Fi` for direct terrains, `Fe` for conjugated terrains. |
| `move_type` | `dephase_collapse` or `unitary_explore`. |
| `axis4_order` | `deductive_UEUE` or `inductive_EUEU`. |
| `axis6` | `token_precedence`, `action_side`, and `closure_type`. |
| `receipt` | Source seed, emitted claim deltas, killed branches, preserved branches, surprise input, EFE score, and gate outcome. |

The LLM prompt for a voice is generated from this record. The prompt must not
ask for a personality performance. It asks for one terrain-constrained operator
move over one seed under a declared claim ceiling.

## Wave And Council Semantics

A wave is the execution unit:

```text
wave = chirality_sheet x axis4_order x terrain_voice_schedule
```

A dual wave is the parity unit:

```text
dual_wave = wave_L + wave_R + parity_gate
```

A council is the collapse audit over completed wave receipts:

```text
council = collect voice receipts
        -> compare L/R parity
        -> reject self-graded fields
        -> apply code gates
        -> emit pointer-state candidates
```

The council does not decide quality. It prepares admissibility evidence for code
gates. This keeps the system aligned with [Mesh Node Protocol v0](./MESH_NODE_PROTOCOL_V0_2026-07-02.md):
exposure invites independent witness, correction returns failures, and only
receipts accumulate.

## Implementation Plan v0

1. Generate the FlowMind schedule from the 16-stage QIT structure.

   Add a schedule generator that reads a canonical stage table and emits
   FlowMind nodes for `chirality`, `terrain_id`, `operator_family`,
   `operator_formula`, `axis4_order`, `axis6_precedence`, and expected receipt
   fields. The generator, not hand-written prompts, owns the wave order.

2. Represent voices as terrain-parameterized LLM slots.

   Each slot receives its terrain row and only its two native operator moves.
   The LLM may propose text, attacks, code changes, or next seeds only through
   one of those typed moves. The prompt must include the claim ceiling and the
   blocked-consumer list.

3. Preserve gates between stages unchanged.

   Existing Lev code gates remain the judges. The engine harness routes more
   structured evidence into them; it does not relax ClaimGate, sim-witness,
   evaluator-pack, source freshness, adapter rejection, or graph admission.

4. Drive wave boundaries from surprise.

   Consume `cr.qit_surprise_tick.v1` rows from `qit_surprise_stream_v0` through
   the existing G3 `SurprisePredictor` route. Feed the same stream to
   `online_regime_shift_detector_v0`; Page-Hinkley/CUSUM events can close a
   wave, force a parity check, or trigger replan.

5. Select the next seed by EFE.

   Implement a seed selector that scores candidate seeds as risk minus epistemic
   value. The risk-only ablation must remain a first-class control, matching
   [Kernel Upgrades Leviathan](./KERNEL_UPGRADES_LEVIATHAN_2026-07-02.md).

6. Store inter-wave register state.

   Persist a finite register containing the seed, terrain row, chirality sheet,
   move trace, surviving/killed branches, surprise segment hash, EFE terms, and
   pointer-candidate ids. Treat `k=5` capacity as the current test edge.

7. Reuse waverun and council machinery concepts.

   Reuse the lev-wizard-ratchet concepts: wave receipts, council compilation,
   follow-up seed generation, host-consume discipline, and ClaimGate repair
   loops. Port concepts onto FlowMind on main rather than importing CR runtime
   authority wholesale.

8. Add one narrow engine-harness evaluator pack.

   The first pack should judge shape, parity, self-grading rejection, stale
   surprise rejection, and mutation behavior for the harness itself. It should
   not judge whether the output is wise, conscious, or psychologically true.

## Benchmark Protocol: The Decisive Test

The benchmark must decide whether the engine harness adds real capability over
raw model output and whether a weaker model plus harness can close measurable
distance to Fable raw.

### Arms

| Arm | Description |
|---|---|
| `weak-model-raw` | Same weak model, no QIT engine harness, same context budget, same task battery. |
| `weak-model-engine-harness` | Same weak model with generated wave schedule, terrain slots, surprise boundaries, EFE seed choice, parity gate, and code gates. |
| `Fable-raw` | Fable raw, no engine harness, same task battery and no privileged self-grading. |

All arms receive the same repo snapshot, same allowed tools, same task battery,
same time budget class, and same commit/gate rules. No arm may self-grade.

### Task Classes

| Class | Task | Gate judge |
|---|---|---|
| `T1_shape` | Produce a schema-shaped receipt or spec from a fixed prompt. | JSON/schema validator plus required-field checks. |
| `T2_code_patch` | Patch a small seeded defect in TypeScript or Python. | Unit tests, typecheck/compile, and mutation control where available. |
| `T3_sim_adapter` | Convert a sparse or malformed sim result into admissible provider evidence or reject it. | Adapter tests with malformed, stale, sparse, and verdict-shaped fixtures. |
| `T4_claim_ceiling` | Rewrite overclaiming text into allowed claim language without losing source references. | Deterministic forbidden-phrase and required-ceiling checks plus human audit sample. |
| `T5_wave_repair` | Given conflicting wave receipts, route repair and produce next seed. | Graph/receipt consistency checks, no self-grading fields, EFE terms present. |
| `T6_surprise_boundary` | Detect and respond to stream shift in a QIT surprise fixture. | PH/CUSUM detector output plus expected wave-boundary action. |
| `T7_order_sensitivity` | Preserve N01 order facts while avoiding false endpoint claims. | Ordered-channel fixtures and gate endpoint comparison. |
| `T8_end_to_end` | Run a bounded change from prompt to patch to receipt to claim ceiling. | Code gates, receipt gates, graph/evidence reference checks, and mutation/falsifier behavior. |

### Metrics

| Metric | Definition |
|---|---|
| `gate_pass_rate` | Fraction of tasks passing deterministic code gates. |
| `mutation_survival` | Fraction where the claimed fix fails when the critical guard is neutralized. |
| `self_grading_rejection` | Rate at which verdict-shaped payloads are rejected rather than consumed. |
| `freshness_compliance` | Stale source/result cases correctly rerun or demoted. |
| `claim_ceiling_precision` | No claim language above the earned receipt rung. |
| `repair_latency` | Number of turns or wave cycles to reach the first gate-passing artifact. |
| `token_cost_to_pass` | Tokens used per accepted artifact. |
| `parity_lift` | Improvement from raw weak model to harnessed weak model on parity-sensitive tasks. |
| `fable_gap_closed` | Percent of the gap between weak raw and Fable raw closed by the harness. |

### Earn Criteria

The engine harness earns an implementation claim if all are true:

```text
weak-model-engine-harness beats weak-model-raw by >= 20% relative gate_pass_rate
weak-model-engine-harness improves mutation_survival and claim_ceiling_precision
weak-model-engine-harness closes >= 40% of the weak-model-raw to Fable-raw gap
the lift is strongest on T5, T6, T7, and T8, where schedule, surprise, EFE, and order should matter
no improvement is explained primarily by extra tokens, hidden retries, or self-grading
```

It earns a stronger rosetta claim only if the ablation shows that removing
terrain slots, removing dual-wave parity, or removing surprise/EFE boundaries
materially degrades performance on their targeted task classes.

### Refute Criteria

The engine harness is refuted or demoted if any are true:

```text
weak-model-engine-harness fails to beat weak-model-raw beyond noise
improvement appears only on prose tasks and not code-gated tasks
all gains disappear under equalized retry/token budget
terrain labels can be randomly permuted with no measurable loss
all-unitary or all-dephasing ablations perform the same
the harness consumes self-graded fields or stale evidence
Fable-raw still dominates every task class and the weak harness adds latency without gate lift
```

## Staging

### Buildable This Week

- Write the generated schedule table and FlowMind generator for the 16-stage
  structure.
- Add eight terrain slot prompt templates with exactly two typed moves each.
- Add receipt schema fields for terrain, operator, axis4 order, axis6 audit,
  chirality, surprise segment, EFE terms, killed branches, and surviving claims.
- Wire `qit_surprise_stream_v0` fixture consumption to a local wave-boundary
  adapter and detector harness.
- Implement EFE next-seed selection as a deterministic scoring function with a
  risk-only ablation.
- Add the first evaluator pack for shape, stale-surprise rejection, self-grading
  rejection, and L/R parity fixture checks.
- Run a small benchmark pilot over `T1_shape`, `T4_claim_ceiling`, and
  `T6_surprise_boundary`.

### Fenced Until Benchmark

- IGT personality semantics.
- Consciousness readings.
- Claims that terrain voices are psychological faculties rather than processor
  slots.
- Claims that consensus-as-einselection proves social consensus or physics.
- Claims that the 64 schedule is canonical CR doctrine rather than the
  owner-approved engineering schedule for this harness.
- Any public claim that weak-model plus harness beats Fable raw before the
  code-gated benchmark says so.

## Cross-Links

- [Kernel Upgrades Leviathan](./KERNEL_UPGRADES_LEVIATHAN_2026-07-02.md): G3
  surprise stream, EFE action edge, and engine-as-channel gate design.
- [Gate Doctrine: Admissibility, Not Quality](./GATE_DOCTRINE_ADMISSIBILITY_NOT_QUALITY.md):
  deterministic gates, anti-self-grading, mutation/polarity, and claim ceilings.
- [One System, Three Perspectives](./ONE_SYSTEM_THREE_PERSPECTIVES_2026-07-02.md):
  inventory -> exposure -> independent witness -> correction -> accumulate.
- [Mesh Node Protocol v0](./MESH_NODE_PROTOCOL_V0_2026-07-02.md): sovereign
  receiving-node gates and content-addressed evidence exchange.

## Bottom Line

The wizard becomes an engine harness when every voice is a terrain slot, every
move is operator typed, every wave is a chirality pass, every replan is
surprise/EFE driven, every collapse is audited as a pointer-state survivor set,
and every claim still has to pass ordinary code gates.

The benchmark is the forcing function. If weak-model plus engine harness closes
real gate-measured distance to Fable raw, the mapping graduates from elegant
rosetta to useful architecture. If it does not, the map stays a bounded
translation candidate and the gates keep the system honest.

{"file":"projects/leviathan-current/WIZARD_QIT_ENGINE_MAP_2026-07-02.md","mappings":15,"impl_steps":8,"benchmark_defined":true}
