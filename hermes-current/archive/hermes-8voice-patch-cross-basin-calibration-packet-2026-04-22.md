# Hermes 8-voice patch + cross-basin + calibration packet — 2026-04-22

Purpose: execute follow-up 14 with the wiki/harness in view: patch the live `/tmp` Hermes harness for 8-voice awareness, carry forward the Claude-side saliency work without blindly importing it, and prepare the next proof packet around cross-basin contradiction and fresh-session calibration.

## What landed
1. Minimal 8-voice harness patch landed.
   - `/tmp/hermes-mass-tune-20260422/voices.md`
     - no longer frames Hermes as seven voices
     - now remembers Systems as a first-class voice attractor while keeping the current `/tmp` systems lane for menu stability
     - now states mini-MMM loading as `L0 ambient preamble + short dense language body` with rule rails kept as audit rails
   - `/tmp/subagent-format-harness/roles.json`
     - added `language_body_ref` for the remembered 8-voice set:
       - hume, zhuangzi, feynman, orwell, popper, factory, strategy, systems
   - `/tmp/subagent-format-harness/run_role_batch_matrix.py`
     - now prepends a compact `# mini_mmm_language` block using:
       - `~/.claude/mmm/00_L0_PREAMBLE.md`
       - the role-specific dense body file when present
     - existing `method_contract` / `scope_contract` / `fail_if` rails remain in place after the language body slice

2. Prompt-shape verification landed.
   - `python3 -m py_compile /tmp/subagent-format-harness/run_role_batch_matrix.py` passed.
   - local prompt inspection confirmed `systems`, `hume`, and `zhuangzi` now include:
     - L0 source
     - voice-body source
     - mini_mmm_language block
     - existing rule rails

3. Fresh-session packet prep landed.
   - prompt snapshot exporter:
     - `/tmp/subagent-format-harness/export_8voice_prompt_snapshots.py`
   - exported snapshots directory:
     - `/tmp/subagent-format-harness/hermes_8voice_prompt_snapshots_20260422/`
   - snapshot summary:
     - `/tmp/subagent-format-harness/hermes_8voice_prompt_snapshots_20260422/summary.json`
   - calibration log stub:
     - `/tmp/subagent-format-harness/hermes_8voice_calibration_log_20260422.md`
   - calibration packet design:
     - `/tmp/hermes_fresh_session_calibration_design_20260422.md`

4. Cross-basin contradiction design note landed.
   - `/tmp/hermes_cross_basin_probe_design_20260422.md`

## Checked now
- The patched prompt exporter produced 8 prompt snapshots, one per remembered voice.
- Summary shows all 8 snapshots have `has_l0: true` and `has_body: true`.
- This is a prompt-shape proof only, not a calibration proof.

## What remains open
- No fresh-session calibration run has landed yet.
- No cross-basin extractor/probe implementation has landed yet; design exists, implementation does not.
- No claim is made yet that the 8 attractors are real in Hermes runtime behavior. Only the harness now loads compact language bodies rather than rule rails alone.

## Routing / failure accounting
- One delegated subtask for the fresh-session design did not finish in time.
- It was not retried repeatedly. The work was rerouted into direct local file/tool work instead.
- This is the current preferred policy for this workspace: if a model/path is not landing in a bounded packet, reroute and report it plainly.

## Best next bounded move
1. Run the 5 pair probes first using the exported snapshots:
   - hume vs zhuangzi
   - systems vs factory
   - systems vs strategy
   - orwell vs popper
   - popper vs feynman
2. Log them into `/tmp/subagent-format-harness/hermes_8voice_calibration_log_20260422.md`.
3. Only if the pair probes look distinct enough, run the full 8-voice fresh-session battery.
4. After that, implement the cross-basin contradiction extractor/gate.
