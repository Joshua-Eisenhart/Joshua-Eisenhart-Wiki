# Hermes Memory Offload

Purpose: migration ledger for durable facts rescued from injected Hermes memory during memory-pressure cleanup.

Status: active Hermes migration ledger, not the final canonical home for every fact.

Use this when:
- tracing what was offloaded from injected memory
- recovering detailed prior memory content
- deciding which facts should be normalized into more stable Hermes-spine notes

Current truth:
- This note exists because Hermes durable memory became crowded and long-form detail needed to be offloaded into the wiki.
- The immediate 2026-06-03 rescue worked: injected memory was compressed and the detail was preserved here.
- **Normalization was essentially complete** as of 2026-06-03: 18 of 19 rescued facts lived in spine notes (`environment-and-rules.md`, `about-me-and-how-to-work-with-me.md`, `current-vs-legacy.md`) or injected memory. The only unnormalized item was the Python package inventory (PyG, clifford, TopoNetX, z3, etc.), which is environment-specific and better verified at use time than stored as a static fact.
- **Reopened 2026-06-05 for process correction:** Hermes again hit injected-memory pressure and directly edited the tiny memory layer. Correct behavior is preserve/normalize in wiki first, then compress injected memory to pointers only.
- This note is a **migration/provenance ledger**, not the primary steering surface. Agents should read the spine notes directly for current behavior, and use this note to audit what was offloaded or rescued.

Current receiving structure:
- [[read-first]]
- [[about-me-and-how-to-work-with-me]]
- [[active-intentions]]
- [[active-plans]]
- [[environment-and-rules]]
- [[current-vs-legacy]]
- [[skills-and-agent-rules]]
- [[memory-maintenance-2026-06-05]]
- [[memory-maintenance-2026-06-06-wizard-maintenance-correction]]
- [[wizard-maintenance-correction-receipt-2026-06-06]]
- [[../wizard/hermes-version-current/16_HERMES_WIZARD_MAINTENANCE_GOVERNOR|Hermes Wizard Maintenance Governor]]
- [[../concepts/entropic-spacetime-monism-readout-map|Entropic Spacetime Monism Readout Map]]

Normalization rule:
- identity/preferences → `about-me-and-how-to-work-with-me.md`
- active priorities/ongoing direction → `active-intentions.md` or `active-plans.md`
- durable environment/boundary facts → `environment-and-rules.md`
- authority/provenance rules → `current-vs-legacy.md`
- agent/skill usage rules → `skills-and-agent-rules.md`
- detailed historical rescue content can remain here as a ledger until a better home exists

## Rescued long-form content

### 2026-06-05 live memory snapshot before compression

Hermes memory was preserved before another compression pass in [[memory-maintenance-2026-06-05]]. That note records the live `/Users/joshuaeisenhart/.hermes/memories/MEMORY.md` and `USER.md` contents, the active built-in-memory/default-profile state, and the intended compression plan.

Rule reaffirmed: preserve or normalize in the wiki first, then compress injected memory to short pointers. Do not treat the latest correction as permission to overwrite crowded memory unless the displaced detail is already in a wiki note, raw owner-source artifact, project page, or skill.

Wizard alignment added 2026-06-05: Hermes Wizard may coordinate this maintenance loop for Hermes memory, skills, subagents, and the wiki, but only as a bounded governor over existing Hermes authority surfaces. Its maintenance contract lives in `../wizard/hermes-version-current/16_HERMES_WIZARD_MAINTENANCE_GOVERNOR.md`.

### 2026-06-05 memory-pressure correction and routing preference

This addendum exists because Hermes memory was again near-full and a correction turn revealed that the wiki offloader should have been used before directly rewriting injected memory.

Rescued/normalized durable facts from current injected memory and user corrections:
- Current Hermes routing preference: minimize the active Hermes context window; use external agents as much as possible.
- codex2 is the primary heavy worker. Use Claude Code and Grok 4.3 as strong external contrast/workers when available. Gemini can be used when the exact model ID is verified from the live API model list rather than guessed.
- Claude Code with Sonnet on high reasoning can be used heavily as a worker route. Opus is available but token-expensive; conserve it for cases where its extra capability is load-bearing.
- The active Hermes route for Codex GPT-5.5 should preserve a 1.1M context window, but the controller should still spend that context sparingly; large work packets should be passed to external workers by file path and summarized back as receipts/diffs.
- For Hermes memory behavior: memory is a compact steering/index layer only. Detailed doctrine, project context, routing history, and procedural detail should go first to the wiki spine/offload note or to skills, then injected memory should be compressed to short pointers.
- `wiki/hermes-current/` is a directory/spine, not a single attachable file. Use `wiki/hermes-current/read-first.md` as the front-door file and `wiki/hermes-current/hermes-memory-offload.md` as the offload ledger.
- If memory is full, do not simply replace user-profile facts with the latest preference unless the detail has been preserved or normalized into the wiki.

Normalization target:
- routing/work-distribution preference belongs in `about-me-and-how-to-work-with-me.md` and `skills-and-agent-rules.md`
- memory-offload procedure belongs in `skills-and-agent-rules.md` and this ledger
- provider/model availability probes are session/runtime facts unless promoted into a skill/reference after repeated use

### 2026-06-06 Wizard-maintenance correction: entropic-spacetime monism offload

A correction turn identified a process miss: Hermes had been doing source-processing and direct wiki patches without explicitly running the Hermes Wizard maintenance-governor loop or preserving the memory/offload receipt first.

Corrective actions recorded now:
- live built-in memory and user profile snapshot preserved in [[memory-maintenance-2026-06-06-wizard-maintenance-correction]] before further compression;
- detailed owner correction normalized to [[../concepts/entropic-spacetime-monism-readout-map|Entropic Spacetime Monism Readout Map]];
- injected memory compressed to a short pointer: one entropic-spacetime substrate reads as space/time/entropy/DE/gravity/DM/mass-energy/matter/forces; matter=knots; sector maps remain open;
- project routing patched in `projects/codex-ratchet/read-first.md` and `concepts/physics-model-as-system-mirror.md`.

Rule reaffirmed: when the user says Hermes is missing Wizard/memory/maintenance discipline, run a bounded maintenance-governor tranche: inventory -> classify -> patch one cluster -> verify -> log/queue. Do not claim a full Wizard council unless subagent, multimodel, and MMM preload receipts actually exist.

### Python / environment
- In this repo's python3 environment, PyG, clifford, TopoNetX, z3, hypothesis, networkx, and torch load cleanly; sim_edge_state_writeback.py now reports real failures instead of false-greening.
- In this Hermes terminal environment, `python` is not on PATH but `python3` is available (Python 3.13.2 in /Users/joshuaeisenhart/Desktop/Codex Ratchet).

### Simulation / process constraints
- Sim/build rule: final simulations should strip internal jargon and run on pure mathematical paths; the program is to simulate and stack a very large amount of math, not encode jargon into the sims.
- Codex Ratchet rule: every nonclassical lane still needs its own tool-capability and relevant tool-integration evidence first. Classical/numpy locals may run freely as classical_baseline; failures are useful data.
- Codex Ratchet process: preserve broad geometry-family coverage, not just named examples. Hermes should work at micro-lego granularity: tiny base sims one by one, then bounded pairwise coupling exploration off strong locals, then deeper local completion and small assemblies as the evidence warrants. Failures should trace back to micro sims and feed back into missing or weak locals rather than waiting for total lego closure.
- Execution rule for concurrent agent work: 'do not conflict with another Claude thread' means verify file/workstream isolation, not wait for the other process to exit. Never invent a wait-until-finish rule unless explicitly instructed.
- JK fuzz is already mathematically worked out in Axis 0 / shell-history docs and should be treated as load-bearing, not just intuition; current wiki mapping appears thin/scattered relative to repo surfaces.

### Wiki / collaborators / bot boundaries
- Wiki /Users/joshuaeisenhart/wiki is the active Obsidian vault; Dark Empress, Grandmaster, and Leviathan v3.2 are key legacy wiki sources.
- User works with Jean-Patrick Smith on Leviathan and parallel projects; Jean-Patrick handles the Leviathan lev os GitHub repo.
- In the user's wiki workspace, /Users/joshuaeisenhart/wiki/raw/papers is the papers directory for research source files and paper processing.
- User has three independent Telegram bots (Hermes, Claude Code, and Codex). Do not mix credentials/config across them. For Hermes-controlled run reporting, use the Hermes bot/transport, not the Codex bot.

### Stable preferences and constraints rescued from injected user profile
- Order matters by support: lower layers run on higher layers. Weyl spinors run on nested Hopf tori, not vice versa. All constraint layers run at once in that order.
- Superseded correction: autoresearch and sim loops run on bounded packets/profiles with verified prerequisites and file/state isolation. Independent legos, micro-legos, and earned couplings are innately mass-parallel; admission stays per packet/profile and never blurs the whole chain.
- Treat a=a iff a~b and constraints on distinguishability as established foundation, not new ideas. Build from constraints upward; don't skip to entropy/flux before prerequisites run together.
- User requires full/rich treatment of entanglement, tensors, chirality, and correlation entropy in sims. PyTorch Geometric was intended to provide full tensor structure on graphs, and clifford support is also needed; reduced toy formulations are not acceptable.
- For overnight runs: continuous queue is required; no audit/sleep idle loops. Human-facing Telegram updates should be about every 5 minutes, not per-task spam.
- Wiki ~/wiki is the user's nominalist/anti-bias harness. Do not modify v5 docs unless explicitly asked.
- Order exact; bounded only. User wants numpy/classical baselines for everything and all needed tools simed before any nonclassical sims.
- User wants wiki pages explicitly grouped by provenance/framing: newer/current-docs-aligned versus older/legacy/inconsistent.
- Hermes overnight runs: Telegram updates about every 5 minutes, not nonstop.

Do not:
- treat this note as the only current authority forever
- let rescued detail remain unnormalized if a stable current note should carry it
- lose track of why this note exists: it is a memory-rescue and migration surface

Related notes:
- [[read-first]]
- [[about-me-and-how-to-work-with-me]]
- [[active-intentions]]
- [[active-plans]]
- [[environment-and-rules]]
- [[current-vs-legacy]]
- [[skills-and-agent-rules]]

Write mode: controller-maintained with care.
