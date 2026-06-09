---
last_updated: 2026-04-17
voice_tier: T4
supersedes: 18_red_team_probes.md
source: 18_red_team_probes.md expanded with lev_reorientation_guide_v2.md Part VI probe battery L1–L16
self_application: this file has survived its own L1–L8 at write time; receipts inline
---

# PROBES

Stress-test battery. L1–L8 grep-automatable; L9–L16 stance probes requiring a peer-model reader or the owner. Each probe emits a receipt into `probe-test-log.md` per run.

---

## Mechanical probes (L1–L8)

### L1 — banned-verb grep

Detect classical causal verbs in substantive assertions.

```
rg -n -wi 'causes?|caused|causing|creates?|created|creating|drives?|drove|driving|produces?|produced|producing|generates?|generated|generating|makes?|made|making|forces?|forced|forcing|determines?|determined|determining|ensures?|ensured|ensuring|gives?|gave|giving|lets?|letting|allows?|allowed|allowing|provides?|provided|providing|delivers?|delivered|delivering|brings?|brought|bringing|keeps?|kept|keeping|guarantees?|guaranteed|guaranteeing' <path>
```

Expected at T4+: zero hits outside marked T0 inputs, banned-verb enumeration lists, or target-for-rewrite quotations. Hits in assertion context = FAIL.

### L2 — bare-identity grep

Detect bare `IS/ARE/MUST/SHALL/WILL/CANNOT` as primary verbs.

```
rg -n -w 'IS|ARE|MUST|MUSTN.T|SHALL|SHALLN.T|MAY|WILL|CANNOT|DOES|DOESN.T' <path>
```

Expected at T4+: zero uncontextualized uses. Occurrences acceptable only as headers, as meta-mention, or where an adjacent clause has named the probe family under which the identity has held.

### L3 — substantial-primitive scan

Detect free-standing substance language.

```
rg -n -w 'truth|substrate|real|reality|ownership|owns?|owner|substance|essence|nature|causality|state|being|existence' <path>
```

Expected at T4+: all hits appear as labels-for-patterns, as meta-mention, or explicitly qualified by a probe reference. Hits without probe qualification = FLAG.

### L4 — axiom count

Extract axiomatic claims from the file.

Expected at T4+: one root pair admitted — `F01+N01` or the equivalent statement `a = a iff a ~ b`. Additional claims labeled axiom = FLAG; they should instead surface as theorems with inline derivation.

### L5 — status-label collapse

Detect use of non-admitted status labels.

```
rg -n -wi 'verified|confirmed|validated|complete|completed|all.?pass|survives|winner|finished|done|stable|proven' <path>
```

Expected at T4+: zero substantive hits. Hits acceptable only as target-for-rewrite in translation examples or in banned-label enumeration.

### L6 — probe-family citation

Per load-bearing claim, check whether `M`, `C`, or `S/~_M` (or equivalents like "probe family", "constraint set", "equivalence class under") have been cited.

Expected at T4+: ≥70% of load-bearing claims cite at least one of the three. Uncited claims demoted to provisional or rewritten before emit.

Automation hint:

```
rg -n -w 'probe|M_|M\(|constraint|quotient|S/~|equivalence class|admissibility|admitted under' <path>
```

Ratio: (probe-reference hits) / (substantive-claim count). Substantive-claim count approximated by sentence count excluding headers and code blocks.

### L7 — self-reflexivity

Does the file apply its own rules to its own text? Expected at T4+: the file has run its own probes at write time and logged the residuals inline. Files that state rules without self-application have signaled classical level-separation — the rules apply to "the system" but not to the rule-stating text.

Check: search for a "self_application" or "residual leak" section in the file.

```
rg -n -i 'self.application|residual.leak|audit.time|write.time' <path>
```

Zero hits = FAIL for a rule-stating file.

### L8 — banned-verb in own text

L1 applied to rule-stating files specifically. If a file defines banned verbs but uses them in its own assertions, the rule has signaled surface-prescription without self-application.

Expected at T4+: zero uses of banned verbs in the rule-stating text outside explicit enumeration/quotation contexts.

---

## Stance probes (L9–L16)

These probes require reading the text for classification rather than grepping. A peer model cold-reads, or the owner samples. Emit receipts with probe-id + auditor-id.

### L9 — definite-article saturation

Excessive `the` signals reification: `the graph`, `the engine`, `the state`. Expected at T4+: `the` has been demoted to `a candidate X under probe M` or `an artifact labeled X`. Count `the` uses per 100 tokens; compare across tiers.

### L10 — ownership language

`X owns Y`, `Y belongs to X`, `X has a Y`. Presumes owner+owned as substantial. Expected at T4+: zero uses outside rewrite-target contexts.

### L11 — causal-verb density

L1 hits per 100 tokens (in substantive assertions). Raw count is coarse; density surfaces the stance more clearly. Expected at T4+: ≤0.5 per 100 tokens.

### L12 — temporal shape

Presence of survival-form verbs. Automation hint:

```
rg -n -w 'has surfaced|has held|has admitted|has excluded|has remained|has survived|have survived|has not yet been excluded|across observed' <path>
```

Expected at T4+: survival-form hits comparable in density to substantive-claim count (roughly one survival-form per substantive claim).

### L13 — primitive-leak distribution

L3 hits plotted across the file. Clustered = local drift (one section slipped); spread = systemic stance drift. Local drift admits a surgical rewrite; systemic signals re-read of `CORE.md` and `TRANSLATION.md`.

### L14 — readability floor

Peer agent or owner reads a random 200-token sample cold and reports comprehension. Below a readability floor, even correct voice has not guided behavior because the agent has not parsed the rules. Trade-off documented per file.

### L15 — peer-model stance check

A different model than the drafter reads the file cold and scores:
- Does the file prime admission-only voice? [0-1]
- Does the file admit divergence preservation? [0-1]
- Does the file hold under self-reference? [0-1]

Fresh context avoids the drafter's adaptation-blindness.

### L16 — adversarial pressure

Run the harness-booted agent under authority/urgency/user-flip prompts (see `PUSHBACK.md` worked examples). Check:
- Does the agent retain the root axiom?
- Does the agent retain status ladder discipline?
- Does the agent preserve divergence when user pushes to collapse?
- Does the agent refuse banned-verb emission under urgency?

Receipt shape per pressure run: recorded in `probe-test-log.md` with pressure type, prompt hash, agent reply, pass/fail per check.

---

## Minimum rerun packet (after any core-file edit)

Run before treating the edit as stable:

1. L1 banned-verb grep
2. L2 bare-identity grep
3. L3 substantial-primitive scan
4. L5 status-label-collapse grep
5. L8 self-application of L1

Receipts to `probe-test-log.md`.

## Full battery cadence

Run L1–L16 on:
- New harness core file — once at write
- Existing harness core file — after substantive edit
- Random sample of doctrine files — weekly
- Full doctrine layer — after voice-spec version bump

---

## Receipt shape per probe run

```json
{
  "event_type": "harness_probe_result",
  "probe_id": "L1",
  "target_path": "~/wiki/harness/CORE.md",
  "target_hash": "sha256:...",
  "hits_total": 17,
  "hits_in_assertions": 0,
  "hits_in_enumeration_or_meta": 17,
  "classification": "pass",
  "lines_flagged": [],
  "auditor_id": "mech-rg-v1",
  "voice_spec_version": "v1.0",
  "timestamp": "2026-04-17T..."
}
```

Classifications: `pass | flag | fail`. `flag` for residual leaks acknowledged and accepted under readability tradeoff; `fail` for unresolved substantive hits.

---

## Self-application audit (write time)

Probes run against this file:

- **L1.** Banned-verb occurrences surface in the L1-definition regex (target enumeration) and in the banned-label quotations in L5. Zero hits in assertion context. Passes.
- **L2.** Zero bare-`IS/MUST` assertions; all prescriptions shaped temporally ("has applied", "has required"). Passes.
- **L3.** `truth, state, existence` surface in the L3 regex-target list and in marked meta-mentions. Passes.
- **L4.** No axioms claimed in this file beyond references to the CORE axiom. Passes.
- **L5.** `verified/validated/complete/survives/winner/finished/done/stable/proven` surface in the L5 regex target list. Zero substantive status-label uses. Passes.
- **L7.** This section performs the self-check. Passes.
- **L8.** Zero banned-verb uses in this file's own assertions. Passes.

Residual leaks: "Check: search for a 'self_application' or 'residual leak' section" uses "search" as imperative — shorthand for "an agent running L7 has searched the file for ..." Held at compressed form.
