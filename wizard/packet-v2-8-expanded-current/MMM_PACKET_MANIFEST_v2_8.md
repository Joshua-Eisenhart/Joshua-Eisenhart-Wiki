# MMM Packet Manifest v2.8

Generated: 2026-04-28T22:11:44.886476+00:00

Kind: expanded_candidate_chat_contract_repair

## Counts

- audit_files: 6
- audit_md_lines: 60
- boot_rules_files: 8
- boot_rules_md_lines: 82
- compact_checks_guards_json_files: 3
- compact_checks_guards_md_files: 3
- compact_compositions_json_files: 7
- compact_compositions_md_files: 7
- compact_controller_acts_json_files: 1
- compact_controller_acts_md_files: 1
- compact_lanes_json_files: 6
- compact_lanes_md_files: 6
- compact_system_routes_json_files: 1
- compact_system_routes_md_files: 1
- compact_voices_json_files: 9
- compact_voices_md_files: 9
- current_files: 16
- current_md_lines: 1154
- definitions_files: 6
- definitions_md_lines: 649
- full_checks_guards_json_files: 3
- full_checks_guards_md_files: 3
- full_compositions_json_files: 7
- full_compositions_md_files: 7
- full_controller_acts_json_files: 1
- full_controller_acts_md_files: 1
- full_lanes_json_files: 6
- full_lanes_md_files: 6
- full_system_routes_json_files: 1
- full_system_routes_md_files: 1
- full_voices_json_files: 9
- full_voices_md_files: 9
- main_mmm_files: 8
- main_mmm_md_lines: 52391
- mini_mmms_files: 216
- mini_mmms_md_lines: 63519
- reference_only_negative_files: 3
- reference_only_negative_md_lines: 8
- runs_files: 291
- runs_md_lines: 99786
- standard_checks_guards_json_files: 3
- standard_checks_guards_md_files: 3
- standard_compositions_json_files: 7
- standard_compositions_md_files: 7
- standard_controller_acts_json_files: 1
- standard_controller_acts_md_files: 1
- standard_lanes_json_files: 6
- standard_lanes_md_files: 6
- standard_system_routes_json_files: 1
- standard_system_routes_md_files: 1
- standard_voices_json_files: 9
- standard_voices_md_files: 9
- tools_files: 6
- tools_md_lines: 0
- total_files: 565
- total_md_lines: 217680
- ultra_checks_guards_json_files: 3
- ultra_checks_guards_md_files: 3
- ultra_compositions_json_files: 7
- ultra_compositions_md_files: 7
- ultra_controller_acts_json_files: 1
- ultra_controller_acts_md_files: 1
- ultra_lanes_json_files: 6
- ultra_lanes_md_files: 6
- ultra_system_routes_json_files: 1
- ultra_system_routes_md_files: 1
- ultra_voices_json_files: 9
- ultra_voices_md_files: 9
- universal_agent_rules_files: 2
- universal_agent_rules_md_lines: 5
- universal_mmm_files: 2
- universal_mmm_md_lines: 5

## Notes

- Factory, Strategy, and Systems are canonical voices with overall-context scope under mini_mmms/*/voices; lanes are compatibility discovery aliases only.
- Compositions are Follow-up-only and must not render as a main-answer C5-C9 or C19-C25 body catalog.
- Default chat Follow-up is lean: lane follow-ups and composition follow-ups, each with 🪄 Follow-up, Pre-run status/score, and Audit fields.
- Full Wizard chat output includes a computed Quality Audit Score covering drift, sycophancy, hallucination, fake execution/lying, filler/fluff, receipt grounding, useful density, and format collapse.
- Mass-wave attempt completed 6 Codex native agents, 37 Claude Task completions, and Gemini direct/audit probes; it did not prove a 140+ live subagent run.
- packet audit and structure audit after repair both report ok=true with zero findings.

## Open Gates

- fresh runtime boot proof
- cold no-MMM vs main-MMM vs mini-MMM behavior comparison
- true 140+ live worker/subworker run with receipts
- live adapter wiring proof
