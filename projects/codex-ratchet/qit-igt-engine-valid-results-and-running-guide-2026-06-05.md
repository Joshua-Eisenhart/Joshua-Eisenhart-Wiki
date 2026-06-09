# QIT / IGT Engine Valid Results And Running Guide

Created: 2026-06-05
Status: wiki reference, source-grounded, diagnostic-result ledger
Project: Codex Ratchet
Active repo root: `/Users/joshuaeisenhart/Codex-Ratchet`

This page collects the valid current results and the explicit math for the
QIT/IGT terrain-operator engine lane. It is not a proof of the full model, not
an Axis0/flux/FEP/bridge admission, and not a final manifold claim.

The active lane here is:

```text
F01 = finite carrier / finite map / finite witness
N01 = order-sensitive composition / noncommutation

Current target:
  get the engines running and make the result surfaces explicit.

Later target:
  use those working surfaces as propositions for stronger proof, basin, and
  admission work.
```

The user correction this page preserves:

```text
Do not make the current lane proof-first.
Do not over-gate exploration.
Strong gates require wide testing and a large graveyard.
The formal proof process can consume working engines later.
```

## Document Shape

Read this page in five parts:

| Part | Sections | Purpose |
|---|---|---|
| Part I | `Claim Ceiling`, `The Ratchet As A Concept`, `Ratchet, Manifold, And Entropy Discipline`, `One-Line Model`, `F01 And N01` | Defines the ratchet method, the chosen root commitments, the manifold/readout status discipline, and the current claim ceiling. |
| Part II | `Axes 0-6` | Lays out the axes as exploratory surfaces with mixed evidence status, not as fixed final ontology. |
| Part III | `Carrier And Geometry`, `Geometry Search Space`, `Entropy Search Space`, `Nested PEPS2D / Hopfield Connection Geometry Results` | Lays out the candidate geometry and entropy landscape, including what replaced PEPS3D in scratch work. |
| Part IV | `Operators`, `Terrains`, `Sixteen Native Placements`, `IGT Pairing Grammar` | Gives the explicit terrain/operator math and the corrected IGT strategy grammar. |
| Part V | `Ways To Get This Model Running`, `Julia And JAX Packages / Tooling`, `Workflow Shape To Use`, `Current Best Next Runs` | Lists the runnable lanes and tooling needed to keep the model moving. |

Companion source ledger:

- `/Users/joshuaeisenhart/wiki/projects/codex-ratchet/qit-igt-source-corpus-ledger-2026-06-05.md`

This page intentionally does not turn every exploratory surface into final
canon. It separates:

```text
chosen root commitments
strong downstream pressure
current finite math
scratch diagnostic results
open candidate landscapes
future proof/admission work
```

Hermes/Grok/Gemini notes may be useful contrast, but they are not authority for
this page unless their claims are tied back to source math, result artifacts, or
repo/wiki surfaces read directly.

## Source Fence

This page was written from current wiki/repo reads, not chat memory alone.

Wiki front door read:

- `/Users/joshuaeisenhart/wiki/hermes-current/read-first.md`
- `/Users/joshuaeisenhart/wiki/hermes-current/active-plans.md`
- `/Users/joshuaeisenhart/wiki/hermes-current/skills-and-agent-rules.md`
- `/Users/joshuaeisenhart/wiki/projects/codex-ratchet/read-first.md`
- `/Users/joshuaeisenhart/wiki/wizard/00-read-first.md`
- `/Users/joshuaeisenhart/wiki/wizard/harness-consolidated/12_f01_n01_nominalist_axioms.md`
- `/Users/joshuaeisenhart/wiki/concepts/holodeck-doctrine.md`
- `/Users/joshuaeisenhart/wiki/concepts/attractor-basins-formal-reference.md`
- `/Users/joshuaeisenhart/wiki/concepts/f01-n01-root-constraint-basin-pressure.md`
- `/Users/joshuaeisenhart/wiki/concepts/basin-manifold-claim-contract.md`
- `/Users/joshuaeisenhart/wiki/concepts/igt-axes-terrain-source-extraction-2026-06-04.md`

Repo authority read:

- `/Users/joshuaeisenhart/Codex-Ratchet/AGENTS.md`
- `/Users/joshuaeisenhart/Codex-Ratchet/CODEX.md`
- `/Users/joshuaeisenhart/Codex-Ratchet/system_v5/docs/ENFORCEMENT_AND_PROCESS_RULES.md`
- `/Users/joshuaeisenhart/Codex-Ratchet/system_v5/docs/LLM_CONTROLLER_CONTRACT.md`
- `/Users/joshuaeisenhart/Codex-Ratchet/system_v5/docs/LEGO_SIM_CONTRACT.md`

Source math read:

- `/Users/joshuaeisenhart/Codex-Ratchet/system_v5/READ ONLY Reference Docs/ENGINE_64_SCHEDULE_ATLAS.md`
- `/Users/joshuaeisenhart/Codex-Ratchet/system_v5/ops/AXES_TERRAINS_OPERATORS_MANIFOLD_SOURCE_LAYOUT_20260522.md`
- `/Users/joshuaeisenhart/Codex-Ratchet/system_v5/ops/AXES_0_6_DEEP_MATH_DEFINITIONS_20260522.md`
- `/Users/joshuaeisenhart/Codex-Ratchet/system_v5/ops/QIT_ENGINE_FOUR_OPERATOR_SIGNED_MATH_20260522.md`

Companion concept read, useful but not higher authority:

- `/Users/joshuaeisenhart/wiki/concepts/igt-pattern-explicit-math-reference.md`

Companion source-corpus ledger:

- `/Users/joshuaeisenhart/wiki/projects/codex-ratchet/qit-igt-source-corpus-ledger-2026-06-05.md`

Result artifacts read:

- `/tmp/native_axis6_allowed_parity_results.json`
- `/tmp/native_axis6_allowed_jax_results.json`
- `/tmp/native_axis6_allowed_julia_results.json`
- `/tmp/engine_stage_order_parity_results.json`
- `/tmp/engine_stage_order_julia_results.json`
- `/tmp/engine_stage_order_jax_results.json`
- `/Users/joshuaeisenhart/Codex-Ratchet/system_v5/julia_carrier/scratch_jax_snapshot_20260604/new_carrier_composition_order_impact_audit_julia_results.json`
- `/Users/joshuaeisenhart/Codex-Ratchet/system_v5/julia_carrier/scratch_jax_snapshot_20260604/connection_geometry_ablation_and_precedence_audit_julia_results.json`
- `/Users/joshuaeisenhart/Codex-Ratchet/system_v5/julia_carrier/explore_julia_results.json`
- `/tmp/explore_jax_results.json`

Older source-mining ledger for ratchet / manifold / entropy deepening:

- `/Users/joshuaeisenhart/wiki/projects/codex-ratchet/ratchet-manifold-entropy-source-mining-ledger-2026-06-05.md`

Legacy core-doc tranche read for this page:

- `/Users/joshuaeisenhart/Codex-Ratchet/READ ONLY Legacy core_docs/00_MANIFEST__CORE_DOCS_ORDER_v1.md`
- `/Users/joshuaeisenhart/Codex-Ratchet/READ ONLY Legacy core_docs/a1_refined_Ratchet Fuel/AXES_0_12_MASTER.md`
- `/Users/joshuaeisenhart/Codex-Ratchet/READ ONLY Legacy core_docs/a1_refined_Ratchet Fuel/AXIS_FOUNDATION_COMPANION_v1.4.md`
- `/Users/joshuaeisenhart/Codex-Ratchet/READ ONLY Legacy core_docs/a1_refined_Ratchet Fuel/TERRAIN_MATH_LEDGER_v1.md`
- `/Users/joshuaeisenhart/Codex-Ratchet/READ ONLY Legacy core_docs/a1_refined_Ratchet Fuel/constraint ladder/Base constraints ledger v1.md`
- `/Users/joshuaeisenhart/Codex-Ratchet/READ ONLY Legacy core_docs/a1_refined_Ratchet Fuel/constraint ladder/CONSTRAINT_MANIFOLD_DERIVATION_v1.md`
- `/Users/joshuaeisenhart/Codex-Ratchet/READ ONLY Legacy core_docs/a1_refined_Ratchet Fuel/constraint ladder/GEOMETRY_ADMISSIBILITY_v1.md`
- `/Users/joshuaeisenhart/Codex-Ratchet/READ ONLY Legacy core_docs/a1_refined_Ratchet Fuel/constraint ladder/STATE_ABSTRACTION_ADMISSIBILITY_v1.md`
- `/Users/joshuaeisenhart/Codex-Ratchet/READ ONLY Legacy core_docs/a1_refined_Ratchet Fuel/constraint ladder/Engine contract v1.md`
- `/Users/joshuaeisenhart/Codex-Ratchet/READ ONLY Legacy core_docs/a1_refined_Ratchet Fuel/constraint ladder/Game theory rosetta v1.md`
- `/Users/joshuaeisenhart/Codex-Ratchet/READ ONLY Legacy core_docs/a1_refined_Ratchet Fuel/constraint ladder/Entropy contract v1.md`
- `/Users/joshuaeisenhart/Codex-Ratchet/READ ONLY Legacy core_docs/a1_refined_Ratchet Fuel/constraint ladder/Axis 0.md`

## Older Source Mining Tranche

The older docs contain useful source kernels, but they also contain stale
authority language, generated elaboration, and drifty closure claims. Use the
ledger above as source genealogy and queue material, not as proof or admission.

Guide-safe extractions from this tranche:

| Source-mined item | Current guide use | Claim ceiling |
|---|---|---|
| `entropic monism` clarification | Doctrine name only: the primitive claim is constraint on distinguishability; entropy is a later admissible measure/readout. | correction / anti-regression fence |
| pre-Axis and pre-entropy ladders | Keep carrier, geometry, transport, chirality/flux candidates, bridge, cut, and kernel separate before Axis-entry language. | process support |
| geometry-stack ratchet rule | A geometry stack is a ratchet candidate only when layer order is noncommutative on a finite witness or reversed order is excluded by a proof guard. | open probe family |
| `Xi_point`, `Xi_shell`, `Xi_hist` | Live bridge-family names for mapping geometry/history into `rho_AB`. | open bridge candidates |
| `j/k` fuzz, ring checkerboard, flux families | Queue as source-elaboration candidates. Do not promote into the main engine claim without fresh lower-layer receipts. | queued / open |
| atlas companion tranche | Keep terrain family, terrain ID, loop placement, schedule slot, `Xi` bridge, and symbolic overlay in separate columns. | current-guide patch |

Additional guide-safe extractions from the legacy core-doc tranche:

| Source-mined item | Current guide use | Claim ceiling |
|---|---|---|
| legacy manifest boundary | Treat A1 refined fuel as ladder/contract fuel and A2 high-entropy feed as intake, not direct admission. | source genealogy |
| base constraint ban list | Expand F01/N01 consequences without turning BC01-BC12 into new root constraints. | anti-smuggling fence |
| constraint-manifold derivation | No canonical points, no total compatibility, no connectedness, no metric, no coordinates, no dimension assertion by default. | process support |
| geometry admissibility | Geometry must be finite relation/path/transport/obstruction structure before any metric or coordinate overlay. | anti-smuggling fence |
| state abstraction | State is an abstraction over finite relation-instances, not primitive identity. | density/state wording |
| engine contract | Engine-like status needs finite cycle, closure witness, obstruction witness, and comparison criterion. | engine-candidate fence |
| entropy contract | Scalars/entropies are finite-scoped descriptive readouts, not identity/admission/optimization laws. | entropy-readout fence |
| game rosetta | IGT/game labels are removable overlays and cannot import payoff, utility, rationality, or selection force. | overlay fence |
| terrain ledger | Terrain = topology x engine_type; loop selects carrier curve; operators are not terrains. | source lock with conflict note |
| Axis 0 options | Axis 0 is a candidate perturbation-response functional, not "entropy" as a slogan. | open bridge candidate |
| v4 axis/terrain/order companions | Preserve Axis 3/4/5/6 witness seats, native-vs-visiting terrain/operator conflict, terrain naming conflicts, and 64-grid as lookup/index rather than schedule truth. | reconciliation queue / guide hardening |
| v5 ops source-authority packets | Current equivalents for missing atlas companions: separate 16 ordered tokens from 16 terrain placements; use `A1 x A2 x A5 x A6` for token identity; keep Axis 6 token precedence separate from QIT action side. | source_math / audit fence |

### Legacy Core-Doc Constraint Discipline

The legacy refined-fuel corpus is useful because it is more explicit about what
must not be smuggled into the lower layers. It is also risky because several
files use stronger "canon/proven" language than this current guide can inherit.

Use the legacy core docs this way:

```text
recover distinctions
recover candidate formulas
recover old conflicts
recover anti-smuggling rules
do not inherit old promotion labels without current evidence
```

Do not use them this way:

```text
prove the current engine
declare all axes settled
override current source-locked operator/terrain math
turn generated rosetta language into kernel truth
```

### Axis Labels Are Overlay Surfaces

The clearest old-source correction is:

```text
kernel/plain math first
axis/Jung/IGT/taijitu labels second
```

The axes are not all fixed final math. They are a family of slices, probes, and
possible explanations over the constraint surface. A given axis can have several
legitimate descriptions at once:

| Lens | What it may explain | What it cannot do |
|---|---|---|
| QIT / channel lens | finite states, channels, generators, order gaps, cut states | import meaning from labels |
| geometry lens | carrier, quotient, path, connection, obstruction, holonomy | assume metric/coordinates/dimension at the root |
| thermodynamic lens | entropy readout, mixing, contraction, reference-engine comparison | prove the QIT engine is Carnot/Szilard |
| information lens | distinguishability, mutual information, coherent information, prediction residual | replace the finite map or bridge object |
| IGT/game lens | strategy grammar, win/loss naming, classical decision-rule analogy | impose payoff, preference, rationality, or ranking |
| Jung lens | operator-role overlay and perception/cognition language | modify the operator math |
| taijitu/chirality lens | handedness, paired loops, orientation reversal | prove L/R without finite invariant and controls |

The current guide can say:

```text
Axis language is a removable explanatory overlay over finite maps.
```

It must not say:

```text
Axis labels themselves prove the kernel structure.
```

### Base Constraint Consequences

F01 and N01 are the chosen root commitments. They are not "forced by the
system"; they are the roots the project chooses to explore. The older base
constraint ledger helps spell out what those roots forbid downstream:

```text
no completed infinity of distinguishables
no commutation-by-default
no primitive identity
no primitive equality-as-substitutability
no global total order
no closure-by-default
no label-only equivalence
no base probability primitive
no base metric, norm, distance, coordinate, or chart
no optimization or utility primitive
no semantic smuggling by synonym
```

These are not twelve new root axioms. They are useful guardrails for avoiding
Cartesian, Platonic, Kantian, payoff-first, metric-first, or object-first
imports while the ratchet is still climbing from finite order-sensitive
distinctions.

### Geometry Admissibility From The Legacy Ladder

The older manifold and geometry contracts give a clean rule:

```text
geometry is admissible first as finite relation/path/transport/obstruction
structure, not as a coordinate space.
```

A guide-safe geometry checklist:

| Required for a geometry claim | Meaning |
|---|---|
| finite carrier tokens | The object is not an unbounded background. |
| finite relation instances | Geometry is expressed as declared relations, not hidden continuum assumptions. |
| indexing relation | State/process tokens are bound to carrier tokens without assuming unique identity. |
| compatibility relation | Local relation is explicit and not total by default. |
| path tokens and endpoints | Paths are finite objects with declared support. |
| transport support | Any path claim is backed by finite transport chains. |
| obstruction witness | Nonflattenability is shown by distinguishable composites or blocked flattening. |
| no metric/coordinate/dimension primitive | Metrics, charts, dimensions, and embeddings are later removable overlays or derived structures. |

This is why Bloch-like readouts can matter while the Bloch sphere remains under
test. A Bloch vector is a useful quotient/readout; it is not automatically the
primitive geometry.

### Engine-Like Mechanics Admission Fence

"Engine" is allowed as a working name, but the legacy engine contract says an
engine-like object needs more than a cycle label:

```text
finite cycle/path object
explicit closure witness
declared domain
transport-comparison criterion
nontrivial obstruction witness
negative/control condition
```

Therefore:

```text
running engine surface = finite maps run and produce observables
engine-like candidate = cycle plus obstruction structure is explicit
admitted engine mechanics = comparison controls show the obstruction matters
```

This matches the current project mode: get the engines working as propositions,
then use those working surfaces to drive stricter proof/admission work later.

### IGT And Game Overlay Fence

The old game rosetta is strict: IGT/game terms are overlay terms. They do not
grant kernel truth.

Good use:

```text
WinWin   = maximax-style overlay
WinLose  = maximin-style overlay
LoseWin  = minimax-style overlay
LoseLose = minimin-style overlay

Losing is a legitimate strategy in this overlay.
```

Bad use:

```text
WIN/LOSE labels imply utility, payoff, rationality, optimality, or admission.
```

The mapping must remain explicit:

```text
source token -> overlay token -> scope -> current finite observable
```

If the observable is not defined yet, say so. The IGT grammar can be real as a
strategy/readout grammar before it is a proved payoff or game-theory semantics.

### Historical Axis-6 Notation Collision

One older terrain ledger writes Axis 6 as:

```text
UP_A(rho)   = A rho
DOWN_A(rho) = rho A
```

The current source-locked terrain/operator guide uses Axis 6 as native
placement/composition order:

```text
operator-first = Phi_T(O(rho))
terrain-first  = O(Phi_T(rho))
```

Do not silently merge these. For this guide:

```text
current kernel = terrain/operator composition order
older A rho / rho A = historical sidedness notation unless reconciled
```

The safe statement is:

```text
Axis 6 is an order/sidedness surface. The currently runnable finite map is the
terrain/operator composition-order version.
```

### Axis 0 Is A Perturbation-Response Search Lane

The legacy Axis 0 material is useful because it does not reduce Axis 0 to a
bare entropy label. It frames Axis 0 as a correlation response under
perturbation:

```text
allostatic  = correlation diversity increases under perturbation
homeostatic = correlation deviation is suppressed under perturbation
```

Generic candidate:

```text
A0(rho) = d/deps D(N_eps(rho)) at eps = 0
```

where:

```text
N_eps = finite perturbation channel family
D     = explicit finite correlation/diversity functional
```

Candidate D objects:

| Candidate | Plain role |
|---|---|
| MI spread entropy | Does perturbation spread pairwise correlations across the system? |
| local/global MI ratio | Does perturbation globalize or localize correlations? |
| coherent information over cuts | Does a signed quantum-information resource survive or spread? |
| boundary reconstruction delta | Does a shell/boundary encoding preserve or lose the chosen observable? |

Axis 0 remains open until the perturbation family, finite state/cut object, and
functional are all explicit.

#### JK Fuzz / Gravity Bridge Candidate

Owner correction:

```text
The fuzz field has to be entanglement information.
It is finite at any witness, can grow across refinement, and can live on every
nested geometry layer.
```

Guide-safe candidate shape:

```text
F_jk(layer, support_point) = finite admissible-continuation field
Xi_fuzz = weighted map from that field into rho_AB
Phi_0 = Axis 0 readout on the resulting cut state
```

In formulas:

```text
Xi_fuzz(n,x,h) = sum_jk p_nx(j,k | h) rho_AB(n,x,j,k)
```

where the weights may later be tested as FEP/prediction-error, compression,
attractor-proximity, boundary, or history-window weights.

Current fence:

```text
This is the path for processing the gravity/Axis0 model, not an admitted
gravity result. The gravity reading becomes testable only after the finite fuzz
field, its growth/refinement rule, the cut states, and the Axis 0 readout are
all explicit.
```

### v4 Axis / Terrain / Order Companion Tranche

The next source-mining pass read the five queued companion packets under:

```text
/Users/joshuaeisenhart/Codex-Ratchet/system_v4/docs
```

Files:

```text
AXIS_3_4_5_6_QIT_MATH.md
TERRAIN_LAW_LEDGER.md
ENGINE_GRAMMAR_DISCRETE.md
TERRAIN_NAMING_MATH_LEDGER.md
MATH_CHART_CORRELATION_MATRIX.md
```

Use these as source genealogy and reconciliation material. They contain useful
math seats, but they also contain old `LOCKED` / `PROVEN` / `canonical` style
labels that do not automatically carry into this current guide.

#### Axis 0 Seat Collision

The v4 companion docs preserve several different Axis 0 seats:

| Axis 0 seat | Formula or object | Safe current status |
|---|---|---|
| torus latitude entropy | `S(rho_bar(eta)) = -cos^2 eta log cos^2 eta - sin^2 eta log sin^2 eta` | geometry/chart readout |
| hemisphere threshold | `b_0 = sgn(cos(2 eta)) = sgn(r_z)` | discrete chart bit |
| correlation entropy | owner correction: Axis 0 can be negative and is not just VN entropy | open correlation-functional lane |
| post-bridge cut entropy | `Xi : geometry/history -> rho_AB`, then `S(A|B)`, `I_c`, `I(A:B)` | bridge-dependent lane |

Do not collapse these into one sentence. The safe statement is:

```text
Axis 0 is an open bridge/readout family with several candidate seats.
```

#### Axis 3/4/5/6 Witness Table

| Axis | Witness seat from v4 docs | Current guide use |
|---|---|---|
| Axis 3 | fiber loop is density-stationary; base-lift loop changes density | strong geometric readout for inner/base distinction |
| Axis 4 | `Phi_UEUE` versus `Phi_EUEU`; inductive/deductive terrain walks | order-class witness, traversal order still needs reconciliation |
| Axis 5 | `Ti/Te` dephasing kernels versus `Fi/Fe` rotation kernels | strong operator-family kernel |
| Axis 6 | operator-first versus terrain-first; v4 also gives `b_6 = -b_0 b_3` | precedence/order-side candidate check, not a new operator identity |

Fiber/base formulas:

```text
gamma_f^s(u) = psi_s(phi_0 + u, chi_0; eta_0)
rho_f^s(u) = rho_f^s(0)

gamma_b^s(u) = psi_s(phi_0 - cos(2 eta_0)u, chi_0 + u; eta_0)
rho_b^s(u) = 1/2(I + r(chi_0 + u, eta_0).sigma)
```

#### Native 16 Versus Visiting / 64 Grid

The v4 terrain-law docs say each terrain can receive all four operators in a
subcycle, with operators marked as `native` when their frame matches the terrain
and `visiting` otherwise.

The current runnable guide surface is narrower:

```text
native 16 placements = current source-locked JAX/Julia parity lane
visiting rows        = candidate cross-affinity / 64-grid extension lane
64 grid             = lookup/index surface, not automatic runtime truth
```

Do not use the v4 all-operator grid to overwrite the current sixteen native
placement table. The next reconciliation should ask:

```text
Which visiting/cross-affinity rows have explicit finite maps?
Which are merely schedule/index cells?
Which have controls?
Which are blocked from current native-lane claims?
```

#### Terrain Naming Conflict Table

| Topology | Type-1 name | Type-2 name | Conflict to preserve |
|---|---|---|---|
| Se | Funnel | Cannon | Cannon is less anchored than Funnel in the mined notes. |
| Ne | Vortex / Spiral-in | Spiral-out | "Vortex" appears near multiple topology stories; tie to tangential circulation. |
| Ni | Pit | Source | Pit/source is stable, but older notes also use vortex-like aliases. |
| Si | Hill | Basin / Citadel | This guide currently uses Citadel; Apple Notes also use Basin. Do not erase either until source reconciliation closes it. |

Older source sentence, fenced:

```text
Type-1 and Type-2 terrains are identical Lindblad dissipative structures
distinguished solely by opposite Weyl chirality of the Hamiltonian.
```

Current guide status:

```text
historical hypothesis / source-mined kernel
```

It must not be promoted unless current finite maps and result artifacts show
the same Lindblad structure with only Hamiltonian sign flipped.

#### IGT Gradient / Ascent Fence

The v4 naming ledger preserves the owner-grounded gradient role language:

| Token | Terrain story | Role language |
|---|---|---|
| `TeSi` | Si hill | ascent / `WIN` maximization |
| `SiTe` | Si hill | descent / `win` minimization |
| `TeNi` | Ni pit | ascent / `lose` minimization |
| `NiTe` | Ni pit | descent / `LOSE` maximization |

This language is allowed as role language only. It becomes math only when the
row names:

```text
functional
terrain target
operator/terrain composition
signed-change or monotonicity witness
negative/control case
```

This keeps the intended social/semantic intuition alive without turning
`Te` itself into a gradient-ascent operator.

### v5 Ops Source Authority Mining Tranche

The current v5 ops packets are the active source-authority equivalents for the
missing companion names in the older atlas queue:

```text
AXES_TERRAINS_OPERATORS_MANIFOLD_SOURCE_LAYOUT_20260522.md
AXES_0_6_DEEP_MATH_DEFINITIONS_20260522.md
QIT_ENGINE_FOUR_OPERATOR_SIGNED_MATH_20260522.md
TERRAIN_GENERATOR_SOURCE_LAYOUT_20260522.md
QIT_ENGINE_SOURCE_AUTHORITY_AUDIT_20260522.md
QIT_ENGINE_MANIFOLD_AUDIT_FREEZE_20260522.md
```

Guide-safe kernels:

| Kernel | Current guide use | Claim ceiling |
|---|---|---|
| `16 ordered tokens = A1 x A2 x A5 x A6` | Token identity is topology x operator-family x precedence. | source_math |
| `A3 x A4 x A5 x A6 = 8 paired loop-placement signatures` | Axis 3/4 place tokens into path/order signatures; they do not identify all 16 tokens. | source_math |
| `16 terrain placements = 4 terrain families x 2 Weyl sheets x 2 path classes` | Terrain placements are generator/path objects, not ordered operator tokens. | source_math |
| Axis 6 has two rows of meaning | Record both token precedence and QIT action side: `L_A(rho)=A rho` versus `R_A(rho)=rho A`. | source_math / audit requirement |
| terrain-only runtime evidence | Useful as terrain-only evidence; quarantined for operator-axis placement or promotion. | audit fence |

Do not use this tranche as proof that the engine, bridge, Axis 0, flux, or
final manifold is admitted. The freeze surface still says the next admissible
move is source-authority/runtime-conformance work, not another full-engine run.

## Claim Ceiling

Everything below is fenced by the strongest result file it cites.

| Surface | Current status |
|---|---|
| 16 native Axis-6 placement parity | `scratch_diagnostic`, `promotion_allowed=false`, `formal_admission_allowed=false` |
| Engine stage order parity | `scratch_diagnostic`, `promotion_allowed=false`, `formal_admission_allowed=false` |
| Nested PEPS2D/Hopfield connection carrier ablation | scratch diagnostic only |
| Wide F01/N01 exploration | `exploration_probe`, `promotion_allowed=false` |
| Hurwitz minimality prelim | `scratch_diagnostic`, `promotion_allowed=false`, `formal_admission_allowed=false` |
| Octonion admissibility prelim / J3(O) observable fork | `scratch_diagnostic`, `promotion_allowed=false`, `formal_admission_allowed=false`; JAX parity within 1e-9 |
| Sedenion / zero-divisor branch | `scratch_diagnostic`, `promotion_allowed=false`, `formal_admission_allowed=false`; algebra/carrier-break facts only, not carrier admission |
| JAX mirror of wide exploration | partial audit lane only |
| Basin proof | not present here |
| Full layer completion | not present here |
| Axis0/flux/FEP/bridge/physics/final manifold admission | blocked |

Good sentence:

```text
The current artifacts show finite scratch maps where the source-locked
terrain/operator composition order is load-bearing and Julia/JAX agree on the
16 native placements and engine-stage order tests.
```

### Hurwitz / Density-Lifted Carrier Fence

Read-only result artifact:

```text
/Users/joshuaeisenhart/Codex-Ratchet/system_v5/julia_carrier/hurwitz_minimality_prelim_julia_results.json
/Users/joshuaeisenhart/Codex-Ratchet/system_v5/julia_carrier/octonion_admissibility_prelim_julia_results.json
/Users/joshuaeisenhart/Codex-Ratchet/system_v5/julia_carrier/octonion_admissibility_prelim_jax_results.json
```

Guide-safe kernel:

```text
The base object is state-on-an-algebra: a positive normalized
probe-functional over the probe algebra under test.

Writing rho as a complex matrix already commits to a complex finite *-algebra
representation. Therefore rho-first means probe-equivalence first, not C or C^2
as a forced root.

Inside the Hurwitz normed-division-algebra frame, N01 plus associativity plus
minimality as proof discipline selects H as the scratch survivor:
R and C fail N01, H passes N01 and associativity at dim 4, and O keeps
noncommutative pressure but fails associativity at dim 8.

The octonion prelim tightens that fence: with associativity required, the
survivor set is {H}; without associativity required, the survivor set is {H,O}.
O passes N01 and normed division, fails associativity, and remains alternative
and power-associative.
```

Carrier fence:

```text
This supports the local neighborhood C^2 ~= H, SU(2) ~= Sp(1), and the
Pauli/even-Clifford/quaternion alignment. Quaternion is not a falsifying
alternative to spinor in this lane. The Hopf readout can be written as
q -> q i qbar or as psi -> <psi|sigma|psi>.
```

Density/lifted-data fence:

```text
rho is S / ~_M made concrete on the complex-QIT route: it encodes exactly the
probe-distinguishable information read by Tr(rho M). Two preparations with the
same rho are indistinguishable to those probes.

For the C^2 route, density-state space gives the Bloch ball, pure states give
the projective S2 readout, and the spinor/purification lift gives S3 over S2
via Hopf. When holonomy, sign, path, phase, or interference matters, keep
lifted psi or q in H plus path data. rho = |psi><psi| is invariant under
psi -> -psi, so rho-only consumers do not see the 360/720 lifted-sign
distinction.
```

Claim ceiling:

```text
diagnostic only; no proof, admission, canon, engine, bridge, Axis0, basin, or
global carrier-exclusion claim. Operator algebras over R/C, Choi/process
carriers, finite groups, spectral triples, higher-qudit routes, and
nonassociative octonionic pressure remain outside this narrow selection frame.
Alternative finite probe algebras remain live outside the Hurwitz +
associativity seam.
```

Octonion / non-associativity fence:

```text
Associativity is not a root constraint. In the observable/probe-side reading,
the owner correction "a=a iff a~b" is a probe-equivalence rule: a~b means no
active probe separates the states. Therefore (ab)c = a(bc) is itself an
equality claim and is allowed only when the active finite probe family cannot
distinguish the two bracketings:

((ab)c) ~_M (a(bc))

So non-associativity is a candidate higher-order order structure:

ab != ba          sequence sensitivity
(ab)c != a(bc)   bracketing sensitivity

Observables naturally form a Jordan algebra under symmetric product; that
observable algebra is commutative but generally non-associative. The
operator/composition side is the lane that conventionally requires associative
closure.

Part B of the prelim records J3(O) as formally real, Jordan commutative,
Jordan non-associative, power-associative, rank-1-idempotent-bearing, and
27-dimensional over R.

O is live when associativity is not required and the observable/Jordan side is
primary. H remains the minimal associative survivor. Exclude O only in lanes
that explicitly require associative operator closure. Arbitrary
non-associativity is not included by default; the live O lane is disciplined by
alternativity and power-associativity.
```

Sedenion / zero-divisor fence:

```text
The owner-supplied sedenion source opens a post-octonion branch, not a carrier
promotion.

Sedenions are 16-dimensional Cayley-Dickson-after-O algebras. They keep
noncommutation and nonassociativity, but unlike O they are not alternative and
they contain zero divisors.

So the safe ratchet reading is:
  H = minimal associative noncommutative branch
  O = nonassociative but disciplined alternative / Jordan observable branch
  S = post-octonion zero-divisor branch

The S branch is more naturally routed to fuzz, branch-kill, annihilation,
graveyard, or cancellation geometry than to a clean stable carrier claim unless
an explicit finite result proves otherwise.

Zero-divisor readout candidate:
  x != 0, y != 0, xy = 0

Probe-relative reading:
  x not~_M 0
  y not~_M 0
  xy ~_M 0

Possible JK fuzz hook:
  K_ZD(l,x) = {((j,k),(j',k')) : a_jk a_j'k' = 0}

Local scratch diagnostic result receipt:
  Julia:
    /Users/joshuaeisenhart/Codex-Ratchet/system_v5/julia_carrier/sedenion_break_prelim_julia_results.json
  JAX parity mirror:
    /Users/joshuaeisenhart/Codex-Ratchet/system_v5/julia_carrier/sedenion_break_prelim_jax_results.json

  classification = scratch_diagnostic
  promotion_allowed = false
  formal_admission_allowed = false
  claim ceiling = no forcing proof, basin, admission, engine, bridge, Axis0, or
                  manifold closure claim

  ladder_stops_at_O = true
  sedenion_is_normed_division = false
  sedenion_zero_divisors = true

  O control:
    alternative_holds = true
    norm_multiplicative_holds_in_probe = true
    zero_divisors_in_search = false
    octonion_cd_vs_prior_max_abs_diff = 0.0

  S diagnostic:
    alternative_holds = false
    flexible_holds = true
    power_associative_holds = true
    norm_multiplicative_holds_in_probe = false
    zero_divisors_in_search = true
    max_norm_mult_residual = 2.0000000000000004
    max_associator_xxy ~= 31.46164835554498
    plus_zero_divisor_count = 84
    signed_zero_divisor_count = 1344
    witness: (e1 + e10)(e5 + e14) = 0, with nonzero inputs of norm sqrt(2)

  JAX parity:
    designated critical scalar/boolean fields within 1e-9
    raw all-scalar witness-index differences are not load-bearing

Do not cite this branch for engine, Axis0, gravity, basin, manifold, or carrier
admission. The tested facts are algebra/carrier-break facts only; the JK-fuzz
branch-kill mapping has not been tested.
```

Bad sentence:

```text
The model is proven, admitted, or a universal basin.
```

## The Ratchet As A Concept

The ratchet is not only a repo workflow. It is one of the core ideas of the
model.

The ratchet says:

```text
choose the smallest root constraints
derive only the pressure those constraints actually create
test many possible survivors
keep the graveyard
let surviving structure constrain the next layer
never jump farther than the evidence supports
```

This matters because the engine is not supposed to enter as a designed object.
The engine is supposed to appear later as a survivor of repeated narrowing.

Bad method:

```text
decide the final engine, then build everything toward that engine
```

Better method:

```text
start from minimal commitments, test many finite order-sensitive candidates,
and let the survivors narrow what the next layer is allowed to be
```

The graveyard is not a side effect. The graveyard is part of the result. Strong
gates require wider exploration, because most candidates should die.

### Root Commitments, Not Forced Claims

F01 and N01 are chosen root constraints. They are not "forced by the
constraints." They are the commitments the project begins from.

F01:

```text
Every claim-bearing witness must be finite.
```

Plainly:

```text
No completed infinity can carry a promoted result.
If a claim needs an infinite object that cannot be finitely witnessed, it is not
admissible in this system.
```

N01:

```text
Order must be able to matter.
```

Plainly:

```text
If every operation commutes with every other operation, the system has erased
the distinction the project is trying to study.
```

Together:

```text
finite witnesses + order-sensitive operations
```

That is the root. Everything else is downstream pressure, candidate structure,
or an admitted result from a specific run.

Bad sentence:

```text
F01 is forced by the constraints.
```

Good sentence:

```text
F01 is one of the chosen root constraints.
```

Bad sentence:

```text
Chirality is already proven by F01 and N01.
```

Good sentence:

```text
Chirality is a strong downstream emergence candidate because finite
order-sensitive systems naturally pressure orientation, handedness, double-cover
behavior, and noncommuting composition. It still needs explicit survivor
evidence.
```

### Ratchet Step

Each ratchet step has this shape:

```text
input layer L_n
constraints from F01 + N01 + admitted survivors so far
candidate next structures C_1 ... C_k
finite tests and negative controls
graveyard of killed candidates
survivors S_1 ... S_m
next layer L_{n+1} is constrained by the survivors, not by preference
```

So a good result does not only say:

```text
candidate X worked
```

It says:

```text
candidate X survived these finite tests
candidate Y died for this reason
candidate Z is still open
the next layer is now constrained by X and by the death of Y
```

### Surface Versus Ladder

Important correction from older source docs:

```text
F01 and N01 constitute the admissible surface M(C).
They are simultaneous constraints, not a causal ladder by themselves.
```

So when this page uses a ladder, it means:

```text
an epistemic / build-order ladder for finite agents
```

not:

```text
the ontology is literally a one-way sequence where F01 causes N01 causes spinors
causes chirality causes engines
```

The surface is simultaneous. The read/build process is ordered because finite
agents need an order in which to explore, kill, record, and ratchet.

### Minimal-Assumption Ladder

This ladder is not final canon. It is the current way to organize how the two
root commitments may pressure increasingly structured candidate layers. It is a
working build-order and explanation surface, not proof that every later object
is already forced by the root commitments.

| Rung | What is being added | Why it is considered | Status |
|---:|---|---|---|
| 0 | Undifferentiated candidate field | Nothing has been admitted yet. | Starting point |
| 1 | F01 finite witness rule | The project refuses completed-infinity carriers as claim-bearing objects. | Chosen root |
| 2 | N01 order-sensitivity rule | The project refuses fully commuting collapse as the interesting object. | Chosen root |
| 3 | Finite distinguishability | A finite witness must distinguish states, probes, paths, or operations somehow. | Strong pressure |
| 4 | Finite probe/operator/path set | Distinguishability must be tested by finite probes and finite paths. | Strong pressure |
| 5 | Density-state style objects | Probe-relative identity pushes toward quotient/equivalence-class state language; mixture, uncertainty, projection, and distinguishability are naturally carried by density matrices or density-like finite states. | Likely emergent |
| 6 | Spinors over raw vectors | Spinors carry phase, orientation, double-cover behavior, and nontrivial transformation better than ordinary Cartesian vectors. | Strong candidate |
| 7 | L/R chirality | Once spinor-like structure and order-sensitive composition appear, handedness becomes a natural survivor candidate. | Strong emergent candidate |
| 8 | Quaternion / SU(2) / Spin language | Quaternionic and spin-group language is the same local carrier neighborhood for rotation, handedness, and double-cover behavior. | Strong candidate |
| 9 | Clifford / anti-commutation | Noncommuting finite generators can sharpen into anti-commuting generator families later. | Likely candidate, not root |
| 10 | Geometry support | S3, Hopf, nested tori, spinor networks, or related finite carriers may organize survivor states. | Open landscape |
| 11 | Connection surface | A bond/connection field can become the geometry the states live on, not a decoration laid over geometry. | Current candidate |
| 12 | Terrain/operator maps | Once a finite carrier and states exist, terrain maps and operator maps become testable finite channels. | Candidate math layer |
| 13 | IGT strategy grammar | Win/loss grammar can be mapped after engines and terrains have real dynamics. | Downstream, not root |
| 14 | Basin / engine mechanics | If many starts flow into a stable survivor with boundary, invariant, escape cases, and killed alternatives, engine mechanics may be called emergent. | Not yet admitted |

Discipline:

```text
Do not promote a rung because it is beautiful.
Promote only what survives the finite tests and controls for that rung.
```

### Pressure Status

These are not equal-status claims. They are separated so the page does not
smuggle certainty.

Strongly pressured by F01 + N01:

| Candidate | Why it is pressured |
|---|---|
| Finite state spaces | F01 rejects completed-infinity carriers as claim-bearing witnesses. |
| Finite operators and paths | A witness must be inspectable and rerunnable. |
| Noncommuting composition | N01 makes order-sensitive composition load-bearing. |
| Density matrices or density-like states | They naturally hold mixture, projection, distinguishability, entropy, and probe-equivalence classes in a finite carrier. |
| Spinors | They express phase, handedness, and double-cover behavior better than raw vectors. |
| Chirality | Order-sensitive spinor systems naturally make left/right handedness a candidate survivor. |
| Quaternionic / SU(2) / Spin structures | They encode finite rotations and double-cover geometry in a way aligned with spinor pressure. |
| Clifford-like generator systems | Noncommuting finite generators can organize into anti-commuting families later. |
| 720-degree behavior | Spinor/double-cover structure naturally distinguishes a 360-degree turn from a 720-degree return. |

Open or flexible:

| Candidate | Why it stays open |
|---|---|
| Exact Hopf chart | Hopf structure may matter, but a particular coordinate chart is not root. |
| Nested Hopf tori | Strong current candidate, but still must be tested against controls. |
| Quantum Hopfield connection surface | Strong current candidate for the post-PEPS3D scratch carrier, but not a root axiom. |
| Exact terrain generators | The channels must be explicit finite maps, and alternatives should be tested. |
| Axis 0 bridge | Still needs more than symbolic meaning. |
| Axis 4 pure QIT version | Needs a formulation that is not just inherited from Jung/IGT language. |
| Layer ordering | The order is itself an object to test. |
| Spinor network layers | Likely direction, but there are multiple finite network forms. |

Possibly excluded or demoted:

| Candidate | Why it may be demoted |
|---|---|
| Primitive Cartesian vector ontology | Cartesian vectors may be too object-first and too flat for the root constraints. |
| Bloch sphere as primitive ontology | A Bloch-like readout is useful, but the ordinary Bloch sphere may be a projection/control surface rather than the real carrier. |
| Scalar PEPS/geometry labels | Labels do not carry finite noncommuting math by themselves. |
| Win/loss as physics before engine formation | IGT labels are downstream grammar unless tied to an explicit observable. |

### Chirality Status

The user is not wrong to think chirality may be emergent from the constraints.
The careful version is:

```text
F01 + N01 do not logically force a final chiral engine by themselves.
But they strongly pressure finite noncommuting transformation systems, and those
systems very naturally admit handedness, orientation reversal, double-cover
behavior, and L/R spinor structure.
```

So chirality is not a decorative add-on. It is one of the strongest downstream
survivor candidates. It becomes an admitted result only when a finite carrier
shows:

```text
left/right or clockwise/counterclockwise distinction
same local rule, opposite handedness
nonzero order gap or commutator signal
negative control where handedness is erased
observable change when handedness is removed or swapped
receipt/result artifact
```

Source-native caveat:

```text
Do not collapse L/R into only H_L = +H0 and H_R = -H0.
The older source handoff requires more than an H-sign flip:
  Hamiltonian sign
  sigma-/sigma+ terrain law swap where relevant
  terrain projector differences
  fiber/base loop ownership
  mirrored finite readout signatures
If those do not matter, chirality has collapsed into trivial relabeling.
```

Good phrase:

```text
chirality is a live emergent consequence candidate of F01+N01
```

Bad phrase:

```text
chirality is already forced/proven
```

### The Seven Axes As Exploration Surfaces

The axes should not be treated as one finished ontology. They are a set of
candidate degrees of freedom that may or may not close into pure QIT math.

For each axis, keep six things separate:

```text
1. the split it makes
2. the current source math, if any
3. the Jung correlation layer
4. the IGT correlation layer
5. the taijitu / symbolic correlation layer
6. what is still undefined in pure QIT
```

An axis can be useful before it is final. But it cannot be promoted from symbol
to math until it has a finite map, observable, invariant, or killed control.

Minimal axis audit table:

| Axis | Current split | Current math seat | Jung layer | IGT layer | Taijitu / symbolic layer | Pure QIT status |
|---|---|---|---|---|---|---|
| A0 | Ne/Ni vs Se/Si | entropy polarity, cut-state kernel candidate, sign of vertical/Hopf coordinate candidate | irrational field polarity / perception polarity | not yet a strategy map | enclosing yin/yang side | open, needs bridge functional |
| A1 | Se/Ni vs Ne/Si | terrain branch bit | attitude/branch style candidate | quadrant branch candidate | cross-pair split | partly defined only through A1 x A2 terrain table |
| A2 | Ne/Se vs Si/Ni | direct vs conjugated frame | orientation/frame candidate | direct/conjugated strategy side | direct/conjugate mirror | source-grounded for terrain frames |
| A3 | fiber vs lifted base | Hopf path split | base/fiber attention candidate | path role candidate | vertical/fiber vs horizontal/base | source-grounded in current carrier math |
| A4 | loop order | U E U E vs E U E U in source language | deductive vs inductive loop candidate | engine sequencing candidate | cycle orientation | needs pure QIT restatement |
| A5 | operator family | Ti/Te vs Fi/Fe, dephasing vs unitary rotation | judging operator family | strategy operator family | judging polarity | source-grounded as operator family |
| A6 | precedence/action side | `T_tau(O(rho))` vs `O(T_tau(rho))`, order gap Delta | up/down placement, not new operator | signed placement grammar | ascent/descent language only if functional is named | source-grounded as composition order |

Important: Axis 6 is not a plus/minus version of the operator. It is placement.

```text
up   = operator first = T_tau(O(rho))
down = terrain first  = O(T_tau(rho))
Delta_{tau,O}(rho) = T_tau(O(rho)) - O(T_tau(rho))
```

### Different Ways To Explain Each Axis

The same axis should have multiple explanatory handles, because each handle
tests a different possible interpretation.

Axis 0:

```text
thermodynamic: entropy polarity / enclosure side
information: what cut or conditional state changes the available information
geometric: vertical/Hopf polarity or enclosing side
QIT: candidate bridge/cut functional over density states
IGT: not directly strategy yet
open question: what finite bipartite object makes A0 measurable
```

Axis 1:

```text
terrain grammar: {Se,Ni} vs {Ne,Si}
information: open/compression side versus closed/circulation side candidate
geometric: branch bit in the terrain square
IGT: quadrant branch
open question: whether A1 has standalone QIT meaning or only exists with A2
```

Axis 2:

```text
frame grammar: direct {Se,Ne} vs conjugated {Ni,Si}
geometric: original frame versus transported/conjugated frame
QIT: rho versus V^dag rho V style frame move
IGT: direct versus mirrored strategy surface
settled part: source math gives the direct/conjugated terrain frame
```

Axis 3:

```text
geometric: Hopf fiber path versus lifted-base path
information: phase/fiber update versus base-state update
QIT: whether rho changes under the path or only the phase chart changes
IGT: path role, not a win/loss rule by itself
settled part: current source math has explicit fiber and lifted-base paths
```

Axis 4:

```text
loop grammar: U E U E versus E U E U
engine grammar: one engine order versus the chiral partner order
information: update/evidence order candidate
QIT: not yet clean enough; needs a pure density/channel restatement
open question: whether Axis 4 is a source schedule artifact or a real survivor
```

Axis 5:

```text
operator grammar: Ti/Te dephasing versus Fi/Fe rotations
QIT: dissipative contraction versus unitary spectral motion
geometry: projection/pinching versus rotation/wave
IGT: operator family used by the strategy grammar
settled part: explicit channels exist
```

Axis 6:

```text
composition grammar: operator-first versus terrain-first
QIT: noncommuting channel order
geometry: does the operator act before the terrain moves the state, or after
IGT: signed placement token
settled part: the operator map itself does not change
```

### Geometry Search Space

The geometry layer should be searched as a landscape, not treated as a single
preselected answer.

| Geometry candidate | What it gives | Why it matters | Main risk / control |
|---|---|---|---|
| Finite graph / cell complex | Finite adjacency, paths, loops | Minimal finite carrier | May be too generic and fail to pressure spinor/chirality |
| S3 | Compact finite-sampled 3-sphere geometry | Natural home for SU(2), Hopf, spinors | Plain S3 effect may masquerade as nesting |
| Hopf fibration | Fiber/base split, linked circles | Natural way to express phase fiber over base geometry | Must not confuse Hopf artifact with nested-geometry signal |
| Nested Hopf tori | Repeated linked torus structure | Current candidate for nesting-specific geometry | Needs flat/plain controls |
| Quaternionic geometry | Finite rotations, handedness, noncommuting multiplication | Aligned with spinor/SU(2) pressure | Must test against complex-only control |
| Clifford geometry | Generator algebra, anti-commutation, spinor modules | Likely later-stage organization of N01 pressure | Anti-commutation should emerge later, not be assumed at root |
| Spin group / Spin(n) | Double cover of rotation groups | Makes spinor-over-vector pressure explicit | Need finite implementation, not group-name decoration |
| G2 | Exceptional geometry with octonionic flavor | Possible later candidate for rich noncommuting orientation structure | High risk of decorative exceptional-language overclaim |
| Spin(7) | Higher-dimensional spin geometry | Possible larger spinor-geometry candidate | Must show finite observable need, not prestige |
| G-structure candidates | Structured frames and admissible reductions | Possible later carrier for geometry constraints | High overclaim risk without explicit finite maps |
| Connection surface / Hopfield bonds | Geometry as relation/bond field, not background container | Current post-PEPS3D direction: bonds become the surface | Must show ablation changes observable |
| Tensor/spinor network | Finite local cells and contractions | Finite carrier for field-like behavior | Avoid dense-state closure and expensive convergence as only evidence |

Important distinction:

```text
Bloch-like coordinates can be a useful readout.
The Bloch sphere need not be the primitive geometry.
```

A density matrix on a two-state carrier can be visualized by a Bloch vector, but
that does not prove the real manifold is an ordinary sphere. The Bloch sphere
may be a projection, a diagnostic surface, or a control surface. The project can
keep Bloch-like readouts while still testing whether the primitive Bloch sphere
is excluded or demoted by the constraints.

### Entropy Search Space

Entropy is not one number in this project. Different entropy functionals may
measure different parts of the ratchet.

| Entropy / information object | Formula or plain math | Possible role |
|---|---|---|
| Shannon entropy | `H(p) = - sum_i p_i log p_i` | Classical uncertainty over finite labels or outcomes |
| Conditional entropy | `H(X|Y) = H(X,Y) - H(Y)` | How much uncertainty remains after a probe |
| Mutual information | `I(X;Y) = H(X) + H(Y) - H(X,Y)` | How much a probe or terrain reveals |
| KL divergence | `D_KL(p||q) = sum_i p_i log(p_i/q_i)` | Prediction mismatch or update pressure |
| Cross entropy | `H(p,q) = - sum_i p_i log q_i` | Model error against target distribution |
| Von Neumann entropy | `S(rho) = - Tr(rho log rho)` | Quantum/state uncertainty for density matrices |
| Quantum relative entropy | `D(rho||sigma) = Tr(rho(log rho - log sigma))` | Distinguishability between density states |
| Free-energy style functional | `prediction error + complexity penalty` or a density-matrix analogue | Candidate bridge to FEP/QIT |
| Path entropy | entropy over finite paths or histories | Candidate for terrain/order basin behavior |
| Basin entropy | entropy over basin labels or basin boundaries | Measures basin fragmentation/uncertainty |

Rule:

```text
Do not call a thing entropy unless the finite object being counted or measured
is explicit.
```

Examples of distinct entropy claims:

```text
entropy of strategy labels
entropy of density states
entropy of path choices
entropy of basin membership
entropy of prediction error
```

Those are not the same claim.

### Classical Engines As Reference Patterns

Carnot and Szilard are not the target identity of the QIT/IGT engine. They are
known reference patterns.

Carnot:

```text
heat-engine baseline
work/heat accounting reference
useful for checking whether a thermal substrate behaves sanely
```

Szilard:

```text
information-engine baseline
bit / entropy / work accounting reference
useful for checking information-processing work
```

The QIT/IGT engine may borrow diagnostic patterns from both, but the project
claim is not:

```text
the engine is Carnot
the engine is Szilard
```

The candidate claim is:

```text
engine-like mechanics may emerge from finite order-sensitive constraints,
processing entropy/information on a nonclassical geometric carrier
```

### Grok And Gemini Contrast

Grok and Gemini can be useful as contrast engines, but not as authority. Their
best role is to attack the current framing from outside:

```text
find math gaps
name alternative geometries
challenge whether chirality really emerged
challenge whether density matrices are necessary
challenge whether Bloch-like readouts are smuggling a sphere
challenge whether IGT labels have an observable yet
challenge whether an axis is symbolic only
```

Their outputs should be classified as:

```text
contrast / audit / idea source
```

not:

```text
proof / authority / admitted result
```

### Tribunal Intake, Fenced

A later Hermes concept doc captured a Grok/Gemini/Codex2 tribunal at:

```text
/Users/joshuaeisenhart/wiki/concepts/igt-pattern-explicit-math-reference.md
```

That file is useful as a companion reference, but it must not replace this
running guide. It is shorter, more schematic, and uses "forced" language in
places that should be translated into the ratchet vocabulary here:

```text
chosen root commitment
strong downstream pressure
survivor candidate
not-yet-killed alternative
admitted result
```

Useful tribunal results to keep:

| Point | How to use it |
|---|---|
| Xi bridge is the biggest gap | Treat Axis 0 / bridge claims as open until geometry/history maps into an explicit bipartite or cut state. |
| Axes 3, 5, 6 are strongest | These have the clearest current finite math: Hopf loop class, operator family, and composition order. |
| Axis 0 is weakest | Do not promote entropy/drive language without a finite bridge functional and controls. |
| 720-degree behavior is density-invisible | If the engine collapses everything to `rho = |psi><psi|`, spinor sign and lifted path data disappear. The engine must preserve spinor/path/interference data when 720-degree structure matters. |
| L/R Weyl was misread as imposed | In this framework, L/R is a ratchet candidate: N01 pressures left/right action, SU(2)/S3 gives two orientations, and minimality selects the two-sheet realization if alternatives die. |
| Minimality is method, not necessarily a third root | "Presume the least" is how the ratchet advances. It should not be silently promoted to M01 unless the project explicitly chooses it. |
| Alternative carriers remain live | Higher qudits, real/quaternionic carriers, finite groups, flag manifolds, channel/Choi geometry, finite spectral triples, and process categories need tests or explicit kills. |

The tribunal and later source-authority pass sharpened five distinct order
concepts that must not be
collapsed:

```text
1. pair-readout order:
   which token appears first/second in labels like winWIN or LOSEwin

2. Axis-6 composition order:
   operator-first  = Phi_T(O(rho))
   terrain-first   = O(Phi_T(rho))

3. four-step loop order:
   the terrain/engine sequence, e.g. Se -> Ne -> Ni -> Si versus its chiral
   partner

4. 64-schedule order:
   the S01-S64 atlas index over 8 terrain IDs x 8 signed operators; this is
   not runtime truth, hexagram semantics, or Axis closure by itself

5. source-file order:
   the order in which source docs or authority packets were read or generated;
   this is source genealogy, not pair order, Axis-6 order, loop order, or
   schedule order
```

Fenced owner correction:

```text
External models tend to see L/R Weyl as imported physics because they see the
endpoint, not the ratchet chain. The project claim is not "we assume Weyl
spinors." The project claim is "if finite noncommuting spinor geometry survives,
then L/R chirality is a minimal candidate for preserving oriented order."
```

What still has to be shown:

```text
left/right or clockwise/counterclockwise distinction
same local rule, opposite handedness
observable invariant under the split
negative control where handedness is erased
alternative carrier tests
result artifact tying the invariant to the finite map
```

Do not write:

```text
The tribunal proved C2, SU(2), spinors, density matrices, chirality, and 720
degrees are forced.
```

Write:

```text
The tribunal supports the current ratchet pressure story, while also naming
open alternatives and the bridge tests needed before admission.
```

## Ratchet, Manifold, And Entropy Discipline

This section tightens the current guide around three separations that are easy
to blur:

```text
ratchet method != third root axiom
constraint manifold M(C) != carrier geometry
entropy readout != primitive engine source
```

The root commitments remain only:

```text
F01 = finitude / bounded witness discipline
N01 = noncommutation / order-sensitive composition
```

Minimality is the proof and logic discipline used after those commitments. It
is not a third root constraint. The ratchet asks for the least additional
structure that has survived the current finite tests, then uses that survivor
to constrain the next layer. A cleaner ratchet ledger for each layer is:

| Ledger field | Required content |
|---|---|
| Prior support | Which admitted or working lower layer this step runs on. |
| Killed alternatives | Which candidates failed a finite test, control, or admissibility fence. |
| Surviving alternatives | Which candidates remain live and why they have not been killed. |
| Current candidate | The structure currently being used or proposed. |
| Status | `candidate`, `admitted under`, `closed/proven survivor`, or `blocked/unbuilt probe`. |
| Open probes | The smallest next tests that could exclude, demote, or narrow the candidate. |

Status words must stay literal:

```text
candidate = useful structure still awaiting enough exclusion evidence
admitted under = passed a named finite witness or bounded result scope
closed/proven survivor = only after alternatives have been explicitly killed
blocked/unbuilt probe = known needed test, no result here
```

Do not let an attractive next layer backfill the lower layer. The next layer is
allowed to run only on the prior support plus the killed/surviving alternative
ledger.

### Geometric Constraint Manifold

Use the explicit source definition:

```text
C = {F01, N01, admissible probe rules, admissible composition rules}
M(C) = {x : x is admissible under C}
```

`M(C)` is the admissible configuration space under active constraints. It is
not the same thing as the geometry of a chosen carrier. A carrier realization is
a packet inside or mapped into `M(C)`, for example:

```text
iota : M_hat_geom -> M(C)
M_hat_geom = paired sheet / density / path / stage realization
```

Geometry must be read from compatibility, support, carrier, quotient, path, and
process structures inside `M(C)`. It is not a front-door Euclidean container.

Keep these geometry levels distinct:

| Geometry level | Current role | What it can show | What it cannot show by itself |
|---|---|---|---|
| Carrier Hilbert/spinor/quaternion structure | Hilbert carrier `C^2`, lifted `psi in S^3`, and `C^2 ~= H` as a real carrier identification | Finite QIT carrier route; spinor/quaternion-level phase/path data if retained | Final exclusion of real, higher-qudit, finite-group, operator-algebra, or process carriers. |
| Quotient/readout geometry | `rho = |psi><psi|`, Bloch vector, `SU(2) -> SO(3)` / `S^3 -> S^2` | Downstream vector/rotation readout from the spinor route | Lifted sign, 720 behavior, and fiber holonomy when only `rho` or Bloch vector is kept. |
| Connection/holonomy geometry | Hopf connection, fiber/base loops, torus strata | Path class, horizontal lift, phase/fiber distinction, candidate holonomy witnesses | Admission of the whole engine or Axis 0 bridge. |
| Channel/process geometry | CPTP maps, Lindblad/unitary channels, Choi/channel states, process categories | Order gaps, channel-level invariants, channel-vs-state geometry tests | Carrier minimality unless compared against alternatives. |
| Entanglement/cut geometry | `Xi : geometry/history -> rho_AB`, shell/history/point cuts | A real surface for conditional entropy, coherent information, mutual information | Any Axis 0 claim before the cut state exists. |
| Sim/network geometry | nested PEPS2D / Hopfield scratch carrier and graph/cell variants | Whether bonds/relations act as the connection surface in scratch diagnostics | Load-bearing carrier admission above scratch ceiling. |

Live geometry/carrier alternatives remain live until killed by explicit probes:

| Alternative | Why it remains live | Example kill or narrowing test |
|---|---|---|
| Higher qudits / multi-qubit carriers | `C^2` may be minimal on one route but not globally final. | Show the added dimension is redundant under the same quotient, holonomy, entropy, and controls. |
| Real carriers | N01 alone does not exclude all real noncommuting algebras or `SO(3)`-level structure. | Show loss of lifted phase/sign/path data needed by a surviving observable. |
| Quaternionic extensions beyond the local spinor form | Unit quaternions are not a spinor falsifier here: `C^2 ~= H` and `SU(2) ~= Sp(1)`. The live question is whether larger quaternionic Hilbert/operator frames add needed observables. | Compare added structure against the same quotient, holonomy, entropy, and density/lifted-data readouts. |
| Finite groups / monoids / braid-like carriers | They can satisfy finite order-sensitive composition without Hilbert space first. | Test whether they lack the required probe, quotient, holonomy, or entropy readouts. |
| Flag manifolds and higher spin geometries | They may be natural higher-dimensional quotient geometries. | Show no lower-presumption advantage at the active layer. |
| Choi/channel geometry | The engine may be better represented at the channel/process level than the state level. | Compare state-carrier and channel-carrier discriminators on the same order gaps. |
| Finite spectral triples / process categories | They encode finite noncommutative structure without starting from vector geometry. | Require equal-or-lower presumptions plus matching quotient and holonomy readout. |

### Entropy And Readout Layer

Entropies are probe/readout functionals over explicit finite objects. They are
not primitive source terms, not root constraints, and not labels that can stand
in for missing bridge math.

Use this rule:

```text
No entropy claim without naming the finite object being evaluated:
state, channel, cut, path family, graph, spectrum, or description code.
```

Keep the readouts separate:

| Entropy/readout | Object evaluated | Can distinguish | Cannot distinguish |
|---|---|---|---|
| Von Neumann entropy `S(rho)` | A density state | Mixedness of `rho`; runtime proxy changes | Lifted spinor sign, 720 path data, or a final Axis 0 cut by itself. |
| Quantum relative entropy `D(rho || sigma)` | Pair of density states | State distinguishability under QIT probes | Channel order if only endpoint states are compared. |
| Conditional entropy `S(A|B)` | Bipartite `rho_AB` | Signed cut entropy once `Xi` exists | Anything before the bipartite/cut state is constructed. |
| Coherent information `I_c(A > B)` | Bipartite/cut state or channel cut | Directional quantum information candidate for Axis 0 | Standalone proof of the correct bridge. |
| Mutual information `I(A:B)` | Bipartite/cut state | Total correlation across a cut | Directional sign unless paired with signed readouts. |
| Entanglement entropy | Reduced state across a real bipartition | Cut entanglement for a specified split | Axis 0 if the split is only named, not constructed. |
| Channel / Choi entropy | Channel or Choi state | Process-level mixing, channel distinguishability, memory | Spinor holonomy unless the channel keeps lifted/path data. |
| Path / holonomy entropy | Finite path family or lifted-history distribution | Path-class diversity, loop/readout distribution | Density-invisible sign if paths are quotiented too early. |
| Graph / spectral entropy | Graph, Laplacian, adjacency, or spectrum | Network/scratch-carrier dispersion and relation structure | Carrier admission unless tied to the same finite map and controls. |
| Algorithmic / description entropy | Finite code or description family | Compression/description cost of candidate structures | Physical or QIT entropy without an explicit bridge. |

The `720` / sign / phase issue is a hard visibility fence:

```text
psi -> -psi after a 360-degree lifted turn
psi ->  psi after a 720-degree lifted turn
rho = |psi><psi| is unchanged by psi -> -psi
```

Therefore a `rho`-only or Bloch-vector-only engine cannot see the lifted sign
unless it carries extra path, phase, interference, or spinor-level data. A
positive Bloch or density result does not by itself admit the holonomy layer.

The `Xi` bridge has the same honesty fence:

```text
Xi : geometry/history -> rho_AB
```

Axis 0 readouts such as `S(A|B)`, `I_c`, or `I(A:B)` require a real bipartite
state, channel cut, shell cut, or history cut. Attaching an entropy label to a
single scalar or symbolic split is not a bridge.

The atlas companion entropy table makes the post-bridge object explicit:

```text
rho_A = Tr_B(rho_AB)
rho_B = Tr_A(rho_AB)
I_c(A > B) = S(rho_B) - S(rho_AB)
I(A:B) = S(rho_A) + S(rho_B) - S(rho_AB)
```

Guide-safe reading: coherent information is a signed Axis 0 candidate only
after `Xi` has built the finite cut object. Mutual information is an unsigned
companion diagnostic, not a replacement for the signed cut question.

### Corrected Spinor-Vector Formulation

Use this boxed formulation when describing the spinor-over-vector argument:

```text
Spinors over vectors is a valid ratchet/minimality argument only with status
fences.

F01 + N01 alone do not prove that spinors are the only survivor.

Under F01 + N01 plus no-assumed-geometry discipline, C^2 with a Hermitian form
is the current working minimal carrier route for the complex two-state lane,
not a global formal admission. The downstream Bloch / SU(2) -> SO(3) quotient
gives access to R^3/SO(3)-style vector readout after the carrier is in place,
so the route starts with less front-door Euclidean geometry than a primitive
vector-space ontology.

The Hermitian form is still structure. Do not say "spinors need no metric."
Say the metric-like structure is carrier-side and geometry-deriving, not a
background Euclidean geometry assumed before the constraints.

N01 alone does not distinguish spinors from vectors. SO(3) is nonabelian, and
su(2) ~= so(3) locally. The spinor surplus is global/topological/holonomy-level:
SU(2) double cover, sign, 720 behavior, path lift, and interference visibility.

That surplus is invisible if the engine keeps only rho = |psi><psi| or only the
Bloch vector. The engine must carry lifted spinor/path/interference data for
the surplus to be testable.

Falsifier: a real, finite-group, spectral-triple, Choi/channel, process
carrier, or quaternionic extension not equivalent to the local `C^2 ~= H`
spinor neighborhood, with equal or lower presumptions and the same quotient
plus holonomy readout, keeps the spinor preference open.
```

Short status sentence:

```text
Spinors are the leading survivor candidate on the C^2 route, not a closed proof
until alternative carriers have been explicitly killed.
```

### Descriptive Next Probes

These are wiki/process targets only. No sims are run by this page.

| Probe target | What to construct | What would narrow the ratchet |
|---|---|---|
| Alternative-carrier minimality comparison | Same finite witness suite across `C^2 ~= H`, higher qudits, real carriers, quaternionic extensions, finite group/monoid, Choi/channel, finite spectral triple, and process-category carriers. | Lower-presumption carrier or extension with same quotient/holonomy/readout keeps spinor exclusivity open; failure against controls demotes it. |
| Geometry-stack order ratchet probe | For candidate geometry layers, test `G_a o G_b` versus `G_b o G_a` on the same finite witness; include G-tower/Hopf/Weyl, holonomy/Connes, commuting controls, and reversed-order proof guards. | Nonzero order gap or reversed-order inconsistency supports a ratchet candidate; commuting controls or order-invariance demote decorative stacks. |
| Quotient geometry test | Explicit map from carrier to readout: spinor/Hopf/Bloch or alternative carrier quotient. | Shows whether `R^3/SO(3)`-style geometry is downstream readout or silently assumed. |
| Holonomy visibility test | Compare `rho`-only engine against `psi` plus path/interference engine on 360/720 lifted loops. | If only lifted data separates cases, density-only consumers are blocked for holonomy claims. |
| Xi bridge construction test | Build point, shell, history, or channel-cut `Xi` into an actual `rho_AB` or Choi/cut object. | Axis 0 entropy claims become evaluable only after this object exists. |
| Entropy discriminator suite | Evaluate `S(rho)`, relative entropy, `S(A|B)`, `I_c`, `I(A:B)`, entanglement entropy, Choi entropy, path entropy, graph/spectral entropy on the same finite candidate families. | Reveals which readouts separate carrier, channel, path, cut, and network alternatives. |
| Order-concept separation audit | Keep pair-readout order, Axis-6 composition order, and four-step loop order in separate columns. | Prevents IGT label order from being mistaken for channel precedence or loop order. |

## One-Line Model

The current working object is a finite density-state engine where terrain maps
and operator maps do not commute:

```text
Delta_{tau,O}(rho) = T_tau(O(rho)) - O(T_tau(rho))
```

That order gap is the active N01 signal.

The IGT/Jung/I-Ching split must stay separate:

```text
IGT     = stage/readout grammar
Jung    = operator grammar
I Ching = 64-schedule index
```

They correlate. They do not redefine each other.

## Carrier And Geometry

The finite density carrier used by the current source math:

```text
H = C^2

rho = 1/2 (I + r_x sigma_x + r_y sigma_y + r_z sigma_z)
```

Spinor chart:

```text
psi_s(phi, chi; eta)
  = [
      exp(i(phi + chi)) cos(eta),
      exp(i(phi - chi)) sin(eta)
    ]^T

rho_s = |psi_s><psi_s|
```

Hopf projection:

```text
pi(psi) = psi^dag (sigma_x, sigma_y, sigma_z) psi
```

Hopf connection:

```text
A = -i psi^dag dpsi
  = dphi + cos(2 eta) dchi
```

Weyl sheets:

```text
H_L = +H_0
H_R = -H_0
```

Path split:

```text
fiber path:
  gamma_fiber^s(u) = psi_s(phi_0 + u, chi_0; eta_0)
  rho_fiber^s(u) = rho_fiber^s(0)

lifted-base path:
  gamma_base^s(u) = psi_s(phi_0 - cos(2 eta_0) u, chi_0 + u; eta_0)
  rho_base^s(u) changes
  A_Hopf(dot(gamma_base)) = 0
```

Current carrier correction:

```text
CTMRG/PEPS3D is retired as the load-bearing carrier for this lane.

Current scratch carrier story:
  nested PEPS2D / Hopfield connection geometry

Meaning:
  the Hopfield/PEPS2D bonds are the connection geometry surface itself,
  not a PEPS3D layer pasted onto the model.

Execution engines:
  Julia = reference / transparent math lane
  JAX   = scale / mirror / stress lane

PyTorch:
  historical 2026-06-05 note superseded on engine role by the 2026-06-08
  canon. PyTorch/PyG is first-class graph/network compute when the bounded
  receipt makes that role load-bearing; Julia remains arbitration canon.
```

Repo authority has not fully rewritten every older PEPS3D gate. Treat that as
repo-authority drift for this lane, not as permission to promote the new carrier
above its scratch ceiling.

## F01 And N01

F01:

```text
No completed infinity as a primitive.
Every witness must be finite, bounded, inspectable, rerunnable, or finitely
represented.
```

N01:

```text
Order matters at the root.
A o B and B o A are different operations unless a control shows they collapse.
Kills are irreversible inside the ratchet.
```

For this engine lane:

```text
F01 witness:
  finite density matrix, finite terrain map, finite operator map, finite
  schedule row, finite sample set, finite result JSON.

N01 witness:
  Delta_{tau,O}(rho) != 0 under native terrain/operator composition.
```

## Axes 0-6

The axes are not all the same kind of thing, and they are not all equally
settled. They are an exploratory coordinate system over possible degrees of
freedom. Some identify terrain families, some identify path/loop structure,
some identify operator families, and Axis 6 is the precedence/action-side audit.

Use this section as a map of live surfaces, not as a claim that every axis is
already closed pure QIT math.

For every axis, keep these layers separate:

```text
source split
current finite math
Jung correlation
IGT correlation
taijitu / symbolic correlation
pure QIT status
kill condition or missing test
```

If an axis has no finite map, invariant, observable, or killed control yet, it
is still a useful exploratory label, but it is not admitted math.

### Axis 0

Owner shorthand:

```text
A0 = Ne/Ni vs Se/Si
```

Source meaning:

```text
entropy polarity / cut-state kernel / enclosing drive
```

The current strong symbolic split:

```text
white / yang side = {Ne, Ni}
black / yin side  = {Se, Si}
```

Candidate math seats:

```text
b_0 = sign(cos(2 eta)) = sign(r_z)

S(rho) = -Tr(rho log rho)

candidate bridge/cut functional:
  Phi_0(rho_AB) = - sum_r w_r S(A_r | B_r)_rho
                =   sum_r w_r I_c(A_r > B_r)_rho
```

Current caveat:

```text
Axis 0 is not closed by this page.
Axis 0 is not an engine operator.
Axis 0 needs a bipartite/cut state to become a bridge claim.
```

### Axis 1

Owner shorthand:

```text
A1 = Se/Ni vs Ne/Si
```

Source meaning:

```text
derived terrain branch bit
```

Split:

```text
A1 side 1 = {Se, Ni}
A1 side 2 = {Ne, Si}
```

Axis 1 alone does not identify a terrain. Axis 1 plus Axis 2 does.

```text
A1 = Se/Ni, A2 = direct      -> Se
A1 = Ne/Si, A2 = direct      -> Ne
A1 = Se/Ni, A2 = conjugated  -> Ni
A1 = Ne/Si, A2 = conjugated  -> Si
```

### Axis 2

Owner shorthand:

```text
A2 = Ne/Se vs Si/Ni
```

Source meaning:

```text
direct frame vs conjugated frame
```

Split:

```text
direct frame     = {Se, Ne}
conjugated frame = {Ni, Si}
```

Frame math:

```text
direct:
  tilde(rho) = rho
  dot(rho_t) = L_t(rho_t)

conjugated:
  tilde(rho_t) = V_t^dag rho_t V_t
  conjugated rows include transport / gauge correction
```

### Axis 3

Source meaning:

```text
fiber path vs lifted-base path
```

It also has a chart-role readout:

```text
Type 1:
  outer = lifted base
  inner = fiber

Type 2:
  outer = fiber
  inner = lifted base
```

Important caution:

```text
Axis 3 is not simply Type 1 vs Type 2.
Axis 3 is not simply left vs right chirality.
Axis 3 has both a geometry-path readout and a chart-role readout.
```

### Axis 4

Source meaning:

```text
loop-order family
```

Runtime families:

```text
deductive = FeTi family
inductive = TeFi family
```

Order math:

```text
Phi_D = U o E o U o E
Phi_I = E o U o E o U
```

Equivalent generator form from the deeper math source:

```text
Phi_D = exp(tau_R L_R) exp(tau_C L_C)
Phi_I = exp(tau_C L_C) exp(tau_R L_R)

first nontrivial difference ~ tau_R tau_C [L_R, L_C]
```

Axis 4 is not Axis 6.

```text
Axis 4 = loop order across the loop.
Axis 6 = token precedence inside a terrain/operator word.
```

### Axis 5

Source meaning:

```text
operator-family split
```

Split:

```text
dephasing / projection = {Ti, Te}
rotation / unitary     = {Fi, Fe}
```

Math class:

```text
Ti, Te:
  unital pinching / conditional expectation / pure dephasing
  entropy non-decreasing in the usual pinching sense
  purity non-increasing
  real negative decay modes

Fi, Fe:
  unitary inner automorphisms
  spectrum preserving
  purity preserving
  entropy preserving
  imaginary circulation modes
```

### Axis 6

Source meaning:

```text
token precedence / action side
```

Source token split:

```text
up   = operator written first
down = terrain written first
```

Runtime composition:

```text
up / operator first:
  T_tau o O
  native token looks like O before terrain, e.g. TiSe

down / terrain first:
  O o T_tau
  native token looks like terrain before O, e.g. SeTi
```

Derived lower-stack law:

```text
b_6 = - b_0 b_3
```

Order gap:

```text
Delta_{tau,O}(rho) = T_tau(O(rho)) - O(T_tau(rho))
```

Axis 6 does not change the operator formula.

```text
Ti^up and Ti^down both use the same Ti map.
Te^up and Te^down both use the same Te map.
Fi^up and Fi^down both use the same Fi map.
Fe^up and Fe^down both use the same Fe map.
```

## Projection Audits

Source-locked projection:

```text
A1 x A2 x A5 x A6 -> 16 ordered tokens
```

This uniquely identifies all 16 tokens.

Non-unique projection:

```text
A3 x A4 x A5 x A6 -> 8 paired loop-placement signatures
```

This does not identify all 16 tokens by itself. It pairs tokens that share path,
loop role, operator family, and precedence while differing in topology.

## IGT Layer

IGT is not yet executable payoff math. It is a stage/readout grammar currently
attached to the engine rows.

Classical decision-rule correspondence from the user:

| IGT pattern | Classical game-theory name | Plain reading |
|---|---|---|
| `WinWin` / `winWIN` / `WINwin` | maximax | maximum possible win orientation |
| `WinLose` / `winLOSE` | maximin | protect the win under loss pressure |
| `LoseWin` / `loseWIN` | minimax | minimize loss by reaching win side |
| `LoseLose` / `loseLOSE` / `LOSElose` | minimin | losing is a legitimate strategy, not an error |

Important fence:

```text
Win/loss labels are not yet selection criteria.
Win/loss labels are not yet a physics observable by themselves.
Win/loss labels are not the same as operator formulas.
```

Use them as chart grammar until a named functional or engine readout makes them
measurable.

## IGT Quadrants And 16 Strategies

Each IGT quadrant / terrain family contains four distinct strategy placements:

```text
4 quadrants x 2 engine types x 2 placements per terrain step = 16 strategies
```

The order notions must not be collapsed:

```text
1. Pair-readout order:
   which token appears first and second in labels such as winWIN or LOSEwin.

2. Axis-6 composition order:
   operator-first T_tau(O(rho)) versus terrain-first O(T_tau(rho)).

3. Four-step loop order:
   the sequence of terrain steps inside a loop, e.g. Se -> Ne -> Ni -> Si.

4. 64-schedule order:
   the S01-S64 atlas index over 8 terrain IDs x 8 signed operators; this is
   lookup/index order unless a runtime map and controls make it load-bearing.

5. Source-file / authority order:
   the read or generation order of source packets; this can guide audit
   genealogy but cannot replace pair-readout order, Axis-6 composition order,
   loop order, or schedule order.
```

Casing is separate from pair position:

```text
UPPERCASE = outer / major loop result
lowercase = inner / minor loop result

The first label slot can be uppercase or lowercase.
The second label slot can be uppercase or lowercase.
```

The quadrant label gives the terrain family:

```text
Se = LoseWin
Ne = WinLose
Ni = LoseLose
Si = WinWin
```

The engine type changes which placement appears first.

### Se Quadrant: LoseWin

| Label | Engine | 1st token | 1st outcome | 2nd token | 2nd outcome |
|---|---|---|---|---|---|
| `LOSEwin` | Type 1 | `TiSe = Se-in(Ti(rho))` | `LOSE` | `SeFi = Fi(Se-in(rho))` | `win` |
| `loseWIN` | Type 2 | `SeTi = Ti(Se-out(rho))` | `lose` | `FiSe = Se-out(Fi(rho))` | `WIN` |

### Ne Quadrant: WinLose

| Label | Engine | 1st token | 1st outcome | 2nd token | 2nd outcome |
|---|---|---|---|---|---|
| `WINlose` | Type 1 | `NeTi = Ti(Ne-in(rho))` | `WIN` | `FiNe = Ne-in(Fi(rho))` | `lose` |
| `winLOSE` | Type 2 | `TiNe = Ne-out(Ti(rho))` | `win` | `NeFi = Fi(Ne-out(rho))` | `LOSE` |

### Ni Quadrant: LoseLose

| Label | Engine | 1st token | 1st outcome | 2nd token | 2nd outcome |
|---|---|---|---|---|---|
| `loseLOSE` | Type 1 | `TeNi = Ni-in(Te(rho))` | `lose` | `NiFe = Fe(Ni-in(rho))` | `LOSE` |
| `LOSElose` | Type 2 | `NiTe = Te(Ni-out(rho))` | `LOSE` | `FeNi = Ni-out(Fe(rho))` | `lose` |

### Si Quadrant: WinWin

| Label | Engine | 1st token | 1st outcome | 2nd token | 2nd outcome |
|---|---|---|---|---|---|
| `winWIN` | Type 1 | `SiTe = Te(Si-in(rho))` | `win` | `FeSi = Si-in(Fe(rho))` | `WIN` |
| `WINwin` | Type 2 | `TeSi = Si-out(Te(rho))` | `WIN` | `SiFe = Fe(Si-out(rho))` | `win` |

Valid current reading:

```text
The source chart supports 16 strategy placements.
Each quadrant has four placements.
Type 1 and Type 2 flip which casing/loop-placement appears first.
This is a strategy-grammar chirality candidate.
```

Fence:

```text
"Maximize", "minimize", "climb", "push into standards", and similar strategy
meanings are interpretation layers until a named functional and finite test are
attached.

Strategy-grammar chirality is not the same as admitted geometric chirality.
Geometric chirality still needs the carrier-side L/R, Hopf, spinor, or
connection-geometry witness named in the result artifact.
```

## Operators

The base operators are four fixed maps on density matrices.

### Ti

Name:

```text
Ti = z-pinching / z-dephase / conditional expectation onto span{I, sigma_z}
```

Projectors:

```text
P0 = |0><0|
P1 = |1><1|
```

Pinching:

```text
E_z(rho) = P0 rho P0 + P1 rho P1
```

Finite channel:

```text
Ti_q(rho) = (1 - q1) rho + q1 E_z(rho)
```

Scratch run value:

```text
q1 = 0.31
```

Bloch map:

```text
Ti(x,y,z) = ((1 - q1)x, (1 - q1)y, z)
           = (0.69x, 0.69y, z) in the scratch parity run
```

Generator:

```text
L_Ti(rho) = (kappa1 / 2) (sigma_z rho sigma_z - rho)
```

Fixed algebra:

```text
Fix(Ti) = span{I, sigma_z}
```

Gradient nuance:

```text
Ti descends distance to the z-fixed algebra and kills z-basis coherence.
Ti is not an arbitrary "win/loss" operator.
```

### Te

Name:

```text
Te = x-pinching / x-dephase / conditional expectation onto span{I, sigma_x}
```

Projectors:

```text
Q+ = |+><+|
Q- = |-><-|
```

Pinching:

```text
E_x(rho) = Q+ rho Q+ + Q- rho Q-
```

Finite channel:

```text
Te_q(rho) = (1 - q2) rho + q2 E_x(rho)
```

Scratch run value:

```text
q2 = 0.27
```

Bloch map:

```text
Te(x,y,z) = (x, (1 - q2)y, (1 - q2)z)
           = (x, 0.73y, 0.73z) in the scratch parity run
```

Generator:

```text
L_Te(rho) = (kappa2 / 2) (sigma_x rho sigma_x - rho)
```

Fixed algebra:

```text
Fix(Te) = span{I, sigma_x}
```

Gradient nuance:

```text
Te is not inherently ascent or descent.

Te descends:
  distance to the x-fixed algebra
  purity

Te usually ascends:
  von Neumann entropy, unless already x-diagonal

Te can only be called "gradient ascent" or "gradient descent" after naming:
  functional
  terrain
  target or attractor
  metric
```

The chart hypothesis:

```text
Te^up   = TeNi, TeSi = exploratory ascent/preconditioning orientation
Te^down = NiTe, SiTe = exploratory descent orientation
```

But the exact math remains the same `Te_q`.

### Fi

Name:

```text
Fi = x-axis unitary rotation / inner automorphism generated by sigma_x
```

Unitary:

```text
U_x(theta) = exp(-i theta sigma_x / 2)
```

Finite channel:

```text
Fi_theta(rho) = U_x(theta) rho U_x(theta)^dag
```

Scratch run value:

```text
theta = 0.41
```

Bloch map:

```text
Fi(x,y,z) = R_x(0.41) r

R_x(theta):
  x' = x
  y' = y cos(theta) - z sin(theta)
  z' = y sin(theta) + z cos(theta)
```

Generator:

```text
L_Fi(rho) = -i [(omega3 / 2) sigma_x, rho]
```

Fixed algebra:

```text
Fix(Fi) = span{I, sigma_x}
```

Functional nuance:

```text
Fi preserves spectrum, purity, and entropy.
Fi is spectral / wave / rotation language, not gradient descent.
Any "broadcast/filtering" role is row-level, not a property of bare Fi alone.
```

### Fe

Name:

```text
Fe = z-axis unitary rotation / inner automorphism generated by sigma_z
```

Unitary:

```text
U_z(phi) = exp(-i phi sigma_z / 2)
```

Finite channel:

```text
Fe_phi(rho) = U_z(phi) rho U_z(phi)^dag
```

Scratch run value:

```text
phi = -0.37
```

Bloch map:

```text
Fe(x,y,z) = R_z(-0.37) r

R_z(phi):
  x' = x cos(phi) - y sin(phi)
  y' = x sin(phi) + y cos(phi)
  z' = z
```

Generator:

```text
L_Fe(rho) = -i [(omega4 / 2) sigma_z, rho]
```

Fixed algebra:

```text
Fix(Fe) = span{I, sigma_z}
```

Functional nuance:

```text
Fe preserves spectrum, purity, and entropy.
Fe can be read as a phase spiral or wave row, but not as bare damping.
"Damping", "lifting", or "entrainment" is row-level language after terrain
composition, not the bare Fe map.
```

## Eight Signed Operator Placements

There are four base operator maps and eight signed placements.

The signed placements are not eight unrelated operators.

| Signed placement | Actual map | Native frame | Axis 6 | Native terrains only | Native tokens | Role language, fenced |
|---|---|---|---|---|---|---|
| `Ti^up` | same `Ti_q` | direct `{Se, Ne}` | operator first | `Se-in`, `Ne-out` | `TiSe`, `TiNe` | z-projection before terrain |
| `Ti^down` | same `Ti_q` | direct `{Se, Ne}` | terrain first | `Ne-in`, `Se-out` | `NeTi`, `SeTi` | z-projection after terrain |
| `Te^up` | same `Te_q` | conjugated `{Ni, Si}` | operator first | `Ni-in`, `Si-out` | `TeNi`, `TeSi` | ascent/preconditioning only if functional is named |
| `Te^down` | same `Te_q` | conjugated `{Ni, Si}` | terrain first | `Si-in`, `Ni-out` | `SiTe`, `NiTe` | descent only if functional is named |
| `Fi^up` | same `Fi_theta` | direct `{Se, Ne}` | operator first | `Ne-in`, `Se-out` | `FiNe`, `FiSe` | x-wave before terrain |
| `Fi^down` | same `Fi_theta` | direct `{Se, Ne}` | terrain first | `Se-in`, `Ne-out` | `SeFi`, `NeFi` | x-wave after terrain |
| `Fe^up` | same `Fe_phi` | conjugated `{Ni, Si}` | operator first | `Si-in`, `Ni-out` | `FeSi`, `FeNi` | z-phase spiral before terrain |
| `Fe^down` | same `Fe_phi` | conjugated `{Ni, Si}` | terrain first | `Ni-in`, `Si-out` | `NiFe`, `SiFe` | z-phase spiral after terrain |

## Terrains

The current scratch parity artifacts use eight terrain realizations:

```text
Type 1 / IN:
  Se-in = Funnel
  Ne-in = Vortex
  Ni-in = Pit
  Si-in = Hill

Type 2 / OUT:
  Se-out = Cannon
  Ne-out = Spiral
  Ni-out = Source
  Si-out = Citadel
```

Atlas companion grammar:

```text
terrain families = {Se, Ne, Ni, Si}
terrain IDs      = 4 families x 2 orientation/sign tags = 8
placements       = 4 families x 2 loops x 2 sides = 16
schedule slots   = 8 terrain IDs x 8 signed operators = 64
```

Keep these objects distinct. A terrain family is a flow/topology class; a
terrain ID is an oriented chart tag; a placement adds the inner/fiber or
outer/lifted-base loop; a schedule slot is an atlas index, not a runtime or
hexagram truth claim.

### Se-in: Funnel

Terrain family:

```text
Se = expansion, open/isothermal, direct frame
```

Generator:

```text
G_Se,in(rho) = sum_k D[L_k^Se,in](rho) - i eps [H_L, rho]
```

Finite Bloch map from scratch parity:

```text
Phi_Se,in(r)
  = R_N(0.13) (
      sqrt(1 - 0.22) x,
      sqrt(1 - 0.22) y,
      (1 - 0.22) z + 0.22 * 0.86
    )
```

Native operator couplings:

```text
TiSe = Phi_Se,in(Ti(rho))
SeFi = Fi(Phi_Se,in(rho))
```

### Ne-in: Vortex

Terrain family:

```text
Ne = expansion, closed/adiabatic, direct frame
```

Generator:

```text
G_Ne,in(rho) = -i [H_L, rho] + eps sum_k D[L_k^Ne,in](rho)
```

Finite Bloch map:

```text
Phi_Ne,in(r) = 0.94 * R_N(0.47) r
```

Native operator couplings:

```text
NeTi = Ti(Phi_Ne,in(rho))
FiNe = Phi_Ne,in(Fi(rho))
```

### Ni-in: Pit

Terrain family:

```text
Ni = compression, open/isothermal, conjugated frame
```

Generator:

```text
G_Ni,in(rho)
  = D[L^Ni,in](rho) - i eps [H_L, rho]

L^Ni,in = sqrt(gamma) sigma_-
```

Finite Bloch map:

```text
Phi_Ni,in(r)
  = R_N(0.09) (
      sqrt(1 - 0.30) x,
      sqrt(1 - 0.30) y,
      (1 - 0.30) z + 0.30 * (-0.92)
    )
```

Native operator couplings:

```text
NiFe = Fe(Phi_Ni,in(rho))
TeNi = Phi_Ni,in(Te(rho))
```

### Si-in: Hill

Terrain family:

```text
Si = compression, closed/adiabatic, conjugated frame
```

Generator:

```text
G_Si,in(rho)
  = -i [H_S^in, rho]
    + sum_j kappa_j (P_j rho P_j - 1/2(P_j rho + rho P_j))

[H_S^in, P_j] = 0
```

Finite Bloch map:

```text
Phi_Si,in(r)
  = R_M_in(0.19) (proj_M_in(r) + 0.58 * (r - proj_M_in(r)))
```

Native operator couplings:

```text
FeSi = Phi_Si,in(Fe(rho))
SiTe = Te(Phi_Si,in(rho))
```

### Se-out: Cannon

Terrain family:

```text
Se = expansion, open/isothermal, direct frame
```

Generator:

```text
G_Se,out(rho) = sum_k D[L_k^Se,out](rho) - i eps [H_R, rho]
```

Finite Bloch map:

```text
Phi_Se,out(r)
  = R_-N(0.13) (
      sqrt(1 - 0.24) x,
      sqrt(1 - 0.24) y,
      (1 - 0.24) z + 0.24 * (-0.86)
    )
```

Native operator couplings:

```text
FiSe = Phi_Se,out(Fi(rho))
SeTi = Ti(Phi_Se,out(rho))
```

### Ne-out: Spiral

Terrain family:

```text
Ne = expansion, closed/adiabatic, direct frame
```

Generator:

```text
G_Ne,out(rho) = -i [H_R, rho] + eps sum_k D[L_k^Ne,out](rho)
```

Finite Bloch map:

```text
Phi_Ne,out(r) = 0.94 * R_-N(0.47) r
```

Native operator couplings:

```text
NeFi = Fi(Phi_Ne,out(rho))
TiNe = Phi_Ne,out(Ti(rho))
```

### Ni-out: Source

Terrain family:

```text
Ni = compression, open/isothermal, conjugated frame
```

Generator:

```text
G_Ni,out(rho)
  = D[L^Ni,out](rho) - i eps [H_R, rho]

L^Ni,out = sqrt(gamma) sigma_+
```

Finite Bloch map:

```text
Phi_Ni,out(r)
  = R_-N(0.09) (
      sqrt(1 - 0.32) x,
      sqrt(1 - 0.32) y,
      (1 - 0.32) z + 0.32 * 0.92
    )
```

Native operator couplings:

```text
NiTe = Te(Phi_Ni,out(rho))
FeNi = Phi_Ni,out(Fe(rho))
```

### Si-out: Citadel

Terrain family:

```text
Si = compression, closed/adiabatic, conjugated frame
```

Generator:

```text
G_Si,out(rho)
  = -i [H_S^out, rho]
    + sum_j kappa_j (P_j rho P_j - 1/2(P_j rho + rho P_j))

[H_S^out, P_j] = 0
```

Finite Bloch map:

```text
Phi_Si,out(r)
  = R_M_out(-0.19) (proj_M_out(r) + 0.55 * (r - proj_M_out(r)))
```

Native operator couplings:

```text
TeSi = Phi_Si,out(Te(rho))
SiFe = Fe(Phi_Si,out(rho))
```

## All 16 Native Terrain/Operator Pairings

This table is copied from the Julia scratch result row structure. It is the
current complete finite-map surface for Axis-6 native allowed placements.

| Token | Signed | Operator | Terrain | A6 | Label | Native formula | Max gap | Mean gap |
|---|---|---|---|---|---|---|---:|---:|
| `TiSe` | `Ti^up` | `Ti` | `Se-in` | `up` | `LOSE` | `Phi_Se-in(O_Ti(rho))` | 0.0134917184713 | 0.0114185599409 |
| `TiNe` | `Ti^up` | `Ti` | `Ne-out` | `up` | `win` | `Phi_Ne-out(O_Ti(rho))` | 0.0534743720917 | 0.0430631023989 |
| `NeTi` | `Ti^down` | `Ti` | `Ne-in` | `down` | `WIN` | `O_Ti(Phi_Ne-in(rho))` | 0.0524035055543 | 0.0433976191916 |
| `SeTi` | `Ti^down` | `Ti` | `Se-out` | `down` | `lose` | `O_Ti(Phi_Se-out(rho))` | 0.0163815520618 | 0.0104169680556 |
| `TeNi` | `Te^up` | `Te` | `Ni-in` | `up` | `lose` | `Phi_Ni-in(O_Te(rho))` | 0.0769344130867 | 0.0736127761647 |
| `TeSi` | `Te^up` | `Te` | `Si-out` | `up` | `WIN` | `Phi_Si-out(O_Te(rho))` | 0.0368647732089 | 0.0302688573228 |
| `SiTe` | `Te^down` | `Te` | `Si-in` | `down` | `win` | `O_Te(Phi_Si-in(rho))` | 0.0431034475638 | 0.0364240628655 |
| `NiTe` | `Te^down` | `Te` | `Ni-out` | `down` | `LOSE` | `O_Te(Phi_Ni-out(rho))` | 0.0819285125108 | 0.078348696079 |
| `FiNe` | `Fi^up` | `Fi` | `Ne-in` | `up` | `lose` | `Phi_Ne-in(O_Fi(rho))` | 0.120982268633 | 0.0997745982412 |
| `FiSe` | `Fi^up` | `Fi` | `Se-out` | `up` | `WIN` | `Phi_Se-out(O_Fi(rho))` | 0.115489913855 | 0.0951823028454 |
| `SeFi` | `Fi^down` | `Fi` | `Se-in` | `down` | `win` | `O_Fi(Phi_Se-in(rho))` | 0.113060770948 | 0.0836980432051 |
| `NeFi` | `Fi^down` | `Fi` | `Ne-out` | `down` | `LOSE` | `O_Fi(Phi_Ne-out(rho))` | 0.111887211096 | 0.0949251324329 |
| `FeSi` | `Fe^up` | `Fe` | `Si-in` | `up` | `WIN` | `Phi_Si-in(O_Fe(rho))` | 0.0803411021144 | 0.0631983903834 |
| `FeNi` | `Fe^up` | `Fe` | `Ni-out` | `up` | `lose` | `Phi_Ni-out(O_Fe(rho))` | 0.0133901907743 | 0.00919648340375 |
| `NiFe` | `Fe^down` | `Fe` | `Ni-in` | `down` | `LOSE` | `O_Fe(Phi_Ni-in(rho))` | 0.0141609692244 | 0.00872282103241 |
| `SiFe` | `Fe^down` | `Fe` | `Si-out` | `down` | `win` | `O_Fe(Phi_Si-out(rho))` | 0.0948791077833 | 0.0738734490055 |

Valid result:

```text
Artifact:
  /tmp/native_axis6_allowed_parity_results.json

Claim:
  JAX/JULIA parity for 16 native Axis-6 allowed terrain/operator placements.

classification:
  scratch_diagnostic

promotion_allowed:
  false

formal_admission_allowed:
  false

rows_compared:
  16

all_pass_tolerance_1e_10:
  true

all_tokens_match:
  true

max_diff:
  5.551115123125783e-17

min_order_gap_norm:
  0.013390190774308273

max_order_gap_norm:
  0.12098226863299887
```

Interpretation:

```text
The native finite maps are runnable in both Julia and JAX.
The two engines agree numerically on the same 16 row object.
The order gap is nonzero for all native rows in this scratch configuration.
```

Non-interpretation:

```text
This is not proof of a basin.
This is not final IGT win/loss math.
This is not terrain admission or full layer completion.
```

## Engine Stage Orders

The source atlas gives two engine types and four loop orders.

### Type 1: IN

Outer / Major / Deductive:

```text
TiSe -> NeTi -> NiFe -> FeSi
```

Inner / Minor / Inductive:

```text
SeFi -> SiTe -> TeNi -> FiNe
```

Pattern readouts:

```text
Se-in:
  TiSe LOSE + SeFi win -> LOSEwin

Ne-in:
  NeTi WIN + FiNe lose -> WINlose

Ni-in:
  TeNi lose + NiFe LOSE -> loseLOSE

Si-in:
  SiTe win + FeSi WIN -> winWIN
```

Note on order:

```text
The pattern string order is the readout order.
It is not always identical to the loop-list order printed in atlas columns.
```

### Type 2: OUT

Outer / Major / Inductive:

```text
FiSe -> TeSi -> NiTe -> NeFi
```

Inner / Minor / Deductive:

```text
SeTi -> TiNe -> FeNi -> SiFe
```

Pattern readouts:

```text
Se-out:
  SeTi lose + FiSe WIN -> loseWIN

Si-out:
  TeSi WIN + SiFe win -> WINwin

Ni-out:
  NiTe LOSE + FeNi lose -> LOSElose

Ne-out:
  TiNe win + NeFi LOSE -> winLOSE
```

Valid result:

```text
Artifact:
  /tmp/engine_stage_order_parity_results.json

classification:
  scratch_diagnostic

promotion_allowed:
  false

formal_admission_allowed:
  false

all_pass_tolerance_1e_10:
  true

numeric_fields_compared:
  135

max_numeric_diff:
  1.5265566588595902e-16
```

Loop reversal deltas:

| Loop | Max final-state delta under reversal |
|---|---:|
| `T1_inner_minor_inductive` | 0.326342411488 |
| `T1_outer_major_deductive` | 0.240228072523 |
| `T2_inner_minor_deductive` | 0.218486538067 |
| `T2_outer_major_inductive` | 0.270712801327 |

Pair reversal deltas:

| Pair | Proper order | Max final-state delta under reversal |
|---|---|---:|
| `T1_Se_in_LOSEwin` | `TiSe`, `SeFi` | 0.135488103793 |
| `T1_Ne_in_WINlose` | `NeTi`, `FiNe` | 0.151862545993 |
| `T1_Ni_in_loseLOSE` | `TeNi`, `NiFe` | 0.0641796411205 |
| `T1_Si_in_winWIN` | `SiTe`, `FeSi` | 0.0934238798834 |
| `T2_Se_out_loseWIN` | `SeTi`, `FiSe` | 0.105839047709 |
| `T2_Si_out_WINwin` | `TeSi`, `SiFe` | 0.0745024352077 |
| `T2_Ni_out_LOSElose` | `NiTe`, `FeNi` | 0.0958560227369 |
| `T2_Ne_out_winLOSE` | `TiNe`, `NeFi` | 0.128454635628 |

Interpretation:

```text
The finite scratch map makes loop order and pair order load-bearing.
Reversing the proper loop orders changes final states.
Reversing the proper pair orders changes final states.
Julia and JAX agree on the numeric readouts.
```

Non-interpretation:

```text
This still does not define win/loss as a physical payoff.
It shows order-sensitivity of the current finite map.
```

## Nested PEPS2D / Hopfield Connection Geometry Results

Current scratch carrier:

```text
nested_peps2d_hopfield_connection_geometry
```

Finite map description from result artifact:

```text
finite L/R Weyl spinor field on nested Hopf-torus connection graph;
ablate PEPS2D/Hopfield bonds;
compare terrain/operator density-channel signatures
```

Valid source-precedence audit:

```text
Artifact:
  /Users/joshuaeisenhart/Codex-Ratchet/system_v5/julia_carrier/scratch_jax_snapshot_20260604/connection_geometry_ablation_and_precedence_audit_julia_results.json

classification:
  scratch_julia_new_carrier_connection_geometry_ablation_and_precedence_audit

promotion_allowed:
  false

formal_admission_allowed:
  false

all_source_precedence_labels_match_chart:
  true

old checked-in JAX-64 runner:
  executable selection appears inverted against chart
```

Chart convention from the artifact:

```text
UP should mean:
  operator_first = terrain_after_operator = T_tau o O

DOWN should mean:
  terrain_first = operator_after_terrain = O o T_tau
```

Old runner drift:

```text
old_runner_UP_currently_selects:
  terrain_first = O o T_tau

old_runner_DOWN_currently_selects:
  operator_first = T_tau o O
```

Composition-order impact artifact:

```text
Artifact:
  /Users/joshuaeisenhart/Codex-Ratchet/system_v5/julia_carrier/scratch_jax_snapshot_20260604/new_carrier_composition_order_impact_audit_julia_results.json

finite_map:
  same Julia nested Hopf/Weyl Hopfield-PEPS2D finite map,
  varying only terrain/operator composition side

classification:
  scratch_new_carrier_composition_order_impact_audit_julia

promotion_allowed:
  false

formal_admission_allowed:
  false
```

Summary:

| Readout | Value |
|---|---:|
| `all_chart_density_health_pass` | true |
| `all_chart_substage_gaps_nonzero` | true |
| `all_variant_distances_nonzero` | true |
| `stress_grid_count` | 24 |
| `min_any_variant_distance` | 0.002600762277701815 |
| chart vs all operator-after-terrain min | 0.0026007622777018155 |
| chart vs all operator-after-terrain mean | 0.0031977117051773846 |
| chart vs all operator-after-terrain max | 0.0038633761353911783 |
| chart vs all reversed min | 0.003678033285634247 |
| chart vs all reversed mean | 0.004522247262021055 |
| chart vs all reversed max | 0.005463638927218759 |
| chart vs all terrain-after-operator min | 0.002600762277701815 |
| chart vs all terrain-after-operator mean | 0.0031977117051773846 |
| chart vs all terrain-after-operator max | 0.0038633761353911783 |

Blocked consumers named by the artifact:

```text
full_layer_completion
terrain_admission
QIT_Hopfield_identity_claim
flux
Xi/Phi0
Axis0
FEP
bridge
physics_gravity
final_manifold_admission
```

Interpretation:

```text
On the scratch nested PEPS2D/Hopfield connection carrier, composition order is
not decorative. Changing it changes signatures while density health remains
good.
```

Non-interpretation:

```text
This does not formally admit the carrier.
This does not prove PEPS2D/Hopfield is identical to QIT.
This does not unlock Axis0/flux/FEP/bridge/physics.
```

## Wide F01/N01 Exploration Result

Artifact:

```text
/Users/joshuaeisenhart/Codex-Ratchet/system_v5/julia_carrier/explore_julia_results.json
```

Claim ceiling:

```text
exploration_probe - promotion_allowed: false
```

Counts:

```text
n_candidates_tested: 40 list rows
n_survivors: 34
n_graveyard: 4
n_unital_controls: 2
unique family names: 40
duplicate family names: none
accounting closes: true
accounting equation: n_candidates_tested == n_survivors + n_graveyard + n_unital_controls
```

Survivors:

```text
hermitian_pairs_dim2
unitary_dynamics_dim2
lindblad_dynamics_dim2
quaternion_carrier_dim2
kraus_channels_dim2_k3
hermitian_pairs_dim3
unitary_dynamics_dim3
lindblad_dynamics_dim3
su2_geometry_dim3
quaternion_carrier_dim3
kraus_channels_dim3_k3
hermitian_pairs_dim4
unitary_dynamics_dim4
lindblad_dynamics_dim4
su2_geometry_dim4
quaternion_carrier_dim4
kraus_channels_dim4_k3
hermitian_pairs_dim6
unitary_dynamics_dim6
lindblad_dynamics_dim6
su2_geometry_dim6
quaternion_carrier_dim6
kraus_channels_dim6_k3
hermitian_pairs_dim8
unitary_dynamics_dim8
lindblad_dynamics_dim8
su2_geometry_dim8
quaternion_carrier_dim8
kraus_channels_dim8_k3
clifford_cl2
clifford_cl3
clifford_cl4
clifford_cl5
clifford_cl6
```

Graveyard:

| Family | Killed by | Reason |
|---|---|---|
| `su2_geometry_dim2` | N01 | max commutator norm 0.0 |
| `commuting_diagonal_control_dim2` | N01 | commuting diagonal ops, max comm near machine eps |
| `commuting_diagonal_control_dim4` | N01 | commuting diagonal ops, max comm near machine eps |
| `continuum_infinite_dim_control` | F01 | dim greater than F01 bound |

Size ladder filter:

| Dim | F01 | N01 | max comm |
|---:|---|---|---:|
| 8 | true | true | 14.9616 |
| 16 | true | true | 48.0855 |
| 32 | true | true | 128.7611 |
| 64 | true | true | 363.662 |

Convergence readout:

| Family | Trials | Basin readout | Chiral/Mobius proxy readout |
|---|---:|---|---|
| `unitary_dim2` | 120 | scatter | two disconnected sectors; no zero crossing observed |
| `lindblad_dim2` | 120 | partial spread | two disconnected sectors; no zero crossing observed |
| `unitary_dim4` | 120 | scatter | single sector; no chiral handedness in attractor |
| `kraus_dim2` | 120 | yes single basin | single sector; no chiral handedness in attractor |
| `unital_control_dim2` | 120 | yes single basin CONTROL | two disconnected sectors; no zero crossing observed CONTROL |
| `unital_control_dim4` | 120 | yes single basin CONTROL | single sector; no chiral handedness in attractor CONTROL |

Unital controls:

| Family | Filter verdict | Control convergence row | Control-only chiral/Mobius readout |
|---|---|---|---|
| `unital_random_unitary_control_dim2` | survives F01+N01 as CONTROL, not survivor | `unital_control_dim2`: yes single basin, dominant fraction 1.0 | both sectors present, no zero crossing observed |
| `unital_random_unitary_control_dim4` | survives F01+N01 as CONTROL, not survivor | `unital_control_dim4`: yes single basin, dominant fraction 1.0 | single sector, no chiral handedness in attractor |

Corrected Chiral/Mobius summary:

```text
both_sectors_present_no_crossing: survivor rows show two disconnected chiral sectors; not Mobius
```

Control summary:

```text
unital_controls_no_mobius_candidate: control rows recorded separately
```

Valid interpretation:

```text
The wide filter killed the intended F01/N01 controls and admitted many finite
noncommuting candidate families.
```

Required demotion:

```text
Do not cite this as evidence that F01+N01 force a real attractor basin.

Reason:
  convergence tracked dynamics class more than the root constraints.
  unital controls now have explicit control-only convergence/chiral rows.
  the chiral/Mobius proxy was not exact geometry.
  raw survivor Mobius rows say no zero crossing observed.
  control rows are excluded from survivor Mobius headlines and promotion evidence.
```

JAX mirror artifact:

```text
/tmp/explore_jax_results.json
```

Ceiling:

```text
audit_lane - promotion_allowed: false
```

Important JAX mirror facts:

```text
julia_loaded: true
n_survivors:
  Julia = 34
  JAX   = 10
  match = false

n_convergence_tested:
  Julia survivor rows = 4
  Julia all rows including unital controls = 6
  JAX   = 3
  match = false

n_single_basin:
  Julia = 1
  JAX   = 1
  match = true

open issue:
  JAX runs 3 families, Julia wide exploration now has 40 filter rows and 6 convergence rows including 2 control rows.
```

Use the JAX wide-exploration artifact as a partial audit mirror only. It is not parity for the wide sweep.

## What Is Valid Right Now

Valid:

```text
1. The source docs define four base operator maps: Ti, Te, Fi, Fe.
2. Axis 6 changes composition order, not operator formula.
3. The source docs define 16 native terrain/operator tokens.
4. The 16 native tokens run in both Julia and JAX in scratch.
5. Julia/JAX parity for those 16 rows passes to 1e-10 tolerance.
6. The finite scratch map has nonzero order gaps for all 16 native rows.
7. Engine loop order and pair order are load-bearing in scratch.
8. Nested PEPS2D/Hopfield connection geometry is the active scratch carrier story.
9. Old PEPS3D wording is stale for this lane but not yet fully repaired in repo authority.
10. The wide F01/N01 exploration calibrated controls and built a useful graveyard.
```

Not valid yet:

```text
1. Win/loss as physics payoff.
2. Universal basin proof.
3. Formal C => Basin theorem.
4. Axis0/flux/FEP/bridge admission.
5. Full layer completion.
6. Final manifold claim.
7. "F01+N01 force this exact engine" as proven.
8. "Te is gradient ascent" without naming a functional and terrain target.
9. "Fi/Fe are gradient operators" at all. They are unitary rotations.
10. "PEPS2D/Hopfield is canon admitted" without gate update and receipts.
```

## Gradient / Ascent / Descent Nuance

Safe statements:

```text
Ti descends distance to the z-fixed algebra.
Te descends distance to the x-fixed algebra.
Ti and Te are dephasing / pinching channels.
Fi and Fe are unitary rotations.
Fi and Fe preserve spectrum, purity, and entropy.
```

Unsafe statements:

```text
Te is just gradient ascent.
Te is just gradient descent.
Fe is damping by itself.
Fi is filtering by itself.
```

Fenced chart hypotheses:

```text
TeNi and TeSi:
  Te^up rows on compression terrains.
  Can be tested as ascent/preconditioning only after naming H_Ni or H_Si.

NiTe and SiTe:
  Te^down rows on compression terrains.
  Can be tested as descent only after naming H_Ni or H_Si.

FeSi and FeNi:
  Fe^up rows.
  Can be tested as phase-spiral/entrainment/lifting row roles.

SiFe and NiFe:
  Fe^down rows.
  Can be tested as terrain-first phase-spiral/equilibration row roles.
```

Named functionals needed before gradient language is earned:

```text
H_Si(rho) = terrain-stratum height, e.g. (M dot r)^2 or distance to an invariant stratum
H_Ni(rho) = pit/source distance, e.g. ||r - p_Ni||^2
metric    = Hilbert-Schmidt, trace distance, Bures, Fisher/QFI, or explicit Bloch metric
target    = named terrain attractor or stratum
test      = monotonicity under the specific row map across finite samples
```

## Ways To Get This Model Running

This section lists concrete run lanes, from lightest to strongest. The point is
to keep exploration wide while keeping claim ceilings honest.

### Lane 1: Re-read source math and regenerate the 16-token lock

Purpose:

```text
Prevent Axis 6, win/loss, and signed operators from drifting.
```

Inputs:

```text
AXES_TERRAINS_OPERATORS_MANIFOLD_SOURCE_LAYOUT_20260522.md
AXES_0_6_DEEP_MATH_DEFINITIONS_20260522.md
QIT_ENGINE_FOUR_OPERATOR_SIGNED_MATH_20260522.md
ENGINE_64_SCHEDULE_ATLAS.md
```

Output:

```text
16_token_axis_projection_matrix.json
```

Required checks:

```text
unique(A1,A2,A5,A6) == 16
unique(A3,A4,A5,A6) == 8 paired signatures
all 16 native tokens have explicit formulas
```

Claim ceiling:

```text
source-lock / doc-lock only
```

### Lane 2: Run 16 native Axis-6 placements in Julia and JAX

Purpose:

```text
Keep all eight signed placements and all 16 native tokens executable.
```

Compute:

```text
For each native token:
  native = T_tau(O(rho))      if Axis 6 up
  native = O(T_tau(rho))      if Axis 6 down

  opposite = the reversed composition

  gap = native - opposite
  gap_norm = ||gap||
```

Required result fields:

```text
classification = scratch_diagnostic
promotion_allowed = false
formal_admission_allowed = false
rows = 16
sample_count
native_formula
opposite_order_formula
operator_density_map
terrain_source_generator
terrain_finite_bloch_map
axis6_difference_math
max_order_gap_norm
mean_order_gap_norm
```

Pass criterion:

```text
Julia/JAX parity to 1e-10 on named numeric fields.
```

### Lane 3: Run engine-stage order tests

Purpose:

```text
Test the actual source stage orders, not just independent pair rows.
```

Orders:

```text
T1 outer major deductive:
  TiSe -> NeTi -> NiFe -> FeSi

T1 inner minor inductive:
  SeFi -> SiTe -> TeNi -> FiNe

T2 outer major inductive:
  FiSe -> TeSi -> NiTe -> NeFi

T2 inner minor deductive:
  SeTi -> TiNe -> FeNi -> SiFe
```

Controls:

```text
reverse each loop order
reverse each pattern pair
swap cross-loop orders
```

Pass criterion:

```text
proper order and reversed/shuffled controls differ in the finite map;
Julia/JAX parity to 1e-10.
```

Claim ceiling:

```text
scratch_diagnostic unless promoted by repo gates.
```

### Lane 4: Named gradient/ascent tests

Purpose:

```text
Stop arguing from labels. Decide what "TeSi goes up the hill" means
mathematically.
```

Required before running:

```text
Define H_Si(rho)
Define H_Ni(rho)
Define metric
Define sample domain
Define monotonicity pass/fail rule
```

Example tests:

```text
TeSi:
  compare H_Si(Phi_Si,out(Te(rho))) vs H_Si(rho)

SiTe:
  compare H_Si(Te(Phi_Si,in(rho))) vs H_Si(rho)

TeNi:
  compare H_Ni(Phi_Ni,in(Te(rho))) vs H_Ni(rho)

NiTe:
  compare H_Ni(Te(Phi_Ni,out(rho))) vs H_Ni(rho)
```

Expected discipline:

```text
If monotonicity is mixed, say mixed.
If it only works on a subset, name the subset.
If it fails, keep the chart role as symbolic/readout only.
```

### Lane 5: Connection-geometry ablations

Purpose:

```text
Test whether the Hopfield/PEPS2D connection surface changes terrain/operator
signatures.
```

Carrier:

```text
finite L/R Weyl spinor field on nested Hopf-torus connection graph
Hopfield/PEPS2D bonds as connection geometry
```

Controls:

```text
baseline_all_hopfield
uniform_all_bonds
identity_no_edges
no_nested_edges
nested_edges_only
drop_half_edges
zero_connection_field
plain-S2 / flat control
```

Pass criterion:

```text
ablation changes signature while density health stays good.
```

Claim ceiling:

```text
scratch carrier evidence until repo authority gates move.
```

### Lane 6: Wide F01/N01 exploration with real controls

Purpose:

```text
Let the graveyard be large.
Do not hand-design the engine too early.
Throw many candidates at F01 and N01, then inspect survivors.
```

Candidate families:

```text
Hermitian pairs
unitary dynamics
Lindblad dynamics
SU(2)/Spin/quaternion-as-spinor carriers
Clifford carriers
Kraus channels
finite graph/cell/hypergraph carriers
```

Required controls:

```text
commuting control killed by N01
infinite/continuum control killed by F01
unital control adjudicated, not left open
N01 toggled off
F01 bound varied
```

Important correction:

```text
Wide does not mean toy if the intended structure cannot live in the toy.
For handedness/chirality, run full-structure candidates:
  Clifford
  quaternion-as-spinor / quaternionic extension
  SU(2)/Spin
  spinor-native
```

Claim ceiling:

```text
exploration_probe unless basin contract is fully satisfied.
```

### Lane 7: Basin test after engines run

Purpose:

```text
Only after the finite engine maps are stable, ask whether repeated updates
converge to a basin.
```

Minimum basin contract:

```text
admissibility predicate
state space
update rule
basin boundary
stability invariant
escape/failure cases
F01 and N01 root tests
killed simpler explanation
receipt
```

Basin classification vocabulary:

```text
deep_basin:
  method-multiple, proxy-resistant, control-survived

candidate_basin:
  promising but missing at least one independence axis

shallow_basin:
  repeated agreement on one proxy/source

anti_basin:
  falsifier shows the convergence target was wrong

open_basin_boundary:
  controls split or variance remains trajectory-dependent
```

Do not call model agreement, one scalar convergence, or all_pass=true a deep
basin. A deep basin needs source independence, observable independence, control
pressure, and a narrow claim ceiling.

Finite update example:

```text
E = Phi_n o ... o Phi_1

Run:
  rho_{k+1} = E(rho_k)

Measure:
  convergence class
  recurrence behavior
  stability invariant
  boundary / escape cases
  order-shuffle control
```

Claim ceiling:

```text
candidate basin until the full basin-manifold contract is met.
```

### Lane 8: Formal proof, later

Purpose:

```text
Optional future consumption of working engines.
Not the active requirement for this page.
```

Possible proof forms:

```text
SMT real-vs-erased control flip
Lyapunov/ranking certificate
interval box graph proof
finite state transition proof
```

Do not let this block the engine-running lanes unless the user explicitly asks
for formal proof.

## Julia And JAX Packages / Tooling

Packages and surfaces used or needed across the current lane:

### Julia

Observed/needed Julia surfaces:

```text
Julia project:
  /Users/joshuaeisenhart/Codex-Ratchet/system_v5/julia_carrier

Used in current artifacts:
  Julia 1.12.6 in native Axis-6 parity artifact

Likely package roles:
  LinearAlgebra       - dense matrices, eigenvalues, norms
  Random             - seeded finite probes
  Statistics         - summaries
  JSON / JSON3       - result artifacts
  StaticArrays       - small fixed-size Bloch vectors
  QuantumOptics.jl   - density/operator/channel lane in older/full placement work
  DifferentialEquations.jl - ODE/GKSL/Lindblad integration lanes
  ITensors.jl / ITensorMPS.jl - post-PEPS3D tensor-network carrier direction
  TensorKit.jl       - exact dense/tensor reference carrier direction
  QuantumClifford.jl - Clifford/stabilizer carrier direction
  IntervalArithmetic.jl - future interval proof lane
  IntervalRootFinding.jl - future interval proof lane
  Satisfiability.jl or direct SMT-LIB - future SMT lane
  PythonCall.jl      - optional bridge to z3/cvc5 if direct SMT is not used
```

### JAX

Observed/needed JAX surfaces:

```text
JAX version in native Axis-6 parity artifact:
  0.10.1

Required mode:
  jnp with x64 enabled
  no NumPy compute for parity claims
```

Likely package roles:

```text
jax
jax.numpy as jnp
jax.scipy.linalg
diffrax for ODE lanes when needed
equinox / optax only if learning or parameter search is opened
```

### Python / proof / graph tools

For current and future lanes:

```text
z3 / z3-solver    - finite constraint and UNSAT checks
cvc5              - solver cross-check / synthesis
sympy             - symbolic identities
networkx          - simple graph controls
rustworkx         - faster directed graph/order controls
XGI               - hypergraph candidates
TopoNetX          - cell-complex candidates
GUDHI             - persistence/topology candidates
clifford          - geometric algebra scouts
geomstats         - manifold metric/geodesic scouts
e3nn              - equivariant neural/tensor direction
PyTorch / PyG     - first-class graph/network compute when current bounded receipts make that role load-bearing; Julia remains arbitration canon
```

## Workflow Shape To Use

Do not run a giant proof workflow as the first move.

Before Axis work, use the pre-Axis admission pipeline:

```text
root constraints
-> finite QIT carrier
-> pre-Axis geometry machinery
-> pre-Axis transport machinery
-> pre-Axis differential / chirality / candidate-flux machinery
-> negative / falsification machinery
-> placement machinery
-> Axis-entry machinery
-> Axis machinery proper
```

Axis embargo rule:

```text
No math may function as an Axis object until it has first been admitted as
constrained, QIT-grounded, simulated, and negatively tested machinery.
```

This protects the axes from smuggling in:

```text
continuum leakage
metric leakage
entropy-first shortcuts
classical flow language
generic geometry assumptions
operator choices that are familiar but not constraint-admitted
```

Use this order:

```text
0. Source lock
   Read source docs and produce machine-checkable 16-token matrix.

1. Native row runner
   Run all 16 native Axis-6 placements in Julia and JAX.

2. Engine stage-order runner
   Run Type 1 and Type 2 loop orders and reversal controls.

3. Functional-role runner
   Only for named functional claims, e.g. TeSi hill ascent.

4. Connection-geometry runner
   Run Hopfield/PEPS2D ablations and source-precedence audit.

5. Wide exploration runner
   Throw candidate families at F01/N01 and keep graveyard.

6. Basin runner
   Only after maps are stable; test recurrence and boundary.

7. Formal proof runner
   Optional later proof consumption of the working finite maps.
```

Each runner should emit:

```text
classification
promotion_allowed
formal_admission_allowed
source docs read
result path
native formulas
control formulas
blocked consumers
```

## Current Best Next Runs

Best next run if the goal is engine clarity:

```text
Run the named functional-role test for TeNi / TeSi / NiTe / SiTe.

Define H_Ni and H_Si first.
Then test whether the chart's ascent/descent role survives as a monotone
finite readout.
```

Best next run if the goal is carrier clarity:

```text
Re-run connection-geometry ablations with the 16-token row table attached
directly to each ablation variant.
```

Best next run if the goal is emergence:

```text
Do wide exploration on full-structure carriers only:
  Clifford
  quaternion
  SU(2)/Spin
  spinor-native

Include unital controls and N01-off controls.
Do not use random 2x2 toys as the main handedness test.
```

Best next wiki/process move:

```text
Patch workflows/skills so every QIT/IGT lane reads this page plus the four
source math docs before simming.
```

## Final Current Verdict

What has been earned:

```text
The terrain/operator grammar is now explicit enough to run.
The 16 native Axis-6 placements have concrete finite maps.
Julia and JAX agree on those 16 placements in scratch.
Engine loop order and pattern pair order are load-bearing in scratch.
The nested PEPS2D/Hopfield connection geometry is the active scratch carrier
story replacing PEPS3D for this lane.
The wide F01/N01 exploration produced a useful graveyard but not a basin proof.
```

What remains open:

```text
Win/loss executable payoff math.
Named gradient/ascent/descent functionals.
Full carrier admission.
Universal attractor basin.
Formal proof.
Axis0/flux/FEP/bridge/physics.
```

The honest project sentence:

```text
The current QIT/IGT engine lane has runnable finite terrain/operator maps with
source-locked order sensitivity. The next job is to keep running them, widen the
graveyard, define the missing functionals, and only then ask which survivor
basin, if any, the constraints converge toward.
```
