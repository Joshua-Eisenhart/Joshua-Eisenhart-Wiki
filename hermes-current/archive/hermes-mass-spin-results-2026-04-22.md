# Hermes mass spin results — 2026-04-22

Purpose: record the bounded mass voice/lane tuning packet that actually ran after the role/context contract was tightened.

## Packet
- run id: `hermes_mass_spin_20260422a`
- harness base: `/tmp/subagent-format-harness`
- tuned inputs:
  - `/tmp/subagent-format-harness/roles.json`
  - `/tmp/subagent-format-harness/context_v2.md`

## What ran
- `sonnet_high`: batch + synthesis
- `codex_xhigh`: batch + synthesis
- `opus_medium`: batch only
- `gemini_full`: not triggered

## Checked results
- `opus_medium`
  - `/tmp/subagent-format-harness/matrix_opus_medium/hermes_mass_spin_20260422a/batch_results.json`
  - 14/14 role receipts landed
- `sonnet_high`
  - `/tmp/subagent-format-harness/matrix_sonnet_high/hermes_mass_spin_20260422a/batch_results.json`
  - `/tmp/subagent-format-harness/matrix_sonnet_high/hermes_mass_spin_20260422a/final_surface_status.json`
  - batch passed; merged surface landed
- `codex_xhigh`
  - `/tmp/subagent-format-harness/matrix_codex_xhigh/hermes_mass_spin_20260422a/batch_results.json`
  - `/tmp/subagent-format-harness/matrix_codex_xhigh/hermes_mass_spin_20260422a/final_surface_status.json`
  - batch passed; merged surface landed
- `gemini_full`
  - no run directory for `hermes_mass_spin_20260422a`
  - not needed because no decisive contradiction remained after Sonnet/Codex + Opus pressure receipts

## Main findings
- The mass packet now proves the harness can actually spin the full 14-role field again under the tightened voice/lane contract.
- Hume/log confusion, strategy-scale drift, and lane collapse were strong enough to justify the contract patch before the packet.
- Sonnet and Codex both kept the controller claim open rather than overclosing it.
- Opus pressure receipts reinforced the same main pressure point:
  - the answer surface is ahead of the control-receipt surface
  - blocked paths must stay blocked
  - the decisive front is still default-controller proof
- Remaining weakness is semantic quality, not mere execution:
  - Sonnet's merged surface is richer and more structured
  - Codex's merged surface is plainer and more route-disciplined, but its follow-up field still trends toward local/simple options
  - neither result proves the controller by default; both keep that claim open

## Why Gemini was skipped
- The packet rule was to add Gemini only if a real unresolved contradiction survived.
- After Sonnet merged surface, Codex merged surface, and Opus pressure receipts, the remaining difference was mostly quality/style/shape, not a decisive contradiction about the campaign front.
- So Gemini stayed unrun on purpose.

## Next bounded move
- Use these packet outputs to patch the live control surfaces only where the packet still shows real drift:
  1. follow-up semantic collapse
  2. body-vs-Results separation
  3. route-truth / control-receipt honesty
- Then run the default-controller proof packet, because the mass tuning packet still supports the same campaign conclusion: tuning is support work until the controller receipt is real.
