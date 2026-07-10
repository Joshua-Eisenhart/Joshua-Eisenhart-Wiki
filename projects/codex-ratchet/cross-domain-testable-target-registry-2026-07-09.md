# Cross-domain testable-target registry — constraint-core ToE
**As of UP-136 / harness 141 GREEN / bundle v107 (2026-07-09).**

Purpose: a single honest map of what the model could be tested and simmed against, across every domain, so
success is measured against an *external* yardstick and not self-graded. Every entry carries three fields:

- **Tier** — `NOW` (simmable on the current foundation), `RUNG` (needs one earned rung first), `MATURITY` (needs
  substantial development before a fair test is even possible).
- **Structure status** — is the machinery the target needs *forced* by the constraints {F01 finite, N01 noncommuting,
  T01 nonassociative} + MSS, or merely *installed / live-but-unforced*? A target that needs installed-only structure
  cannot be a clean win — it can only be a consistency check on that branch.
- **Failable test** — the specific measurement whose control must flip. No target is "done" without one.

The non-negotiable discipline (project doctrine, learned the hard way): a gate that cannot fail is a rubber stamp;
external quotes are attribution not verified fact; fixes go in the measurement, never in the gate; and grand prizes
stay deferred behind the foundations — **loop back and audit up from the base on every rung.**

---

## Tier legend and honesty about "solving"

The model's stance (owner doctrine): it does not literally re-derive GR/SM/etc.; it proposes **new foundations from
the least presumptions** that reproduce what the empirical universe shows and, where possible, make a *distinguishing*
prediction. "Solving Yang–Mills / P-vs-NP / Riemann" means, in this frame, **a structural result that the constraint
ratchet forces** — not a fitted coincidence. Most of the famous targets are `MATURITY`: listed honestly, with the
one earned rung that would move each from wish to test.

---

## 1. Physics — grounded in real data (the strongest current lane)

| Target | Tier | Structure | Failable test |
|---|---|---|---|
| **Dark-sector acceleration scale a0 = c·H0/2π** (UP-134) | **DONE** | forced (cosmogenesis + Unruh 2π) | zero-parameter match to observed MOND a0 (0.90×); Planck-scale control off by 1e61; baryonic Tully-Fisher on 4 galaxies. SHIPPED. |
| **a0(z) redshift fork, data-selected** (UP-135) | **DONE** | forced fork | Branch A (a0∝(1+z)^1.5) vs B (constant); Genzel/Milgrom high-z data (attributed) kill A; no-expansion control → disc 1.0. SHIPPED. |
| **Physics loops back → core (2π = engine holonomy)** (UP-136) | **DONE** | forced | a0's thermal 2π = engine's computed Berry holonomy (−2π at pole); half-loop control breaks. b1/b2 fork recorded. SHIPPED. |
| **Full SPARC + high-z joint a0(z) fit** | **NOW** | forced | measure a0(z) slope directly vs the ~175-galaxy SPARC catalog + high-z points; residual scatter vs ΛCDM. *Needs network approval to fetch catalogs.* The single strongest next physics test. |
| **b1 vs b2 growing-room-rate resolution** | **RUNG** | forced identity, open selection | derive whether the rate is frozen-today (b1) or de Sitter (b2) from the engine's own horizon structure, not asserted. Falsifiable in Ω_Λ. |
| **Fine-structure constant α** | **MATURITY** | *unknown — likely needs a forced dimensionless coupling* | α is a numerology graveyard; only defensible if the field-of-engines layer (axes 7–12) *forces* a dimensionless coupling. Gate must reject any fitted value. Do NOT attempt as a fit. |
| **Yang–Mills mass gap** | **MATURITY** | needs forced non-abelian gauge structure + confinement analogue | the model's chiral/entanglement gauge content (weak-force chirality is forced) is suggestive, but a mass gap needs a spectral-gap theorem on a forced non-abelian structure. Rung: earn a non-abelian gauge algebra from the ratchet (currently only U(1) phase + chirality are forced). |
| **GR + SM unification (new foundations)** | **MATURITY** | partial: entropic-gravity + chirality forced, full SM not | reproduce established results on the info↔physics seam (Landauer, einselection, entropic Newton — DONE as reproductions); a genuine unification needs the field layer. |

## 2. Mathematics — foundations & the grand problems

| Target | Tier | Structure | Failable test |
|---|---|---|---|
| **Division-algebra ladder ℝ→ℂ→ℍ→𝕆** | **DONE** | ℂ forced (F01∧N01), ℍ forced, 𝕆 *installed not forced* | engine runs on ℍ (assoc, dim 4); 𝕆 needs a grouping(T01)-load-bearing demand, none present. Octonion table oracle-verified basis-independently (UP-136). |
| **Exceptional chain G2→F4→E6→E7→E8** | **DONE (as inventory)** | g2/f4/e6 derived, e7/e8 cited; all *live-but-unforced* | each is the symmetry of one layer over the octonions; NOT forced at the qubit-engine level. Candidate to become load-bearing at the field layer. |
| **Malcev / T01 ceiling** | **DONE** | names the exact non-Jacobi structure 𝕆 needs | engine commutators are all Lie (Jacobi ~5e-14); earning 𝕆 needs a forced Malcev bracket, absent. The honest ceiling. |
| **P vs NP** | **MATURITY** | oracle-duality (deduction↔induction) is core vocabulary | frame P-vs-NP in the model's oracle-duality; realistically a framing/partial, not a proof. Rung: make "oracle" an operational object (perception side) with a complexity separation. |
| **Riemann hypothesis / prime distribution** | **MATURITY** | none forced yet | would need a forced self-adjoint operator whose spectrum is the zeros (Hilbert–Pólya flavor); the model has natural spectral objects (BKM/modular) but no forced link to ζ. |
| **Navier–Stokes regularity** | **MATURITY** | none forced yet | the dissipative-flow (GKSL) machinery is present but finite-dim; NS needs a continuum PDE limit the model does not yet take. |
| **von Neumann CA / Penrose tiling / aperiodic order** | **DONE** | real & constructible, *not forced* | Penrose 10-fold diffraction 0.998 (forbidden for periodic); E8 240 roots — both installed projections, same unforced status as F4/E6. |

## 3. FEP / IGT — the "different view" lane (pure-QIT, no classical thermo)

| Target | Tier | Structure | Failable test |
|---|---|---|---|
| **QIT-FEP surprise stream** (Umegaki relative entropy per tick) | **DONE** | forced (Umegaki is the forced pawl) | per-tick S(obs‖belief), pure QIT; emitted for Lev's evidence port. |
| **known/unknown reframe of win/lose** | **DONE** | method-level holds, per-stage falsified | Type-1 tests-the-known / Type-2 explores-the-unknown at method level; per-stage surprise tracks operator family not label (honest failure). |
| **Exploit/explore & compression/prediction frames** | **NOW** | same forced substrate | additional FEP lenses onto the same engine trajectory; each needs an erasure control collapsing only that lens. |
| **Active-inference planning (EFE) on the engine** | **RUNG** | needs differentiable tick loop | trainable perception via PyTorch autograd through the tick loop (torch is the learning substrate). |

## 4. The field of engines — axes 7–12 (the model's declared next level)

| Target | Tier | Structure | Failable test |
|---|---|---|---|
| **Two engines in relation (weakest field)** | **NOW** | to be earned | build the minimal forced structure of a *pair* of engines as one object; distinguishability across the pair survives probe rotation. The right immediate next rung. |
| **Field metric / geometry engines embed in** | **RUNG** | open | is the field a flat checkerboard or curved? The exceptional algebras may become load-bearing HERE (owner's conjecture) — the one place 𝕆/F4/E6 could move from installed to forced. |
| **IGT as the natural home of the field** | **RUNG** | open | information-geometric game structure across the node-space; win/lose/known-unknown as field-level observables. |
| **Dimensionless couplings from the field** | **MATURITY** | open | IF the field forces a dimensionless number, α becomes attemptable. Watch for this. |

## 5. Chemistry / biochem / evolution / consciousness bridges

| Target | Tier | Structure | Failable test |
|---|---|---|---|
| **Chemical bond (Hubbard dimer)** | **DONE** | forced from anticommutation | bond IS entanglement; covalent→ionic crossover; singlet S²=0. |
| **Biomolecular switch = qubit (coherent tunneling)** | **DONE** | forced | L↔R tunneling purely noncommutative, no classical shadow; improves on classical Kramers. |
| **Weak-force / biochemical chirality (left-Weyl)** | **DONE** | forced (F01∧N01 → chirality) | no self-mirror generator can be finite+noncommuting → chirality forced; which side is empirical. |
| **Evolutionary selection ↔ engine stages** | **RUNG** | installed (single-source map) | Ne/Se/Ni/Si ↔ selection types; needs a forced link, currently taxonomy overlay. |
| **Consciousness / perception teeth (object formation)** | **RUNG** | partial | objecthood as continuous formation loss; re-identification across novel probes 16/16. Needs the objective criterion sharpened into a standalone benchmark. |

---

## Recommended near-term order (my plan, loop-back discipline)

1. **Field of engines, weakest rung** (§4 row 1) — `NOW`, and it's the model's own declared next level; earning it
   also audits whether the single-engine foundations survive composition. *This is my default next build.*
2. **Full SPARC + high-z a0(z) fit** (§1) — `NOW` but needs network approval to fetch the catalogs; strongest
   external physics test, upgrades UP-135 from a quoted bound to a direct measurement.
3. **More FEP lenses** (§3) — `NOW`, cheap, deepens the "different view" without new forcing.
4. Everything in `MATURITY` (α, Yang–Mills, Riemann, Navier–Stokes, P-vs-NP) stays deferred behind the field layer,
   each with its one named rung above. They are listed so the path is visible, not so they are attempted early.

**The through-line:** every rung loops back to the base. The field layer is the next real climb; the grand prizes
become *fair tests* only once the structure they need is forced, not installed — and the registry names, for each,
exactly which rung would do that.
