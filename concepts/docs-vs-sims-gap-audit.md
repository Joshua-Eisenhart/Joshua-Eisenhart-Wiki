---
title: Docs vs Sims Gap Audit
created: 2026-04-09
updated: 2026-04-11
type: concept
tags: [audit, system, simulation, planning, status]
sources:
  - /Users/joshuaeisenhart/wiki/concepts/probe-doc-result-map.md
  - /Users/joshuaeisenhart/wiki/concepts/pytorch-ratchet-build-plan.md
  - /Users/joshuaeisenhart/wiki/concepts/migration-registry.md
  - /Users/joshuaeisenhart/wiki/concepts/tool-manifest-audit.md
framing: current
---

# Documentation vs Simulation Gap Audit

Tracks the alignment between what the wiki documents and what the sim code actually produces. Three categories: documented but not simed, simed but not documented, alias collisions.

## Documented But Not Simed

These concepts appear in wiki pages but have no matching sim file or result JSON:

| Concept | Wiki page | Missing |
|---|---|---|
| Levi-Civita connection | [[geometry-ingredient-map]] | No sim file found |
| Geodesic exponential map | [[geodesic-structure-state-space]] | No sim file found |
| Geodesic deviation (Jacobi) | [[geodesic-structure-state-space]] | No sim file found |
| Gauss-Bonnet on CP¹ | [[geometry-ingredient-map]] | No sim file found |
| TLA+/TLAPS proofs | [[pytorch-ratchet-build-plan]] | Not installed |
| Lean 4 formalization | [[pytorch-ratchet-build-plan]] | Not installed |

## Simed But Not Dedicated Wiki Page

These have result JSONs but no dedicated concept page (content may be partial in other pages):

| Result JSON | Content | Current wiki coverage |
|---|---|---|
| contact_structure_s3_results.json | Contact structure on S³ | [[contact-structure-s3]] (NEW) |
| riemannian_curvature_results.json | Riemann tensor on carrier | [[riemannian-curvature]] (NEW) |
| qfi_killpoint_divergence_results.json | QFI at cascade transitions | [[qfi-killpoint-behavior]] (NEW) |
| pure_lego_symplectic_kahler_weyl.json | Symplectic/Kähler geometry | Partial in [[clifford-algebra-qit]] |
| entropic_curvature_lattice_results.json | Entropic curvature | No dedicated page |
| majorana_spinor_reps_results.json | Majorana representations | No dedicated page |
| lorentzian_geometry_results.json | Lorentzian signature geometry | No dedicated page |

## Stale Claims (docs say one thing, sims show another)

The quantitative rows below are preserved as 2026-04-10 audit findings. In this 2026-04-11 wiki pass they were not rerun against fresh repo outputs; treat them as bounded audit snapshots, not current-run measurements.

Skim fence:
- do not use this table as current-run evidence
- use it only as an audit-memory surface until the relevant rows are rerun or replaced by fresher result-backed pages

| Claim | Source | Status |
|---|---|---|
| Phase 7 "PASS" all 28 | PYTORCH_RATCHET_BUILD_PLAN.md | STALE — 2026-04-10 audit snapshot: C2 = 11/28 non-null, 17/28 null, 0/28 NOT_TESTED |
| tool_manifest 0.7% | tool-manifest-audit.md | FIXED — now 44.8% tool_manifest / 41.0% all three |
| Migration all NOT_STARTED | migration-registry.md | ACCURATE as a 2026-04-10 registry snapshot but misleading if read as "no torch work exists" |
| SHELL_COUPLING_PROGRAM.md exists | Referenced in controller contract | MISSING — file does not exist |

## Related Pages

- [[probe-doc-result-map]] — the bridge mapping this audit tracks
- [[geometry-ingredient-map]] — geometry ingredients documented
- [[pytorch-ratchet-build-plan]] — build plan with stale claims
- [[migration-registry]] — per-family status
- [[llm-controller-contract]] — status label definitions
- [[tool-manifest-audit]] — tool usage compliance
- [[pytorch-distributed-training-reference]] — distributed training gap / scaling shell
