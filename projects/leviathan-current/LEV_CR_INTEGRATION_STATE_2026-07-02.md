---
title: Lev / CR integration state
created: 2026-07-02
type: collaboration-state-record
status: current collaboration snapshot
claim_ceiling: owner-approved session record; records landed upstream facts, live local run facts, and CR-side asks; does not promote CR corpus results to canon
tags: [lev, codex-ratchet, sim-eval, integration, admissibility]
---

# Lev / CR Integration State - 2026-07-02

## Status ladder

Status words are bounded by the receipt rung they actually earned:

```text
exists < runs < passes fresh local rerun < mutation-proven load-bearing < landed upstream < canonical by process
```

This page records collaboration state. It does not claim canonical promotion for any CR result, scout, lego, or theory layer.

## Related

- [Gate Doctrine: Admissibility, Not Quality](./GATE_DOCTRINE_ADMISSIBILITY_NOT_QUALITY.md)
- [Relevant Docs Index](./RELEVANT_DOCS_INDEX_2026-07-02.md)
- [LINEAGE_AND_VERDICTS](../constraint-core/LINEAGE_AND_VERDICTS_2026-07-02.md)
- [RATCHET_STATE_BY_TIER](../constraint-core/RATCHET_STATE_BY_TIER_2026-07-02.md)

## Landed upstream

JP's session LANDED our first 3 eval-pack commits:

- pack tests: 10/10
- core/eval: 168/168
- typecheck: clean
- sensor hardening: verified "mutation-proven load-bearing"

The packs relocated upstream to `plugins/sim-eval/evals`. Boundary rule: core ships the judge, plugins ship witnesses.

JP fixed sensor rounding upstream in `41a63116e`: unrounded-compare before tolerance. That closes the rounded-value/tolerance-0 hole.

JP built `plugins/sim-eval/src/cr-result-adapter.ts`. It consumes `codex_ratchet.engine_leg_result.v1` and structurally bans `all_pass`, `promotion_allowed`, and `formal_admission_allowed` from gate observables.

`cr_constraint_battery` is LIVE upstream in `6265dbaeb`:

- single-lane gating
- empty-battery blocks
- fixtures adapter-generated from our real `probe_quotient` jax leg

Claim ceiling: `cr_constraint_battery` admits single-engine exact-gate evidence. It is battery-eligible evidence, not cross-engine parity promotion.

## Live milestone

MILESTONE: our sim ran LIVE inside Lev's loop on JP's machine.

Receipt facts:

- shared venv: `jax 0.10.2` + `z3` + `cvc5`, Python 3.13
- `probe_quotient` jax leg fresh
- exit 0
- `cvc5` unsat/sat flip confirmed
- adapter -> battery -> PASS with zero hand-touching

Status ceiling: `runs` plus adapter/battery pass on JP's live machine. This proves the seam works end to end for that leg; it does not promote the result above its earned rung.

## Corpus opening

JP is building `FORMAL_SCOUT_RESULT_v1` and `LEGO_RESULT_v1` adapter extensions. Once those land, scouts and legos corpus intake opens through the same admissibility path.

## Asks in flight

CR-side only; zero Lev changes requested.

1. Julia legs must emit `negative_tests` in v1 shape.

   Current controls live in `flip_control` / `smt_flip`. The adapter refuses to guess per-field polarity. Live cross-engine parity blocks until the Julia leg shape is fixed. Conformance work has been dispatched.

2. Single-engine drafts need fresh full-leg reruns.

   `finite_low_rank_gram`, SMT sims, and PCG currently emit sparse legs: `written_at` missing, `negative_tests` null, `draft_unaudited`. Fresh reruns emitting full legs make them battery-eligible.

## Gate feedback

Adapter-generated fixtures caught our hand-built fixtures asserting controls that the real Julia artifact does not carry. Gates catching us is the system working.

The patch-series flow is the working delivery channel. Our local branch has ordered_channel, battery, bridge pack, and seam receipts. The battery pack is now superseded by JP's `6265dbaeb`; drop it from the next series.

## Claim ceiling

This record can be used as a collaboration state pointer and next-action checklist. It may not be cited as canonical CR promotion, formal admission, or proof that sparse or draft legs are acceptable. The governing rule remains:

```text
candidate evidence survives declared gates; it never grades itself
```

## Update 2026-07-02 later

JP landed our 4-patch outbox. Cover was verified, all patches read clean, and the seam receipt was called "exactly the world-model edge we wanted."

UPSTREAM RENAME: `plugins/sim-eval` -> `plugins/sim-witness`. `eval` is reserved for core/eval judging; packs are witnesses. Schema id is `lev.sim_witness.provider_evidence.v1`; address prefix is `sim-witness:fnv1a32:`. `qit-bridge-stream.ts` relocates into the plugin, `sim.qit` joins plugin lane vocabulary, and JP adapted our 4 patches himself. All FUTURE patch series target `sim-witness` paths.

ALL-LIVE cross-engine parity is GREEN on JP's machine. JP installed Julia 1.12.6 plus Z3.jl, independently patched our Julia leg so polarity is read from source, and fresh JAX x fresh Julia parity passed with `max_abs_diff 0`. JP's return patch on branch `lev/julia-leg-negative-tests` is pending convergence diff against our independently-authored `0d7eb4dec`.

BASIN GATE is formalized as the third gate type alongside parity and polarity: `k` independent builders blind to each other, comparator on behavioral equivalence; convergence admits, divergence measures a missing constraint. Three basin events have appeared on the seam so far: self-grading ban, Julia-leg fix, and eval-builder/sim-contract convergence.

Product decision guidance sent: contract in core as dependency-free witness schema plus negative-test rule plus measurement -> graph edge; math as one witness family behind `enable sim-witness`; code witnesses such as tests, mutation, and k-builder convergence work out of the box.
