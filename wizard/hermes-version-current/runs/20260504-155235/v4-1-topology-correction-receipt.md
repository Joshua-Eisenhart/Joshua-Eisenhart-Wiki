# v4.1 topology correction receipt — 2026-05-04

User correction: new Wizard v4.1 runs three different LLM councils in sequence, with wide parallel work inside each council. This should not be news during Hermes Wizard adaptation.

Checked source anchors:

- `/Users/joshuaeisenhart/wiki/wizard/packet-v4-1-current/01_UNIVERSAL_THREE_COUNCIL_WIZARD.md`
  - says the three councils are sequential write barriers;
  - says parallelism happens inside a wave.
- `/Users/joshuaeisenhart/wiki/wizard/packet-v4-1-current/05_RUN_PROTOCOL_AND_RETRY.md`
  - says full run minimum needs dedicated parent members for Decision, Failure, and Follow-Up;
  - says accepted parents satisfy child quorum when runtime supports children;
  - gives useful constrained Max Assembly as 3-6 council parents per wave, 2-3 oversight parents, and 5-10 child/subsubagent tasks per counted parent.
- `/Users/joshuaeisenhart/wiki/wizard/packet-v4-1-current/06_OUTPUT_FORMAT_AND_SCORING.md`
  - says visible output must reduce cognitive load;
  - separates waves, parents, children, tools, score, and runtimes.
- `/Users/joshuaeisenhart/wiki/wizard/packet-v4-1-current/08_EXAMPLE_OUTPUT.md`
  - example uses three LLM councils with wide parent/child receipt counts.
- `/Users/joshuaeisenhart/.codex/skills/three-council-wizard-v4-1/SKILL.md`
  - says run three sequential councils and parallelize inside a council.

Changes made:

- Created `/Users/joshuaeisenhart/wiki/wizard/hermes-version-current/09_V4_1_LLM_COUNCIL_TOPOLOGY_CORRECTION.md`.
- Patched `/Users/joshuaeisenhart/wiki/wizard/hermes-version-current/01_RUNTIME_CONTRACT.md`.
- Patched `/Users/joshuaeisenhart/wiki/wizard/hermes-version-current/08_HERMES_WIZARD_RUN_HARNESS.md`.
- Patched `/Users/joshuaeisenhart/wiki/wizard/hermes-version-current/README.md` read order.
- Patched `/Users/joshuaeisenhart/wiki/wizard/hermes-version-current/MANIFEST.md`.
- Patched `hermes-wizard` skill required read order and core procedure.
- Rewrote `runs/20260504-155235/final-render.md` to downgrade the run to `REAL_ATTEMPT_PARTIAL` and state that wide v4.1 LLM council coverage is not proved.
- Patched `conformance/validate_hermes_wizard_run.py` so this minimal validator now requires the corrected partial label and explicit no-full-v4.1 boundary.

Validator rerun:

```text
PASS
validated: /Users/joshuaeisenhart/wiki/wizard/hermes-version-current/runs/20260504-155235
```

Current truth:

The prior run is useful as a minimal sequential topology fixture. It is not a proper/full v4.1 wide LLM council run.
