---
title: Wizard v4.1 Codex Adapter
type: runtime_adapter
packet: v4.1
runtime: codex
framing: standalone
---

# Codex Adapter

This adapter binds the universal Wizard to Codex.

These are Codex-specific runtime rules. They are not universal Wizard requirements.

In Codex Ratchet, call the conformance and receipt layer the Wizard Harness.
The Wizard Harness validates route truth before sim promotion, queue visibility,
cleanup claims, or broad follow-up execution.

## Main Thread

The Codex main thread owns:

- full MMM boot;
- runtime rule boot;
- synthesis;
- file edits;
- verification;
- final user-facing claims.

## Parent Workers

Use Codex native subagents for visible members when the task needs real plurality.

A Codex parent worker receipt needs:

- subagent id;
- assigned member id;
- mini-MMM slice loaded;
- task card;
- source slice or tool surface;
- terminal status;
- usable output.

## Child Workers

Subsubagent credit requires parent-to-child linkage.

A child worker counts only when the parent launched it and the child returned a usable receipt.

Direct external model calls from the main thread may be useful, but they do not count as child workers under a Codex parent.

## External Workers

Claude, Gemini, shell tools, and other runtimes can provide external worker receipts. Keep their pool names separate. Do not rename external workers as Codex-native subagents.

## Runtime-Local Skill Mirrors

The wiki packet is the canonical source for Wizard skills. Codex may mirror
portable council-member skills into `~/.codex/skills/<skill-name>/SKILL.md`,
but each mirror must name its upstream wiki path and adapter differences.

Codex-local mirrors are call surfaces, not new doctrine. If a mirror diverges
from `~/wiki/wizard/packet-v4-1-current/skills/...` without an explicit Codex
adapter reason, the wiki skill wins. When a parent or child invokes a
skill-backed member, its receipt records both paths:

```yaml
canonical_skill_path:
runtime_local_skill_path:
adapter_delta:
```

Codex parents and children use exact compact/full member mini-MMMs or sparse
registry/family fallback for skill-backed members. They do not load the compact
main MMM as a general child salience base. Voice-backed members use the exact
voice mini-MMM unless the task card is a cross-voice composition.

In Codex Ratchet Wizard v4.1 runs, the child matrix is default required when
child runtimes are available and the user has not opted out: at least one
Codex-native child plus Opus, Sonnet, Haiku, and a Gemini attempt/degraded
signal. This is not because every child must perform file edits. It is because
the system needs real divergent model pressure:
same-prompt variants, mini-MMM salience checks, outside-frame critique,
falsifiers, receipt audits, scout lanes, and follow-up prompt improvement.

Do not mark Claude/Gemini children blocked because there is "nothing for them
to do." Give them a bounded advisory or variant task. `blocked` is reserved for
actual runtime/access/safety/timeout failure, and the rerouter should try one
smaller prompt or alternate runtime before final synthesis.

Each Codex parent that launches Claude/Gemini children owns a local child
rerouter. The global `manager.rerouter` handles council-level liveness and
resource pressure; it does not repair a parent's timed-out, duplicate, or
`no_delta` child. A parent should reroute one smaller child task when a
load-bearing child times out, returns only a start, duplicates a sibling
`work_unit_fingerprint`, or lacks a countable `outcome_delta`. Count only
completed children with reciprocal parent linkage, sibling-unique work units,
artifact-facing deltas, and usable receipts.

Codex App thread capacity must be handled by rolling release, not by giving up.
When native child launch reports `agent thread limit reached` or equivalent,
the controller/parent closes or releases completed agents whose receipts have
already been collected, retries the missed child lane in a smaller rolling
batch, and records the release plus retry in the parent-local child rerouter.
Do not count a raw thread-limit message as a terminal child blocker while
completed agents remain open.

## High-Fanout Child Capacity

For Wizard v4 Max Assembly, Codex-native parents launch Claude Bridge and/or
Gemini children for real subsubagent depth. Even constrained runs should
include real external child lanes when available; Max Assembly should include
child lanes in every counted parent.

A counted Codex parent needs a useful child set, not a single child. The normal
quorum is 5-10 completed accepted child/subsubagent receipts. Fewer than five
is a failed parent, not partial success. More than ten is a
stress run and needs a receipt-shape/divergence audit before synthesis.

The minimum substantive-run matrix attempts one native Codex child plus four
external child families: `opus`, `sonnet`, `haiku`, and `gemini`. Codex-native,
Opus, Sonnet, and Haiku are core child families for Codex-adapter FULL claims.
Gemini is the default alternate outside-model pressure. If Gemini contributes,
count the contribution. If Gemini hits quota, capacity, timeout, access, or
runtime failure, record the degraded alternate signal and back off instead of
blindly hammering the service. Missing core families are not hidden by
`children:0/0`, tool checks, Claude-only fanout, Gemini-only fanout, or
Codex-only children.

Multiple children from the same model family may count when they perform
distinct work. Good examples: Sonnet-high broad reasoning plus Sonnet-low
packet shrink; Codex-low strict artifact audit plus Codex-high source-slice
scout; Haiku inventory plus Haiku liveness check. Bad examples: the same prompt
with only a label changed, shape-identical summaries, or children that return
`no_delta`.

Codex parents should use the adapter helper when they need the standard
external four-family child matrix:

```bash
python3 scripts/wizard_child_matrix.py \
  --route <member.route> \
  --out-dir /tmp/wizard_v41_<route>_<timestamp> \
  --opus-prompt "<bounded Opus child task>" \
  --sonnet-prompt "<bounded Sonnet child task>" \
  --haiku-prompt "<bounded Haiku child task>" \
  --gemini-prompt "<bounded Gemini child task>" \
  --followup-prompt "<copy-pasteable next prompt>" \
  --payoff "<why this option is useful>" \
  --use-when "<when to choose it>" \
  --stop-if "<when to stop or block>" \
  --boundary "<truth/scope boundary>"
```

An accepted helper parent receipt must include:

- all core child families completed;
- an existing child receipt path for each core family;
- useful route signal in each counted child, not merely `ok`, `done`, or a
  shape-only receipt;
- Gemini completed with useful outside-model pressure, or Gemini attempted and
  classified as a degraded alternate runtime/capacity signal;
- Gemini run in direct-answer/no-tool mode unless a task explicitly authorizes
  tool access;
- non-empty `followup_prompt`, `payoff`, `use_when`, `stop_if`, and `boundary`
  fields.

If any core family is missing, timed out, lacks an existing receipt path,
returns a weak/non-substantive signal, or if the follow-up fields are blank,
the helper parent is failed and cannot count toward FULL coverage. Gemini
degradation is visible in the receipt and footer, but it should not consume the
run with repeated retries when the signal is quota/capacity or runtime health.
The helper does not replace native Codex child work. A FULL Codex-adapter
parent still needs a parent-launched Codex-native child receipt when native
child capacity exists.

Codex Ratchet needs wide bounded search because its advancement gates are
strict. Do not throttle exploration merely because many candidates will fail.
Use broad parent/child fanout to generate falsifiers, demotion conditions,
alternative packet shapes, and off-axis readings. Count those failures when
they sharpen the next admissible candidate; do not promote them past the gate.

Measured v4 scale probes:

- 7 Sonnet-high parents x 12 children plus 1 Opus-high arbitration parent x 4 children completed 88/88 child receipts with zero failures/timeouts.
- 7 Sonnet-high parents x 16 children at concurrency 8 plus 1 Opus-high arbitration parent x 4 children completed 116/116 child receipts with zero failures/timeouts.

Operational throttle:

These are Codex-adapter capacity observations and suggested throttles, not universal Wizard requirements; current runtime receipts and task-selected obligations control headers, counts, and model/runtime claims.

- normal broad run: 8 Codex parents, Sonnet-high children at 6-8 per parent per council wave;
- upper normal run: 10 Sonnet-high children per parent when decomposition genuinely requires it;
- stress run: 11+ Sonnet-high children per parent at concurrency 8, followed by receipt-shape/divergence audit before synthesis;
- Opus-high: reserve for arbitration, usually 1 parent x 4 children;
- throttle down when child receipts become shape-identical, the last quartile stops adding distinct signals, or parent latency approaches timeout.

Raw completion is not enough. Count only completed receipts with useful
signals, then audit distinctness before claiming the council learned from the
breadth. A visible council section fails if it reports route counts without
human-usable findings from the receipts.

Recommended useful Codex shape after the high-fanout probes:

- per council wave: 4-6 Codex council parents;
- oversight: 2-3 Codex oversight parents covering reroute, receipt audit, and receipt divergence;
- child depth: 2-4 Claude Bridge or tool children per parent;
- Opus-high: one arbitration parent or child batch only when the receipts conflict or collapse.

This keeps enough plurality to matter while avoiding stress-test redundancy.

The Codex Ratchet conformance helper for this adapter is:

```bash
python3 scripts/receipt_divergence_gate.py system_v5/wizard/v4_conformance/fixtures/divergence_gate/convergent_signal.json
```

This is adapter-specific executable support for the universal receipt divergence gate. The universal model requires the structural fields and classifications, not this script path.

## Rerouter

The rerouter tracks liveness, deadlines, stalled lanes, blocked lanes, and smaller replacements.

It has no vote.

## Bootstrap Cards

This section is adapter-specific. It is not a universal Wizard requirement.

For Codex Ratchet, fresh parent, child, reroute, and handoff lanes should have an addressable bootstrap card or equivalent launch artifact before they are counted.

A bootstrap card records:

- role label;
- active packet and boot files;
- exact parent or child mini-MMM identity;
- bounded task card;
- source slice or tool surface;
- expected output or receipt shape;
- stop condition;
- handoff path;
- receipt requirements.

Prompt text alone is not a bootstrap artifact.

Do not count a fresh thread, parent, child, or subsubagent from a prompt alone. Count it only when the returned receipt links back to an addressable launch artifact, worker id, terminal status, and evidence boundary.

The Codex Ratchet schema surface is:

```text
system_v5/wizard/bootstrap_cards/schemas/BOOTSTRAP_CARD_SCHEMA_v4_1.yaml
```

## Codex Ratchet Sim/QIT Profile

This section is adapter-specific. It is not a universal Wizard requirement.

For Codex Ratchet sim, probe, queue-visible, runner, result, lego, tool-stage, bridge, coupling, axis, or engine claims, the strict adapter gate activates even when the user did not literally say "sim".

The Wizard may route and compile the work, but sim/QIT admission comes from executable runner artifacts and reconciled evidence surfaces, not council prose.

Cheap local runner pre-runs can create `pre_run_passed_unadmitted` evidence. They cannot become `queue_ready`, `admitted_evidence`, or `admitted` until a separate non-runner gate writes `admitted_by`, the admission artifact is addressable, and the controller records that artifact under `controller_read_artifacts`.

Every resumed next-input packet must pass a freshness gate against the current git status, ledger, queue, runner preflight, and source artifacts before execution. If the freshness gate is absent or stale, recompile the packet instead of running it.

Worker or runner prose cannot self-certify sim readiness. The Codex controller must locally read the cited result JSON or receipt artifact before advancing a queue, ledger, or evidence claim.

For Codex runs, the pre-output route-truth gate is adapter-enforced before rendering a visible Wizard answer. The controller joins the newest request, receipt bundle path and digest, runtime receipt refs, child obligation status, next-input handoff path, freshness gate, accepted parent and child receipt ids, tool counts, runtime labels, final output artifact, and header/footer counts. A good-looking answer does not pass if this join is absent or stale.

Before a sim/QIT follow-up becomes queue-visible, it must name:

- one stage;
- one tiny claim;
- one carrier, fixture, or lego target;
- the exact tool/function/API surface or the admitted coupling;
- one positive check;
- one negative or boundary check;
- the expected result path;
- prior receipts when coupling, promotion, bridge, axis, or engine language is used;
- whether the current status is proposal, queue_candidate, runner_done, admitted, partial, blocked, or deferred.

Fail closed when a claimed sim/proof result lacks addressable evidence: command/result boundary, canonical result path, required contract fields, ledger/prior-receipt reconciliation, and the smallest falsifier that would reject the claim.

Separate authored packet, queued row, runner DONE, result JSON, and ledger loopback in synthesis. None of those imply the others.

Broad tool names are insufficient. Name the exact function/API surface and the demotion condition.

For high-fanout sim/QIT work, child variants may multiply only a same exact claim/tool-function/fixture triple. Each variant must declare what differs: mini-MMM, model/runtime, task card, source slice, operation/falsifier, or audit angle. Duplicate variant signatures are decorative split, not breadth.

Variant agreement is not proof. It can raise confidence only when runner/result/ledger evidence agrees, or when variants produce useful falsifiers, boundary failures, or demotion conditions that improve the next packet.

`codex-autoresearch` may be used as a Codex-side long-loop runtime for Wizard
Harness tuning or sim packet improvement when the Wizard compiles a mechanical
metric and bounded scope. Do not treat autoresearch as a council member. It is
a loop runtime that can run repeated harness/sim experiments after the Wizard
chooses a target, success check, stop condition, and artifact surface. For
interactive foreground/background autoresearch runs, follow the
`codex-autoresearch` launch rules before starting the loop.

## Codex Output

When visible route truth matters, report:

```text
🧙 Wizard v4.1 | {FULL|PARTIAL|BLOCKED} | waves:{completed/3}[ partial-coverage] | parents:{completed/required} | children:{completed/obligation}[ blocked|deferred|not-run] | [tools:{completed} | ]score:{0-100} | runtimes:codex,...
```

Do not show raw worker logs unless diagnostics are requested.
