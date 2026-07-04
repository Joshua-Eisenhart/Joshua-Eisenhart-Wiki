---
title: Moloch Trap Reference
created: 2026-04-10
updated: 2026-04-12
type: concept
tags: [reference, entropy, coordination, quantum, simulation, legacy]
sources:
  - raw/articles/legacy-books/leviathan-v3-2-word.txt
framing: current
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# Moloch Trap Reference

## Overview
This page keeps the QIT-aligned Moloch trap narrow. It is not a universal sociology claim. It is a finite shared-resource claim: locally greedy extraction can deplete a common resource faster than agents preserve it, causing future extraction to stall.

## Working definition
A QIT-aligned Moloch trap is a finite shared-bath coordination failure in which individually greedy extraction strokes consume the common athermality or distinguishability resource faster than the group repairs it.

Important constraints:
- finite carrier only
- explicit admissible maps only
- no infinite bath idealization as primitive
- no policy-universality claim
- the earned claim is about resource longevity, not total human governance theory

## Why it matters here
This concept is useful because it gives the system a bounded way to talk about coordination loss without leaving operator-state language. The trap is not "evil" or mystical. It is a failure mode in shared resource bookkeeping.

## Live repo status
- `sim_qit_moloch_coordination_trap.py` with `qit_moloch_coordination_trap_results.json` is now the clean owner row. It shows that greedy local extraction drives the shared bath below a usable threshold sooner, while scheduled repair / lose strokes keep that shared resource usable longer.
- `igt_moloch_trap_sim.py` with `igt_moloch_trap_results.json` remains older exploratory evidence.
- `sim_moloch_trap_field.py` with `moloch_trap_field_results.json` is not the owner row because its current live result disagrees with its strongest classical-collapse claim.

## Interpretive guardrails
- This row does not prove that every real coordination problem is a Moloch trap.
- It does not prove that repair is free or globally optimal.
- It does not turn a resource-longevity comparison into a full thermodynamic engine theorem.
- It does give one clean bounded sim where greedy local policy depletes a shared resource faster than a balanced coordination schedule.

## Legacy Genealogy

The coordination-failure patterns described here have a clear genealogy in [[the-dark-empress]]:

- **Chapter 6 (Slavery and Servitude):** Identifies how hierarchical systems can become self-sustaining even when the dominated parties would collectively prefer dissolution. The "Neocapitalist Servitude" framing treats debt, dependency, and institutional capture as coordination traps — mechanisms that produce locally stable but collectively suboptimal outcomes. The chapter's structural analysis of why closed systems without exit or transparency sustain themselves maps onto the moloch-trap framing of greedy local extraction depleting a shared resource.
- **Chapter 7 (OpenGovernment):** The governance critique is that monopoly on force and information creates a coordination trap where no individual actor has the incentive to reform the system even if all actors would benefit from reform. "Power scales by distribution" — a ruler of a poor country is less powerful than an elected president of a rich one. This is the system-level version of the bath depletion argument: a shared resource (collective capability) can be exhausted by individually rational extraction (hoarding, centralization) faster than it is replenished.
- **Chapter 4 (Money):** The critique of existing monetary systems treats debt as a coordination trap: instruments that should increase capacity become instruments that extract it. The open-finance proposal is a resource-repair protocol — keeping the shared bath (financial coordination capacity) usable rather than depleting it through asymmetric extraction.

These chapters should be read as legacy genealogy for the coordination-failure framing, not as formal claims about the QIT system.

**Leviathan v3.2 — Governance Mechanics as Coordination-Failure Mitigation:**

v3.2 explicitly addresses power concentration and resource depletion through three mechanisms that map onto the moloch-trap framing:

- **Chapter 3 (Delegated Proxy Voting):** The apex leader holds sole responsibility for decisions, but the base retains a 60% dissent veto enforced by smart contract. Revocable delegation is the mechanism that prevents the individually rational strategy (concentrating power) from depleting the shared resource (trust and governance capacity). The document explicitly names this: "Power Concentration Risks: addressed by transparent blockchain logging, veto mechanisms, and revocable delegations."
- **Chapter 7 (Ecosystem Development Mirror) — Principle 8:** "Resources Are Finite: Ecosystems must prioritize efficiency, or scarcity will tear them apart." This is a direct statement of the finite shared-resource depletion pattern. The ECC currency system is the designed repair mechanism: sharing assets earns ECC while pure extraction earns nothing, keeping the shared bath (collective capability) usable.
- **Rival Leviathans:** Multiple competing hierarchies with voluntary delegation between them creates a cooperative-competitive dynamic. Greedy extraction within one Leviathan is visible across the network; the fluid delegation mechanism routes votes away from extractors toward better-performing leaders. This is the system-design response to the bath-depletion argument.

These should be read as legacy design responses to coordination-failure patterns — governance-level analogues of the QIT moloch trap, not formal claims about the QIT system.

## Related pages
- [[stochastic-thermodynamics-reference]]
- [[qit-engine-proto-ratchet-and-sim-plan]]
- [[qit-basin-engine-synthesis]]
- [[probe-doc-result-map]]
- [[the-dark-empress]]
- [[legacy-governance-bootpacks]]
- [[leviathan-framework]]
