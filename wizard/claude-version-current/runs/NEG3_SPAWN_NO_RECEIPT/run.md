# Claude Code Wizard run manifest

wizard_run: true
trigger: /wizard
breadth: auto
runtime: claude_code
date: 2026-06-13
scope: smoke fixture — Decision/Failure/Follow-Up topology exercising a failure path
note: |
  This is a SELFTEST / smoke fixture, not a real task run. The opt-in gate here
  is checked against THIS artifact (wizard_run + trigger token), not raw prompt
  text — a pure-Python validator cannot classify ordinary-vs-wizard prompts.
