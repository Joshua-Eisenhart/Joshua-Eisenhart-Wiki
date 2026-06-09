# Claude Code Opus subagents / subsubagents proof — 2026-04-23

Main finding
The working live path for Opus subagents is Claude Code custom agents in print mode, not Hermes-native `delegate_task`.

What was proved
- File-based custom agent on Opus works.
- Dynamic `--agents` custom agent on Opus works.
- Nested manager -> leaf agent delegation works.
- Parent Opus max + Opus subagent works.
- Parent Opus max + Opus manager -> Opus leaf nested chain works.

Artifacts
- File-agent probe:
  - `/tmp/claude-opus-agent-probe/file_agent_probe.json`
- Dynamic-agent probe:
  - `/tmp/claude-opus-agent-probe/dynamic_agent_probe.json`
- Nested agent probe:
  - `/tmp/claude-opus-agent-probe/nested_agent_probe.json`
- All-Opus parent + subagent probe:
  - `/tmp/claude-opus-agent-probe/all_opus_probe.json`
- All-Opus parent + nested manager/leaf probe:
  - `/tmp/claude-opus-agent-probe/all_opus_nested_probe.json`
- Machine summary:
  - `/tmp/claude-opus-agent-probe/summary.json`

Key evidence
- `file_agent_probe.json` result = `OPUS_AGENT_OK`; `modelUsage` includes `claude-opus-4-7[1m]`.
- `dynamic_agent_probe.json` result = `DYN_OPUS_OK`; `modelUsage` includes `claude-opus-4-7[1m]`.
- `nested_agent_probe.json` result includes `NESTED_OK`; `modelUsage` includes `claude-opus-4-7[1m]`.
- `all_opus_probe.json` result = `ALL_OPUS_OK`; `modelUsage` shows only `claude-opus-4-7` (+ haiku helper), meaning parent and agent lane stayed on Opus.
- `all_opus_nested_probe.json` result = `ALL_OPUS_NESTED_OK`; `modelUsage` shows only `claude-opus-4-7` (+ haiku helper), proving a working all-Opus nested manager -> leaf path in Claude Code.

Contrast with Hermes-native delegate
- Hermes `delegate_task` attempted with `acp_command="claude"` and Opus ACP args still returned child `model: gpt-5.4` in the checked proof run.
- So the present practical recommendation is:
  - use Claude Code custom agents for Opus subagents/subsubagents now
  - treat Hermes-native Opus delegate routing as still unproved/open

Recommended next move
- Standardize one reusable Claude Code Opus custom-agent harness and use that as the current baseline while Hermes-native delegate Opus routing is debugged separately.
