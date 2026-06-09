---
title: Wizard v4.2 Mini-MMM Redesign Spec
created: 2026-05-19
updated: 2026-05-21
type: concept
tags: [wizard, mmm, mini-mmm, saliency, v4-2]
sources:
  - /Users/joshuaeisenhart/wiki/wizard/packet-v4-2-current/mmm/FULL_MMM_v4_2.md
  - /Users/joshuaeisenhart/wiki/wizard/packet-v4-2-current/mmm/COMPACT_MMM_v4_2.md
  - /Users/joshuaeisenhart/wiki/wizard/packet-v4-2-current/mmm/mini/MEMBER_MINI_MMM_REGISTRY_v4_2.md
  - /Users/joshuaeisenhart/wiki/queries/mmm-saliency-abcd-behavior-test-2026-05-19.md
framing: prompt_design_candidate_snapshot
---

# Wizard v4.2 Mini-MMM Redesign Spec

## Correction

As of the packet paths cited in this page, the v4.2 main MMM and compact MMM are the primary salience reservoirs. Verify the current packet before booting a fresh runtime from this page.

The old mini-MMM voice/lane set is not automatically useful just because it exists. Some cards are too generic, some are inherited v4.1 shapes, and the old lanes in particular can decorate the route without creating a real saliency difference.

Mini-MMMs should be promoted only when they make a child attend to different things, choose different evidence, produce a different output shape, or block a different failure mode.

## Priority order

1. `FULL_MMM_v4_2.md` — main high-bandwidth salience field.
2. `COMPACT_MMM_v4_2.md` — compact fallback salience field; likely the most important practical boot surface under small context.
3. Function-specific mini-MMMs — only for child/subchild jobs where a narrow slice changes behavior.
4. Legacy voice/lane mini-MMMs — reference/provenance until behaviorally re-earned.

## Prompt-admission rule

A mini-MMM should be admitted for prompt use only if it passes at least one behavioral test:

- attention shift: the child selects different source lines or evidence anchors;
- claim-fence shift: the child refuses a promotion it would otherwise allow;
- output-shape shift: the child returns a different schema that fits the job;
- preservation shift: the child keeps a live/open/dead split it would otherwise collapse;
- falsifier shift: the child names a concrete kill condition it would otherwise miss;
- compression shift: the child keeps the right kernel while cutting tokens;
- route-health shift: the child reports spawned/blocked/deferred truth rather than route vibes;
- output-language self-saliency shift: the child emits language that improves its own next-token salience and the next worker's salience, not merely a correct hidden analysis.

If a mini-MMM only changes vocabulary or label color, it is not useful. But language is not cosmetic when it changes future attention: the LLM's own output becomes part of the next prompt basin, so emitted terms, sentence patterns, and claim fences should be scored as saliency-shaping artifacts.

## Denote mini-MMMs by what they do well

Name and group new mini-MMMs by behavioral function, not by old generic lanes.

Recommended naming pattern:

`mini.<function>.<strength>`

Examples:

| Proposed id | Does well | Failure it blocks |
|---|---|---|
| `mini.claim_ceiling.artifact_tier` | maps artifact class to maximum claim class | prose/result promotion |
| `mini.source_lift.separation` | separates source quote, worker report, local read, and verified artifact | source text becoming proof |
| `mini.receipt_truth.route_status` | classifies spawned/completed/blocked/deferred/not_run | fake worker/council claims |
| `mini.branch_ledger.open_dead_survivor` | preserves open/dead/surviving alternatives | best-narrative collapse |
| `mini.falsifier.concrete_kill` | forces strongest falsifier and decisive check | vague critique without stop condition |
| `mini.operation.observable_check` | turns explanation into operation/observable/pass-fail | clarity without testability |
| `mini.language_compaction.kernel_keep` | compresses while keeping root constraints and project terms | token saving that erases salience |
| `mini.nominalist.object_admission` | asks what object/construction/witness is being admitted | primitive identity or abstract-object smuggling |
| `mini.formal_boundary.godel_tarski` | distinguishes system/proof/model/object-language/metalang | mystical incompleteness or truth-talk blur |
| `mini.basin.evidence_shape` | preserves attractor-basin language only with operational support | basin metaphor becoming proof |
| `mini.queue.bottleneck_handoff` | names next handoff artifact and rate-limiter | process prose with no queue movement |
| `mini.output_language.self_saliency` | emits terms/sentence patterns that shape the next context toward correct salience | good hidden reasoning followed by salience-erasing prose |
| `mini.followup.preworked_choice` | makes follow-up options copy-pasteable with payoff/stop | decorative menus |

## Old lane assessment

The old lanes are probably not good mini-MMMs as-is:

| Old lane | Problem | Keep only if rewritten as |
|---|---|---|
| Direct | too generic; often just says “answer directly” | exact artifact audit / line-by-line claim pass |
| Alternative | can preserve plurality, but may invent alternatives | live-reading preservation with exclusion conditions |
| Reframe | dangerous for fixed artifact audits; can dodge evidence | framework-change proposal with explicit non-mutation boundary |
| Wildcard | high creativity, low receipt discipline | novel-test generator with kill/safety gate |
| Back | useful only when it recovers source/provenance | provenance recovery / stale-context audit |
| All-of-the-Above | usually a route bloat attractor | compile gate that proves why each included slice changes output |

## Old voice assessment

Some old voice cards are still useful, but only as functional moves:

| Old voice | Useful behavior | Rewrite target |
|---|---|---|
| Hume | evidence boundary and support level | `mini.evidence_boundary.support_class` |
| Zhuangzi | preserve live readings | `mini.branch_ledger.open_dead_survivor` |
| Feynman | operation/observable/pass-fail | `mini.operation.observable_check` |
| Orwell | cut fog | `mini.language_compaction.plain_action` |
| Popper | falsifier | `mini.falsifier.concrete_kill` |
| Pushback | overclaim correction | `mini.claim_ceiling.bounded_correction` |
| Factory | bottleneck/handoff | `mini.queue.bottleneck_handoff` |
| Strategy | sequence/retreat | `mini.sequence.retreat_condition` |
| Systems | feedback/second-order effects | `mini.feedback.second_order_effect` |

## Main and compact MMM roles

The main and compact MMMs should carry the broad basin:

- root constraints: finitude, noncommutation, bounded distinguishability;
- evidence grammar: artifact class, receipt, support level, current vs stale;
- anti-collapse grammar: live/open/dead branches and graveyard evidence;
- nominalist grammar: no primitive identity, no object without construction/witness;
- formal-boundary grammar: proof/model/system/object-language/metalang separation;
- operational grammar: tool, check, observable, pass/fail, countermodel, unsat core;
- route grammar: spawned/completed/blocked/deferred/not_run;
- output grammar: answer-first, concise, proof strip, useful follow-up;
- self-saliency grammar: emitted words should seed the next turn with the right distinctions, fences, and live branches.

Mini-MMMs should not duplicate the whole basin. They should act like narrow lenses that change a child’s local behavior or its emitted salience field.

## Redesign procedure

For each candidate mini-MMM:

1. Name the function it does well.
2. Name the failure mode it blocks.
3. Specify source tokens from FULL/COMPACT MMM that it preserves.
4. Specify the required output-shape delta.
5. Specify the required output-language saliency delta: what words, fences, or sentence patterns should survive into the next prompt basin.
6. Run A/B against baseline and main/compact-only.
7. Admit for prompt use only if the delta is visible in the returned artifact and its emitted language.
8. Mark weak/legacy cards as `reference_only` until rewritten.

## Test matrix

Each new mini-MMM should be tested against at least three job families:

| Job family | Expected saliency delta |
|---|---|
| overclaim audit | stronger claim ceiling and artifact-tier classification |
| source ingestion | better source/lift separation and quote-as-saliency boundary |
| compression | fewer tokens while preserving root constraints, route truth, and future-salient wording |
| output-language shaping | emitted prose carries the right nouns, fences, and branch states into the next turn |
| follow-up generation | concrete next prompts with payoff and stop condition |
| sim/proof planning | finite tool/function probe, not broad scientific leap |

## Decision

Do not treat the current mini-MMM registry as validated. Treat it as a legacy inventory and candidate pool.

The next real work is to derive a small v4.2 mini-MMM set from FULL/COMPACT MMM, named by function and tested behaviorally.
