---
title: QIT Vocabulary Discipline Reference
created: 2026-04-10
updated: 2026-04-10
type: concept
tags: [reference, research, language, qit, harness]
sources:
  - /Users/joshuaeisenhart/wiki/concepts/operationalism-and-measurement-reference.md
  - /Users/joshuaeisenhart/wiki/concepts/cptp-maps-and-channels.md
  - /Users/joshuaeisenhart/wiki/concepts/distance-metrics-state-space.md
  - /Users/joshuaeisenhart/wiki/concepts/information-geometry-reference.md
  - /Users/joshuaeisenhart/wiki/concepts/resource-theories-quantum-reference.md
  - /Users/joshuaeisenhart/wiki/concepts/stochastic-thermodynamics-reference.md
  - /Users/joshuaeisenhart/wiki/concepts/attractor-basins-formal-reference.md
framing: current
---

# QIT Vocabulary Discipline Reference

## Overview
Use established public terms first. Add house language only when the existing term really fails to express the narrower claim. This page is a routing and usage-discipline surface, not a replacement for the owner pages.

## Honesty fence
- this page is a vocabulary/routing aid, not a source of proof
- use it to discipline naming and translation, then hand into the owner math or result page for the actual claim

## Use discipline
- Prefer parent terms from quantum information, open quantum systems, dynamical systems, and thermodynamics before introducing custom labels.
- Use stronger terms only when the live repo evidence earns them.
- Translate into system style by narrowing the term, not by replacing it.
- Route readers to the owner page for the actual math instead of restating it here.
- Block ontology smuggling: do not turn operational classifications, metrics, or witnesses into unearned object claims. See [[ladders-fences-admission-reference]].
- For support-tradition language, borrow public discipline before private branding: Confucian zhèngmíng is useful for keeping names tied to actual role-performance, and Daoist anti-essential language is useful for warning that naming is never the whole structure.

## Dictionary

| Term | Use it for | System-style translation | Avoid using it for | Owner page |
|---|---|---|---|---|
| Operationalism | Meaning through admissible probes, measurements, and tests | what the system can mean is what the allowed probes can actually pick out | A claim that measurement creates arbitrary truth by fiat | [[operationalism-and-measurement-reference]] |
| Distinguishability | What can be told apart under an allowed probe family | what the active probe family can still separate | A total ontology by itself | [[distinguishability-formal-reference]] |
| Operational equivalence | Identity up to indistinguishable measurement statistics | same for the active probes, not necessarily the same in itself | Exact microscopic equality or automatic ontic identity | [[distinguishability-formal-reference]] |
| Quantum channel / CPTP map | Formal update rule for physical finite-state evolution | admissible finite update map on operator-state carriers | Any arbitrary nonlinear ML update | [[cptp-maps-and-channels]] |
| Noncommutativity | Order-sensitive operator structure | update order is load-bearing | Generic complexity or vagueness | [[cptp-maps-and-channels]] |
| Order dependence | Readable statement that update order matters | changing the sequence changes the live result | A substitute for proving noncommutation | [[cptp-maps-and-channels]] |
| Open quantum systems | System-environment coupling, damping, dephasing, Lindblad-style evolution | the carrier is not closed and cannot ignore its bath or surroundings | Closed unitary toy models with no environment | [[cptp-maps-and-channels]] |
| Finite-dimensional Hilbert space | The strict finite carrier for admissible state-space claims | the carrier stays finite; no infinite idealization is primitive | Infinite idealization smuggled back in as primitive | [[formal-constraints-and-geometry]] |
| Recurrence | Repeated return of trajectories or structures under ordered updates | order keeps re-forming after disturbance | Exact convergence to one fixed point unless proven | [[attractor-basins-formal-reference]] |
| Metastability | Persistent but not permanent structured regimes | order can hold for a while without being forever | Eternal or exact equilibrium | [[attractor-basins-formal-reference]] |
| Stability region | Safer parent term for bounded recovery behavior under perturbation | nearby states still come back under the tested update family | Full basin-of-attraction claims without stronger dynamical evidence | [[attractor-basins-formal-reference]] |
| Basin of attraction | A real dynamical-systems term when convergence structure is actually characterized | use only when return geometry has actually been measured well enough | Any pleasing recovery example or one-off toy row | [[attractor-basins-formal-reference]] |
| Invariant set | Preserved state or process structure under dynamics | the update keeps some structure fixed even when individual states move | A blanket synonym for every stable pattern | [[attractor-basins-formal-reference]] |
| Fixed point / limit cycle | Exact stationary or cyclic recurrence structure | exact rest point or exact repeating loop | Loose metaphors for approximate return | [[attractor-basins-formal-reference]] |
| Perturbation | Bounded admissible disturbance used to test robustness | controlled disturbance that tests whether order survives | Arbitrary uncontrolled corruption | [[attractor-basins-formal-reference]] |
| Resource theory | Free states, free operations, monotones, convertibility | what costs, what is free, and what can still be converted | A vague synonym for “valuable thing” | [[resource-theories-quantum-reference]] |
| Quantum thermodynamics | Finite-state work, heat, entropy, baths, Landauer, fluctuation structure | entropy and work bookkeeping on finite operator carriers | Runtime or social metaphors with no operator bookkeeping | [[stochastic-thermodynamics-reference]] |
| Measurement and feedback control | Szilard-like measurement-branch-update-reset structure | probe, branch, act, and pay the reset cost | Magic work extraction or demon language without bookkeeping | [[stochastic-thermodynamics-reference]] |
| Relative entropy | Asymmetry, monotonicity, discrimination rate, resource monotones | directed distinguishability cost, not symmetric distance | A metric in the strict symmetric sense | [[distance-metrics-state-space]] |
| Trace distance | Single-shot state discrimination distance | one-shot separation power under optimal discrimination | A generic “difference score” with no operational meaning | [[distance-metrics-state-space]] |
| Fidelity | State-overlap / preparation-quality closeness notion | overlap-style closeness, not the same thing as distinguishability advantage | Interchangeable with trace distance | [[distance-metrics-state-space]] |
| Information geometry | Contractive metric geometry on state or statistical space | geometry induced by how sharply probes can still tell states apart | A license to ignore operational meaning | [[information-geometry-reference]] |

## Current repo usage guidance
- For the current basin-recovery row, safer parent terms are `operational equivalence class`, `recurrence behavior`, `metastable class`, and `stability region`.
- Reserve `basin of attraction` for stronger dynamical evidence such as sampled basin volume, return-time structure, or invariant-set characterization.
- For AI bridge pages, prefer `predictive world model`, `bounded state update`, `measurement/observability limit`, and `shared-resource coordination trap` before any larger doctrine language.
- For engine pages, prefer `measurement and feedback control`, `resource monotone`, `open-system dynamics`, and `quantum thermodynamics` before custom engine slogans.

## Related pages
- [[operationalism-and-measurement-reference]]
- [[distinguishability-formal-reference]]
- [[cptp-maps-and-channels]]
- [[distance-metrics-state-space]]
- [[information-geometry-reference]]
- [[resource-theories-quantum-reference]]
- [[stochastic-thermodynamics-reference]]
- [[attractor-basins-formal-reference]]
