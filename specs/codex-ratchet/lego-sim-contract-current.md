---
title: Lego Sim Contract Current Mirror
created: 2026-05-21
updated: 2026-05-21
type: contract-mirror
framing: current_snapshot
tags: [specs, codex-ratchet, lego, sims, contract]
sources:
  - /Users/joshuaeisenhart/Codex-Ratchet/system_v5/docs/LEGO_SIM_CONTRACT.md
---

# Lego Sim Contract Current Mirror

This is a spec-side mirror of the live repo lego/sim contract. It is a routing and salience surface, not the authority itself.

Authoritative source: `system_v5/docs/LEGO_SIM_CONTRACT.md`.

## Core Rule

A small sim is not automatically a valid lego. A sim counts as a real lego only when it declares its role and tier, uses required tools, emits required artifacts, includes required negatives, states promotion status, and can be consumed upward without hidden assumptions.

If those are missing, the sim is `diagnostic_only`.

## Required Fields

Every lego sim must declare identity, purpose/scope, constraint context, tooling, inputs, negatives, outputs, and evaluation fields.

Key current fields that the old concept mirror was missing:

- `sim_execution_kind`
- `tool_manifest`
- `tool_integration_depth`
- `classification`
- `divergence_log` for classical baselines when applicable

## `sim_execution_kind`

Allowed values:

- `classical`: baseline/control evidence only.
- `nonclassical`: requires claim-relevant nonclassical stack, such as PyTorch/PyG for tensor or graph dynamics, Clifford for geometric product/spinor/rotor claims, and z3/cvc5 for structural proof or UNSAT claims.
- `bridge`: connects a named classical-side baseline to a named nonclassical tool plan and remains gated until bridge work is explicitly opened.

## `classification`

Allowed values in the current contract:

- `classical_baseline`: baseline/control evidence only.
- `canonical`: admitted local sim evidence, still limited by its stated claim ceiling.
- `tool_lego_fit_probe`: pre-admission tool-lego fit evidence only.

`tool_lego_fit_probe` must keep `promotion_allowed: false` or an equivalent claim ceiling. It cannot be cited as canonical, bridge, QIT, GStack, axis, or nonclassical admission without a later admitted receipt.

## Promotion State

Internal `promotion_status` values:

- `admitted`
- `keep_but_open`
- `audit_further`
- `diagnostic_only`
- `broken`

These are internal sim-role states. They are not the public repo truth labels from [[specs/codex-ratchet/llm-controller-contract-current|LLM Controller Contract Current Mirror]].

## Tool Rules

Required tools must be listed and actually used. If a tool is listed but not used in the real execution path, the sim is `diagnostic_only`.

Underpowered tool use blocks promotion when the tier requires proof, graph, topology, or other rich surfaces.

## Negative And Artifact Rules

Every real lego sim needs explicit negatives when the tier requires them. Negatives must be named and artifacted, not just described in prose.

Minimum artifact classes:

- result artifact;
- witness trace or event trace;
- tool-usage evidence;
- classification summary.

Missing required artifacts make the sim under-specified.

## Composition Rules

A lego sim must be safely composable. It must declare hidden dependencies, eligible consumers, blocked consumers, bridge/cut status, and whether the output supports executable bridge use, doctrine-facing cut use, control-only use, or discriminator-only use.

Higher packets cannot use lower sims merely because a broad packet score is green. Executable winners, doctrine-facing winners, and pointwise discriminators must remain distinct if they differ.

## Claim Ceiling

This mirror supports lego/sim contract routing. It does not make any sim a real lego, promote any result, or authorize higher-stage composition by itself.

Concept mirror: [[lego-sim-contract]].
