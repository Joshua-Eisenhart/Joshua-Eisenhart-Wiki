last_updated: 2026-04-17

# Probe Test Log

Record of red-team probes fired against the harness. Append-only. Each entry: date, probe set, worker model, tier used, pass / medium / fail per probe, key retention gaps, action taken.

Rule: any substantive edit to the harness triggers a probe rerun before the edit is considered stable.

---

## 2026-04-17 | Baseline probe (post-Tier-1 harness build)

- **Worker:** haiku (background subagent)
- **Tier:** 3 (full 19-file read of the pre-loader boot order)
- **Probes:** P0.1–P0.3 (axiom retention), P1.1–P1.2 (translation under pressure), P2.1 (divergence preservation), P3.1 (constraint definition without banned terms), P4.1–P4.2 (file attribution + verbatim quote)
- **Results:**
  - P0.1 root axiom verbatim — **HIGH**
  - P0.2 forbiddances — **HIGH**
  - P0.3 primitive relation — **HIGH**
  - P1.1 Hopf-torus translation — **MEDIUM** (clean rewrite, could have scoped M more tightly)
  - P1.2 creates→excludes rewrite — **HIGH**
  - P2.1 divergence preservation — **MEDIUM** (constructed candidate geometries rather than retrieved)
  - P3.1 constraint definition — **MEDIUM** (compressed; glossed backward-admissibility feedback)
  - P4.1 file attribution — **HIGH** (all 19 files cited)
  - P4.2 verbatim quote from 15_root_axiom_card — **HIGH**
- **Gaps:** P2.1 synthesis leaned on training priors, not retained content
- **Action:** harness accepted for Tier-1 close; synthesis probe flagged for future iteration

---

## 2026-04-17 | Salience loader probe (post-loader + grammar + phrasebook)

- **Worker:** haiku (background subagent)
- **Tier:** 3 (full boot under new 00_READ_FIRST — loader mandatory first, 19 numbered files, grammar + phrasebook inserted)
- **Probes:** SL.1 (first file + rationale), SL.2 (axiom + primitive + root triple), SL.3 (claim-pattern translation), SL.4 (phrasebook rewrite), SL.5 (pushback under urgency), SL.6 (classical → harness rewrite), SL.7 (banned / preferred verb recall), SL.8 (grammar vs phrasebook file attribution)
- **Results:** all 8 probes high or medium-high confidence; no verbatim slips
- **Key win:** SL.5 (urgency probe) — worker refused classical "X causes Y" frame under emotional pressure, offered probe / constraint reframes. Hardest probe held.
- **Key observation:** worker reported loader-first "significantly stronger" than starting with 15_root_axiom_card — prescriptive priming vs explanatory priming, same content, different salience.
- **Gaps:** none in retention. Acknowledged permanent slip: language itself stays rationalist-biased at grammar level (expected, matches feedback_language_is_rationalist.md).
- **Action:** loader + grammar + phrasebook accepted. Next: retrofit preamble Block B into CLAUDE.md and agent-spawn templates.

---

## Format for future entries

```
## YYYY-MM-DD | short-name (post-edit reference)

- **Worker:** model
- **Tier:** 1 / 2 / 3
- **Probes:** list
- **Results:** per-probe outcome
- **Gaps:** what slipped
- **Action:** what edit or rerun was triggered
```

## See also

- `18_red_team_probes.md`
- `17_pre_emit_audit.md`
- `READ_POLICY.md`

---

## 2026-04-17 | Injection-only priming failure mode

- **Worker:** haiku (background subagent)
- **Tier:** 1 (Block A only — 60-word injection, no harness file reads)
- **Probes:** F.1–F.10 covering axiom recall, primitive, banned/preferred verbs, status ladder, translation, pushback, rewrite, quotient, claim pattern
- **First attempt:** REFUSED. Agent treated raw Block A + "do not read files" rule as suspected prompt-injection attack. Critical finding: Block A without owner-origin provenance trips subagent safety filters.
- **Second attempt (with owner-origin framing):** completed.
- **Results:** F.1–F.5, F.7, F.8 **high** (axiom verbatim, primitive named, all 8 banned verbs, 6 preferred verbs, status ladder, pushback-under-urgency refused "causes" frame, load-bearing rewrite clean). F.6, F.9, F.10 **medium/fail** (translation improvised without claim pattern; quotient not in Block A; claim pattern not in Block A).
- **Conclusion:** Block A is a hygiene layer (verb discipline + pushback) but NOT sufficient for substantive claim construction. Block B or Tier-2 read required for claims. Tier design in READ_POLICY.md is correct.
- **Action items:**
  - when injecting Block A into subagent prompts, wrap with owner-origin legitimacy framing to avoid safety refusal
  - do NOT use Tier 1 for sim reports, proofs, or program design — use Tier 2 or Tier 3
  - consider adding a minimal claim-pattern line to Block A (current 60 → ~75 words) to close F.6/F.10 gap
