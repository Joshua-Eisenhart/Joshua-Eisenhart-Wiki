---
title: Wizard Child MMM Functional Loader
created: 2026-05-18
updated: 2026-05-18
type: concept
tags: [wizard, mmm, child-agents, routing, saliency]
sources:
  - /Users/joshuaeisenhart/wiki/wizard/packet-v4-2-current/mmm/mini/MEMBER_MINI_MMM_REGISTRY_v4_2.md
  - /Users/joshuaeisenhart/wiki/concepts/mmm-saliency-test-harness.md
  - /Users/joshuaeisenhart/wiki/wizard/packet-v4-2-current/mmm/SALIENCY_TRANCHE_01_CANDIDATE.md
framing: current
---

# Wizard Child MMM Functional Loader

## Correction
Child agents should not be assigned MMMs by simple voice category or by the old lane set. The current v4.2 main MMM and compact MMM are the primary salience reservoirs. Mini-MMMs are secondary and must earn their place by changing behavior.

The existing mini-MMM registry is a legacy inventory / candidate pool, not a validated set of good slices. Some old voice cards are useful when rewritten as functions; old lane cards are especially suspect because they can decorate route shape without changing evidence selection or output.

See [[wizard-v4-2-mini-mmm-redesign-spec]].

## Loader rule
Use bounded randomness only after functional fit, and only after the main/compact MMM basin has been considered.

1. Identify the child job type.
2. Start from `FULL_MMM_v4_2.md` or `COMPACT_MMM_v4_2.md` as the broad salience basin.
3. Add only function-specific mini-MMMs that should change the child’s local behavior.
4. Denote each selected mini-MMM by what it does well, not by old lane branding.
5. Suppress old lanes unless the lane has a tested function-specific rewrite.
6. Record loaded slices and the expected behavior delta in the child receipt.

## Candidate functional bundles

These are target functions, not proof that current registry cards are good enough. A slice is promotable only after a behavioral A/B test shows it changes output.

| child job | needed saliency functions | current status |
|---|---|---|
| sim/router overclaim audit | claim ceiling, artifact-tier fence, source/lift separation, concrete falsifier, branch ledger, basin evidence shape | redesign needed |
| source-doc ingestion | source/lift separation, quote-as-saliency boundary, object admission audit, live-reading preservation, plain rewrite | redesign needed |
| research enrichment | pressure-lens not authority, operational test extraction, source tier labels, branch ledger, outside-field boundary | redesign needed |
| MMM compression / language extraction | kernel keep, fog cut, constraint preservation, route truth, no salience erasure | redesign needed |
| route-health / worker proof | spawned/completed/blocked/deferred/not_run classifier, receipt truth, reroute threshold, stale artifact guard | redesign needed |
| follow-up Make/Scout/Audit | preworked choice, payoff/use/stop condition, option falsifier, no decorative menu | redesign needed |

## Source-language overlay
For any bundle that edits or audits Codex Ratchet language, also load the packet-local candidate:

`wizard/packet-v4-2-current/mmm/SALIENCY_TRANCHE_01_CANDIDATE.md`

Use it for:

- kernel terms: finitude, noncommutation, probe-relative identity, admissibility, graveyard, constraint survival;
- drift rewrites: no primitive identity, no completed infinity, no prose-upgrades-result, no best-narrative collapse;
- preservation fences: attractor-basin and graveyard language may be load-bearing, not fog.

## Randomness policy
Random assignment is useful only as exploration around a constrained core. It should not be the default for v4.2 mini-MMM loading.

Allowed randomness:

- choose one optional function-specific slice after the required behavior-changing core is loaded;
- rotate between concrete falsifier / observable check / plain-action compression when the job needs a different pressure angle;
- add queue/sequence/feedback mini-MMMs only when queue movement, dependency order, or second-order effects are genuinely load-bearing.

Not allowed:

- assigning an old lane because it sounds different;
- assigning only `voice.popper` to a sim overclaim audit;
- assigning only `voice.orwell` to source-language cleanup where it may erase load-bearing metaphor;
- assigning a child a random voice when the job actually needs source/receipt/claim-ceiling functions;
- counting route diversity when the loaded slices do not change the child's expected output.

## Child receipt requirement
Each child receipt should include:

```yaml
job_type:
loaded_required_slices:
loaded_optional_slices:
source_language_overlay: yes|no
why_these_slices:
which_loaded_slice_changed_the_output:
missing_slice_if_any:
```

A child that cannot say which loaded slice changed its output did not prove saliency.

## Behavioral test link
See [[mmm-saliency-test-harness]] and [[mmm-saliency-abcd-behavior-test-2026-05-19]]. The first A/B/C/D test showed that registry names help only when paired with source-language salience. It did **not** validate the old mini-MMM set as good. It exposed the next correction: derive a smaller v4.2 mini-MMM set from the main/compact MMM and name each slice by the behavior it changes.

## Related
- [[wizard-v4-2-mini-mmm-redesign-spec]]
- [[mmm-source-language-reservoir]]
- [[cross-field-research-intersection-map]]
- [[sim-run-catalogue-and-result-family-router]]
- [[repo-tool-use-router]]
