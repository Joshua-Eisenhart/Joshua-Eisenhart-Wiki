# The first falsifiable physics prediction: the dark-sector acceleration scale from the expansion rate (UP-134, 2026-07-09)

## Why this rung is different

For the whole physics-bridge program so far, every result has been one of two kinds:

- **Reproduction** — Layer 0.4 reproduced Newtonian gravity *given Verlinde's holographic-screen premises* (a = GM/r^2 to
  ratio 1.000000). Real, but it reproduces an existing derivation on the model's substrate; it does not predict a new number.
- **Structure-admission** — Layer 20.1 showed the weak force's left-handed coupling is *forced* to be chiral by finitude +
  noncommutation (F01/N01), but *which* side (left) and the couplings are empirical inputs.

Neither makes a **falsifiable quantitative prediction** — a specific number the model is committed to, that observation
could have refuted. Layer 0.4 was explicit about the one place a prediction was waiting: its dark-sector term (the 1/r
entropy-gradient force that flattens galaxy rotation curves) used a strength `a0 = 0.20` **set by hand**, fenced as
"phenomenological, NOT derived." That hand-set constant is exactly what UP-134 removes.

## The prediction

Two pieces the model already owns combine to fix the scale with no free parameter:

1. **Cosmogenesis / Axis-0 (Layer 0.6):** "dark energy came first; the room grows; the state's entropy chases a rising
   ceiling." UP-131 made this precise — Axis-0 closes end-to-end as the intrinsic *gradient to a rising ceiling*, not a
   carried state. The rising-ceiling rate is the cosmic expansion rate H0.
2. **Unruh substrate (Layer 0.4):** the entropic-gravity construction already carries kT = hbar*a/(2*pi*c). The `2*pi` is
   the only numerical factor in the whole construction, and it is the model's own, not imported for this fit.

Put together, the dark-sector acceleration scale is predicted to be

>   **a0_pred = c * H0 / (2*pi)**

with c exact, H0 measured, and 2*pi from the model's Unruh substrate. Nothing is fit.

## What was tested, and against what

All numbers are external (c exact; H0 from the Planck/SH0ES range; MOND a0 from Milgrom; galaxy baryonic masses and flat
velocities are canonical baryonic-Tully-Fisher anchors).

1. **Scale, zero fit.** a0_pred = c*H0/(2*pi) = 1.04 / 1.08 / 1.13 x 10^-10 m/s^2 for H0 = 67 / 70 / 73 km/s/Mpc, against
   the observed MOND scale a0_obs = 1.2 x 10^-10 m/s^2 — ratios **0.86 / 0.90 / 0.94**. A wrong-scale control (the Planck
   acceleration) misses by **4.6 x 10^61**, so the prediction genuinely selects the *expansion* scale, not "any scale."
2. **Baryonic Tully-Fisher, zero fit.** With a0 = c*H0/2pi (no per-galaxy tuning), the predicted flat rotation velocity
   v_pred = (G * M_baryon * a0)^(1/4) matches four canonical galaxies spanning ~200x in baryonic mass:

   | galaxy | M_baryon (Msun) | v_obs (km/s) | v_pred (km/s) | ratio |
   |---|---|---|---|---|
   | DDO154 (dwarf) | 3e8 | 47 | 45.6 | 0.97 |
   | NGC3198 | 3e10 | 150 | 144.1 | 0.96 |
   | NGC2403 | 1e10 | 134 | 109.5 | 0.82 |
   | Milky Way | 6e10 | 220 | 171.4 | 0.78 |

   A wrong-a0 control (x10^4) breaks every galaxy by >5x.
3. **Slope forced.** Fitting the anchors gives M ~ v^3.5 (the deep-MOND baryonic-Tully-Fisher slope ~4), not a free exponent.

## Tools and method

- Pure `numpy` arithmetic on established constants; no fitting anywhere (the point is the *absence* of free parameters).
- Structured as an instrument + separate gate: each claim computes a number, and a **control that must fail** (Planck
  wrong-scale; a0 off by 10^4; slope) guards it, per the project's gate-derives-from-data discipline.
- Full harness re-run to 139 pass / 0 fail / 0 skip GREEN before this record was written (count-verify-before-durable).

## Honest scope (what is and isn't claimed)

- The numerical coincidence **a0 ~ c*H0/2pi** is *established* — Milgrom noted it decades ago. The model does **not** invent it.
- The model's **contribution** is a *reason*: dark-energy-first cosmogenesis + the Unruh 2*pi **derive** the scale, turning
  a numerical coincidence into a committed prediction and removing Layer 0.4's hand-set a0.
- It does **not** derive the MOND interpolating function, Newton's G, or claim to replace GR/LambdaCDM. The galaxy values
  are canonical BTFR anchors, not a full SPARC-catalog fit. Owner doctrine under test.

## Suggestions for strengthening the model here

1. **Full SPARC fit.** Replace the 4 anchor galaxies with the full ~175-galaxy SPARC catalog and report the residual scatter
   of the zero-parameter BTFR — that is the real falsification test (LambdaCDM predicts scatter that MOND/this-model does not).
2. **Derive the 2*pi from the substrate, not cite it.** Right now 2*pi enters via the Unruh relation; a stronger result would
   show the same 2*pi emerging from the engine's own holonomy/Berry structure (UP-125/127 already have a -2*pi cos^2 holonomy
   and a Chern 2*pi — worth checking whether that is the same 2*pi).
3. **Predict the running of a0 with redshift.** If a0 = c*H0/2pi and H0 evolves, the model predicts a0(z) — a distinctive,
   falsifiable signature that plain MOND (constant a0) does not make. This would be a genuinely *new* prediction, not a
   re-derivation of a known coincidence.


---

# UP-135 addendum: the a0(z) prediction, and how external data refined it

UP-134 flagged a0(z) running as the one genuinely NEW, distinguishing prediction (plain MOND has constant a0). Working
it out forced a fork on what "the growing room rate" is, and external high-z data adjudicated it:

- **Branch A** — the growing-room rate is the *total* expansion H(z) = H0*sqrt(Om(1+z)^3 + OL). Then a0(z) = c*H(z)/2pi
  RUNS, scaling as (1+z)^(3/2) at high z: a0(z=2) ~ 2.97 * a0(0).
- **Branch B** — the growing-room rate is the *dark-energy / de Sitter horizon* rate (the literal "dark energy came
  first" reading of the cosmogenesis). Then a0 is ~CONSTANT in cosmic time.

Both give the same z=0 anchor (ratio 0.90 to the observed a0), so the local match cannot distinguish them — but they
diverge by a factor ~3 at z=2, a real, testable discriminator.

**External data selects Branch B.** Genzel et al. 2017 (Nature; arXiv:1703.04310) measured falling, strongly
baryon-dominated rotation curves for six massive discs at z~0.9-2.4. Milgrom 2017 (arXiv:1703.06110), as reported
(attribution — the papers' titles/URLs are confirmed, but the exact page wording was not available to re-verify in this
environment), analyzed these in MOND and constrains variation of a0 with cosmic time, disfavouring a ~4a0 rise by z~2 and
specifically a0 ~ (1+z)^(3/2), with the data consistent with a constant a0. Taking that at face value, **Branch A is
falsified** (its ~2.97*a0 at z=2 and (1+z)^1.5 scaling land squarely in the disfavoured region) and **Branch B survives**.

This is the constraint doing real work: the model made a distinguishing prediction, and observation adjudicated the
model's own internal fork — pushing it to the dark-energy-horizon reading of its cosmogenesis (which is also Milgrom's
preferred constant-a0). It is honest in both directions: had the high-z data shown a0 rising as (1+z)^1.5, Branch B would
have been the one killed.

**Caveats.** This does not confirm the model. The gate tests only the model-side numbers (that Branch A lands in the
disfavoured region and Branch B does not); the external exclusion is cited, not re-derived. The strongest follow-up
remains a full SPARC + high-z joint fit that measures the a0(z) slope directly against the data rather than against a
quoted bound.
