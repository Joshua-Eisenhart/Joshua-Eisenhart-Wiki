# MMM v2.8 Validation Report

Status: PASS for packet structure, output contract, and wiki packaging.

This report is the acceptance receipt for the expanded v2.8 candidate after the redundancy and collapse repairs. It does not claim live-runtime behavior proof; cold no-MMM/main-MMM/mini-MMM comparison remains the next behavior gate.

## Repairs Verified

- `universal_mmm/` is now an alias surface that points to `main_mmm/` instead of duplicating the full MMM tree.
- `universal_agent_rules/` is now an alias surface that points to `current/` instead of duplicating Wizard rule files.
- `definitions/json/MMM_DEFINITIONS_ALL_v2_8.json` is the only canonical definitions JSON; exact duplicate tier JSON files were removed.
- `definitions/full/MMM_DEFINITIONS_FULL_v2_8.md` contains the full route contracts; compact, standard, and ultra files are labeled as digests.
- `current/WIZARD_ROUTE_REGISTRY_v2_8.*` preserves legacy voice/lane discovery aliases while keeping repaired taxonomy paths.
- Positive boot prompts no longer name the negative/reference subtree or use negative receipt fields.
- Body voice output reports run contributions; default Follow-up is lanes and compositions only.
- Body compositions use `C19-C25` stable IDs and explain members, integrated result, tension handled, and next gate.
- Follow-up choices use scale IDs `P/S/G/A` and include `Outcome`, `Use when`, and `Stop/gate`.
- Factory, Strategy, and Systems are context-scale lanes, not voice reruns.
- Main MMM rows containing high-risk agency verbs were scrubbed from the v2.8 candidate.
- Hume mini-MMM rows containing academic-Hume jargon were scrubbed from the v2.8 candidate.

## Verification Receipts

- Repo harness: `system_v5/tests/test_wizard_behavior_harness.py`, `test_run_wizard_system.py`, `test_package_wizard_candidate.py`, and `test_run_wizard_proof_manifest.py` passed together.
- Full Wizard run: `runs/wizard_full_expanded_latest/` produced `ok=true` with no final-answer findings.
- Packet audit: `audit/MMM_V2_8_PACKET_AUDIT_AFTER_REPAIR.json` produced `ok=true` with zero findings.
- Wiki probe: `/Users/joshuaeisenhart/wiki/tools/wiki_probe.py` found zero broken links, malformed wikilinks, stubs, or orphans after sync.
- External model audit: Claude Opus 4.7 was used through `claude-bridge`; Codex accepted only the concrete repair items that matched local evidence.

## Size Receipts

- mini_mmm_full_voice_json: 12
- mini_mmm_full_lane_json: 12
- mini_mmm_standard_voice_json: 12
- mini_mmm_standard_lane_json: 12
- mini_mmm_compact_voice_json: 12
- mini_mmm_compact_lane_json: 12
- mini_mmm_ultra_voice_json: 12
- mini_mmm_ultra_lane_json: 12
- main_full_words: 1024
- main_full_couplings: 14925
- main_full_triplets: 22000
- main_standard_words: 982
- main_standard_couplings: 3688
- main_standard_triplets: 3109
- main_compact_words: 720
- main_compact_couplings: 1900
- main_compact_triplets: 1900
- main_ultra_words: 420
- main_ultra_couplings: 950
- main_ultra_triplets: 753

## Still Open

- Cold behavior comparison: no-MMM vs main-MMM vs mini-MMM.
- Runtime salience proof for Hume, Zhuangzi, Popper, Feynman, and follow-up handling.
- Adapter-specific installs for Claude, Codex, Hermes, and future agent systems should be generated from the wiki reference, not hand-edited into the universal packet.
