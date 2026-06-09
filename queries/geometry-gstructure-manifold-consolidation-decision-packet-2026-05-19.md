---
title: Geometry G-Structure Manifold Consolidation Decision Packet 2026-05-19
created: 2026-05-19
updated: 2026-05-19
type: query
tags: [query, wiki, audit, consolidation, geometry, g-structure]
---

# Geometry / G-Structure / Manifold Consolidation Decision Packet 2026-05-19

Purpose: convert the read-only cluster audit into a concrete consolidation proposal without editing/archiving the concept pages yet.

Status: proposal packet. No merge/archive action has been taken.

Source audit: [[geometry-gstructure-manifold-cluster-readonly-audit-2026-05-19]].

## Recommended cluster architecture

Keep the cluster, but clarify page roles and reduce duplicate jobs.

### A. Main educational / learning pages

These should teach the math directly:

- [[differential-geometry-and-bundles-reference]] — broad differential-geometry primer: bundles, connections, curvature, holonomy, forms.
- [[fiber-bundles-and-spin-geometry-reference]] — bundle/spin/Hopf reference page; likely better main educational page than the shorter non-reference sibling.
- [[hopf-fibration-mathematics]] — focused Hopf map/fiber/torus/connection page.
- [[contact-structure-s3]] — focused contact/Reeb/Hopf odd-dimensional branch page.
- [[quaternion-and-spinor-carrier-foundations]] — quaternion/spinor carrier foundations and genealogy.

Possible merge/deepen action later:

- Merge useful content from [[fiber-bundles-and-spin-geometry]] into [[fiber-bundles-and-spin-geometry-reference]], then either archive the shorter page or convert it into a short reading card that points to the reference page.

### B. G-structure pages

Keep distinct roles:

- [[g-structure-tower]] — educational + status summary for support-manifold tower and branching reductions.
- [[g-structure-variant-sim-ledger]] — result/sim ledger only; should not become the educational explanation.
- [[g-tower-hopf-weyl-integration]] — specific application/synthesis page for G-tower + Hopf + Weyl integration.

Later page-shape correction:

- Move some sim-detail weight out of [[g-structure-tower]] into [[g-structure-variant-sim-ledger]] if the tower page becomes too status-heavy.
- Add clearer “read this first / then ledger” role fences at the top of both pages.

### C. Geometry synthesis / application pages

These should not compete with educational reference pages:

- [[geometry-stack-ratchet-doctrine]] — concise doctrine/application page for noncommutative geometry stack pressure.
- [[support-first-constraint-manifold-dependency-chain]] — support-order / runs-on / dependency-chain synthesis.
- [[g-tower-hopf-weyl-integration]] — specific integration application page.

Potential consolidation:

- [[geometry-stack-ratchet-doctrine]] is short and may be a section of a larger geometry curriculum hub unless it carries unique repo-current doctrine.
- [[support-first-constraint-manifold-dependency-chain]] seems central enough to keep, but should link explicitly to root F01/N01 and the basin contract.

### D. Routers / maps / status ledgers

Keep few and explicit:

- [[geometry-ingredient-map]] — router/map candidate.
- [[current-geometry-spine-status]] — status ledger, not educational primer.
- [[g-structure-variant-sim-ledger]] — variant sim ledger.

Potential consolidation:

- [[geometry-ingredient-map]] and [[current-geometry-spine-status]] have notable overlap. Likely keep both only if one is a stable map and the other is dated status. Otherwise merge the map content into the status page or a future geometry curriculum hub.

### E. Archive / repair candidates

- [[constraint-manifold-architecture]] is currently a 20-word placeholder. It has one meaningful inbound live link from [[qit-engine-doctrine]] plus index/audit links. It should not remain as an empty “detailed constraint geometry” target.

Recommended options:

1. rewrite it into a real educational/application page, or
2. replace inbound links with [[support-first-constraint-manifold-dependency-chain]] / [[f01-n01-root-constraint-basin-pressure]] / [[basin-manifold-claim-contract]], then archive the placeholder.

Do not archive until inbound links are repaired.

## High-overlap decisions

| Pair | Decision hypothesis | Action later |
|---|---|---|
| [[g-structure-tower]] + [[g-structure-variant-sim-ledger]] | not duplicates; educational/status summary vs result ledger | add role fences; move excess ledger detail into ledger if needed |
| [[g-structure-tower]] + [[g-tower-hopf-weyl-integration]] | not duplicates; general tower vs specific integration application | crosslink with reading order |
| [[geometry-ingredient-map]] + [[current-geometry-spine-status]] | possible router/status overlap | decide map-vs-status roles; maybe consolidate |
| [[fiber-bundles-and-spin-geometry]] + [[fiber-bundles-and-spin-geometry-reference]] | likely duplicate/short-vs-reference | merge short page into reference or convert short page to reading card |
| [[fiber-bundles-and-spin-geometry-reference]] + [[hopf-fibration-mathematics]] | not duplicates; broad reference vs focused Hopf page | keep separate; crosslink |
| [[differential-geometry-and-bundles-reference]] + [[fiber-bundles-and-spin-geometry-reference]] | possible broad reference overlap | keep if one is general differential geometry and one is spin/Hopf-focused |
| [[g-tower-hopf-weyl-integration]] + [[contact-structure-s3]] | not duplicates; integration page vs contact-branch concept | keep separate; crosslink odd-dimensional branch |

## Proposed first edit tranche after approval

Smallest safe consolidation tranche:

1. Add role fences to:
   - [[g-structure-tower]]
   - [[g-structure-variant-sim-ledger]]
   - [[current-geometry-spine-status]]
   - [[geometry-ingredient-map]]
2. Repair [[constraint-manifold-architecture]] placeholder path:
   - either rewrite it, or retarget inbound link from [[qit-engine-doctrine]] and archive it.
3. Merge/redirect the short [[fiber-bundles-and-spin-geometry]] page into [[fiber-bundles-and-spin-geometry-reference]] if direct read confirms no unique content.

## Do not do yet

- Do not archive pages before inbound-link repair.
- Do not merge result/sim ledgers into educational concept pages.
- Do not create a new geometry hub until page roles are cleaned up; otherwise the hub becomes another redundant router.
- Do not promote formal-scout G-structure variant results beyond their artifact labels.
