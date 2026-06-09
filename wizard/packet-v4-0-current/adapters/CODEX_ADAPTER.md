---
title: Wizard v4.0 Codex Adapter
type: runtime_adapter
packet: v4.0
runtime: codex
framing: standalone
---

# Codex Adapter

This adapter binds the universal Wizard to Codex.

These are Codex-specific runtime rules. They are not universal Wizard requirements.

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

## High-Fanout Child Capacity

For Wizard v4 Max Assembly, Codex-native parents may launch Claude Bridge children when the task needs real subsubagent depth.

Measured v4 scale probes:

- 7 Sonnet-high parents x 12 children plus 1 Opus-high arbitration parent x 4 children completed 88/88 child receipts with zero failures/timeouts.
- 7 Sonnet-high parents x 16 children at concurrency 8 plus 1 Opus-high arbitration parent x 4 children completed 116/116 child receipts with zero failures/timeouts.

Operational throttle:

- normal broad run: 8 Codex parents, Sonnet-high children at 10-12 per parent per council wave;
- stress run: 16 Sonnet-high children per parent at concurrency 8, followed by receipt-shape/divergence audit before synthesis;
- Opus-high: reserve for arbitration, usually 1 parent x 4 children;
- throttle down when child receipts become shape-identical, the last quartile stops adding distinct signals, or parent latency approaches timeout.

Raw completion is not enough. Count only completed receipts, then audit distinctness before claiming the council learned from the breadth.

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

## Codex Ratchet Sim/QIT Profile

This section is adapter-specific. It is not a universal Wizard requirement.

For Codex Ratchet sim, probe, queue-visible, runner, result, lego, tool-stage, bridge, coupling, axis, or engine claims, the strict adapter gate activates even when the user did not literally say "sim".

The Wizard may route and compile the work, but sim/QIT admission comes from executable runner artifacts and reconciled evidence surfaces, not council prose.

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

## Codex Output

When visible route truth matters, report:

```text
🧙 Wizard v4.1 | {FULL|PARTIAL|BLOCKED} | waves:{completed/3}[ partial-coverage] | parents:{completed/required} | children:{completed/obligation}[ blocked|deferred|not-run] | [tools:{completed} | ]score:{0-100} | runtimes:codex,...
```

Do not show raw worker logs unless diagnostics are requested.
