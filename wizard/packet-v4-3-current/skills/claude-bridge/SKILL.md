# Claude Bridge v4.3

authority_status: canonical-skill

Use Claude as an external child worker surface from Wizard v4.3.

## Rules

- Premortem and Opus audit are separate steps.
- Opus audit does not replace premortem.
- Claude output counts only with receipt evidence.
- A Claude child must have model, prompt, terminal status, output path or returned conclusion, and route-local child role.
- Use Opus for audit/arbitration, Sonnet for implementation/scout, Haiku for cheap liveness/inventory.
- Use bounded budgets and timeouts.

## Packet-Local Scripts

The packet includes local wrappers in `skills/claude-bridge/scripts/`.

Use the packet-local copy when running from this packet so v4.3 is self-contained.

## Return Fields

Every Claude child or audit must record:

- model;
- prompt or prompt path;
- parent route or external audit step;
- terminal status;
- output path or returned conclusion;
- receipt path;
- cost when available;
- whether the result is a council child, management child, or external audit.

## Separation Rule

Premortem and Opus audit are separate hardening steps. The normal loop is:

1. Run Wizard or local packet check.
2. Run external premortem.
3. Apply fixes.
4. Run Opus audit.
5. Apply fixes.
6. Run conformance and smoke.

Opus can audit premortem outputs but cannot replace the premortem method.
