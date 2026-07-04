---
title: Wizard Followup Format V2 7
created: 2026-04-28
updated: 2026-04-28
type: concept
tags: [wizard, mmm, packet, receipt]
framing: current
source_path: current/WIZARD_FOLLOWUP_FORMAT_v2_7.md
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# Wizard Follow-up Format v2.7

## Core

Follow-up is a ready next-action menu.

Follow-up options are next-action offers; only the Results section can claim execution.
Follow-up options are not proof that the route already ran.
A follow-up option is a selectable next route unless Results says it already ran.

The full candidate bank includes:
- Voices
- Lanes
- Checks / Guards
- System routes
- Compositions

The final visible Follow-up should normally be the audited useful subset, not the raw full bank.

## Follow-up prework

If follow-ups are claimed as preworked, these subagent waves must have receipts:

1. 🪄 Follow-up Make Wave — build the full candidate bank for this turn.
2. 🏃 Follow-up Run/Scout Wave — run or scout every candidate that is visible or selected for the full run.
3. 🔎 Follow-up Audit/Improve Wave — audit, suppress weak options, improve wording, and list the useful options.

If these waves did not run, the menu is future-choice only.

## Default follow-up shape

```text
🪄 Follow-up

1. 🎯 Direct — {next bounded action}; delivers {artifact/result}; blocker: {blocker or none}.
2. 🔀 Alternative — {real second route}; compare against current route by {tradeoff axis}.
3. 🪞 Reframe — {changed premise/target/unit}; use if current frame is causing {failure}.
4. 🃏 Wildcard — {bounded off-axis probe}; payoff: {possible unlock}; stop if {risk}.
5. 🔗 All-A — {integrated build route}; delivers {receipt/artifact}; stops if {condition}.
```

## Full candidate bank shape

Use this internally in the Follow-up Make Wave. Show it only when the user asks for the full bank or the task is follow-up-system tuning.

```text
🪄 Follow-up candidate bank

Voices
1. 🦉 Hume — rerun warm evidence bridge.
2. 🦋 Zhuangzi — rerun live-reading anti-collapse.
3. 🔬 Feynman — rerun operation/observable/pass-fail.
4. ✂️ Orwell — rerun anti-fog wording.
5. 🧨 Popper — rerun falsifier pressure.
6. 🥊 Pushback — rerun earned-boundary check.
7. 🏭 Factory — rerun throughput lens.
8. ♟️ Strategy — rerun campaign lens.
9. 🔁 Systems — rerun loop/incentive lens.

Lanes
10. 🎯 Direct — return shortest bounded action.
11. 🔀 Alternative — produce real second route.
12. 🪞 Reframe — change premise, target, or unit.
13. 🃏 Wildcard — run bounded off-axis probe.
14. ⬅️ Back — return to previous decision surface.

Checks / Guards
15. 🔎 Audit — run receipt-truth check.
16. 🧼 Hygiene — run readability/structure check.
17. 🛡️ Security — run control-law/risk check.

System routes
18. 🧠 LLM Council — run independent council routes.

Compositions
19. 🔗 All-A — Deterministic repair: make the smallest patch, name the falsifier, turn it into a test, check downstream effects, keep a second route open, and audit receipts before moving forward.
20. 🧬 All-B — Behavior proof: compare the live readings and run the observable MMM/no-MMM difference before deciding whether the salience body helped.
21. 🧹 All-C — Closeout and shipping: land the artifact, make it readable, check boot/runtime boundaries, make the handoff repeatable, and audit the final receipt.
22. 🧙 All-D — Full Wizard: run preflight, voices, lanes, checks, system routes, compositions, follow-up make/run/audit, and final receipt audit when partial coverage would hide drift.
```

## Final audited menu shape

After the Follow-up Audit/Improve Wave, render useful choices like this:

```text
🪄 Follow-up

1. {emoji} {label} — {audited action}; delivers {specific payoff}; blocked/deferred if {condition}.
2. {emoji} {label} — {audited action}; delivers {specific payoff}; blocked/deferred if {condition}.
3. {emoji} {label} — {audited action}; delivers {specific payoff}; blocked/deferred if {condition}.
```

## Follow-up wave truth report

If follow-ups actually ran:

```text
🌊 Follow-up wave truth
- 🪄 Make: spawned {n}, blocked {n}, deferred {n}
- 🏃 Run/Scout: spawned {n}, blocked {n}, deferred {n}
- 🔎 Audit/Improve: spawned {n}, blocked {n}, deferred {n}
- Final menu: {n} useful options, {n} suppressed, {n} blocked/deferred
- Changed after audit: {what improved or was removed}
```

If follow-ups did not run:

```text
🌊 Follow-up wave truth
- Follow-up options are future routes only.
- No follow-up run/scout wave was executed in this turn.
```

## Category rule

Audit, Hygiene, Security, and LLM Council are not voices or lanes.

They may appear in:
- their own output sections when they ran
- the follow-up candidate bank as Checks / Guards or System routes
- compositions that include them

These stay outside lanes and voices.
