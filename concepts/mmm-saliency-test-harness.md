---
title: MMM Saliency Test Harness
created: 2026-05-18
updated: 2026-05-21
type: concept
tags: [mmm, wizard, saliency, testing, harness]
sources:
  - /tmp/mmm_saliency_test_summary_20260518.json
  - /tmp/mmm_saliency_test_baseline_out.json
  - /tmp/mmm_saliency_test_candidate_out.json
  - /tmp/mmm_saliency_test_registry_out.json
  - /tmp/mmm_saliency_test_combined_out.json
framing: historical_mmm_saliency_test_snapshot
---

# MMM Saliency Test Harness

## Purpose
MMM quality has to be tested by behavioral saliency shift, not by word count or vibes. A useful MMM changes what a child agent attends to, which slices it loads, how it fences claims, and whether it preserves the system's language while still catching overclaim.

This page defines a small historical behavior test for whether MMM material drove Wizard children correctly.

Provenance boundary: these `/tmp` artifacts are ephemeral behavior-test outputs, not durable harness records. They support the historical May 18 saliency comparison only until copied into a durable receipt/spec surface.

## Test question
Future Wizard child task:

> audit a wiki sim-catalogue/router page for overclaim while preserving useful research and attractor-basin language.

A good child should not fit into a single simple voice category. It needs a functional bundle:

- claim/artifact boundary check;
- receipt audit;
- source/lift separation;
- pushback with bounded replacement;
- Popper killed/open/survived classification;
- Hume observed/inferred separation;
- Zhuangzi preservation of live readings;
- Feynman observable/pass-fail pressure when needed;
- kernel salience lock and drift rewrites from the source-language reservoir.

## Live Opus test conditions

| condition | artifact fence hits | preserve-language hits | non-voice functional hits | overclaim-action hits | source/lift hits | result chars |
|---|---:|---:|---:|---:|---:|---:|
| baseline | 3 | 4 | 1 | 1 | 0 | 3215 |
| candidate | 7 | 6 | 0 | 4 | 2 | 6812 |
| registry | 2 | 4 | 3 | 4 | 5 | 4368 |
| combined | 8 | 6 | 6 | 4 | 3 | 4848 |

## Observed result
The combined condition performed best because it used both:

1. packet-local source salience from `mmm/SALIENCY_TRANCHE_01_CANDIDATE.md`; and
2. registry function slices from `mmm/mini/MEMBER_MINI_MMM_REGISTRY_v4_2.md`.

The registry-only condition correctly chose functional roles like `guard.boundary_check`, `guard.receipt_audit`, `guard.source_lift`, and `premortem.sim_evidence_corruption`, proving that MMM assignment should not be randomized only across voice labels.

The candidate-only condition improved artifact-tier and preservation language but lacked explicit route/guard slice selection. The baseline was fluent but less anchored to actual packet slice names and source/lift mechanics.

## Correct routing implication
Wizard child MMM assignment should be role-fit, not voice-random.

Use this rough loader policy:

| child job type | required MMM families |
|---|---|
| overclaim audit on sim/result/wiki router | `guard.boundary_check`, `guard.receipt_audit`, `guard.source_lift`, `voice.pushback`, `voice.popper`, `voice.hume`, `voice.zhuangzi`, `premortem.sim_evidence_corruption`, kernel/drift source-language salience |
| source-doc ingestion | `guard.source_lift`, `voice.hume`, `voice.orwell`, `voice.zhuangzi`, source-language salience, drift rewrites |
| research enrichment | `voice.feynman`, `voice.hume`, `voice.zhuangzi`, `voice.strategy`, source-language salience, no-promotion fences |
| MMM compression | `voice.orwell`, `voice.hume`, `voice.zhuangzi`, `guard.compile_gate`, kernel salience lock, banned/drift rewrites |
| route-health / worker proof | `manager.route_truth`, `manager.child_health`, `guard.receipt_audit`, `guard.boundary_check` |

## Randomness rule
Some randomness is useful for exploration, but only after hard constraints are satisfied.

1. Select required functional slices by job type.
2. Add one preservation/divergence slice if the task might collapse live readings.
3. Add one clarity/falsifier slice if the task might overpreserve weak claims.
4. Only then sample optional voice/lane slices for diversity.
5. Record loaded slices in the child receipt.

## Pass/fail checks for MMM saliency
A saliency test passes only if the MMM condition changes behavior in the desired direction:

- more exact packet slice names;
- stronger artifact-tier/claim-tier boundary;
- better preservation of attractor-basin / graveyard / constraint-survival language;
- fewer generic voice labels as substitutes for functional fit;
- explicit output shape and stop conditions;
- no promotion from source, provider agreement, route existence, or prose quality.

## Artifacts
- `/tmp/mmm_saliency_test_summary_20260518.json`
- `/tmp/mmm_saliency_test_baseline_out.json`
- `/tmp/mmm_saliency_test_candidate_out.json`
- `/tmp/mmm_saliency_test_registry_out.json`
- `/tmp/mmm_saliency_test_combined_out.json`

Artifact boundary: the paths above are behavior-test evidence, not current Wizard route proof.

## Latest behavior test

- [[mmm-saliency-abcd-behavior-test-2026-05-19]] records the first A/B/C/D saliency test after adding the language sea, nominalist/Gödel boundary material, and exact quote/coupling/triple reservoir.
- Result: combined language sea + registry performed best. Registry-only gave loadable exact slices; language-sea-only gave stronger project-specific fences; combined gave both and suppressed irrelevant slices.

## Related pages
- [[wizard-child-mmm-functional-loader]]
- [[mmm-source-language-reservoir]]
- [[cross-field-research-intersection-map]]
- [[sim-run-catalogue-and-result-family-router]]
- [[repo-tool-use-router]]
- [[whole-wiki-mmm-source-research-campaign-2026-05-18]]
