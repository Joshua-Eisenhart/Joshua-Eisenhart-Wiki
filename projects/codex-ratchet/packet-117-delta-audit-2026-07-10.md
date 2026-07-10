# Packet 117 Delta Audit - 2026-07-10

## Verdict

Packet 117 is a narrow external delta over packet 116, not a new engine run or
new canonical state.

- packet SHA-256: `f3cef779feb214d55ab63187cb9fe922fd1015367b998cd60b1bcbebdcf593c1`
- 116 file count: 491
- 117 file count: 496
- common files: 491
- byte-identical common files: 483
- changed common files: 8, all documentation/registry surfaces
- added files: 5
- removed files: 0

Generated ledgers/docs changed to describe the additions, but the harness count
remains the inherited `144/0/0` and both new sims are explicitly unregistered.

## Five Additions

1. `reference_docs_external_reviews/brave_thread_math_objects_2026-07-10.txt`
   is byte-identical to the already audited 1,882-line Brave attachment.
2. `reference_docs_external_reviews/chatgpt_mannheim_review_2026-07-10.txt`
   is byte-identical to the already audited 1,698-line workbench proposal.
3. `BRAVE_THREAD_MATH_DISPOSITION.md` maps 19 thread query lines to existing
   packet sims and identifies two gaps.
4. `nonassociativity_not_needed_for_halo_profiles_sim.py` is a withdrawn
   scaffold.
5. `three_view_semiconjugacy_gate_sim.py` is a withdrawn scaffold.

## Disposition Audit

The document's `17 of 19 processed` language means packet-local placement or
discussion, not that 17 hypotheses have been experimentally established. Most
map to an existing `live-but-unforced` exceptional-math cluster. Flag-manifold
generation counting lacks a dedicated check. Nonassociative halo dynamics has
no valid model or test.

The stronger wiki claim ladder remains:

```text
source inventoried
< primary literature checked
< concrete model specified
< failable instrument run
< independent result reproduced
< Ratchet admission
```

## Correct Withdrawals

### Halo Scaffold

The code never implements an octonion associator, Malcev bracket, or any other
nonassociative dynamics. Its `A` value is a hand-built smooth function of galaxy
mass, and its four-point leave-one-out behavior is dominated by leverage. It
cannot test whether nonassociativity explains halo profiles. The structural
conclusion is only that current engines do not force a nonassociative gravity
sector. A physical halo claim still requires a real action/dynamics, profile,
full observational benchmark, baryonic nuisance model, and conventional
controls.

### Semiconjugacy Scaffold

Each domain update was defined from the same core matrix `P`, either directly
or by conjugation. Therefore

```text
Q_d T = T_d Q_d
```

holds by construction. Scramble and wrong-matrix controls only verify the
installed intertwiner. They do not show that independently specified QIT,
reaction-network, and agent dynamics share one attractor.

A valid test must freeze each domain's native dynamics independently, fit only
the projection on train interventions, and evaluate off-fixed-point
semiconjugacy, transported prediction, and paired ablation on held-out
interventions.

## Fable Workflow Audit

A high-effort `claude-fable-5` bridge workflow launched three real Agent/Task
workers and completed all three. The stream receipt reports 361 JSONL events,
three task starts, three completions, models `claude-fable-5` and
`claude-sonnet-5`, one rate-limit event, no final error, and cost
`$6.24516585`. Authority remained advisory.

It independently confirmed the 117 delta boundary and the UFPO red ceiling. It
also corrected the UFPO failure diagnosis: unbatched `ndim=2` versus batched
`ndim=3`, not four views versus eight.

Its proposed cheapest four-count falsifier, remove the `0.006` MDL length
penalty while preserving the already-hashed raw geometry/entropy scores, had
already been executed in the live repo. The post-hoc reanalysis finds that
length-four repeated-operator cycles can win, but no primitive all-four-once
length-four cycle qualifies for either engine type. The fixed-per-beat exposure
control also produces repeated length-five/six winners, not four. This does not
promote the post-hoc result; it closes one obvious scoring-bias explanation for
the current red.

## Current Ceiling

Useful new evidence: two bad instruments were built, adversarially rejected,
and retained as failed approaches. No new registered sim, engine stage,
substage, perception capability, exceptional rung, halo theory, or shared basin
was earned.

## Live Advisory Cross-View

The same bounded evidence brief was sent through authenticated live APIs to
`grok-4.5`, NVIDIA `z-ai/glm-5.2`, and NVIDIA
`qwen/qwen3.5-397b-a17b`. All three returned HTTP 200. The prompt SHA-256 was
`3849639fa2257826f76f67499114be83f4a9a4ca85dc1bf5851938bb0b4c9824`.
These are advisory model receipts, not Ratchet votes.

Agreement:

- packet 117 earns no new sim or rung;
- packet 116's local green is real execution but metadata/string-gate weak;
- UFPO v1 produced no learned test result;
- temporal-shuffle parity is a serious validation warning;
- installed 64 rows are only a provisional `16 stages x 4 internal substages`
  grid and do not establish additional intelligence-bearing stages;
- the next experiment must use independently specified dynamics, frozen
  projections/training, held-out interventions, explicit provenance, and hard
  shuffle/circularity kills.

Corrections to the advisors:

- The learner failure does not invalidate the exact 2,367-object registry.
  Exact object semantics and learned perception are separate claims.
- The PyTorch crash is a sealed process/contract failure, not evidence that the
  trained model itself failed on test metrics; no test metrics exist.
- Installing octonionic ground truth would violate foundation-first order. A
  nonassociative carrier belongs only in a dedicated candidate arm with an
  associative control after a grouping-load-bearing demand is declared.
- Requiring exactly four clusters is circular unless four is absent from the
  candidate count, clustering rule, and stopping criterion.

Receipt hashes:

- Grok 4.5 response:
  `fe94d83b27289aabd913811b35f7abd8eda60b472f578215bfc573746a7570e3`
- GLM 5.2 response:
  `c988cde5bad0bc239c6e98554b975ee08692a645a2951d2bbdf8402362cea167`
- Qwen 3.5-397B response:
  `92a0a126c7cf7a710bedd371b15739c8761083faa3c987d6480419261310795e`

## Related

- [[projects/codex-ratchet/packet-116-external-audit-2026-07-10]]
- [[concepts/brave-exceptional-math-thread-research-audit-2026-07-10]]
- [[projects/codex-ratchet/cross-view-math-workbench-wiring-intake-2026-07-10]]
- [[projects/codex-ratchet/unseen-finite-predictive-objects-v1-2026-07-10]]
