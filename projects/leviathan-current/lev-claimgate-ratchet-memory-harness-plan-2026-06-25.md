---
title: Lev ClaimGate Ratchet Memory Harness Plan
created: 2026-06-25
updated: 2026-06-25
type: implementation-plan
status: current-integrated-plan
claim_ceiling: current plan and source-router for a Lev patch; not merged canon; not runtime proof; not full Wizard, Holodeck, or three-engine implementation proof
source_repo: /Users/joshuaeisenhart/GitHub/lev
wiki_probe: /tmp/wiki_probe_lev_plan.json
---

# Lev ClaimGate Ratchet Memory Harness Plan

## Purpose

This is the current integrated plan for the work that was drifting across threads:

```text
Upgrade Lev's graph/execution/memory process with ClaimGate admission,
Ratchet-style gate loops, projection-binding memory, sim-engine PROBEs,
Spinor Memory read-models, and a small Holodeck/world-model prototype.
```

This is not a new system beside Leviathan. It is a plan to patch Leviathan using
Lev's own primitives: FlowMind, graph operations, proposals, gates, PROBEs,
receipts, memory projections, orchestration loops, and host admission.

It also preserves the Josh/JP boundary:

- JP / Lev owns the runtime lane: FlowMind, orchestration, graph, event/receipt
  machinery, execution surfaces, and host semantics.
- Josh / Codex Ratchet supplies the sharper constraint/admissibility lane:
  no primitive objects, no primitive equality, no primitive causality, survivor
  quotients under probes, strict finitude, non-commutation, purgatory/suspension
  records for family-relative splits, and scope-local integrity/authority
  blocks outside the identity layer when admission must close, sim probes, gate
  digging, and attractor-basin discipline.
- The bridge is not identity. Codex Ratchet and Leviathan can be aligned without
  collapsing one into the other.

## Root framing in Lev terms

Lev's root constraints are C1 and C2:

- **C1 Finitude**: every context expansion, loop, probe, model lane, sim run, and
  memory update must be bounded.
- **C2 Non-Commutation**: order matters; the trace of operations is part of the
  survivor-class hypothesis being evaluated.

C3-C5 are important governance consequences, not equal-level roots:

- projected names do not execute by themselves;
- ratchets converge through bounded, ordered selection;
- every claim has local scope and local authority.

In this plan, the first-class substrate is not a dictionary entry or a fixed
object. It is an actual thesaurus field: a finite neighborhood of similar
surfaces under declared rotations, translations, projections, and probes.
Objecthood is a later quotient claim over that field. A projected label,
embedding neighbor, wiki title, prompt phrase, code symbol, or LLM
reconstruction is not graph identity by itself.

## Actual object we are building

The patch object should be named something like:

```text
Lev ClaimGate Ratchet Memory Harness
```

It is a minimal Lev-native harness with these pieces:

1. **ClaimGate host admission**: source projections can propose; host Lev
   recomputes and admits or blocks.
2. **Transformation-aware thesaurus memory**: similar surfaces form candidate
   neighborhoods first; only later can a survivor class become an object
   candidate after evidence, authority, role, rotations, and receipts survive
   probes.
3. **Three-engine mechanical PROBEs**: Julia, JAX, and PyTorch act as bounded
   evidence probes for uncertain claims. They are not proof authority.
4. **Spinor Memory foundation**: ordered read-model cells over operator traces,
   gate results, receipts, survivor state, purgatory state, and outer
   scope-block state. A Spinor cell cannot mutate graph state.
5. **Holodeck/world-model proto**: a small predictive tick loop:
   predict -> project -> sense/probe -> residual -> survive / split to
   purgatory / re-merge / remain exhausted-in-scope / escalate to an outer
   scope block only on integrity or authority failure -> update/re-enter.
6. **Wizard/council/swarm as execution topology**: councils and model lanes
   generate proposals, failures, repairs, and dissent. Deterministic gates and
   host receipts decide.
7. **GraphPatch admission path**: admitted work becomes `GraphOperation[]`
   through Lev's graph compositor and gate hooks, not prose closure.

## Existing Lev anchors

Observed in current local repo `/Users/joshuaeisenhart/GitHub/lev`:

- `dna/graph.yaml` already names the kernel/projection split, C1/C2 roots,
  graph primitives, graph op algebra, `PROBE`, and lossy projection discipline.
- `.lev/validation-gates.yaml` already names ClaimGate steering admission and
  overclaim blocking gates, graph semantics, module gates, progress gates, and
  validation expectations.
- `core/graph/src/types.ts` already has `Entity`, `Claim`, `Evidence`,
  `GraphOperation`, `GraphEvent`, and `TruthState`.
- `core/graph/src/compositor.ts` already uses extract -> classify -> validate
  -> apply, with gates as validation hooks and evidence refs wired to graph
  events.
- `core/memory/src/session-state-projection.ts` already shows the read-model
  pattern: regenerate a projection from canonical inputs rather than letting
  the projection become authority.
- `plugins/qit-engines/config.yaml` and
  `plugins/qit-engines/schemas/engine.schema.yaml` already hold Joshua/QIT
  engine vocabulary and provenance.
- `.lev/pm/designs/design-world-model-stack.md` already frames the predictive
  world-model as the unbuilt half of the kernel, feeding admission/projection
  rather than replacing them.
- `docs/design/design-codex-ratchet-claim-gate-bridge.md` already states the
  bridge law: Codex Ratchet can mine axioms, constraints, gates, basin maps, and
  repairs, but it does not create a second admission authority.

Observed active patch work, not automatically canon:

- `core/orchestration/src/proof/claim-gate-steering-run.ts`
- `core/orchestration/src/proof/claim-gate-steering-produce.ts`
- `core/orchestration/src/proof/claim-gate-loop.ts`
- `core/orchestration/src/proof/claim-gate-ratchet-harness.ts`

At the time of this note, some ClaimGate/Ratchet files are untracked in the
local worktree. Treat them as active patch evidence, not merged Lev truth.

## ClaimGate in Lev terms

ClaimGate is the host-side gate for source projections that want authority.

```text
source projection
  -> ClaimGate proposal / steering run
  -> host Lev recomputes the proposed survivor-binding claim, evidence, verdict, and claim ceiling
  -> host_consumed | host_blocked
  -> receipt
```

It exists to prevent:

- source projections from self-promoting;
- model/council agreement from becoming proof;
- beautiful reports from counting as admission;
- graph patches from bypassing host gates;
- verdict strings from outranking per-evidence recomputation.

In Lev language, ClaimGate is a gate/eval/receipt boundary around proposed graph
state. It should feed `GraphOperation[]` only after host recomputation.

## Memory upgrade in Lev terms

This is not "add a bigger vector database."

The memory upgrade is an actual thesaurus layer, not a dictionary layer:

```text
ProjectionSurface
  -> ThesaurusNeighborhood
  -> Rotation / Transformation family
  -> SurvivorClass / split class
  -> SurfaceBindingCandidate / ObjectCandidate quotient claim
  -> ProbeFamily + GateResult + OperatorTrace
  -> SurvivorReceipt | PurgatoryRecord
  -> ResurrectionTrigger (when applicable)
  -> SpinorMemoryCellCandidate
  -> future context assembly / graph patch proposal

Outer admission/governance layer only:
  proposal or purgatory branch
    -> ScopeBlockReceipt (when applicable)
```

Where:

- `ProjectionSurface` is where a surface appeared: prompt, wiki page, skill,
  receipt, code symbol, search result, graph view, dashboard, model output.
- `ThesaurusNeighborhood` is the finite set of nearby surfaces before identity
  is asserted. This is not just synonym lookup; it is the candidate field under
  transforms.
- `Rotation` / `Transformation` records the probes that move a surface through
  other views: wording changes, code-path shifts, graph projection, sim engine
  transforms, source binding, receipt recomputation, session reset, and model
  family change.
- `SurvivorClass` is what remains indistinguishable under the active transform
  family. Split classes are kept too; they are not noise.
- `ObjectCandidate` is a later quotient claim over a survivor class, not a
  primitive object and not a dictionary definition.
- `SurfaceBindingCandidate` says two surfaces may co-survive under one declared
  transform family, pending gates. It never implies global identity.
- `ProbeFamily` is the finite set of checks that can distinguish, split, or
  preserve the survivor class.
- `OperatorTrace` is the ordered history of transformations and gates.
- `SurvivorReceipt` says the binding survived the declared probes under a
  specific family.
- `PurgatoryRecord` says the binding split or failed under one family without a
  terminal object death. It records obstruction depth, reopen budget, and how
  the candidate can reopen.
- `ResurrectionTrigger` records the new family, evidence, or repaired source
  binding that is allowed to re-open a purgatory record.
- `ScopeBlockReceipt` belongs to the enclosing admission/governance layer, not
  the identity/thesaurus layer. It records host-local integrity or authority
  closure, not ontological death of the surfaces.
- `SpinorMemoryCellCandidate` is a read-model over the ordered trace. It cannot
  apply graph operations by itself.

So the short formula is:

```text
Thesaurus field + rotations + graph + gates + receipts + ordered time = Lev memory.
```

Graph alone is structure. Gates alone are decisions. Dictionary terms alone are
handles. Receipts and ordered traces make the transformation history durable.

### Purgatory, not premature graveyard

The identity-binding layer must not turn a split under one probe family into
final death. That would make the negative path another dictionary.

Use this state machine:

```text
M1 survive:
  SurfaceBindingCandidate(state=under_review, family=M1)
    -> probes pass
    -> SurvivorReceipt(scope=M1, status=provisional_survivor)

M2 split:
  prior survivor
    -> stricter or different transform family distinguishes the surfaces
    -> PurgatoryRecord(status=suspended_by_M2)
    -> ObjectCandidate claim is downgraded to family-local / provisional

M3 re-merge:
  PurgatoryRecord
    -> ResurrectionTrigger(new_family=M3 | new_evidence | repaired_source_binding)
    -> re-evaluate split branches
    -> SurvivorReceipt(scope=M3, status=remerged_survivor)

M4 exhausted in current scope:
  PurgatoryRecord
    -> obstructionDepth reaches max OR reopenBudgetRemaining reaches 0
    -> PurgatoryRecord(status=exhausted_in_scope)

Outer gate only:
  proposal or purgatory branch
    -> integrity/authority failure in enclosing host scope
    -> ScopeBlockReceipt(blockKind=integrity|authority|lineage)
```

`PurgatoryRecord` fields should include `bindingCandidateId`, `surfaceRefs`,
`priorSurvivorReceiptRefs`, `splitFamilyId`, `splitReason`,
`distinguishingEvidenceRefs`, `branchClassRefs`, `operatorTraceRef`,
`claimCeiling: family_local_nonterminal`, `obstructionDepth`,
`obstructionDepthMax`, `reopenableFamilyRefs`, `reopenBudgetRemaining`,
`reopenBudgetMax`, and `status`.

`ResurrectionTrigger` fields should include `triggerKind`, `triggerFamilyId`,
`triggerEvidenceRefs`, `remergeHypothesis`, and `operatorTraceRef`.

Do not rename existing terminal `graveyardReason` fields in ClaimGate loop code
until there is a migration plan. Those fields describe bounded terminal
failures such as max-pass exhaustion, not family-relative identity splits.

## Three-engine PROBEs

The three sim engines should enter Lev as mechanical `PROBE`s, not as authority:

```text
UNCERTAIN gate
  -> ProbeFamily:
       julia_exact
       jax_geometry
       pytorch_graph
       source/hash/receipt checks
       negative controls
  -> evidence
  -> gate resolves pass/fail/uncertain
```

The desired role split:

- **Julia**: exact/canonical/algebraic probe.
- **JAX**: vectorized/differentiable/geometry probe.
- **PyTorch**: graph/autograd/tensor probe.

Agreement across engines is not proof. It is only evidence if:

- inputs are source-backed;
- outputs are content-hashed;
- the expected negative control fails;
- by-construction invariance is excluded;
- the result can change a gate outcome.

Implementation should start in `plugins/qit-engines` as schemas and fixture
validators. Heavy Julia/JAX/PyTorch runtimes should not become core Lev
dependencies.

## Holodeck proto in Lev terms

Holodeck is not a literal UI or replay store here. In Lev terms, it is a
predictive memory/world-model loop:

```text
predict
  -> project
  -> observe / PROBE
  -> residual / error
  -> survive / split to purgatory / possible re-merge / terminalize only under closed scope
  -> receipt
  -> re-enter next tick
```

This maps to Lev's tick:

```text
INGEST -> OBSERVE -> PROPOSE -> GATE -> APPLY -> UPDATE -> EMIT
```

The first patch should be a proto contract and fixture, not a full predictive
world model. The existing `.lev/pm/designs/design-world-model-stack.md` already
marks the predictive world-model as unbuilt, and that ceiling should stay
visible.

## Wizard, councils, and swarm in Lev terms

Wizard/council/swarm output is proposal generation and critique, not authority.

Correct hierarchy:

```text
Run
  -> bounded wave phases
      -> councils
          -> subcouncils / teams
              -> agents
                  -> skills + MMMs + tools + source packs
```

Waves are larger phases. Axiom digging, gate digging, premortem, source truth,
Ponytail/Krypton, falsifier, and repair routing are councils or subcouncils.

Lev placement:

- FlowMind declares the run topology and policy.
- Orchestration schedules bounded execution.
- Context/memory loaders resolve declared skills, MMMs, and source packs.
- ClaimGate/graph gates decide whether outputs can affect graph state.
- Receipts preserve the ordered result.

## Patch slices

### Slice 0: Stabilize the patch object

Goal: one clean patch/zip, not a smear across Lev.

- Separate committed Lev truth, dirty worktree patch files, old ZIP/source
  packs, and wiki notes.
- Quarantine `wavegraph` vocabulary as historical/drift unless explicitly
  renamed into Lev terms.
- Verify from a fresh extract/worktree before stronger claims.

### Slice 1: ClaimGate host bridge

Goal: source projection -> host recompute -> consumed/blocked receipt.

- Keep `claim-gate-steering` as the narrow host boundary.
- Preserve `host_blocked` for verdict mismatch, overclaim, tamper, and missing
  evidence.
- Ensure GraphPatch proposal remains proposal-only until host admission.

### Slice 2: Transformation-aware thesaurus contract

Goal: build the actual similarity field without pretending it is already graph
identity.

Add or mirror contracts for:

- `ProjectionSurface`
- `ThesaurusNeighborhood`
- `Rotation`
- `Transformation`
- `SurvivorClass`
- `SplitClass`
- `ObjectCandidate`
- `SurfaceBindingCandidate`
- `ProbeFamily`
- `OperatorTrace`
- `SurvivorReceipt`
- `PurgatoryRecord`
- `ResurrectionTrigger`
- `ScopeBlockReceipt` (outer layer only)

Start with fixture validators and graph claims before adding new storage.

### Slice 3: Spinor Memory read-model

Goal: ordered memory cells from canonical inputs.

Add a `SpinorMemoryCellCandidate` projection under memory/orchestration that:

- records ordered transformations;
- records gate statuses and reasons;
- links receipts;
- marks `promotionAllowed: false`;
- can be regenerated from canonical inputs.

### Slice 4: Three-engine PROBE envelope

Goal: make sim engines useful to Lev gates.

Add `ThreeEngineProbeEnvelope` under `plugins/qit-engines` with:

- engine id;
- source ref;
- input hash;
- output hash;
- transform claim;
- negative control;
- expected gate effect;
- result status.

Do not install heavy engines in core. Start with fixtures and contracts.

### Slice 5: Holodeck/world-model proto tick

Goal: one bounded predictive memory fixture.

- Use Lev tick language.
- Emit proposed graph claims, residuals, survivor receipts, purgatory records,
  resurrection triggers, and outer scope-block receipts when host
  integrity/authority gates close the lane.
- Connect to ClaimGate as a proposal source.
- Do not claim full predictive world-model runtime.

### Slice 6: Wizard/council execution topology

Goal: bounded proposal generation with real context loading.

- Durable members declare role, skills, MMMs, source refs, tools, contracts,
  gate contracts, requeue policy, model lane, and receipt target.
- Loaders must actually resolve and hash those refs.
- Councils generate candidate proposals/failures/repairs.
- Gates and host receipts decide.

## Minimal acceptance tests

The first real test suite should prove:

1. Similar labels do not auto-collapse into the same survivor quotient or binding claim.
2. Different labels can bind when role, authority, evidence, and receipts match.
3. A binding can survive under `M1`, split under `M2`, and re-merge under `M3`.
4. Family-local failure creates a `PurgatoryRecord`, not terminal suppression.
5. Only enclosing integrity/authority gates mint a `ScopeBlockReceipt`;
   family exhaustion stays `PurgatoryRecord(status=exhausted_in_scope)`.
6. A Spinor memory cell cannot apply a graph mutation.
7. Three-engine probe envelopes require source refs, hashes, and negative
   controls.
8. ClaimGate blocks overclaim and verdict mismatch.
9. A good proposal can become a host-admitted GraphPatch apply plan.
10. Wizard/council/model output remains proposal-only.
11. Every loop has a budget, stop condition, and receipt.

## What not to do

- Do not require Neo4j, Docker, Julia, JAX, or PyTorch for the minimal core
  slice.
- Do not build a second proof brain beside Lev.
- Do not let model lanes, councils, dashboards, or wiki pages promote graph
  state.
- Do not treat vector similarity or matching words as identity.
- Do not treat Spinor Memory as authority.
- Do not treat three-engine agreement as proof without negative controls.
- Do not turn a fixture into a runtime claim.
- Do not flatten Josh's purist constraint lane into generic product language.
- Do not erase JP's runtime/FlowMind implementation lane.

## Immediate next move

The next concrete move should be:

```text
Build one fixture-level vertical slice:

two ProjectionSurfaces
  -> ThesaurusNeighborhood
  -> TransformFamily
  -> SurfaceBindingCandidate
  -> uncertain gate
  -> mechanical PROBE fixture
  -> SurvivorReceipt or PurgatoryRecord
  -> ResurrectionTrigger when later families justify re-merge
  -> SpinorMemoryCellCandidate
  -> ClaimGate GraphPatch proposal
  -> host consume/block receipt
```

Keep it small, local, and testable. This is the bridge from the existing
ClaimGate patch project into Lev memory/graph semantics.

## Deep audit update 2026-06-25

A three-lane read-only audit was run after the thesaurus correction:

- **Lev graph implementation lane**: converged on `core/graph` as the owner of
  canonical contracts and validators; `core/memory` as read-model only;
  `plugins/qit-engines` as fixture/schema owner for sim PROBEs; and
  `core/orchestration` as ClaimGate host-consumption owner.
- **Nominalist/thesaurus lane**: corrected remaining object-smuggling terms.
  `ObjectCandidate` must stay a later quotient claim over a survivor class.
  Prefer `SurfaceBindingCandidate` and survivor-binding claim wording over
  `same object` or unqualified `binding`.
- **Enforcement/gate lane**: found the most concrete next gap. The generic
  `core/graph/src/handlers/graph-patch.ts` path accepts raw operations and
  currently treats `applyPlanReceiptId` as metadata rather than a hard admission
  precondition. That means a bad model-generated graph operation can still reach
  the graph compositor unless the caller voluntarily uses the ClaimGate path.

Therefore the next implementation slice should tighten the generic graph write
surface:

```text
ClaimGate GraphPatch proposal
  -> host-issued admission/apply-plan receipt
  -> graph-patch handler verifies receipt
  -> graph.process applies GraphOperation[]
```

Negative test:

```text
raw graph patch with missing/tampered/non-host applyPlanReceiptId
  -> rejected
  -> no graph.operations_applied event
  -> no local graph mutation
```

This is the smallest enforcement move that makes the graph itself participate
in ClaimGate authority instead of relying on LLMs, councils, or callers to stay
on the honest path.

## Cross-corpus memory audit update 2026-06-25

A second broader audit read Lev, Codex Ratchet, and the wiki memory/nominalism
cluster. The converged object is:

```text
finite projection surfaces
  -> candidate neighborhoods
  -> ordered transforms / probes
  -> survivor / split claims
  -> receipts
  -> read-model projections
  -> possible graph patch
```

This is the memory concept that transcends vector databases. It is not
anti-vector. Vectors, hashes, and indexes are useful salience and confirmation
handles. They answer:

```text
what is nearby?
what candidate reconstruction should be checked?
which stored cue may confirm this reconstruction?
```

They do not answer:

```text
what is the object?
what is graph identity?
what may mutate Lev state?
```

### Dictionary vs thesaurus correction

A dictionary memory stores definitions under names. That is the failure mode:
once the name is present, downstream agents treat the named thing as already
formed.

A thesaurus memory stores finite neighborhoods of surfaces under rotations,
translations, contexts, and probes. It says:

```text
these surfaces are near each other under family M
these rotations preserve the neighborhood
these rotations split it
these traces and receipts explain the current status
```

Only after that can Lev form a family-local `SurfaceBindingCandidate` or
`ObjectCandidate`. The "object" is not a primitive entry in the memory store. It
is a quotient claim over a survivor class, under a declared probe family.

### Holodeck kernel that matters

The Holodeck memory kernel is:

```text
predictive world model
  + semantic/vector confirmation handles
  + contextual trigger chains
  + confirmation-over-free-recall
  + world/sim as recall space
```

In implementation terms:

```text
current context / trigger
  -> activate partial cue lattice
  -> generate candidate reconstruction
  -> compare against positive and negative handles
  -> compute residual / obstruction
  -> survivor, purgatory, or outer authority block
  -> update / re-enter next bounded tick
```

The world, ASCII scene, dashboard, or graph view is not automatically memory.
It can become a memory-bearing recall space when it carries durable contextual
cues that reactivate and check reconstruction chains.

### Lev alignment

Lev already has the right owner surfaces:

- `core/graph`: canonical graph semantics, `Entity`, `Claim`, `Evidence`,
  `GraphOperation`, `TruthState`, validation hooks, and graph events.
- `core/memory`: retrieval/read-model machinery. It can project Spinor cells
  from canonical graph/event/receipt inputs, but should not decide identity.
- `plugins/qit-engines`: natural home for sim-engine PROBE schemas and fixtures.
  Heavy Julia/JAX/PyTorch runtimes stay optional.
- `core/orchestration`: ClaimGate host-consumption and receipt boundaries.
- FlowMind/orchestration/ticks: bounded execution topology for running probe and
  repair loops.

The current memory subsystem is still mostly hybrid retrieval: keyword/vector/
graph backends plus rank fusion and session projections. That is useful, but it
is not yet probe-relative identity memory. The upgrade is to add graph-owned
binding/probe/receipt contracts and then let `core/memory` project read-models
from those contracts.

### Codex Ratchet alignment

Codex Ratchet supplies reference behavior, not Lev canon:

- `gate_object_binding.py` is the reference for membership/location/lineage
  binding. Its ceiling is explicit: it does not prove execution freshness,
  runner identity, or notary authenticity.
- Holodeck probes show finite probe-relative indistinguishability,
  reconstruction-with-residual, and substrate-dependent refutation.
- `validate_three_engine_sim_result.py` validates a three-engine envelope. It is
  a shape/source/negative-control discipline, not mathematical proof.
- Ratchet's controller contracts already name the LLM failure mode: models
  collapse `exists`, `runs`, `passes`, `verified`, and `canonical`. Lev must make
  code carry those distinctions.

### Three-engine role in memory

The three engines are not memory stores and not proof authority. They are
mechanical `PROBE` families that put independent reconstruction pressure on a
candidate:

```text
Julia: exact / algebraic / canonical probe
JAX: geometry / differentiable / vectorized probe
PyTorch: graph / tensor / autograd probe
```

The useful memory event is not "all engines agree." The useful event is:

```text
each engine ran from source-backed inputs,
each emitted content-hashed outputs,
negative controls failed as expected,
divergence was measured,
and the result changed or could change a gate outcome.
```

Agreement without controls is decorative. Divergence is a distinguishability
event and should usually produce a `PurgatoryRecord`, not prose smoothing.

### Negative memory states

Use three different negative planes:

- `PurgatoryRecord`: identity/thesaurus split under a family; reopenable with
  obstruction depth and finite reopen budget.
- active negative handle: Holodeck/Ratchet "graveyard hash" as a suppression or
  exclusion cue inside reconstruction. This should not be treated as a final
  graph death.
- `ScopeBlockReceipt`: outer host/admission integrity or authority block, for
  forged lineage, tamper, missing authority, or invalid apply-plan receipt.

Do not collapse these into one `graveyard` primitive.

### Implementation consequence

The correct first code move is still not a database choice. It is a small set of
Lev-owned contracts and validators:

```text
core/graph/src/contracts/projection-binding.ts
  ProjectionSurface
  ThesaurusNeighborhood
  TransformFamily
  SurfaceBindingCandidate
  ProbeFamily
  OperatorTrace
  SurvivorReceipt
  PurgatoryRecord
  ResurrectionTrigger
  ScopeBlockReceipt

core/memory/src/... spinor projection
  SpinorMemoryCellCandidate regenerated from canonical graph/event/receipt inputs

plugins/qit-engines/... three-engine envelope
  ThreeEngineProbeEnvelope with source refs, hashes, controls, divergence

core/graph graph-patch gate
  require host-issued apply-plan receipt before raw GraphOperation[] can apply
```

This lets retrieval systems nominate candidate neighborhoods, sim engines probe
them, ClaimGate admit or block their graph effects, and Spinor Memory preserve
the ordered trace without becoming authority.

## Purgatory audit update 2026-06-25

A second three-lane agent audit checked the `graveyard` terminology after the
family-relative binding correction.

Verdict:

- In the identity/thesaurus layer, unqualified `GraveyardReceipt` is too strong.
  It turns a split under one transform family into terminal death and smuggles a
  dictionary back into the negative path.
- The correct default is `PurgatoryRecord`: a suspended, reopenable binding
  candidate with obstruction depth and resurrection triggers.
- The identity/thesaurus layer should not mint a terminal graveyard primitive.
  When closure is needed, it should happen in an outer admission/governance
  layer as a `ScopeBlockReceipt` for integrity, authority, or lineage failure.
- Existing ClaimGate `graveyardReason` fields should not be renamed casually.
  They are serialized terminal loop evidence, not the new family-relative
  identity-binding state.

The demonstrator must prove:

```text
M1: two surfaces co-survive
  -> SurvivorReceipt(scope=M1)

M2: stricter family splits them
  -> PurgatoryRecord(status=suspended_by_M2)
  -> no terminal receipt

M3: later family or repaired evidence re-merges them
  -> ResurrectionTrigger
  -> SurvivorReceipt(scope=M3, status=remerged_survivor)
```

If that M3 re-merge is missing, the fixture has not proven purgatory. It has
only proven a nicer-named rejection list.

## Bounded Hermes intake pack

```yaml
purpose: "Preserve and route the current Lev ClaimGate/Ratchet/memory patch plan."
role: "bounded_synthesizer"
frame: "Translate Josh-origin constraint/sim/memory ideas into Lev graph, FlowMind, orchestration, memory, PROBE, and receipt terms without claiming runtime proof."
read_order:
  - hermes-current/read-first.md
  - hermes-current/skills-and-agent-rules.md
  - hermes-current/current-vs-legacy.md
  - hermes-current/active-intentions.md
  - projects/leviathan-current/read-first.md
  - projects/leviathan-current/index.md
  - projects/leviathan-current/josh-root-constraints-in-leviathan.md
  - projects/leviathan-current/codex-ratchet-vs-leviathan-boundary.md
  - projects/leviathan-current/research-ratchet-deep-patch-plan-2026-06-21.md
  - projects/leviathan-current/nested-wave-council-management-plane-patch-2026-06-23.md
  - dna/graph.yaml
  - .lev/validation-gates.yaml
do_not_read: "Do not treat raw chats, old ZIPs, dirty worktree files, or model prose as authority without current file-backed receipts."
questions:
  - "Which piece is current Lev canon, active patch work, source pack, or wiki synthesis?"
  - "Which Lev primitive owns this: FlowMind, graph, orchestration, memory, qit-engines, ClaimGate, or validation gate?"
  - "What is the smallest fixture that proves the contract without overclaiming runtime?"
required_output: "One current integrated plan note plus a next implementation slice."
promotion_rule: "Wiki note routes work; only Lev tests, gates, and host receipts can promote code/graph state."
target_codex_surface: "Lev repo patch plan and projects/leviathan-current wiki memory."
minimal_test: "wiki_probe clean plus current repo file reads and explicit claim ceilings."
```

## Processing receipt

Files/probes used for this note:

- `dna/graph.yaml`
- `.lev/validation-gates.yaml`
- `core/graph/src/types.ts`
- `core/graph/src/compositor.ts`
- `core/memory/src/session-state-projection.ts`
- `.lev/pm/designs/design-world-model-stack.md`
- `docs/design/design-codex-ratchet-claim-gate-bridge.md`
- `core/orchestration/src/proof/claim-gate-ratchet-harness.ts`
- `docs/specs/spec-memory.md`
- `core/graph/src/handlers/graph-patch.ts`
- `plugins/qit-engines/config.yaml`
- `/Users/joshuaeisenhart/Codex-Ratchet/AGENTS.md`
- `/Users/joshuaeisenhart/Codex-Ratchet/CODEX.md`
- `/Users/joshuaeisenhart/Codex-Ratchet/system_v5/docs/LLM_CONTROLLER_CONTRACT.md`
- `/Users/joshuaeisenhart/Codex-Ratchet/system_v5/docs/LEGO_SIM_CONTRACT.md`
- `/Users/joshuaeisenhart/Codex-Ratchet/system_v5/docs/HOLODECK_AXIS0_MEMORY_ENGINE_PROPOSAL_HANDOFF_20260516.md`
- `/Users/joshuaeisenhart/Codex-Ratchet/scripts/gate_object_binding.py`
- `/Users/joshuaeisenhart/Codex-Ratchet/scripts/validate_three_engine_sim_result.py`
- `/Users/joshuaeisenhart/Codex-Ratchet/system_v4/probes/sim_holodeck_deep_probe_relative_indistinguishability.py`
- `/Users/joshuaeisenhart/Codex-Ratchet/system_v4/probes/sim_holodeck_reality_reconstruction_probe.py`
- `/Users/joshuaeisenhart/Codex-Ratchet/system_v4/probes/sim_cross_holodeck_x_science_method.py`
- `concepts/spinor-memory.md`
- `concepts/projective-holodeck-memory-model.md`
- `concepts/holodeck-as-recall-space.md`
- `concepts/prediction-first-memory-vs-llm-memory.md`
- `concepts/nominalism-in-this-system.md`
- `concepts/constraint-on-distinguishability.md`
- `concepts/nominalist-cs-framing.md`
- `concepts/translation-methodology-reference.md`
- `projects/leviathan-current/read-first.md`
- `projects/leviathan-current/index.md`
- `projects/leviathan-current/josh-root-constraints-in-leviathan.md`
- `projects/leviathan-current/codex-ratchet-vs-leviathan-boundary.md`
- `projects/leviathan-current/research-ratchet-deep-patch-plan-2026-06-21.md`
- `projects/leviathan-current/nested-wave-council-management-plane-patch-2026-06-23.md`
- `python3 /Users/joshuaeisenhart/wiki/tools/wiki_probe.py --wiki-root /Users/joshuaeisenhart/wiki --output /tmp/wiki_probe_lev_plan.json`

Wiki probe result observed:

```text
page_count: 460
index_header_count: 460
indexed_link_count: 578
missing_pages: []
broken_links: []
stubs: []
malformed_wikilinks: []
stale_namespace_wikilinks: []
```
