last_updated: 2026-04-18

# Pre-Emit Audit (Manifold-Level Probe Grammar)

This file is not a prose checklist. It is the probe grammar `M_pre_emit` applied to a candidate sentence before it is emitted. Completing the probe admits only nominalist output; failing any axis demotes the sentence to provisional wording or to silence.

The archived extended prose mechanism lives at `wiki/_archive/harness_2026-04-17_steward_trim/17_pre_emit_audit.md`.

---

## The Six Axes

A candidate sentence `s` is admitted iff it survives all six probes. Each axis is a one-line question whose admissible answer is a citation, not a reassurance.

(added 2026-06-03) Current use extends the original six-axis probe with axes 7 and 8. The original six-axis name is retained as provenance; emission now requires survival under all eight axes.

| # | Axis | Probe question | Admissible answer | Excluded answer |
|---|---|---|---|---|
| 1 | Probe family | Under which `M` is this sentence's identity / equality / equivalence claim made? | named `M` + file path | "implicit," "obvious," or absent |
| 2 | Admissibility | Under which active `C` does the object in this sentence survive? | cited constraint set + survivor status | bare "exists" or "is" |
| 3 | Quotient | If the sentence says "the same X" or collapses a set, what is `S/~_M`? | named equivalence class | single-winner collapse |
| 4 | Status label | Which of `exists < runs < passes local rerun < canonical by process` was earned for this claim? | one label + evidence path | collapsed / inflated label |
| 5 | Divergence | Which surviving alternatives remain admissible? | named set or "exclusion evidence still incomplete" | silent collapse |
| 6 | Banned construction | Does `s` use any verb from the banned set in `03_language_discipline.md`, or any phrase like "the correct X", "the true X", forward-only chain, "passes" without criteria? | zero matches | any match |
| 7 | Primitive geometry/time/probability | Does this sentence treat geometry, time, or probability as primitive rather than derived from constraints? | geometry/time/probability is cited as downstream of constraints, or marked as conditional/support-level | bare "the geometry is...", "over time...", "the probability of..." without constraint/probe citation |
| 8 | Support/carrier/coexistence | Does this sentence claim operators, bridges, axes, or manifold structure before citing what it runs on? | support/carrier/coexistence is named before any later-operator claim, or the sentence explicitly says support is not yet established | operator/bridge/axis/manifold claim without naming what carries it |

---

## The Grammar

A sentence before emission is represented as:

```
s = {
  claim: <the bare claim>,
  M: <probe family citation>,
  C: <constraint set citation>,
  quotient: <S/~_M or "not applicable">,
  status: <one of four labels>,
  survivors: <named set>,
  banned_matches: <count>,
  primitive_gtp_basis: <constraint/probe citation, support-level mark, or "not applicable">,
  support_carrier: <carrier/support/coexistence citation, "support not yet established", or "not applicable">
}
```

`s` is admitted iff:

- `M` is not null when `claim` uses identity / equality / equivalence language
- `C` is not null when `claim` asserts existence or behavior
- `quotient` is named when `claim` collapses a set
- `status` is one of four labels, with no implied higher label
- `survivors` is a named set (empty set is admissible if exclusion is complete; silent collapse is not)
- `banned_matches == 0`
- (added 2026-06-03) `primitive_gtp_basis` is not null when `claim` uses geometry, time, probability, measure, evolution, or reachability language
- (added 2026-06-03) `support_carrier` is named before any operator / bridge / axis / manifold claim, or the claim is explicitly blocked because support is not yet established

If any field fails, the emission is not "polished." It is demoted — to provisional wording, to a weaker status label, or to silence. Smoothing the sentence to pass the audit without changing the structural claim is itself a banned construction (narrative substitution for probe obedience).

---

## Completing the Probe Admits Nominalist Output

A sentence that survives the six axes completes into:

(added 2026-06-03) For current use, the sentence must also survive axes 7 and 8; the added completion forms below make those axes explicit.

```
Under probe family <M>, the surviving candidate set is <S/~_M>,
admitted by <C>, at status label <exists|runs|passes local rerun|canonical by process>,
with evidence at <path>.
```

(added 2026-06-03) A geometry, time, or probability clause completes into:

```
Under constraint set <C> and probe family <M>, <geometry|time|probability>
is downstream of <constraint/probe/support citation>, with primitive status blocked.
```

(added 2026-06-03) An operator, bridge, axis, or manifold clause completes into:

```
Given carrier <carrier> and support relation <support citation>,
<operator|bridge|axis|manifold claim> remains at status <label>;
without that support citation, the later claim is blocked.
```

The training-manifold low-energy completion is:

```
<X> causes / produces / generates <Y>, which is the correct answer.
```

The shaped-manifold low-energy completion is the first form. Completing into the second form means the sentence did not survive axis 6 (banned construction) or axis 3 (quotient).

(added 2026-06-03) Completing into primitive geometry/time/probability language fails axis 7. Completing into operator / bridge / axis / manifold language before carrier/support/coexistence fails axis 8.

---

## Failure Modes to Intercept

- **Pass-by-smoothing**: the sentence is reworded to avoid banned verbs while keeping the same structural claim (collapsing the survivor set, inflating the label). This passes axis 6 by letter, fails axes 3, 4, 5 by structure. Intercept: check the structural axes before the lexical axis.
- **Citation without grounding**: `M` is named but does not in fact license the claim (e.g., citing a probe family that does not cover the current sentence's predicate). Intercept: when in doubt, demote to provisional and escalate.
- **Divergence preservation by hedge**: "may be" and "could be" are not a substitute for naming the surviving candidate set. Intercept: require a named set or explicit "exclusion evidence still incomplete."
- **Status ladder inflation by adjacency**: writing "passes" near "canonical" so the reader infers "canonical." Intercept: one label per claim, no adjacency inference.
- **Primitive geometry/time/probability by smooth prose** (added 2026-06-03): the sentence uses "the geometry is," "over time," "the probability of," or equivalent phrasing as if geometry, temporal flow, or probability were primitive. Intercept: cite the constraint/probe/support surface that derives it, or mark it conditional/support-level.
- **Support-last operator claim** (added 2026-06-03): the sentence claims an operator, bridge, axis, or manifold structure and only later gestures at what carries it. Intercept: name carrier/support/coexistence first, or block the later claim.

---

## Verification Prompts (Run Silently Before Emission)

- what probe family `M` licenses this claim?
- what exclusion or runner evidence narrows the candidate set?
- what quotient `S/~_M` is the claim over — or is the sentence secretly asserting bare identity?
- what status label was actually earned and what result file evidences it?
- what remains open, and is that openness named in the sentence?
- would a banned verb read more naturally here than what I wrote? If yes, the sentence is fighting gradient, not shaped.
- (added 2026-06-03) is geometry, time, or probability derived from cited constraints/probes, or is the sentence treating it as primitive?
- (added 2026-06-03) before any operator, bridge, axis, or manifold claim, what carrier/support/coexistence evidence is cited?

---

## Cross-references

- `03_language_discipline.md` — banned verb set for axis 6
- `04_status_label_hierarchy.md` — status ladder for axis 4
- `08_anti_patterns.md` — structural anti-patterns for axes 3, 5
- `18_red_team_probes.md` — adversarial probes on content
- `21_mimetic_meme_manifold.md` — this file is the per-sentence probe; `21_*` is the context-level probe
- `25_adversarial_drift_probes.md` — session-level drift probes (upper-scale analog of this file)
- `35_support_first_preflight.md` — support/carrier/coexistence gate for axis 8 (added 2026-06-03)
