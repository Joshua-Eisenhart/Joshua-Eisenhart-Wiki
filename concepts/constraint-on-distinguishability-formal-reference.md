---
title: Constraint On Distinguishability Formal Reference
created: 2026-04-07
updated: 2026-04-08
type: summary
tags: [reference, research, formal]
sources:
  - raw/articles/new-docs/archive_hermes_overlaps/CONSTRAINT_ON_DISTINGUISHABILITY_FORMAL_REFERENCE.md
framing: legacy
priming: false
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# Constraint On Distinguishability: Formal Reference

## Overview
Collects existing formal concepts that express a limit on what can be told apart under a restricted family of observations, measurements, or processes. Superseded by [[constraint-on-distinguishability-full-math]] for the system's own treatment, but useful for external tradition mapping.

## Key Formal Concepts

### Indistinguishability Relation / Observational Equivalence
x ~ y iff all allowed observables agree on x and y. Quotienting gives equivalence classes of observationally identical items. Generic support for [[nominalism-in-this-system|probe-relative identity]].

### Operational Equivalence
Two preparations, processes, or states are operationally equivalent if no allowed experiment distinguishes them. Physics and information-processing settings.

### Coarse-Graining
A map that collapses fine-grained distinctions into fewer observed classes. Formalizes lost resolution. Explains how constraints reduce distinguishability.

### Pseudometric
Distance-like function d(x,y) with symmetry, triangle inequality, d(x,x)=0, but possibly d(x,y)=0 for x != y. Quantitative but constraint-friendly.

### Trace Distance
For quantum states rho and sigma: D(rho,sigma) = 1/2 ||rho - sigma||_1. Optimal distinguishability advantage in binary state discrimination. Primary quantitative notion in [[quantum-information-measures|quantum information]].

### Helstrom Bound
Optimal minimum-error probability for distinguishing two quantum states. Direct operational discrimination limit.

### Data Processing Inequality
Applying an allowed channel cannot increase distinguishability or information divergence. Strongest general formal statement for a constraint on distinguishability. Monotonicity under CPTP maps.

### Blackwell Order
One experiment is more informative than another if the second can be obtained from the first by garbling. Comparing probe families by how much distinguishability they preserve.

### Superselection Rules
Restrictions on the observable algebra that forbid certain coherent superpositions or transitions between sectors. Physics-specific constraint on what distinctions are physically meaningful.

## Best-Fit Mapping
- Quantum-adjacent system: trace distance + Helstrom bound + DPI = best core trio
- Probe-family based: operational equivalence + indistinguishability relation + coarse-graining = best core trio
- Comparing probe sets: Blackwell order is highly relevant

## Translation Rule
Use existing formal terms directly. Do not invent compound labels when literature already has clean terms.

## Fit for this wiki
Best fit:
- probe-relative identity and admissibility language
- quotienting the carrier by what the allowed observations cannot tell apart
- distinguishing what is structurally different from what is merely different in name

Mismatch:
- this reference is about formal support, not the system's own full math
- operational equivalence is not the same as ontological sameness
- a coarse-grained quotient is a loss of resolution, not a claim that finer distinctions are unreal

## Related pages
- [[constraint-on-distinguishability-full-math]]
- [[cross-domain-equivalence-map]]
- [[formal-methods-and-witness-discipline-reference]]
- [[distinguishability-formal-reference]]
- [[nominalism-in-this-system]]
