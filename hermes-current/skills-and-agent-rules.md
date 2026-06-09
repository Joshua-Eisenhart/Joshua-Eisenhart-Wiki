# Skills and Agent Rules

Purpose: explain how skills and agents should interact with this wiki.

Status: active Hermes working-spine agent-governance note.

Use this when:
- deciding whether to load skills
- deciding what an agent should read before acting
- designing or patching skills for this workspace

Current truth:
- Skills are procedures, not the main store of long-form doctrine.
- The wiki is the primary long-form frame and memory surface.
- For substantive Hermes work, read the `hermes-current/` spine before acting, even if it consumes context.
- Concept-level harness pages such as `harness-boot-pack.md`, `llm-ingest-policy.md`, and `current-canonical-spine.md` are second-layer doctrine surfaces: load them after the `hermes-current/` spine when the task needs controller/repo-doctrine depth.
- Skills should help agents read the right notes in the right order and keep updates disciplined.
- Good skills reduce drift and confusion; they should not duplicate large amounts of wiki doctrine unnecessarily.
- Memory-offload discipline is mandatory under memory pressure: write/preserve detailed durable facts in the wiki spine or `hermes-memory-offload.md` first, normalize to the right spine note when clear, then compress injected memory to short pointers. Do not directly overwrite crowded memory with a new preference unless the displaced detail is already preserved.
- For Hermes memory maintenance, preserve the live memory/profile snapshot in a dated `hermes-current/memory-maintenance-YYYY-MM-DD.md` receipt before compression. Then update `hermes-memory-offload.md`, patch the relevant skill if the process failed, and only then use the memory tool or memory files to shrink injected entries.
- The active Hermes session should act as controller/verifier/editor, not bulk context sink, when external workers can do the heavy read/write work. codex2 is the primary heavy reading/patching worker; Claude Code with Sonnet/high reasoning is a heavy-use worker route; Grok 4.3 and verified Gemini routes are contrast/pressure workers when useful; conserve Opus because it burns tokens fast.
- Wizard is a composable controller over standalone skills, agent routes, model routes, and tools. A component should remain usable alone, and Wizard should compose it only when it materially changes the answer, evidence, falsifier, repair plan, or follow-up packet.
- Wizard can also serve as the bounded maintenance governor for Hermes, durable memory, skills, subagent ledgers, and the wiki. In that mode it inventories, classifies, patches one cluster, verifies, logs/queues, and stops at finite caps; it coordinates existing Hermes authority surfaces rather than replacing them.
- Subagent management belongs in explicit ledgers/receipts: task card, route/owner, launch/block status, allowed inputs, output artifact, status, and promotion decision. Parent-reported nested work is not raw child proof until the controller verifies the artifact.
- For now, ordinary Hermes sessions are expected to share one main memory/workspace rather than pretending each session is an independent agent.
- If independent Hermes agents are created later, give them separate Hermes profiles before giving them separate operational wiki surfaces.
- When that later split happens, keep canonical/shared truth pages shared unless there is a concrete reason to isolate them; only agent-local queues, logs, and scratch should split by default.

Expected behavior for Hermes:
1. Read `hermes-current/read-first.md`.
2. Read the most relevant Hermes spine notes for identity, intentions, environment, and provenance.
3. For substantive work touching the system/physics/geometry, load the `nominalist-harness-steering` skill — it distills the 6-axis pre-emit audit, language discipline, mandatory pushback, and anti-patterns from the harness into actionable checks.
4. Read project-specific notes if the task is project-bound.
5. Escalate into deeper concept-level harness notes only when the task needs formal doctrine, translation rules, controller contract detail, or evidence-routing structure beyond what `hermes-current/` carries.
6. Load/use relevant skills.
7. If a skill proves incomplete, patch the skill or record the gap.

**Mandatory gate reads before any stage task:**

Before launching, executing, or authorizing any stage-advancing task (tool-integration sim, lego coupling, coexistence test, emergence test, bridge/axis work), read and cite:
- `ENFORCEMENT_AND_PROCESS_RULES.md` — which stage gate criterion must be satisfied
- `06_coupling_program_order.md` Operational Gate Definition table — which result file satisfies the criterion
- The result file itself — status label must be `passes local rerun` or `canonical by process`

If the result file cannot be cited from the current session: the stage gate is not satisfied. Report the block. Do not proceed. Do not construct a narrative that reframes the blocked work as authorized.

This read requirement is not optional for stage tasks. It applies even when the task feels obviously correct, the research direction is clear, and the agent reporting the prerequisite sounds confident.

Meta-skill directions:
- harness-bootstrap: load the core wiki spine first
- project-bootstrap: load project-specific current notes after the spine
- skill-audit: inspect whether a skill has clear triggers, read-order rules, verification, and low drift risk
- skill-patch-from-session: patch or record missing skill guidance after real use
- wiki-upgrade-audit: decide whether a wiki change is local or whether it should update an integrator/Hermes-spine note

## Project routing

Agent governance rules apply per-project. For Codex Ratchet work: read `projects/codex-ratchet/read-first.md` + `wizard/harness-consolidated/00_READ_FIRST.md`. Preserve the corrected loop model there: tool capability/integration before nonclassical use; then iterate between strong shell-local parents and bounded pairwise couplings, feeding failures back into locals. Keep coexistence, topology-variant promotion, emergence, bridge, axis, and engine claims behind late-stage evidence blocks. For Leviathan OS work: read `~/GitHub/leviathan/docs/NORTH_STAR.md` + `wizard/harness-consolidated/14_leviathan_os_constraint_map.md`. Cross-project work reads both.

Do not:
- let skills replace the wiki as the main frame surface
- allow skills to duplicate large amounts of stale doctrine when linking to a canonical current note would suffice
- assume every agent should have broad write authority

Related notes:
- [[read-first]]
- [[active-intentions]]
- [[active-plans]]
- [[current-vs-legacy]]

Write mode: controller-maintained.
