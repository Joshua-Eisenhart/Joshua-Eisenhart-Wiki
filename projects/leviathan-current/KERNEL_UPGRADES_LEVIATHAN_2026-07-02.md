---
title: Kernel Upgrades Leviathan
created: 2026-07-02
updated: 2026-07-03
type: horizon-map
status: scratch-kernel integration map
claim_ceiling: v9 bundle state is treated here as scratch_diagnostic only; promotion_allowed=false; this page routes possible upgrades and current receipts without promoting any constraint-core result to canon
tags: [lev, leviathan, codex-ratchet, constraint-core, mesh, privacy-membrane, admissibility]
sources:
  - ../constraint-core/RATCHET_STATE_BY_TIER_2026-07-02.md
  - ./MESH_NODE_PROTOCOL_V0_2026-07-02.md
  - ./GATE_DOCTRINE_ADMISSIBILITY_NOT_QUALITY.md
  - ./LEV_CR_INTEGRATION_STATE_2026-07-02.md
  - ./CR_LEV_MERGE_PROJECT_PLAN_2026-07-02.md
  - ./LEVIATHAN_CONSTRUCT_TO_MESH_MAP_2026-07-02.md
---

# Kernel Upgrades Leviathan - 2026-07-02

This page says what the constraint-core sim kernel upgrades in the Leviathan / `lev` / mesh stack, without letting a later horizon borrow status from an earlier one.

The source tier map keeps two lanes: canon-by-process and hypothetical scratch. Everything below that depends on the v9 bundle state is `scratch_diagnostic`, `promotion_allowed=false`, and not a Codex Ratchet canon promotion. Where the tier source records explicit `v1..v8` laptop lineage, this page does not amend that lineage; `v9 bundle state` is the owner prompt label for the current scratch bundle posture.

## Sibling Docs

- [Lev / CR Integration State](./LEV_CR_INTEGRATION_STATE_2026-07-02.md)
- [Mesh Node Protocol v0](./MESH_NODE_PROTOCOL_V0_2026-07-02.md)
- [Gate Doctrine: Admissibility, Not Quality](./GATE_DOCTRINE_ADMISSIBILITY_NOT_QUALITY.md)
- [CR / Lev Merge Project Plan](./CR_LEV_MERGE_PROJECT_PLAN_2026-07-02.md)
- [Relevant Docs Index](./RELEVANT_DOCS_INDEX_2026-07-02.md)

Additional local map: [Leviathan Construct To Mesh Map](./LEVIATHAN_CONSTRUCT_TO_MESH_MAP_2026-07-02.md).

## Related Docs - 2026-07-03

Wiki:

- [[projects/leviathan-current/source/README]] and `projects/leviathan-current/source/leviathan-v3.2.txt` - archived owner v3.2 normative source and lineage-gap note.
- [[concepts/emotional-evolution-personality-system]] - commune/personality-system support for privacy membrane and mirror-card constraints.
- [[wizard/harness-consolidated/19_grammar]], [[wizard/harness-consolidated/20_phrasebook]], [[wizard/harness-consolidated/32_mmm_word_ratchet]], [[wizard/harness-consolidated/33_mmm_language_fingerprint]], and [[wizard/harness-consolidated/34_mmm_research_reservoir_map]] - MMM language and grammar surfaces for semantic-sovereignty kernel work.
- [[_archive/harness_2026-04-17_steward_trim/19_grammar]] and [[_archive/harness_2026-04-17_steward_trim/20_phrasebook]] - archived grammar/phrasebook lineage.

Lev repo refs:

- `docs/design/design-semantic-control.md`
- `docs/specs/spec-semantic-control.md`
- `docs/specs/proposal-scan-ingestion-and-dictionary-transport.md`
- `docs/glossary/lev-qit-engine-glossary-eisenhart.md`
- `docs/specs/spec-poly-*`

## Horizon Fence

| Horizon | What may be claimed | What is fenced out |
|---|---|---|
| NOW | Wired receipts, landed or live seams, and declared integration routes that already have receipts or commits. | Broad product readiness, generalized mesh launch, and canonical CR promotion. |
| NEXT | Buildable-now flagship sim spec that current gates can host. | Claiming that the sim has run, passed, or justified policy before receipts exist. |
| LATER | Research directions whose machinery is suggestive but not yet a Leviathan contract. | Consensus, governance, terrain, or operator claims as current implementation facts. |

## NOW - Wired Receipts Exist

The kernel already upgrades Lev at the evidence boundary, not by importing theory wholesale.

1. `surprise_bits` now has a named route into the G3 `SurprisePredictor` seam.

   The merge plan names M6 as the route: QIT bridge `surprise_bits` enters Lev's existing G3 `SurprisePredictor` port as evidence, with malformed, stale, or verdict-shaped surprise evidence rejected by adapters. The receipt-backed bridge side exists as `cr_qit_bridge_stream_v0`: the tier map records the Lev bridge as real on `lev-main` at commit `586df5307`, and the integration state records the four-patch outbox landing plus upstream rehoming toward `sim-witness`. The ceiling is route/receipt evidence, not a release claim.

2. The agent loop becomes an EFE action edge.

   The gate doctrine maps the game-engine tick to the surprise stream and the action edge to the expected-free-energy loop. The tier map's L14 row records a closed EFE loop convergence result with an important exclusion: in the direct-goal world, the epistemic term was non-load-bearing under the risk-only ablation. That is useful because it prevents a vague "active inference everywhere" claim. The upgrade is narrow: Lev gets a concrete action-selection edge with a falsifier-shaped ablation story.

3. Engine-as-channel informs gate design.

   The QIT engine-as-processor result says Holevo `chi` through a composed schedule peaked at `0.0924` at stage 1 and went to `0` by stage 13; order changed the trajectory but not the endpoint. Gate doctrine already turns this pattern into implementation discipline: engines are witness lanes, channels carry shaped evidence, and receivers reject self-grading fields such as `all_pass`, `promotion_allowed`, and `formal_admission_allowed`. The kernel upgrade is therefore a gate-design principle: every bridge is a noisy, capacity-bounded channel, so admissibility must measure what survives declared observations rather than trusting sender verdicts.

Receipt anchors in this horizon include JP's upstream sensor rounding fix `41a63116e`, the live `cr_constraint_battery` at `6265dbaeb`, the bridge commit `586df5307`, and the pending convergence comparison against independently-authored `0d7eb4dec` for Julia negative-test shape. These are receipts for seams and fixes, not global proof.

## NEXT - Flagship Buildable Sim

### The Privacy Membrane As Probe-Relative Quotient

Root axiom, in the form the sim should test:

```text
a =_M b iff a ~_M b under the probe family M granted to the observer
```

Identity is not absolute exposure. A node exposes `S / ~_M`: the quotient of its internal state `S` under the probe family it grants each peer. Privacy is therefore provable indistinguishability, not policy prose. If two protected states land in the same quotient class for the granted probe family, the peer cannot distinguish them through that exposure channel.

This formalizes selective exposure in the [Mesh Node Protocol v0](./MESH_NODE_PROTOCOL_V0_2026-07-02.md): inventory stays sovereign, exposure is shaped, peer witness receives only the channel it was granted, and correction must respect the receiving node's own gates.

The two information-theoretic locks are:

- Holevo bound: each exposure channel has a capped extractable information budget. A peer may receive `S / ~_M`, but the channel cannot leak more distinguishable information than `chi` permits for that granted ensemble and measurement family.
- Data-processing inequality: derived reputation can never contain more source information than the exposure it was computed from. Trust degrades through intermediaries by theorem. Reputation-inflation attacks die structurally because a downstream score is a processed channel output, not a fresh authority source.

### Membrane Sim v0

Status: `scratch_diagnostic`, `promotion_allowed=false`.

Carrier:

Node state is a density matrix `rho_node` over a small finite attribute Hilbert space. A first version can use four binary attributes: capability, provenance strength, owner-private flag, and service-history flag. The exact labels are not load-bearing; label-erased controls must preserve the observables.

Probe families:

Each peer class receives a declared measurement set:

| Peer class | Probe family | Intended exposure |
|---|---|---|
| public | `M_public` | coarse proof rung and public capability only |
| peer node | `M_peer` | proof rung, source-address shape, and selected service facts |
| auditor | `M_auditor` | expanded provenance and falsifier shape |
| owner | `M_owner` | full diagnostic probe for control only |

Equivalence:

`x ~_M y` when every measurement in the granted family gives the same observable distribution for `x` and `y`. The exposed object is the quotient `S / ~_M`, not the raw state.

Observables:

- quotient class counts per probe family;
- protected-pair indistinguishability under wrong-probe families;
- Holevo `chi` for each exposure channel;
- monotone degradation of derived reputation through composed channels.

Controls:

- wrong-probe family cannot distinguish protected pairs and must fail to read the protected attribute;
- full-probe owner control recovers every attribute;
- label-erased control preserves quotient counts and channel bounds;
- reputation-composition control must satisfy data-processing monotonicity.

Admission ceiling:

The sim can be eligible for Lev witness-pack treatment only after it emits shaped evidence, source addresses, negative controls, freshness metadata, and a claim ceiling. It still remains scratch until admitted by declared gates. It may not certify human privacy, product policy, or mesh governance.

## LATER - Fenced Research Directions

Consensus-as-einselection is later. The physics bridge has an einselection eigenproblem and fixed-point machinery, so the analogy is concrete enough to keep: pointer states are the claims that survive network interaction. But no current doc may claim consensus implementation from that analogy. A future sim would need to show that network-surviving claims are stable under perturbation, label erasure, adversarial sender behavior, and receiving-node gates.

The terrain/operator layer as twin dynamics is also later. The tier map has terrain and operator layers, IGT-grounded enough to suggest a twin-dynamics path: terrain supplies the state-space deformation, operators supply the admissible transformations. That is not current Lev behavior. It belongs behind a separate scout with declared carriers, controls, and a hard claim ceiling.

## The Recursion

The kernel enters Leviathan through the gates it will eventually justify.

Name it plainly: bootstrapped legitimacy. The constraint-core kernel does not get to bypass admissibility because it explains admissibility. It must first arrive as shaped evidence, witness packs, negative controls, adapter rejections, local reruns, and claim-language ceilings. Only after those gates survive can later versions use the same kernel to explain why those gates were the right kind of membrane.

That is not circular promotion. It is recursive self-hosting under a ratchet: LLMs and humans propose the kernel, code gates its artifacts, failures become permanent gates, and the surviving gate family becomes the object the kernel tries to model.

## Claim Ceiling

This page may be cited as a three-horizon integration map and as the v0 spec for a privacy-membrane sim. It may not be cited as proof that the privacy membrane has run, that consensus-as-einselection is implemented, that terrain/operator dynamics are grounded in Lev, or that any scratch constraint-core result is canonical.

{"file":"projects/leviathan-current/KERNEL_UPGRADES_LEVIATHAN_2026-07-02.md","horizons":3,"flagship_sim_specced":true}
