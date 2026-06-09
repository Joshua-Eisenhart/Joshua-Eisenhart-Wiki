# Hermes Opus-heavy window + hybrid microfix packet — 2026-04-22

Purpose: record the user's temporary model-budget instruction and the bounded microfix packet run under it.

## Budget / routing instruction from user
Temporary window:
- use Opus 4.7 max as much as possible before the quota reset window
- still check Opus work with other models
- Codex 5.4 xhigh is currently the more trusted audit / containment layer
- Opus has more upside for good ideas but should not be trusted alone
- after this window, budgeting should become stricter again

Operational reading for the current packet:
- Opus max = idea generation / plurality / synthesis pressure
- Codex xhigh = audit / containment / compression guard
- Sonnet = stable base scaffold when needed
- Gemini = falsifier / negative sample, not default final synthesizer

## What was done
1. extracted hybrid synthesis and contradiction rules from the 4-family compare
2. patched `run_role_synthesis_matrix.py` with a small hybrid microfix
3. reran the synthesis on the same receipt packs
4. observed which defects were actually fixed

## Microfix applied
File patched:
- `/tmp/subagent-format-harness/run_role_synthesis_matrix.py`

Microfix content:
- stronger write-first output contract
- explicit ban on literal `Dropped narratives: ...`
- single-use rule for route-status phrases like `all three live` / `no merge performed`
- later raised Sonnet synthesis `--max-turns` from `10` to `14`

## Fix packet run ids
Full synth rerun:
- `matrix14_hybrid_fix_20260422a`

Contradiction synth rerun:
- `contradiction_hybrid_fix_20260422a`

## Observed outcomes
Clear wins:
- Gemini full synthesis artifact write failure was fixed
  - old: `matrix14_hybrid_synth_20260422a` -> `final_surface_exists: false`
  - fixed: `matrix14_hybrid_fix_20260422a` -> `final_surface_exists: true`
- Codex contradiction placeholder defect was fixed
  - old hybrid contradiction had literal `Dropped narratives: ...`
  - fixed contradiction output has `Dropped narratives: none`
- Opus full + contradiction both landed cleanly under the microfix prompt

Still open / regressed:
- Sonnet contradiction synthesis still failed under the stricter prompt, now as `error_max_turns` even after raising `--max-turns` to `14`
- Sonnet full rerun produced a file but still returned non-clean process status before final closure
- Codex microfix audit process was killed after hanging; no contained Codex audit artifact landed for that subpacket

## Best current reading
- The microfix is worth keeping.
- It fixed two real defects:
  1. Gemini write/no-file failure
  2. Codex contradiction placeholder leakage
- The cost is added prompt pressure, which currently hurts Sonnet contradiction synthesis.

## Recommended routing after this packet
For the remaining Opus-heavy budget window:
- use `opus_max` as the main synthesis / idea / contradiction-pressure lane
- keep `codex_xhigh` as the main audit / containment lane when it is responsive
- use `sonnet_high` as the readable base scaffold reference, but do not force it through the strictest contradiction synthesis packet until the prompt is shortened or split
- keep `gemini_full` as a falsifier / negative-sample lane

## Best next bounded move
1. keep the microfix in place
2. do not widen the prompt further
3. shorten the contradiction-specific synthesis contract for Sonnet instead of increasing turns again
4. continue Opus-heavy compare/tuning packets with Codex audits while the quota window is open
