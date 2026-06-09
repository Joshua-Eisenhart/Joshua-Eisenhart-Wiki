# Strategy Loop Skill v4.2

authority_status: canonical-skill

Preserve strategy across loops.

## Method

1. Identify prompt intent.
2. Identify standing context that must not be lost.
3. Name current strategy state.
4. Name what this loop killed, changed, or confirmed.
5. Choose next priority.
6. Set retreat, hold, or stop condition.

Do not optimize only the latest prompt if doing so would lose the broader strategy.

## Return Fields

- current strategy state;
- next priority;
- retreat/hold condition;
- killed assumption;
- carry-forward context.

Also include the common child receipt fields required by `WIZARD_v4_2.md`.
