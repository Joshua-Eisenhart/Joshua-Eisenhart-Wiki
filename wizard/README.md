---
title: Wizard Universal Harness
created: 2026-04-28
updated: 2026-05-17
packet: v4.2
type: concept
tags: [wizard, harness, multi-agent, workflow]
framing: current
---

# Wizard Universal Harness

The active Wizard packet is v4.2:

- `packet-v4-2-current/README.md`
- `packet-v4-2-current/WIZARD_v4_2.md`
- `packet-v4-2-current/mmm/FULL_MMM_v4_2.md`
- `packet-v4-2-current/skills/SKILLS_MANIFEST_v4_2.md`
- `packet-v4-2-current/mmm/` route-local mini-MMMs as needed

The packet is standalone. Boot law, route truth, councils, MMMs, mini-MMMs, receipts, compile gates, follow-up, and adapters all live inside that folder.

Wizard v4.1 remains reference/legacy for older universal-packet comparisons:

- `packet-v4-1-current/README.md`
- `packet-v4-1-current/PACKET_MANIFEST_v4_1.md`
- `packet-v4-1-current/mmm/FULL_MMM_v4_1.md`

Do not silently downgrade current Wizard work to v4.1. Use v4.1 only when a task explicitly asks for legacy v4.1 comparison or provenance.

## Reading order

1. `00-read-first.md`
2. `packet-v4-2-current/README.md`
3. `packet-v4-2-current/WIZARD_v4_2.md`
4. `packet-v4-2-current/mmm/FULL_MMM_v4_2.md`
5. `packet-v4-2-current/skills/SKILLS_MANIFEST_v4_2.md`
6. `packet-v4-2-current/mmm/` route-local mini-MMMs as needed
7. Load only the runtime adapter needed for the active runtime.

For legacy v4.1 comparison/provenance work only, switch after step 1 to `packet-v4-1-current/README.md`.

## Wizard contract

The v4.2 packet owns the current Wizard contract. Visible routes require current receipts. Synthesis is not execution.

Topology is Decision Council -> Failure Council -> Follow-Up Council, with wide parallel work inside each council barrier. Current Hermes work uses the v4.2 council/subcouncil shape where the task invokes Wizard topology, with route truth for each council/subcouncil.

## Runtime-native adaptations

- `hermes-version-current/` — Hermes-owned adaptation surface. It treats the universal packet as source material and binds useful Wizard mechanisms to Hermes strengths: skills, memory/session recall, toolsets, `delegate_task`, cron/background/gateway surfaces, profile-scoped state, pretty terminal output, and compact receipt truth.

## Packet archive

- `packet-v4-2-current/` — current Wizard packet.
- `packet-v4-1-current/` — prior packet; reference/provenance only.
- `packet-v4-0-current/` — prior packet; reference only.
- `packet-v3-5-current/` — prior packet; reference only.
- `packet-v3-4-current/` — predecessor; reference only.
- `packet-v3-3-current/` — older predecessor; reference only.
- `packet-v2-8-expanded-current/`, `packet-v2-7-current/` — provenance.

## Status

`packet-v4-2-current/` is the current Wizard surface. `packet-v4-1-current/` is reference/provenance unless explicitly requested. Hermes-specific runtime adoption lives in `hermes-version-current/` and the `hermes-wizard` skill; it is not a global HERMES/SOUL rewrite.
