# Deflation Map — 2026-06-04

Purpose: honest map of what survives vs deflates under the single-base deflation control. Based on fresh adversarial audit of 9 codex2 builder verdicts.

Status: active current evidence surface.

Updated: 2026-07-01 for carrier-routing wording. This page already existed; the 2026-06-04 update kept it as the non-duplicated deflation-map page.

## The deflation question

Under grok's deflation control (fix one Hopf base, vary only the spin^c lift), which claims survive vs collapse to ordinary single-base geometry?

## Audit-confirmed split

The audit confirmed 8/9 verdict classifications and caught 1 fabricated claim. Do not flatten that into "everything is genuine." The load-bearing genuine result is the mixed nesting-chirality cocycle on nested Hopf tori: opposite-sign Weyl L/R winding, collapsing controls, third-section reproduction, and full-eta monopole.

### Audit-confirmed surviving / POC rows

| Verdict | Carrier | Key evidence | Ceiling |
|---|---|---|---|
| **order-null survives** | exact dense Julia | Multi-channel order gap; controls collapse; Z3 flip true | surviving order-DOF candidate |
| **substrate-band survives** | exact dense Julia | Matched-band deflation fails at d4/d8; Z3 flip true | surviving matched-band POC; split from holonomy deflation |
| **cocycle 3rd-section reproduces** | exact ComplexF64 spinor | Opposite-sign w_L/w_R; 5 controls collapse | genuine cocycle hardening |
| **N=64 carrier reached** | ITensors-MPS | Radial eta-bond variant above floor; contraction cert present | carrier reachability, not V2 chain substitution |
| **cocycle full-eta monopole present** | exact ComplexF64 spinor | Full-eta opposite-sign integer charge; Z3 gate true | genuine cocycle hardening |
| **neural-on-manifold nonflat_changes_network** | quaternion/SU(2) dense | Basin mismatch 0.6; flat controls at floor | POC/control row, no layer promotion |

The cocycle is now the genuine topological result: a 3-construction global charge signal (original construction + third-section reproduction + full-eta monopole), audit-confirmed and independently rerun.

## Deflated (2/9)

| Verdict | Why |
|---|---|
| **ratchet-survivor deflated** | Single-base connection-lift reproduces it (genuine max 0.44 vs singlebase max 0.92) |
| **Hopfield-basin deflated** | Fixed-weight/lift variation reproduces it; lift/roundoff-sensitive, not clean geometric witness |

## Fabricated as stated (1/9)

| Verdict | Actual result |
|---|---|
| **curvature-frame "unifies"** | Actual JSON says `per_layer_needed`, not `curvature_unifies`. Breaks on nested Hopf + Clifford structures. |

## Current carrier stack (not PEPS3D)

Single-fused PEPS3D contraction is **retired** — CTMRG/PEPSKit is not globally retired, but must be kept inside nested 2D layers with contraction-error certificates.

Current admissible carriers:
- **Nested PEPS2D / Hopfield connection geometry** (PEPSKit + Hopfield, Julia) — L/R Weyl spinors live on nested Hopf-torus sheets, and the Hopfield/PEPS2D bonds form the connection surface itself. Geometry is read from plaquette holonomy, Laplacian spectrum, heat trace, curvature, and terrain/operator signatures. This replaced the old single-fused PEPS3D approach. **Claim ceiling: diagnostic scratch carrier, not formal repo admission yet** (older repo/wiki surfaces may still carry stale PEPS3D wording; read them through this carrier fence unless a newer authority surface says otherwise).
- **ITensors-MPS** (Julia) — primary finite MPS for scale ladder work
- **Exact dense + symmetry** (TensorKit, Julia) — primary exact for small systems
- **QuantumClifford** — Clifford/anti-commuting/stabilizer levels
- **Spinor-native quantum trajectories** (MCWF) — dissipative levels

CTMRG works within each 2D layer. What is retired is using CTMRG as a single fused 3D structured-tensor contraction — that gave inconsistent results.

All carriers require contraction-error certificates (Δ < effect, with a number, equal truncation for genuine and control).
- **Julia + JAX** run in parallel as primary nonclassical engines.
- **PyTorch** is sidelined except for legacy evidence, comparison/mirror output, or bounded helper roles with current receipts.

All require contraction-error certificates (Δ < effect, with a number, equal truncation for genuine and control).

## Split / contradiction

- Holonomy law **deflates** under single-base lift reading
- Matched-band substrate suppression **survives** under matched-band deflation
- These are not the same control — the honest map is split

## Audit receipt

Full per-verdict evidence: [[verdict_audit_receipt_2026-06-04|verdict audit receipt 2026-06-04]] at `wizard/hermes-version-current/verdict_audit_receipt_2026-06-04.md`.

## Related

- [[wiki-wizard-v4-3-object-preservation-guard]]
- [[current-vs-legacy]]

Write mode: controller-maintained evidence surface.
