# Hermes current multi-family compare packet — 2026-04-23

Bottom line
A fresh bounded current-process packet was run across the requested live family mix instead of just describing it from memory.

What ran
- Opus 4.6 max -> landed
- Opus 4.7 max -> landed
- Sonnet 4.6 high -> landed
- Codex gpt-5.4 xhigh -> landed via reroute
- Codex gpt-5.4-low -> blocked on checked ChatGPT-account path
- Gemini -> landed via reroute
- Hermes-native delegate gpt-5.4 -> landed

Reroutes
- Codex OMX path stalled with no output/artifact; rerouted to direct `codex exec -m gpt-5.4`
- Gemini first try hit workspace-read restrictions on absolute wiki paths; rerouted to an inline prompt pack
- gpt-5.4-low was not retried after the checked unsupported error

Artifacts
- `/tmp/hermes-model-packet-20260423a/summary.json`
- `/tmp/hermes-model-packet-20260423a/`

Open
- This packet proves the family routing paths now, but it is not yet a full nested Hermes-native subagent/subsubagent orchestration proof for every family.
- Current Hermes-native delegate children still default to `gpt-5.4` unless explicitly routed otherwise.
