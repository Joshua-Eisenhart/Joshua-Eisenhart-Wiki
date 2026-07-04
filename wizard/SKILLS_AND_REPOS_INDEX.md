# Skills and repos index — for the Lev wizard-ratchet patch

Status: reference index, built 2026-06-28 from a read-only seven-agent audit. Not canonical by process. Paths cited; counts re-probed at scan time. Verbs follow harness discipline (survived, admitted, excluded, coupled with) and the status ladder (exists < runs < passes local rerun < canonical by process).

Purpose: index every skill across the owner's repos and the external ecosystem, tag each for relevance to the Lev wizard-ratchet loop, and name what to integrate into the lev patch and what to add to this wiki.

The loop this index serves: a turn becomes structured work — classify, pre-run safe branches, gate owner-choice items, record receipts, chain run-to-run seeds (`nextRunSeed`), and evolve agent skills over time. The deterministic claim-gate stays the only admission authority; LLM lanes are advisory.

---

## 1. Bottom line

- CORRECTED 2026-06-29 by the stress test (see section 9): the lev loader loads real skills but emits ZERO formal skills from them — `executionProfileFor` (skill-source-pack-runner.ts:122) gates emission on four hard-coded tokens that no real SKILL.md carries. "Point pack requests at more roots" produces inert candidates, not loaded skills. The fix is a code change, not a config change.
- The seed chain is real and receipt-validated, and reaches `host_consumed` with a real `nextRunSeed` from the CLI under `--real-engines --real-skills --real-source-evidence` (cross-model confirmed). The fixture ceiling applies only to the bare demo.
- CORRECTED 2026-06-29: the hermes evolution machinery has a hole. Session importers, secret redaction, and the constraint gate are real and hold under adversarial input, but the `LLMJudge` is dead code (zero call sites) — GEPA optimises bag-of-words keyword overlap (`fitness.py:130`), not LLM judgment. Do not adopt it as a quality engine assuming the judge runs.
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

---

## 9. Stress-test verdict (2026-06-29) — what really works

Method: ~140 agents across five model tiers — Claude Opus/Sonnet-high, OpenRouter Chinese fleet (deepseek-v3.2/r1, qwen3-235b-thinking, kimi-k2-thinking, minimax-m2, glm-4.6), codex 5.5 low, gemini-via-OpenRouter. All read-only, no lev edits, no `--run-model-lanes`. Eleven distinct models returned usable verdicts. Top status reached: `passes local rerun`; none canonical.

### The single highest-leverage fix
Stop gating formal-skill emission on hard-coded trigger tokens in `executionProfileFor` (skill-source-pack-runner.ts:122). Derive the execution profile from the skill's declared frontmatter, parsed with a real YAML library (the current `parseFrontmatter` at :65 is a line splitter that silently admits malformed YAML with corrupted fields, `ok=true`). One change clears three findings: zero-formal-skills (F2), malformed-admit (F3), and makes every real library integrable. Skills still stay candidate-only (`formal_skill_set_candidate_not_runtime_loaded`).

### Works (passes local rerun, no API)
lev core: orchestration 720/720, graph 357, event-bus 353, build 279, index 101, exec 90, telemetry 147, workstream 135; plugins: autoresearch-unit 156, context 69, scheduling 45, dna 40. claimgate-suite 37 files + ratchet ~80 ECDSA (mutation-tested). hermes constraints 16. Seed/ratchet chain end-to-end under `--real-engines` (cost $0).

### Works with a ceiling
hermes redaction + constraint gate (real, but GEPA judge is keyword overlap, not LLM). lev `--real-engines` demo (local Julia/JAX/PyTorch flip true; verdict stays `scratch_diagnostic`). daemon (in-process; cross-process e2e hardcoded off). memory (mock backends only).

### Broken / fail-closed (not API-gated)
lev flowmind 6/966 (missing fixtures), platforms 12/336, sdlc, browser, slate, harness 9/677 — missing fixtures and stale model strings. Codex-Ratchet `make tools`/`make sim` fail-closed on a hygiene gate (missing supervisor JSON; run `make maintenance-report` first).

### Sim corpus census (2026-06-29, 137 agents, corrects an earlier overstatement)
Ran + linted all 4,998 sims. v5 run-rate 72.5% (543/749 exit 0); lint-pass v5 62.2%, v4 70.8%, combined 69.5%. The dominant blocker is MISSING metadata, not bad values: `C1_classification_missing` 1,077 + `C2_manifest_missing` 589 + `C3_depth_missing` 533 = 94% of violations. The `CLASSIFICATION="lego"` issue I earlier called dominant is only 13 sims (`C1_classification_invalid`), and the linter's default scope is `system_v4/probes` — it does not even scan `system_v5/legos`. Three external models ruled the "lego is the systemic blocker" claim NOT_REAL (3/3). The fix is mechanical honest-per-sim metadata backfill + probe refresh — not auto-stamping classifications to pass lint. Census JSON in the session scratchpad.

### By-construction green to distrust
claimgate `doctor()` returns hardcoded `ok:true` without calling `gateObjectBinding`. lev voice plugin certifies a substring-match stub router. autoresearch `experiment.ts --help` exit 0 = import succeeded, not a CLI.

### Self-corrections the cross-model fleet caught
F1: the suite passes (~103 tests, exit 0) but the earlier "89/89" count was wrong (a whole handler test file was uncounted). F4: the seed chain is reachable from the CLI after all (only the bare demo fails). The external Chinese-model lane caught the count error the Claude agents made — the cross-model lane earning its place.

---

## 10. Cross-runtime skill registry (2026-06-29)

Full typed registry of 367 runtime skills persisted at `skill_registry.json` (this directory). Counts by runtime: hermes 202, agents 73, codex-second 48, codex 41, claude 3. By category: orchestration 69, gate-quality 67, code-build 54, other 48, content 40, research 25, handoff-capture 20, skill-lifecycle 18, memory 16, mcp-index 10. Two malformed placeholders (`test-skill` in agents and claude) — exclude from any index.

### First integration tranche (18 skills, all blocked behind the loader fix above)
One runnable council, one Claude controller, two sim/tier orchestrators, the four-skill lifecycle cluster, five gate-quality auditors, the full handoff loop:
`three-council-wizard-v4-3` (codex), `claude-wizard-loop-engineering` (claude), `tier-gate-watch-and-launch` (hermes), `hermes-sim-controller-orchestration` (hermes), `skill-builder`/`skill-creator`/`skill-discovery`/`skill-installer` (agents), `nominalist-harness-steering` (hermes), `codex-ratchet-sim-audit-spine` (codex), `codex-ratchet-tool-status-auditor` (codex-second), `lego-sim-classifier` (codex), `claude-to-codex-intake` (agents), `close`/`propose` (agents), `closeout-result-ingest` + `external-research-return-ingest` (codex), `a2-a1-memory-admission-guard` (codex).

### Dedup: codex and codex-second are near-mirrors
15 overlap groups, almost all codex↔codex-second duplicates (the wizard family, ingest paths, sim contracts, memory-admission-guard). Verdict pattern: where both copies are reference-only, keep one reference; where one is runnable, the runnable copy is canonical; where the skill carries per-runtime state (`a2-brain-refresh`, `codex-automation-controller`), leave it runtime-local. Codex is canonical home for the wizard/ingest rows; `.agents` is canonical for the lifecycle cluster.

### Anti-laundering index scheme (Hermes's good idea, kept)
One index per corpus, never merged: `idx_wiki_reference`, `idx_lev_runtime`, `idx_codexratchet_canon`, `idx_hermes_skills`, `idx_codex_skills`, `idx_codexsecond_skills`, `idx_claude_skills`, `idx_agents_skills`. Every row carries immutable `source_corpus`, `authority_level`, `runnable_vs_reference` — indexing never promotes them. A cross-corpus `view_skill_union` may exist for search only; it grants no authority and surfaces `source_corpus` on every row. Owner canon (Codex-Ratchet) beats a stale Hermes script regardless of mtime.

### Do not integrate yet
Anything that runs on a timer or calls models without a human in the loop: `codex-automation-controller`, `hermes-autoresearch`, the overnight/cron runners, the telegram gateway, the broad `hermes-wizard`. Tranche-three at the earliest.

### Verify-then-trust
Hermes-named skills are mostly real, but `find-skills`, `autodev-loop`, `sidequest` do not exist. The lifecycle cluster lives in `~/.agents/skills` as `skill-builder` / `skill-creator` / `skill-discovery` / `skill-installer`. Treat any name not found by direct registry search as absent, not a synonym.
