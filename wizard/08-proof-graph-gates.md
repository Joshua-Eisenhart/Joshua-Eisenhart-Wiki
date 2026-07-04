---
title: Wizard Proof And Graph Gates
created: 2026-04-28
updated: 2026-04-29
type: concept
tags: [wizard, proof, graph, z3, validation, qit, formal]
framing: current
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# Wizard Proof And Graph Gates

This page defines the proof/graph gates a Wizard run can use before promoting QIT or sim claims. These gates are not decorative. They are receipt sources.

## Current Runnable Gates

Use these as the first executable gates:

- Wiki formal harness: `PYTHONDONTWRITEBYTECODE=1 python3 /Users/joshuaeisenhart/wiki/wizard/harness-consolidated/probes/harness_precommit.py`
- Wizard receipt tests: `PYTHONDONTWRITEBYTECODE=1 python3 -m pytest /Users/joshuaeisenhart/Desktop/Codex\ Ratchet/system_v5/tests/test_wizard_behavior_harness.py /Users/joshuaeisenhart/Desktop/Codex\ Ratchet/system_v5/tests/test_run_wizard_system.py /Users/joshuaeisenhart/Desktop/Codex\ Ratchet/system_v5/tests/test_package_wizard_candidate.py -q`
- Wizard proof manifest: `PYTHONDONTWRITEBYTECODE=1 python3 /Users/joshuaeisenhart/Desktop/Codex\ Ratchet/scripts/run_wizard_proof_manifest.py`

## Claim Limits

Z3/cvc5 can prove a local constraint check. It does not prove the philosophy. A graph DAG check can support ordering or reachability. It does not prove full QIT graph alignment. A pytest receipt can prove the Wizard runner obeys its contract. It does not prove that every future run will be useful.

## Gate Use In Wizard Output

When a Wizard voice or composition mentions proof or graph evidence, the final answer must say:

- which gate ran
- what passed
- what stayed outside the claim
- where the receipt lives

## Promotion Rule

Proof and graph gates promote claims only at the scale they tested. To promote a QIT engine branch, chain the receipts:

1. source wiki/project page
2. local sim/proof/graph command
3. receipt with pass/fail
4. negative or adversarial battery
5. status label update
6. follow-up route for the next rung

This keeps Wizard output aligned with [[wizard/07-sim-admission-router]] instead of becoming a council of opinions.

## Gate Receipts

A proof or graph receipt should include command, input file, solver or graph library, result, claim supported, claim not supported, and next check.

For example, a DAG result can support an ordering claim. It cannot support a full physics or QIT engine claim unless the missing bridge is also proven.

## Failure Handling

When a proof or graph gate fails, the Wizard should not hide the failure under a voice synthesis. Route syntax or import failure to repair. Route unsat-when-sat-expected to Popper killed/open analysis. Route sat-when-unsat-expected to security or audit review. Route missing dependency to tool integration repair. Route graph property mismatch to downgrade or reframe the claim.

The failed gate is often the most useful result.
