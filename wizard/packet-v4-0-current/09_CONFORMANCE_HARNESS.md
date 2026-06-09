---
title: Wizard v4.1 Conformance Harness
type: conformance_harness
packet: v4.1
framing: standalone
---

# Conformance Harness v4.1

The packet is not accepted just because the docs are clear.

A runtime should be able to test whether Wizard v4.1 actually ran.

## Required Checks

The conformance harness should verify:

- main thread loaded `mmm/FULL_MMM_v4_0.md` before boot/runtime rules;
- selected skill or runtime surface is explicitly v4.0;
- no older packet path or old header shape appears in accepted receipts;
- parent receipts name exact member mini-MMM slices;
- parent member utility distinguishes current-run cut, reboot candidate, suppression, and retirement evidence;
- child receipts count only when terminal status is completed and accepted;
- same-triple sim/QIT child variants do not reuse the same initialization signature;
- non-sim tasks pass with only `bounded_work_compile_gate`;
- sim/probe/queue-visible tasks require the strict adapter gate;
- visible output is answer-first and includes the compiled move before council detail.
- no-prompt runs include source-scan context, inferred target, evidence boundary, and a bounded action;
- visible output has a cognitive-load budget: council results, three to four follow-ups, all-of-the-above, and footer.
- every visible follow-up option includes evidence that it was pre-run, audited, and improved.
- the footer is the final section and begins with a `🧙 Time/value:` signal, so slow runs must justify their reader cost.
- route-truth reconciliation separates waves, parent subagents, child/subsubagents, and tool checks before the header is emitted.
- tool checks never satisfy child/subsubagent counts.
- `waves:3/3` includes `partial-coverage` when sequential barriers completed but selected parent/member coverage did not.
- footer truth cannot contradict header route counts.
- visible verification counts are tied to exact commands and current pass totals.
- pseudo-heading answers using bold labels instead of required Markdown sections fail.
- `children:0/0 not-run` fails when a visible three-council run has a child/subsubagent route obligation.
- option/route labels replacing Decision, Failure, and Follow-Up council identities fail.
- visible Wizard output without a concise full-MMM and mini-MMM proof line fails.
- v4.0 visible headers fail after the v4.1 upgrade.
- displayed header score must equal computed conformance score.
- MMM proof parent counts must match accepted parent receipt counts.
- prior-run council receipts cannot be counted as the current Wizard header.

## Golden Fixture Classes

At minimum, keep fixtures for:

- documentation cleanup;
- bug triage;
- refactor planning;
- research synthesis;
- implementation handoff;
- valid sim packet;
- vague sim packet that must fail;
- fake `FULL` with started child that must fail;
- version drift that must fail;
- worker-log output that must fail.
- promptless ambient source scan that must pass;
- promptless run with no source context that must fail;
- output with too many visible follow-ups that must fail.
- output with un-preworked follow-up options that must fail.
- receipt-divergence collapse that requests a sharper rerun;
- receipt-divergence cap hit that blocks after the rerun cap;
- malformed structural fields that block instead of passing as fake evidence.
- reboot candidate without concrete boot/task/source/model delta that must fail;
- retire candidate without repeated evidence that must fail;
- same-triple child variants with duplicate initialization signatures that must fail.
- tool check claimed as child/subsubagent that must fail;
- partial parent coverage with plain `waves:3/3` that must fail;
- footer denying child receipts while the header counts children that must fail;
- stale verification count without the matching fresh command that must fail.
- pseudo-heading output that must fail even when route truth is otherwise honest;
- hidden child obligation output that must fail when child routes were expected but not launched.
- council identity drift output that must fail when Proof/Premortem/Scout replace the three councils;
- missing visible MMM proof output that must fail.
- stale v4.0 visible header that must fail;
- score mismatch output that must fail;
- MMM proof/header contradiction that must fail;
- prior-run receipt reuse output that must fail.

## Codex Ratchet Harness

The Codex Ratchet adapter may use:

```bash
python3 scripts/wizard_v4_conformance.py --out-dir work/wizard_v4_conformance/latest
```

This is an adapter harness. The universal packet does not require this exact script.

The Codex Ratchet adapter may render supplied v4 receipts through:

```bash
python3 scripts/run_wizard_v4.py --receipts work/wizard_v4_runs/latest/input_receipts.json --out-dir work/wizard_v4_runs/latest
```

This is an adapter runner. It must remain v4-only and must not import or mutate old Wizard runner paths.

## Acceptance Rule

Do not improve more Wizard prose until the conformance harness passes its golden fixtures.
