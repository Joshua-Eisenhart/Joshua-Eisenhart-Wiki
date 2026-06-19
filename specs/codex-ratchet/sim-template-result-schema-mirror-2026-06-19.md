---
title: SIM_TEMPLATE Result Schema Mirror
created: 2026-06-19
type: spec-mirror
status: draft_upgrade_pack
claim_ceiling: wiki routing / documentation upgrade only; no sim admission, no repo status promotion
tags: [codex-ratchet, sim-template, schema]
sources:
  - Codex-Ratchet/system_v4/probes/SIM_TEMPLATE.py
  - Codex-Ratchet/system_v5/docs/LEGO_SIM_CONTRACT.md
---


# SIM_TEMPLATE Result Schema Mirror — 2026-06-19

## Minimal result keys to keep searchable in wiki

```yaml
name:
probe_family:
constraint_set:
tool_manifest:
tool_integration_depth:
positive:
negative:
boundary:
classification:
surviving_alternatives:
claim_ceiling:
next_lego_target:
promotion_condition:
blocked_until:
demotion_condition:
out_of_scope:
all_pass:
criteria_checked:
```

## Tool manifest row

```yaml
tool:
  tried: false
  used: false
  reason: ""
```

Every tried/used tool needs a non-empty reason.

## Tool integration depth

Use:

```text
load_bearing
supportive
None
```

Avoid decorative tool imports. If a tool is declared but not used, promotion is blocked.

## Classification values

```text
classical_baseline
canonical
tool_lego_fit_probe
```

## Boundary language

Positive = admitted configurations under `C`.

Negative = excluded configurations under `C`.

Boundary = places where probe family `M` loses resolution.

## Claim ceiling

A template result alone does not unlock lego promotion, bridge, axis, engine, emergence, Tier D, physics, or scientific coupling claims.
