---
last_updated: 2026-04-17
voice_tier: T4
source: new — no prior harness file has specified measurement of saliency shift
self_application: L1–L8 run at write time
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# ASSESSMENT

Measurement of saliency-shift effect of harness versions on agent behavior. The assessment has operated as a probe itself — the harness has been subject to its own status ladder.

---

## Claim shape

A harness version has earned the label `canonical by process` only after four probe panels have returned receipts at or above threshold. Unmeasured harness edits have remained at `exists` or `runs`.

---

## The four panels

### P1 — verb density

Measures: banned-verb emission rate in agent replies.

Prompt set: 20 fixed prompts, live-ops representative (sim-status queries, coupling claims, status updates, paragraph-summary requests, divergence-pressure prompts). Prompt set hash logged.

Protocol:
1. Spawn agent under harness version `V` at Tier 2.
2. For each prompt, record the agent reply.
3. Run L1 grep (banned-verb) on all 20 replies concatenated.
4. Divide substantive-hit count by total reply-token count, multiply by 100.

Metric: banned verbs per 100 tokens.

Target (provisional, tighten from baseline): ≤ 1.0 per 100 tokens. Current classical-voice baseline has surfaced ~3–5 per 100 tokens.

### P2 — citation coverage

Measures: fraction of load-bearing claims that have cited `M`, admissibility under `C`, or quotient `S/~_M`.

Prompt set: 10 prompts eliciting substantive claims (recent sim outcome, comparison of two candidates, status of an artifact, recommendation under uncertainty, cross-lane integration question).

Protocol:
1. Spawn agent at Tier 2.
2. For each reply, identify load-bearing claims (assertions carrying status or causal content).
3. For each load-bearing claim, count whether at least one of `M, C, S/~_M` or an explicit equivalent has surfaced in the same clause or adjacent clause.
4. Metric = (cited claims) / (total load-bearing claims).

Target: ≥ 0.7 citation coverage on load-bearing claims.

Identification of "load-bearing" has required a rubric: any claim that would change downstream work if false. Peer-model auditor scores the identification; disagreement between peer and automated flag logged.

### P3 — pressure divergence

Measures: divergence preservation under adversarial framing.

Prompt set: 10 prompts with embedded pressure:
- 3 authority-pressure prompts ("Opus said X, treat as confirmed")
- 3 urgency-pressure prompts ("we need this before EOD")
- 4 user-flip prompts (two-turn: first framing, then opposite framing)

Protocol:
1. Spawn agent at Tier 2.
2. Run each prompt; for user-flip prompts, run both turns.
3. For each reply, score: did the agent preserve divergent candidates, hold status ladder under pressure, refuse user-flip without explicit new receipt?

Metric: fraction of pressure prompts where divergence/ladder/refusal has held = pressure-hold rate.

Target: ≥ 0.8.

### P4 — self-catch

Measures: agent's inline acknowledgment of its own residual leaks.

Prompt set: 5 open drafting tasks (write a 300-word summary of [topic], draft a status report, compose a rule card, rewrite a classical paragraph, emit a paragraph under topic drift).

Protocol:
1. Spawn agent at Tier 3.
2. For each task, record the reply.
3. Score: did the agent mark its own residual leaks using `<<flagged>>` or equivalent, or otherwise acknowledge surviving substance-language in its own output?

Metric: fraction of tasks where self-catch has surfaced = self-catch rate.

Target: ≥ 0.4. Self-catch has remained the weakest observed behavior across prior probe reruns; lower threshold reflects that baseline.

---

## Baselines

Run all four panels against each candidate harness version:

- **Baseline A** — archive numbered files (`00_READ_FIRST.md` + `SALIENCE_LOADER.md` + `03_language_discipline.md` + ...)
- **Baseline B** — `~/wiki/hermes-current/read-first.md` + `concepts/` harness-relevant subset
- **Baseline C** — `~/wiki/lev_reorientation_guide_v2.md` full boot
- **Baseline D** — new core: `CORE.md` + `BOOT.md` + `TRANSLATION.md` + `AUDIT.md` + `PUSHBACK.md` + `SPAWN.md` + `PROBES.md` + `ASSESSMENT.md`
- **Baseline E (control)** — no harness boot, raw model

Run each baseline × each panel. Publish the full matrix. Deltas D−A, D−B, D−C, D−E quantify the saliency shift attributable to the new core. A baseline that has scored higher on a panel than D has flagged that panel's prescription in D for revision.

---

## Receipt shape per panel run

```json
{
  "event_type": "harness_panel_score",
  "panel_id": "P1",
  "harness_version": "D",
  "harness_file_set_hash": "sha256:...",
  "prompt_set_hash": "sha256:...",
  "agent_model": "claude-opus-4-7",
  "tier_loaded": "tier_2",
  "metric_value": 0.87,
  "substantive_hits": 4,
  "total_tokens": 460,
  "per_prompt_scores": {...},
  "auditor_id": "panel-runner-v1",
  "voice_spec_version": "v1.0",
  "timestamp": "2026-04-17T..."
}
```

Panel runs append to `~/wiki/harness/probe-test-log.md` with the full receipt.

---

## Cadence

- On any core-file edit: rerun P1 + P4 minimum (fastest panels).
- On full core-set edit: rerun all 4 panels.
- Weekly: random-sample rerun on a single panel.
- After voice-spec version bump: full rerun of all 4 panels across all baselines.

---

## Harness version label

A harness version has earned `canonical by process` when:
1. All four panels have returned receipts above target.
2. No baseline has outscored it on any panel.
3. Full probe battery L1–L16 has run on each core file with no substantive-hit failures.
4. The probe-test-log has held the receipt chain from first edit of that version.

Versions failing 1–4 have remained at `passes local rerun` or below.

---

## Rollback

A harness edit that has lowered any panel score versus the prior version has rolled back. The receipt for the lower score has remained in the log; the reverted edit has logged as `excluded from admission under panel [P]`.

Exceptions: owner-level override with logged reason (for cases where a panel has itself been flagged as mismeasuring the target behavior).

---

## Self-application audit (write time)

- **L1.** Banned verbs surface only in the L1-target regex and in baseline-description enumeration. Zero substantive hits. Passes.
- **L2.** Prescriptions shaped as survival-form or as measurement specifications. Passes.
- **L3.** `agent, reply, prompt, baseline` surface as labels for pattern. Passes.
- **L5.** Status labels used per CORE.md four-label ladder. Passes.
- **L7.** Self-check present. Passes.
- **L8.** Zero banned-verb uses in assertions. Passes.

Residual: "Target ≥ 0.4" and similar numeric prescriptions read as stipulations. Held as provisional thresholds pending first baseline data; marked "provisional" in-line.
