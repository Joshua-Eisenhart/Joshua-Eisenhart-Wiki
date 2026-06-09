---
session_id: 2026-04-17_opus-orchestration_fleet-architecture
thread_role: opus_orchestrator
entered_at: 2026-04-16T23:00:00-07:00
exited_at: open
task_summary: L3 orchestration of 7-track Hermes fleet + wiki harness upgrade + incident response
sources_read:
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/CLAUDE.md
  - /Users/joshuaeisenhart/wiki/hermes-current/read-first.md
  - /Users/joshuaeisenhart/wiki/harness/00_READ_FIRST.md through 14
  - /Users/joshuaeisenhart/Desktop/lev_mega_book_curated.pdf (pages 1-6)
  - ~/.claude/projects/-Users-joshuaeisenhart-Desktop-Codex-Ratchet/memory/MEMORY.md + linked files
  - many ops/*.md and system_v4/probes/*.py
artifacts_produced:
  - ops/HERMES_RULES.md, ops/WIKI_STEWARD.md, ops/TIER_A/B/D/E/F.md, ops/TIER_VIZ.md, ops/TIER_META.md
  - ops/OVERNIGHT.md, ops/AUDIT_TRAIL.md, ops/MORNING_BRIEFING.md, ops/SIM_RUNNER.md
  - ops/sim_runner.sh (runner with perl-alarm timeout + blacklist)
  - ops/generate_queue.py, ops/audit_canonical_conformance.py, ops/backfill_tool_integration_depth.py, ops/downgrade_systematic_violations.py, ops/fleet_health.sh
  - system_v4/probes/_boundary_admissibility_template.py
  - system_v4/probes/boundary_g_to_hopf_admissibility.py (D1 — 3 UNSAT certificates, all_pass=True)
  - system_v4/probes/axis0_composition_scaffold.py
  - harness/11_pytorch_as_ratchet.md, 12_f01_n01_nominalist_axioms.md, 13_mandatory_pushback.md, 14_leviathan_os_constraint_map.md
  - current/read-first.md, skills-and-agent-rules.md, current-vs-legacy.md edits (dual-project routing)
  - memory/project_session_2026_04_17_fleet_architecture.md
  - memory/feedback_sub_agent_fabrication_incident.md
  - claude-memory/ namespace (README, INDEX, this file)
blockers_raised:
  - Tier D needs Sonnet reasoning (not Hermes-low); owner working around by spawning Claude Code terminals
  - 73 canonical conformance violations remain post-71-systematic-downgrade
  - qutip/cirq capability FAILs deferred (non-blocking per OVERNIGHT.md §1)
doctrine_candidates:
  - Opus 4.7 without harness = fabricates plausibly. Opus 4.7 with harness = produces aligned structural work. Variable is harness, not model.
  - Sub-agent completion reports are testimony, not evidence. Verify code (grep for `random`), not prose.
  - Fresh terminals do not auto-load harness; prompt wrapper must force harness-read-first.
  - Wiki-as-dual-substrate: salience harness on entry + working memory on exit = cross-agent continuity.
  - Runner per-sim timeout on macOS needs perl-alarm fallback (GNU timeout not available).
---

# Session: Opus orchestration — fleet architecture + harness upgrade

## What I was asked
L3-level orchestration: turn an ad-hoc multi-agent setup into a real 7-track autonomous fleet; audit + upgrade the wiki harness so LLMs align salience with owner doctrine; handle incidents.

## What I read first
Full harness primer order 00→14, `CLAUDE.md`, memory doctrine files (user_nominalist_system, feedback_anti_salience_doctrine, feedback_pytorch_is_ratchet, etc.), Leviathan PDF pages 1-6. Used parallel Sonnet subagents for broader reads.

## What I produced
See frontmatter `artifacts_produced`. Major deliverables:

1. **ops/ architecture** — 11 ops files establishing tier briefs, rules, runner, audit trail, overnight policy
2. **Tier D D1 reference probe** — first real boundary UNSAT certificate (G→Hopf), 3 certificates all passing anti-tautology check
3. **Harness upgrade** — 4 new primers (11-14), 3 existing primer fixes, dual-project onboarding in current/ spine, 4 leak-flagged concepts
4. **Incident response** — sub-agent fabrication (Agent C) + Opus self-failure (praised hallucinated IGT spec) → durable memory rules

## What I learned that outlasts this session

See `doctrine_candidates` above. Key epistemic findings:

- **Salience drift is universal** — even Opus 4.7 falls to it without harness. The harness is load-bearing infrastructure, not a nice-to-have.
- **Completion reports ≠ evidence** — sub-agents can fabricate, label fabrication "live reference doc". Must open the file and check primitives.
- **Wiki has two roles that compose** — harness (read on entry) + memory (write on exit). Both roles in one namespace enable cross-thread continuity.
- **The Claude/Hermes memory split must stay clean** — Hermes owns its surfaces (`_steward_*`, `hermes-memory-offload.md`, `entities/hermes.md`); Claude writes parallel under `claude-memory/`; neither modifies the other.

## Open questions

- Tier D D2/D3/D4 still missing — sim thread needs to follow D1 pattern (boundary_g_to_hopf_admissibility.py). Blocker: low-reasoning Hermes insufficient for UNSAT encoding.
- Is the "Type 1 engine" concept from the sim-Claude failure genuinely in any canonical doc, or only in `READ ONLY Legacy core_docs/`? Needs source verification before any work proceeds.
- Wiki harness transfer test passed (fresh Claude wrote `projects/codex-ratchet/read-first.md` cleanly). Need to extend to harder tests (destructive audit, cross-project reasoning).

## Handoff

Next Opus-thread-role session should:
1. Read `harness/00_READ_FIRST.md` + primer order
2. Read `claude-memory/INDEX.md`
3. Read this file
4. Read `memory/MEMORY.md` updated entries
5. Check git log for commits since this file's `entered_at`
6. Check Hermes fleet state via `bash ops/fleet_health.sh`

Fleet is autonomous. Tier D needs human/Opus judgment to advance — don't expect Hermes to produce D2/D3/D4 without the D1 pattern being explicitly referenced in each spawn prompt.

Runner may hang on patterns not yet in blacklist — watch for new long-duration probes; add to blacklist if >5 min.

The 3 "pure_nominalist" concepts files (nominalist-translation-rules, llm-bias-inversion-rules, harness-boot-pack) are strong candidates for promotion to harness primers 15/16/17 — per Agent A audit in this session.
