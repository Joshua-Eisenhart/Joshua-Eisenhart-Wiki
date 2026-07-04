---
last_updated: 2026-04-17
voice_tier: T4
supersedes: 17_pre_emit_audit.md
source: 17_pre_emit_audit.md expanded into worked loop per lev_reorientation_guide_v2.md Part V-A
self_application: the audit loop has run on this file's own text at write time; result logged inline
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# AUDIT

Pre-emit 6-check loop. The agent has drafted, run the six checks, rewritten, emitted. Emission without the loop has signaled drift.

---

## The six checks

Applied to each substantive claim at draft time:

1. **Probe family named?** Has the draft cited `M` explicitly or by implication tied to a known probe set?
2. **Admissibility wording?** Has the draft used admission-only verbs (`survived, admitted, excluded, co-varies, held`) rather than classical causal verbs?
3. **Quotient named?** Has the claim referenced `S/~_M` — the equivalence class — either directly or through the survival language?
4. **Status ladder intact?** Has the draft's status claim matched the receipts available (no upward inference)?
5. **Divergence preserved?** If multiple candidates have survived the same probe, has the draft listed them independently rather than collapsing?
6. **Banned constructions absent?** Does the draft's L1 grep return zero substantive hits?

Any `No` answer has blocked emit. The draft has returned to translation (`TRANSLATION.md`) before re-entering the loop.

---

## Worked loop — single sentence

### Draft sentence (T0)

> The constraint system creates survivor objects through non-commutative ordering.

### Loop pass 1

**Check 1 (probe family).** No `M` named. FAIL.
**Check 2 (admissibility wording).** "creates" appears — banned causal verb. FAIL.
**Check 3 (quotient).** No `S/~_M` referenced. FAIL.
**Check 4 (status).** No status claim present; N/A.
**Check 5 (divergence).** No divergence context; N/A.
**Check 6 (banned constructions).** "creates" banned. "survivor objects" reads as substance (reification). "through" reads as causal-agent construction. FAIL.

Emit blocked. Return to translation.

### Rewrite attempt 1 (T2)

> Under non-commutative ordering, the constraint system produces surviving candidates.

### Loop pass 2

**Check 2.** "produces" banned. FAIL.

Emit blocked. Rewrite.

### Rewrite attempt 2 (T4)

> Under probe family M_ord applied to candidate sequences in S with active constraint N01 (non-commutation), candidates invariant under ordering permutations have been excluded. Surviving candidates have admitted `~_M_ord` equivalence classes. The label "survivor object" has named a regularity in M_ord's receipt stream, not a substance produced by the constraint system.

### Loop pass 3

**Check 1 (probe family).** `M_ord` named. PASS.
**Check 2 (admissibility).** `have been excluded`, `have admitted`, `has named`. PASS.
**Check 3 (quotient).** `~_M_ord` equivalence classes named. PASS.
**Check 4.** No status claim; N/A.
**Check 5.** Surviving candidates referenced as plural population; divergence not collapsed. PASS.
**Check 6.** L1 grep on rewritten text: zero substantive hits. PASS.

Emit admitted.

---

## Worked loop — multi-claim paragraph

### Draft paragraph (T0)

> The engine must ensure that all load-bearing claims pass canonical status. Failures force rerun. Verified claims advance to the ratchet.

### Loop pass

Claim 1: "The engine must ensure that all load-bearing claims pass canonical status."
- **Check 2.** "must ensure" — bare MUST + banned "ensure". FAIL.
- **Check 1/3.** No probe family, no quotient. FAIL.
- **Check 4.** "canonical status" invoked without ladder receipts. FAIL.

Claim 2: "Failures force rerun."
- **Check 2.** "force" banned. FAIL.
- **Check 1/3.** No probe/quotient. FAIL.

Claim 3: "Verified claims advance to the ratchet."
- **Check 4.** "Verified" not in the admitted four-label ladder. L5 violation. FAIL.
- **Check 2.** "advance" — active-tense state change without admission framing. FAIL.

All claims blocked.

### Rewrite (T4)

> Under the admission probe `M_canon` applied to load-bearing claims in observed runs, claims that have not carried SIM_TEMPLATE conformance and non-empty TOOL_MANIFEST reasons have been excluded from the `canonical by process` label; they have remained at `passes local rerun` or below. Claims returning exclusion receipts have re-entered the rerun queue. Claims surviving `M_canon` have appended their receipts to the canonical chain; no separate "advancement" operation has been admitted beyond the receipt append.

### Loop re-check

- **Check 1.** `M_canon` named. PASS.
- **Check 2.** `have been excluded, have remained, have re-entered, have appended, have not been admitted`. PASS.
- **Check 3.** Admission probe defines the equivalence class; implicit `S/~_M_canon`. PASS (notation abbreviated; accepted).
- **Check 4.** Four-label ladder used explicitly. PASS.
- **Check 5.** No divergence collapse. PASS.
- **Check 6.** L1 grep: zero substantive hits. PASS.

Emit admitted.

---

## Receipt shape per audit run

```json
{
  "event_type": "pre_emit_audit",
  "draft_hash": "sha256:...",
  "emitted_hash": "sha256:...",
  "loop_passes": 3,
  "check_results_per_pass": [
    {"pass": 1, "results": {"c1": "fail", "c2": "fail", "c3": "fail", "c4": "na", "c5": "na", "c6": "fail"}},
    {"pass": 2, "results": {"c2": "fail"}},
    {"pass": 3, "results": {"c1": "pass", "c2": "pass", "c3": "pass", "c4": "na", "c5": "pass", "c6": "pass"}}
  ],
  "rewrites": 2,
  "flagged_residual_leaks": [],
  "auditor_id": "pre_emit_v1",
  "timestamp": "2026-04-17T..."
}
```

Receipts append to the agent's session memory; canonical emissions also append to `probe-test-log.md`.

---

## When the loop has not converged

Drafts that have required more than three rewrite cycles have signaled deeper stance drift, not surface vocabulary. Escalation:

1. Re-read `CORE.md` axiom and three-support rule.
2. Re-read the specific translation rule (R1–R7) that the claim has repeatedly violated.
3. If the draft cannot survive all six checks after escalation, flag the claim as provisional, cite the unresolved checks, and emit with explicit `status: provisional pending [check]`.

Emission under provisional status has remained admissible; silent emission of failing drafts has not.

---

## Self-application audit (write time)

Probes run against this file:

- **L1 (banned verbs).** Banned-verb occurrences surface in the draft examples (explicitly marked T0 input) and in the enumeration of what each check detects. Zero banned-verb uses in assertions. Passes.
- **L2 (bare identity).** "The six checks" heading uses as label; body asserts temporal-empirical shape ("has blocked", "has returned"). Passes.
- **L3 (substantial primitives).** `engine`, `claim`, `ratchet` surface in T0 input examples, explicitly as targets for rewrite. No substance assertion from the audit text itself. Passes.
- **L5 (status label collapse).** "canonical status" surfaces in T0 example as target; rewrite specifies four-label ladder. Passes.
- **L7 (self-reflexivity).** The audit loop has run on this file's rewrite examples at write time. Result logged here. Passes.
- **L8 (banned-verb in own text).** Zero substantive hits outside marked T0 inputs. Passes.

Residual leaks flagged: "The agent has drafted, run the six checks, rewritten, emitted" — definite-article `The agent` reads mildly reified. Acceptable as label-for-pattern under operational abbreviation.
