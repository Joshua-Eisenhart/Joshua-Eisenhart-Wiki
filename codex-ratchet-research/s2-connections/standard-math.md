# S2 Connections - Standard Math

Scope: standard mathematical facts for the S2 connection/flux/foliation layer.
This is corpus material, not an MMM head.

## Objects

The working model is a principal U(1) bundle over an S2/Hopf-chart carrier,
with connection one-form locally written in the registry convention as
`A = dphi + f(eta)dchi + g_phi dphi + g_chi dchi`. The committed representative
uses `f(eta)=cos(2eta)` with the accumulated `phi` holonomy convention pinned by
the registry.

For a U(1) bundle the curvature is `F=dA` because the structure group is
abelian. Gauge-equivalent local potentials can differ by exact transition terms
without making the same lifted holonomy convention. Classification of the
underlying principal U(1) bundle is by the first Chern class, but classification
of a connection is finer: curvature density, holonomy, and boundary convention
remain live data after `c1` is fixed.

## Equivalence Levels

- Bundle topology: same first Chern class can identify the bundle class while
  leaving many inequivalent connections.
- Curvature equality: same `F` fixes local curvature density but does not by
  itself fix all lifted holonomy conventions on a pinned chart.
- Gauge equivalence: local forms may differ by allowed gauge transition terms;
  the registry still requires the lifted convention tuple before aliasing.
- Holonomy data: leaf holonomy spectra and annular fluxes are finer than `c1`
  and are the intended discriminator rows for near-neighbor families.

## Stokes And Annuli

For abelian connections, the holonomy around a contractible loop is controlled
by the integral of curvature over a spanning surface, with boundary and chart
choices made explicit. Annular flux rows compare adjacent listed leaves rather
than only the total endpoint integral, so endpoint-preserving density changes
remain detectable.

## Source Anchors

- Registry: `/Users/joshuaeisenhart/Codex-Ratchet/system_v6/receipts/round3_discriminator_registry_20260611.md`.
- Hopf fibration and Bloch-sphere treatment: H. K. Urbantke, "The Hopf
  fibration--seven times in physics", Journal of Geometry and Physics 46
  (2003), 125-150, https://www.fuw.edu.pl/~suszek/pdf/Urbantke2003.pdf.
- Principal U(1) bundle classification reference surface:
  https://ncatlab.org/nlab/show/principal%2BU%281%29-bundle.
- Standard background: Kobayashi and Nomizu, Foundations of Differential
  Geometry; Milnor and Stasheff, Characteristic Classes.
