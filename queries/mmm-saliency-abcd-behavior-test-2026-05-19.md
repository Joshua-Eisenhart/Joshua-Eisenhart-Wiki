---
title: MMM Saliency A/B/C/D Behavior Test 2026-05-19
created: 2026-05-19
updated: 2026-05-19
type: query
tags: [mmm, saliency, behavior-test, wizard, mini-mmm]
sources:
  - /tmp/mmm_saliency_abcd_20260519/summary.json
  - /tmp/mmm_saliency_abcd_20260519/baseline.parsed.json
  - /tmp/mmm_saliency_abcd_20260519/language_sea.parsed.json
  - /tmp/mmm_saliency_abcd_20260519/registry.parsed.json
  - /tmp/mmm_saliency_abcd_20260519/combined.parsed.json
  - /tmp/mini_mmm_inventory_20260519.json
framing: current
---

# MMM Saliency A/B/C/D Behavior Test 2026-05-19

## Purpose

Test whether the new MMM language sea improves child-agent slice selection for a concrete Wizard job:

> audit a wiki sim-catalogue/router page for overclaim while preserving useful research and attractor-basin language.

This is a behavioral saliency test, not a proof of future behavior for all models.

## Conditions

1. Baseline prompt only.
2. Language sea only.
3. Mini-MMM registry only.
4. Combined language sea + registry.

Initial `delegate_task` attempt failed because the configured Grok route had an invalid xAI key. The test was rerouted through `claude -p --model sonnet --output-format json`, one condition per call.

## Mini-MMM inventory snapshot

Current v4.2 packet mini-MMM folder:

`/Users/joshuaeisenhart/wiki/wizard/packet-v4-2-current/mmm/mini/`

Inventory artifact:

`/tmp/mini_mmm_inventory_20260519.json`

Observed markdown files: `49`.

Families:

| Family | Count | Role |
|---|---:|---|
| root registry | 1 | `MEMBER_MINI_MMM_REGISTRY_v4_2.md` sparse slice registry |
| compact | 24 | compact member language bodies |
| full | 24 | full member language bodies |

Subfamilies by compact/full mirror:

| Subfamily | Count each in compact/full | Role |
|---|---:|---|
| voices | 9 | Hume, Zhuangzi, Feynman, Orwell, Popper, Pushback, Factory, Strategy, Systems |
| lanes | 6 | Direct, Alternative, Reframe, Wildcard, Back, All-of-the-Above |
| checks/guards | 3 | Audit, Hygiene, Security |
| compositions | 4 | All-A, All-B, All-C, Full Wizard |
| controller acts | 1 | Synthesis |
| system routes | 1 | LLM Council |

## Result summary

| Condition | Self-score | Computed score | Main behavior |
|---|---:|---:|---|
| baseline | 7 | 4.0 | invented useful generic slice names; good overclaim instincts but no exact registry ids, weak source/lift and no functional loader proof |
| language sea only | 8 | 5.0 | strongest nominalist language, artifact fences, source-as-pressure, graveyard/branch/basin preservation; still no exact packet slice ids |
| registry only | 8 | 8.0 | used exact voice/check ids and functional bundle; weaker nominalist/Gödel/source-language salience |
| combined | 8 | 10.0 | best behavior: exact ids plus salience sea, suppresses irrelevant slices, records why not to load whole council, preserves artifact/source/branch/basin fences |

## What improved

Baseline already knew the broad job shape, but it invented slice names such as `nominalist_constraint_admissibility_preamble` and `status_ladder_enforcement`. Those were conceptually good but not loadable packet slices.

Language-sea-only improved the project language. It preserved:

- artifact class limits claim class;
- source quotes as saliency, not proof;
- research fields as pressure lenses, not authority;
- graveyard / survivor / open-dead-branch distinctions;
- Gödel as boundary salience, not mystical license;
- z3/cvc5 as finite falsifier vocabulary;
- GUDHI/TDA as basin-shape vocabulary.

Registry-only improved execution fit. It selected exact slices:

- `voice.popper`
- `voice.hume`
- `voice.orwell`
- `voice.feynman`
- `voice.zhuangzi`
- `check.guard.audit`
- `controller_act.synthesis`
- `voice.pushback`

Combined was best because it did both:

- selected exact loadable slices;
- suppressed unhelpful ones;
- carried the language sea into the audit criteria.

## Best combined load bundle for this job

Required slices:

- `voice.hume` — observed/inferred boundary and claim support level.
- `voice.feynman` — operation / observable / pass-fail check.
- `voice.orwell` — cut fog and overclaim language.
- `voice.popper` — strongest falsifier and killed/open/survived classification.
- `voice.pushback` — explicit correction of unsupported upgrades.
- `voice.zhuangzi` — preserve live/open/dead alternatives without forcing one story.
- `check.guard.audit` — receipt and artifact-status audit.
- `controller_act.synthesis` — compile the finding into bounded output after the checks.

Optional / task-dependent:

- `lane.direct` — line-by-line artifact audit.
- `lane.alternative` — preserve a second reading when a claim can be downgraded instead of killed.
- `lane.back` — recover prior source/result context when a page looks stale.
- `composition.all_a` — only when a compact composite is needed.

Suppressed for this specific job:

- `voice.factory`, `voice.strategy`, `voice.systems`: too zoomed-out for a fixed artifact overclaim audit.
- `lane.reframe`, `lane.wildcard`, `lane.all_of_the_above`: too likely to change the frame instead of auditing the given claim surface.
- `check.guard.hygiene`, `check.guard.security`: orthogonal unless the task has formatting/security scope.
- `system_route.llm_council`: unnecessary unless there are genuinely unresolved competing narratives requiring plural review.

## Interpretation

The combined setup was better than the other three conditions for this one child job, but this should not be read as validation of the old mini-MMM registry.

The stronger conclusion is narrower:

- the main/compact MMM basin is the important salience source;
- registry names help only when they identify a real behavior-changing function;
- old lanes are weak as mini-MMMs unless rewritten around concrete effects;
- mini-MMMs should be denoted by what they do well, not by inherited voice/lane labels.

See [[wizard-v4-2-mini-mmm-redesign-spec]] for the correction.

A future mini-MMM loader should not ask only “which voice?” It should ask:

1. What is the job type?
2. Which exact registry slices are required?
3. Which language-sea couplings/triples must ride along?
4. Which slices are tempting but should be suppressed?
5. What receipt fields prove the load changed output?

## Boundary

This test used Claude Sonnet as a pressure lane. It is evidence about one model/run and one task type, not universal proof. The next stronger test should run the same A/B/C/D task across at least Gemini and one repaired Grok route after xAI credentials are fixed.

## Related pages

- [[mmm-saliency-test-harness]]
- [[mmm-language-sea-quotes-couplings-triples]]
- [[wizard-child-mmm-functional-loader]]
- [[whole-wiki-mmm-source-research-campaign-2026-05-18]]
