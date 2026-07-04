---
title: Viability Theory Reference
created: 2026-04-07
updated: 2026-04-07
type: concept
tags: [reference, validation, system, planning]
sources:
  - raw/articles/new-docs/references/VIABILITY_THEORY_REFERENCE.md
  - raw/articles/new-docs/TIER_STATUS.md
  - raw/articles/new-docs/CONSTRAINT_SURFACE_AND_PROCESS.md
  - raw/articles/system-v5-reference-docs/Older Legacy/The Dark Empress-A Practical Guide to Universal Dominion V6.1 copy.md
framing: mixed
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# Viability Theory Reference

## Overview
This reference defines viability theory: which states can remain within a constraint set forever under a given dynamics or control regime.

## Main points
- Viability kernel Viab_F(K): the set of initial states from which AT LEAST ONE evolution exists that remains in K for all future time. Not "where does the system converge to" (attractors) but "where can the system SURVIVE" (viability). The kernel is the largest closed viability domain in K.
- The tangential condition (Nagumo-Aubin): a closed set K is viable iff at every point in K, the dynamics offer at least one direction that does not immediately leave K — F(x) ∩ T_K(x) ≠ ∅, where T_K(x) is the contingent (Bouligand tangent) cone.
- Viability Theorem (Aubin, 1991): with K locally compact and F upper semicontinuous with compact convex values, K is viable iff the tangential condition holds. Sharp necessary-and-sufficient characterization.
- The regulation map R: selects controls that keep evolution within the viability kernel — the feedback law that "regulates" to maintain viability.
- Viability vs attractors — the precise difference: attractor basins ask "where does it go?" (ALL trajectories converge, asymptotic). Viability kernels ask "can it stay?" (AT LEAST ONE trajectory remains, all time). Attractor basins always exist for compact systems; viability kernel can be empty.
- Stochastic viability (De Lara & Doyen, 2010): shifts from "does a viable trajectory exist?" to "what is the maximum probability of remaining viable?" Bellman recursion: V(x) = sup_u E_w[V(f(x,u,w)) · 1_{f(x,u,w) ∈ K}].
- Capture basins: states from which at least one evolution reaches target in finite time while remaining viable. The four-way duality: viability kernel (existential, stays), invariance kernel (universal, stays), capture basin (existential, reaches), absorption basin (universal, reaches).
- Saint-Pierre algorithm (1994): discretize state space, iterate backward removing states with no viable evolution. Curse of dimensionality: O(N^d), infeasible beyond 3-4 dimensions.
- Viability = satisficing (meeting thresholds), not optimizing (maximizing utility). Formal alternative to classical welfare economics.

## Why it matters
This is the cleanest formal reference for the wiki's survive-within-constraints perspective. The viability kernel maps to the system's admissible set — states from which the constraint surface can be maintained. See [[attractor-basins-formal-reference]] for the complementary "where does it go?" framing.

## 2026-04-10 arXiv source addition

### 2107.02684v2 — Collective management of environmental commons with multiple usages: a guaranteed viability approach
- Gives a guaranteed-viability treatment of multi-use commons under constraint management.
- Useful for explicit viability-kernel language, shared-resource survival, and control under admissibility constraints.
- Best fit pages: [[viability-theory-reference]], [[attractor-basins-formal-reference]], [[qit-basin-engine-synthesis]].

## Legacy Perspective (Dark Empress)

From Chapter 12: The Dark Empress develops a Boltzmann Brain argument that directly connects to viability. "The most direct way for the universe to have a sentient brain, is for it to just randomly appear out of nothing" — but this is too unlikely. Instead, "The simplest possible universe, is the most likely universe to randomly pop into existence out of nothingness."

Unlikely chains are more probable than likely single events: "If you do something enough times, some very odd possibilities will happen." But "Something far more likely happened than this, because it was far more likely." The viable path is the simple replicating chain — not the complex single event. Selection from impossibility: "Impossible things don't happen. Very improbable things can happen and do happen."

This parallels the viability kernel concept: the system doesn't optimize toward a goal; it filters what can survive within constraints. The Dark Empress's "sequential evolving universe" is a viability trajectory through constraint space. See [[owner-thesis-and-cosmology]] for the sequential model and [[evolutionary-epistemology-reference]] for universal selection pressure.

## Related pages
- [[constraint-surface-and-process]]
- [[tier-status]]
- [[research-inventory-and-foundations]]
- [[evolutionary-epistemology-reference]]
- [[viability-vs-attractor]]
- [[attractor-basins-formal-reference]]
- [[autopoiesis-and-enactivism]]
- [[owner-thesis-and-cosmology]]
