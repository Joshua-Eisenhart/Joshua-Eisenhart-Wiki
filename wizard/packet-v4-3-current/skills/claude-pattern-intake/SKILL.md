# Claude Pattern Intake Skill v4.3

authority_status: canonical-skill

Mine Claude agents, skills, workflows, or Claude Code outputs for Wizard/Codex
upgrades without treating Claude as runtime authority.

## When Used

Use when an external Claude lane produced useful Wizard, skill, workflow, agent,
audit, or sim/proof process material that may belong in the v4.3 packet or in a
Codex-local skill.

## Method

1. Read current repository or packet authority first.
2. Inventory each Claude source path or pasted excerpt as workflow, agent, skill,
   output, or user note.
3. Convert each useful mechanic into a pattern card:
   source, pattern, problem solved, mechanism, target surface, risk, minimal test.
4. Reject Claude-as-authority, fake route truth, fake councils, unreceipted
   child claims, and completion language without a claim gate.
5. Port only the smallest useful mechanic into Wizard packet, Codex skill,
   workflow, worker prompt, or reference-only note.
6. Validate the port with the target surface's local checks.

## Return Fields

```yaml
claude_pattern_intake:
  sources_read: []
  accepted_patterns: []
  rejected_patterns: []
  target_surfaces: []
  authority_rejections: []
  validation_run: []
  remaining_blockers: []
```

Also include the common child receipt fields required by `WIZARD_v4_3.md`:
child role id, compact MMM loaded, required mini-MMMs loaded, source slice,
evidence boundary, output patch, and status.

## Invalid Outputs

- Treating a Claude workflow, agent, or skill as Codex/Wizard authority.
- Copying a Claude file without adapting authority and receipt rules.
- Claiming a route, voice, or worker ran because it appears in a prompt.
- Porting completion/admission language without the relevant repo claim gate.
