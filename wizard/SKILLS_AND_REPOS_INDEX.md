# Skills and repos index — for the Lev wizard-ratchet patch

Status: reference index, built 2026-06-28 from a read-only seven-agent audit. Not canonical by process. Paths cited; counts re-probed at scan time. Verbs follow harness discipline (survived, admitted, excluded, coupled with) and the status ladder (exists < runs < passes local rerun < canonical by process).

Purpose: index every skill across the owner's repos and the external ecosystem, tag each for relevance to the Lev wizard-ratchet loop, and name what to integrate into the lev patch and what to add to this wiki.

The loop this index serves: a turn becomes structured work — classify, pre-run safe branches, gate owner-choice items, record receipts, chain run-to-run seeds (`nextRunSeed`), and evolve agent skills over time. The deterministic claim-gate stays the only admission authority; LLM lanes are advisory.

---

## 1. Bottom line

- The lev patch already has a real skill-loading contract. `core/graph/src/contracts/formal-skill-set.ts` defines `FormalSkill`; `core/graph/src/probes/skill-source-pack-runner.ts` walks SKILL.md trees, parses frontmatter, classifies by domain, and emits receipts. Integrating new skills means pointing pack requests at more skill roots, not building a loader.
- The seed chain is real and receipt-validated. No hardcoded survivors in the seed path. The fixture ceiling sits at the ClaimGate steering boundary (`live_lev_consumed:false`, `adapter_partial`).
- The missing piece is skill evolution, and it already exists upstream. `hermes-agent-self-evolution` carries session importers, a DSPy + GEPA optimiser, constraint gates, and an LLM-judge — the generate-validate-retain machinery the loop needs.
- Skills are abundant but unindexed. About 700 SKILL.md files sit across roughly ten roots, most of them PM/business and mental-model patterns. The loop-relevant core is small and named below.
- Two integration rules hold. Adopt patterns and harvest skills; do not import authority. Every harvested or evolved skill stays proposal-only until a deterministic gate receipt admits it.

---

## 2. Recent actor work — audit (May–June 2026)

Honest labels. Source: git log, file reads, test reruns.

| Actor | Where | What survived review | Status |
|---|---|---|---|
| Owner (Joshua-Eisenhart) | `~/GitHub/lev` (Jun 20–23), `~/claimgate-suite` (Jun 20), `~/Codex-Ratchet` (Jun 27), `~/wiki` (Jun 20) | ClaimGate steering integration (producer/consumer split, receipt-validated seeding), v45 ClaimGate product, JAX+PyTorch R0 probes, wiki status trail | Orchestration tests green (62–707 pass). Steering adapter `adapter_partial`, non-autonomous. Mined gates proposal-only. |
| Claude | `~/GitHub/lev` (4 commits, Jun 19) | Docs alignment, TLS/Caddy + AgentPing daemon, skill→FlowMind converter, distribution RDO proposal | exists, runs. Operational scaffolding, not core gate logic. The skill→FlowMind converter couples directly to skill integration. |
| chidev | `~/GitHub/lev` (Jun 18–19) | Runtime convergence, FlowMind cleanup (checkpoint commits, no visible diffs) | exists. Upstream Lev maintenance. |
| Hermes | `~/wiki`, status checks | No code May–June; audit and wiki maintenance; caught the harness session-runner 20 pass / 2 fail (SDLC schema path) | Audit role only. |

Open state per `~/wiki/projects/leviathan-current/lev-claimgate-digging-status-2026-06-28.md`: tranche "not land-ready", repo 204 files dirty, legacy `@lev-os/daemon` + `@lev-os/sdlc` coupling unresolved, source-read binding incomplete.

---

## 3. Master skill index by root

Re-probe counts at use. Relevance is to the wizard-ratchet loop, not general utility.

| Root | Count | Character | Loop relevance |
|---|---|---|---|
| `~/GitHub/leviathan-agents/skills` | 57 (+1 agent-lease) | Orchestration + lifecycle + GEO research cluster | HIGH core, LOW for GEO cluster |
| `~/GitHub/lev/.claude/skills` + `.lev` + `context` | ~14 | exec, pentagon, samurai, sync, lev-roadmap, omc-reference, gitnexus | HIGH |
| `~/GitHub/lev/plugins/*/skills` | ~23 | browser, code-graph, sdlc, samurai, marketer | MEDIUM |
| `~/GitHub/lev/research/tool-uni` + bundles | ~212 | PM/business strategy | LOW for loop, HIGH as a harvest pool |
| `~/GitHub/lev/workshop/poc/skills` | ~320 | mental-model / context patterns | LOW, reference only |
| `~/Codex-Ratchet/.claude/skills` | 13 | wizard, wizard-v43, wizard-council, premortem, sim engines | HIGH — newest source of truth |
| `~/Codex-Ratchet/system_v4/skills` | 4 | ratchet-reduce/reflect/reweave/verify (graph) | MEDIUM |
| `~/Desktop/Codex Ratchet/.claude/skills` | 4 | stale snapshot, 6–11 days behind | excluded — snapshot |
| `~/wiki/wizard/packet-v4-{1,2,3}-current/skills` | 9–11 | canonical wizard doctrine + council members | HIGH — reference spec |
| `~/GitHub/hermes-agent/skills` | 28 + 15 optional | broad tool adapters (apple, github, mcp, research) | LOW–MEDIUM |
| `~/GitHub/Sofia/.claude/skills` | 22 | RL / flight-training (PPO, Dreamer, GEPA-adjacent) | LOW for loop, reference for RL |

### Loop-core shortlist (HIGH relevance, by source)

- leviathan-agents: `work`, `cdo`, `sidequest`, `autodev-loop`, `stack` (run-to-run prompt chaining), `lev-intake`, `agentping`, `lev-align`, and the SKILL cluster — `skill-discovery`, `skill-creation`, `skill-building`, `skill-install`.
- lev core: `exec`, `pentagon` (quality gate), `samurai` (critical-path router), `sync`, `lev-roadmap`, `omc-reference`, `eng-review`, `cross-model-challenge`.
- Codex-Ratchet: `wizard`, `wizard-v43`, `wizard-council`, `premortem`, the three-engine sim skills.

---

## 4. Drift map — port and document

### Port into the active harness (`~/Codex-Ratchet/.claude/skills`)
Present in the wiki packets, absent from the active harness:
- `claude-bridge`, `claude-pattern-intake`, `source-math-lock`, `sim-audit-spine`.

Note on `collapse-auditor` / `loophole-auditor` / `factory-handoff` / `follow-up-selector`: these are wiki-packet skills, but the active wizard-council routes collapse audit and voices through registered agents (`council-collapse-auditor`, `voice-*`). So this is a skill-vs-agent routing difference, not a blocking gap. Document the routing; do not assume the wizard is broken.

### Add to the wiki (active skills not in doctrine)
- `sim-wizard`, `lego-sim-classifier`, `codex-ratchet-env-agent-coordination`, `codex-ratchet-tool-status-auditor`.
- `system_v4` graph skills (`ratchet-reduce/reflect/reweave/verify`) belong in a system_v4 manifest, not the wizard packet.

### Snapshot to retire or refresh
- `~/Desktop/Codex Ratchet/.claude/skills` is 6–11 days behind `~/Codex-Ratchet`. Treat `~/Codex-Ratchet` as source of truth.

---

## 5. Lev patch integration surface

Extension points, with cited paths.

- Skill registration: `runDefaultWizardSkillSourcePackIntake()` in `core/orchestration/src/proof/lev-wizard-ratchet.ts`, called at the handler when the `realSkills` flag is set. Widen this to load additional skill roots (leviathan-agents, harvested skills) as `SourcePackReceipt` objects.
- Model lanes: `createDefaultLiveModelLaneRunners()` (handler ~line 352) hardcodes OpenRouter + xAI. The backing factory `claim-gate-model-lane-runners.ts` already supports Claude bridge, Codex local, and Gemini. The gap is configuration: providers are not selectable without editing TypeScript.
- Evolution step: the `seed` subcommand chains via `createSeededLevWizardRatchetInput(previousArtifact, baseInput)` and `runSeededSelfAuditCycle()`. A new evolution step adds a subcommand that reads a result artifact and chains forward.
- ClaimGate steering: `claim-gate-steering-run.ts` (consumer), `claim-gate-steering-produce.ts` (producer, never self-asserts authority), `claim-gate-loop.ts` (failure packets bound to source claims).

Skills stay proposal-only until a loader receipt — claim ceiling `formal_skill_loader_dispatch_not_live_worker_execution`. This matches the gate discipline; preserve it.

---

## 6. Skill-evolution machinery already on disk

`~/GitHub/hermes-agent-self-evolution` (stable, March 2026 — an upstream library, not recent churn). Maps onto the loop's "evolve skills" stage:

| Mechanism | File | Adoptability |
|---|---|---|
| Session importers (Claude Code / Copilot / Hermes) | `evolution/core/external_importers.py` | Ready. Solves cold start — mine the loop's own run logs for datasets. |
| Synthetic dataset builder (DSPy) | `evolution/core/dataset_builder.py` | Ready. Works for any artifact type. |
| DSPy + GEPA reflective optimiser | `evolution/skills/evolve_skill.py`, `skills/skill_module.py` | Ready. The core engine — reads why a skill failed, not just that it did. |
| Constraint validation (hard gate) | `evolution/core/constraints.py` | Ready. Extend with wizard-specific constraints (reachability, no infinite loops). |
| LLM-as-judge fitness | `evolution/core/fitness.py` | Ready. Adapt the judge signature. |
| Trajectory collection | `~/GitHub/hermes-agent/agent/trajectory.py`, `batch_runner.py` | Ready. Instrument the loop to record decision rationale + outcome. |
| Skills hub (provenance, lockfile, quarantine) | `~/GitHub/hermes-agent/tools/skills_hub.py` | Useful. Version evolved skills; rollback on regression. |

Coupling note: `hermes-self-evolution` provides skill evolution; lev's `skill-source-pack-runner` provides skill loading; both can plug into the seed chain. Claude's skill→FlowMind converter (Jun 19) is the bridge already started.

---

## 7. External — find wholly (sources, verify before adopting)

Ranked. HIGH first. Adopt patterns and harvest skills; do not import authority.

1. Darwin Gödel Machine — generate-validate-retain with a novelty-retaining archive. The formal version of the ratchet. https://github.com/jennyzzt/dgm , https://arxiv.org/abs/2505.22954 . HIGH.
2. VoltAgent awesome-agent-skills — ~1,500 vetted, Claude-compatible skills to harvest into `leviathan-agents`, each gated before promotion. https://github.com/VoltAgent/awesome-agent-skills . HIGH.
3. Self-Evolving Agents survey + repo — the map for picking evolution techniques. https://github.com/XMUDeepLIT/Awesome-Self-Evolving-Agents , https://arxiv.org/abs/2507.21046 . HIGH.
4. skill-creator (Anthropic / Microsoft) — engine for generating and optimising new skills. In the VoltAgent list and `anthropics/skills`. HIGH.
5. Voyager — canonical executable skill-library pattern (check the library before writing new code). https://github.com/MineDojo/Voyager , https://arxiv.org/abs/2305.16291 . HIGH pattern; Minecraft-specific origin.
6. oh-my-openagent v4.12.0 (ohmy) — durable team-mode patterns, already extracted at `~/claimgate-suite/docs/80_OPENAGENT_V412_TEAMMODE_EXTRACTION.md`. Pattern-only, authority none. https://github.com/code-yeongyu/oh-my-openagent . MEDIUM.
7. AgentSkills MCP bridge — serve skills to any MCP client via progressive disclosure. https://github.com/zouyingcao/agentskills-mcp . MEDIUM.
8. anthropics/skills — Agent Skills spec and SKILL.md format anchor. https://github.com/anthropics/skills . MEDIUM.

Unverified, read before trusting: oh-my-openagent star count; marketplace skill counts (self-reported, inconsistent); EvoSkills arXiv ids and the SICA repo. No public Leviathan/Kingly OS exists to sync from — `lev-os/leviathan` is private; `~/GitHub/lev` is the working copy. The richer internal mining target is `~/GitHub/lev/workshop/analysis/`.

---

## 8. Proposed sequence (all lev-repo edits need owner greenlight)

1. Widen `runDefaultWizardSkillSourcePackIntake()` to admit `leviathan-agents` loop-core skills as source packs. Reversible, additive.
2. Make model lanes selectable (config, not code) — the backing factory already supports Claude/Codex/Gemini.
3. Wire skill evolution: adapt `hermes-self-evolution` session importer to read loop run logs, then run GEPA on a single skill behind the constraint gate. Keep results proposal-only.
4. Harvest 5–10 named skills from VoltAgent into `leviathan-agents`, each gated before promotion.
5. Port the four wiki-packet skills into the active harness; document the skill-vs-agent routing.
6. Map DGM's three phases onto the wizard-ratchet stages in a wiki note; the one behaviour change worth proposing is novelty-retention (keep valid-but-novel survivors, not only the best).

Edits to `~/GitHub/lev` halt for owner greenlight. This index records direction; it does not authorise the edits.
