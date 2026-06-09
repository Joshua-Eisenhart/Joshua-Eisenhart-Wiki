---
title: Wizard v4.1 Conformance Harness
type: conformance_harness
packet: v4.1
framing: standalone
---

# Conformance Harness v4.1

The packet is not accepted just because the docs are clear.

A runtime should be able to test whether Wizard v4.1 actually ran.

The discoverable loop-contract fixture index is
`conformance/fixtures/loop_contract_fixtures_v4_1.json`. New loop, premortem,
audit-independence, and output-format clauses must either map to an entry in
that index or name a concrete external test id.

The packet-local validator is
`conformance/validate_loop_contract_fixtures.py`. It reads the fixture index,
checks fixture ids and clause references, runs in-memory pass/fail cases for
digest recomputation, structural audit divergence, model-family key presence,
loop-kind digest handling, prose/YAML contradiction handling, and fixture
mapping. It also asserts packet-root identity, recomputes skill and quote
digests from files, checks stale mirror and cross-loop ledger fixtures, and
requires family statuses to be accepted terminal values rather than merely
truthy strings. It writes no reports and opens no browser.

## Required Checks

The conformance harness should verify:

- main thread loaded the selected main MMM before the runnable Wizard doc;
- selected skill or runtime surface is explicitly v4.1;
- no older packet path or old header shape appears in accepted receipts;
- parent receipts name exact member mini-MMM slices;
- parent member utility distinguishes current-run cut, reboot candidate, suppression, and retirement evidence;
- child receipts count only when terminal status is completed and accepted;
- substantive Codex-adapter child model matrix coverage is proven by accepted
  child receipts for Codex-native, Opus, Sonnet, Haiku, and Gemini-attempt/
  degraded coverage, not by header labels;
- counted parents in substantive Codex-adapter runs prove 5-10 accepted
  child/subsubagent receipts each, or fail closed unless an explicit
  atomic/low-decomposition override is present;
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
- v4.1 visible headers fail after the v4.1 upgrade.
- displayed header score must equal computed conformance score.
- MMM proof parent counts must match accepted parent receipt counts.
- prior-run council receipts cannot be counted as the current Wizard header.
- next-input handoff packets cannot render output until a pre-output route-truth gate joins current input identity, freshness refs, accepted receipt ids, header counts, runtime labels, handoff path, and final output artifact.
- loop iteration greater than 1 must include `cross_loop` with every prior
  load-bearing open finding under exactly one disposition.
- `cross_loop` dispositions must include rationale, artifact/clause reference,
  and a real delta for `extends`; synonym-only disposition drift fails.
- loop `done` must fail unless done predicate fields are satisfied, including
  independent audit receipt ids and an audit independence vector.
- audit independence must fail when the only difference is timestamped prompt
  seed or model label; at least one structural axis must differ.
- premortem loaded status must fail when `skill_body_read_ref` is empty or
  when the skill body reader worker differs from the synthesis worker without
  `degraded_local`.
- premortem loaded status must fail when the skill body source is unversioned,
  stale, or not tied to the active v4.1 packet/local mirror.
- a substantive Codex-adapter run with partial child-model family coverage must
  fail `FULL` unless missing families have accepted smaller-retry/degraded
  receipts.
- loop state rendered only as prose must fail for loop iterations after the
  first.
- every new conformance clause must have a discoverable fixture or named test
  id before it can raise the score.
- `extends` and `resolved` cross-loop dispositions must fail unless the cited
  artifact or clause digest is fresh and the delta/rationale is material.
- audit independence must be validated from structured fields, not prose
  divergence claims.
- stale, placeholder, malformed, or non-recomputed premortem skill digests
  must fail.
- prose/YAML loop-state contradictions must fail before visible output.
- absent required `model_family_statuses` keys must fail `FULL` in substantive
  Codex-adapter runs.
- read-only loops must not be forced to fabricate digest changes, and edit
  loops must not resolve findings with stale digests.
- skill-body quote anchors must be recomputed from packet-local file lines.
- fixture mapping must be bidirectional: every new clause has a fixture/test id
  and every fixture id maps back to a live clause.
- done predicate validation must count only load-bearing findings, not raw
  premortem hypotheses.

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
- promptless hook wake that idles with "no further action is authorized" while source context exists, which must fail;
- output with too many visible follow-ups that must fail.
- output with un-preworked follow-up options that must fail.
- `pre_run_passed_unadmitted` self-promoting to `queue_ready` or admitted evidence without `admitted_by`, which must fail;
- stale `next_input_ready` packet without a freshness gate, which must fail;
- runner success cited without controller-read result artifact, which must fail;
- receipt-divergence collapse that requests a sharper rerun;
- receipt-divergence cap hit that blocks after the rerun cap;
- malformed structural fields that block instead of passing as fake evidence.
- deliberator contract missing `query_class`, `per_thinker_verdict`,
  `all_wrong_rederive`, `minority_report`, or `format_alignment_check`;
- serialized trajectory cache entry that prunes away source receipt id,
  evidence anchor, executable delta, dissent/anomaly, pruning reason, or
  evidence boundary;
- all-agree plural synthesis without distinct evidence anchors or a divergence
  audit;
- strange but testable minority trajectory dropped without bounded
  falsification, preservation, or artifact-backed kill.
- reboot candidate without concrete boot/task/source/model delta that must fail;
- retire candidate without repeated evidence that must fail;
- same-triple child variants with duplicate initialization signatures that must fail.
- tool check claimed as child/subsubagent that must fail;
- partial parent coverage with plain `waves:3/3` that must fail;
- footer denying child receipts while the header counts children that must fail;
- stale verification count without the matching fresh command that must fail.
- substantive sim/proof/queue-visible run with missing Codex-native/Opus/Sonnet/Haiku/Gemini
  child model matrix coverage that must fail;
- pseudo-heading output that must fail even when route truth is otherwise honest;
- hidden child obligation output that must fail when child routes were expected but not launched.
- child routes marked blocked merely because there was no exact implementation
  task or "nothing useful" for an external model to do. That must fail: child
  lanes can still run variants, scouts, falsifiers, mini-MMM checks, receipt
  audits, or follow-up improvers.
- council identity drift output that must fail when Proof/Premortem/Scout replace the three councils;
- missing visible MMM proof output that must fail.
- stale v4.1 visible header that must fail;
- score mismatch output that must fail;
- MMM proof/header contradiction that must fail;
- prior-run receipt reuse output that must fail.
- next-input handoff with a valid freshness gate and joined pre-output route-truth gate that must pass;
- next-input handoff missing the joined pre-output route-truth gate that must fail;
- pre-output route-truth gate whose header counts disagree with accepted receipts that must fail.
- loop output after loop 1 missing full prior-open-finding coverage in
  `cross_loop`, which must fail;
- loop output saying `done` without two independent audit receipts and an
  independence vector, which must fail;
- premortem receipt with `skill_method_invoked:true` but missing
  `skill_body_read_ref` or mismatched worker provenance, which must fail;
- partial child-model surface labeled `FULL`, which must fail;
- loop state flattened into prose with no `wizard_loop_state` block or artifact
  reference, which must fail.
- cross-loop disposition drift where every prior id is present but `extends`,
  `resolved`, and `unchanged` lack rationale/artifact deltas, which must fail;
- audit receipts with only timestamp/model-label differences, which must fail;
- premortem receipt reading a stale or unversioned skill path, which must fail;
- new harness fixture file not referenced by a discoverable test id, which must
  fail.
- `FX-NF-11b-prose-divergence-only`: audit receipts claim divergence in prose
  but lack a verified structural axis; this must fail.
- `FX-NF-11b-structural-divergence`: audit receipts include a verified
  structural axis and non-timestamp/non-label differences; this should pass.
- `FX-NF-12b-boilerplate-rationale`: cross-loop dispositions cite all ids but
  reuse boilerplate rationales or stale digests; this must fail.
- `FX-NF-12b-fresh-delta`: `extends` cites a fresh digest and material delta;
  this should pass.
- `FX-OF-03b-missing-status-key`: required family key is absent from
  `model_family_statuses`; this must fail `FULL`.
- `FX-OF-10b-prose-yaml-contradiction`: prose says done/full while YAML says
  continue/partial; this must fail.
- `FX-NF-14a-bogus-digest`: premortem skill digest is malformed or placeholder;
  this must fail.
- `FX-NF-14a-stale-mirror`: mirror digest differs from active packet-local
  source without an adapter delta; this must fail.
- `FX-meta-clause-fixture-mapping`: every new loop-contract clause maps to a
  fixture id or named test id; this should pass.
- `FX-NF-15a-index-without-validator`: fixture ids exist but no validator
  consumes them; this must fail.
- `FX-NF-15b-recomputed-skill-digest`: validator recomputes the premortem
  skill digest from the packet-local path; this should pass.
- `FX-NF-15c-author-asserted-structural-axis`: receipt asserts
  structural-axis verification while primitive fields match; this must fail.
- `FX-NF-15d-read-only-loop-unchanged-digest`: read-only loop keeps a finding
  unchanged against the same digest; this should pass.
- `FX-NF-15e-receipt-derived-substantive-classifier`: accepted route receipts
  activate family accounting regardless of renderer label; this should pass.
- `FX-NF-15f-completion-synonym-prose`: prose uses a completion synonym that
  contradicts YAML; this must fail.
- `FX-NF-15g-skill-body-quote-anchor`: quote anchor hash matches the cited
  packet-local skill line range; this should pass.
- `FX-NF-15h-dispositions-ref-summary`: large ledgers may be cited by
  `dispositions_ref` with summary while validator inspects the full ledger;
  this should pass.
- `FX-NF-15i-hypothesis-not-load-bearing`: raw premortem hypotheses do not
  reset done predicate unless promoted to load-bearing; this should pass.

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
