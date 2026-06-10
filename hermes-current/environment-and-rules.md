# Environment and Rules

Purpose: durable operational facts and boundary rules that agents should check before acting.

Status: active Hermes working-spine operational note.

Use this when:
- checking tooling/environment assumptions
- planning runs or reporting
- deciding which operational constraints are load-bearing

Current truth:
- In this Hermes terminal environment, `python` is not on PATH; use `python3`.
- Detailed environment/process context was offloaded from injected memory and should be recovered from `hermes-memory-offload.md` when needed.
- The wiki is the active long-form harness/workspace.
- The research papers directory is `/Users/joshuaeisenhart/wiki/raw/papers`.
- Hermes, Claude Code, and Codex bot/config surfaces are separate. Do not mix credentials or transports across them.
- For Hermes-controlled run reporting, use the Hermes bot/transport.
- Jean-Patrick Smith collaborates on Leviathan/parallel projects and handles the Leviathan lev os GitHub repo.
- Do not modify v5 docs unless explicitly asked; prefer the Hermes spine, the project front doors, and the repo-current authority surfaces for active steering.
- Ordinary Hermes sessions should share one main memory/workspace unless and until there is a real need for an independent agent boundary.
- Hermes durable memory is profile-scoped rather than single-running-instance-scoped: same-profile Hermes sessions share memory; separate profiles isolate it.
- If truly independent Hermes agents are introduced later, isolate them with separate profiles first rather than prematurely fragmenting the shared main wiki now.
- Keep canonical wiki pages shared by default; create per-agent queues/logs/scratch only when an independent agent actually exists.
- Overnight/controller-style runs should use a continuous queue, not idle audit/sleep loops, and human-facing updates should be periodic rather than spammy.

Simulation/process shorthand:
- final sims should run on pure mathematical paths rather than internal jargon; simulate the math rather than encode internal jargon into the sims. For Codex Ratchet geometry work, use [[projects/codex-ratchet/geometry-sim-program-canonical-2026-06-10]] and [[projects/codex-ratchet/s1-qubit-ladder-f01-n01-t01-2026-06-10]] as anti-collapse roadmaps before accepting a geometry sim or S2 runtime: F01 finitude, N01 noncommutation, and T01 bracketing boundaries must be explicit.
- tool-first before nonclassical
- classical baselines are broadly useful
- bounded micro-lego → pairwise → small assembly progression is preferred
- preserve broad geometry-family coverage, not just named examples
- failures should trace back to smaller units where possible
- for concurrent agent work, verify file/workstream isolation rather than inventing wait-for-other-thread rules unless explicitly instructed

Do not:
- assume `python` works when only `python3` is available
- blur bot boundaries
- forget that the wiki is the primary long-form memory surface now

Related notes:
- [[read-first]]
- [[hermes-memory-offload]]
- [[active-plans]]

Write mode: agent-editable with care.