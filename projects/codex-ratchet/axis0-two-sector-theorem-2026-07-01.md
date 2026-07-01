---
title: The Axis-0 Two-Sector Theorem — Why the Parity Is Unreachable by Entropy
created: 2026-07-01
updated: 2026-07-01
type: project-result
status: synced-not-canon
claim_ceiling: scratch_diagnostic; promotion_allowed=false. Gauge proof and sector theorem are solid numerics; the bridge's phase-charge readout (chi_2) is OPEN. Closed-loop holonomy proven insufficient.
framing: codex-ratchet
sources:
  - concepts/axis-0-1-2-qit-packet.md (Axis-0 needs bipartite rho_AB; discrete N/S projection)
  - concepts/igt-pattern-explicit-math-reference.md (axis operator table)
provenance: Claude Science session 2026-07-01. Synced for review, NOT canon.
---

# The Axis-0 Two-Sector Theorem

> **SYNC STATUS: not canon.** scratch_diagnostic. Deepens `Axis-0 = Axis-1 XOR Axis-2` (spec S7m).

## What this turn dug up

Asking whether a genuine bipartite rho_AB object can CONSTRUCT the parity Axis-1 XOR Axis-2 — and,
in failing to force it, proving exactly why the whole Axis-0 investigation stalled.

## 1. Axis-2 (frame) is a gauge choice

The direct/conjugated frame is rho -> V^dag rho V. Over 200 random 2-qubit states, EVERY state
invariant (entropy, purity, coherent information, mutual information) is preserved to **2e-15**
(machine precision). Half of Axis-0's content is provably NOT in the state.

## 2. Two-sector theorem

Decompose a density matrix into eigenVALUES (entropy sector) and eigenVECTORS (phase sector). Under
frame conjugation the eigenvalues move by 1.8e-16 while the state moves by 0.67 — the frame lives
ENTIRELY in the eigenvector sector.

- **Axis-1 = ENTROPY charge** (eigenvalue sector; read by S, I_c, MI, purity).
- **Axis-2 = PHASE/GAUGE charge** (eigenvector sector; invisible to every entropy functional).
- **Axis-0 = their parity** -> needs ONE entropy readout AND ONE phase readout, multiplied.

No single scalar functional spans both sectors. This is the precise, sector-level reason all 14
tested single-cut readouts (every one entropy-type) could never see Axis-0.

## 3. Why the frame needs a second system

Frame-sensitivity is 0.22 for dissipative terrains {Se,Ni} and EXACTLY 0 for unitary {Ne,Si} (their
dynamics commute with H0). Reading a basis needs a reference to read it against — precisely why the
repo insists Axis-0 needs a bipartite cut-state rho_AB: register B supplies the reference for
register A's basis.

## 4. Bridge status — one sector solved, one open

The Xi bridge is a TWO-OUTPUT, TWO-SECTOR map: chi_1 = entropy charge (eigenvalue sector, purity
sign — WORKS); chi_2 = phase charge (eigenvector sector — OPEN); Axis-0 = chi_1 * chi_2. A
closed-loop geometric phase does NOT serve as chi_2: a closed loop is gauge-invariant (H0 and
V^dag H0 V have identical spectra), so it is blind to the frame. (A prototype scoring 4/4 by
assigning chi_2 from the known frame bit was CIRCULAR and is discarded — a caution: any readout that
reproduces the label without measuring it is not a bridge.) The open piece is a RELATIONAL,
OPEN-PATH phase observable: A entangled with a reference B the gauge does not rotate, evolved on a
non-closed segment, read as the A-B relative phase.

## Model recommendation

Axis-0's bridge is not a functional to be discovered but a TWO-SECTOR INSTRUMENT to be built: an
entropy meter (have it) and a relational phase meter (open). Both closed-loop holonomy and all
entropy functionals are provably insufficient for the second.

## Artifacts

`axis0_sector_theorem.png`, `xi_bridge_sector_findings.json`, `axis0_sector_sim.py`.
Spec S7n: `constraint-core-formal-spec-2026-07-01.md`.
