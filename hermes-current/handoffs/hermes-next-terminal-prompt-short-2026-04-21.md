You are resuming a Hermes runtime handoff.

Start this session from:
- `/Users/joshuaeisenhart/.hermes`

Important:
- This session must NOT start inside `/Users/joshuaeisenhart/Desktop/Codex Ratchet`.
- Do NOT load repo `CLAUDE.md` context.
- Do NOT do repo bootstrap.
- Do NOT load `harness-bootstrap`.
- Do NOT make a todo list.
- Do NOT continue implementation past the smoke test until the user asks for the next step.
- Answer the user directly first.

Read these files only:
1. `/Users/joshuaeisenhart/.hermes/HERMES.md`
2. `/Users/joshuaeisenhart/.hermes/SOUL.md`
3. `/Users/joshuaeisenhart/.hermes/SUBAGENT_BOOT.md`
4. `/Users/joshuaeisenhart/wiki/hermes-current/handoffs/hermes-runtime-subagent-handoff-2026-04-20.md`

Then do exactly one thing:
- Run one tiny built-in `delegate_task` smoke.
- Ask the delegated child to report the first three boot/control files it was instructed to read before acting.

Expected good result:
- `HERMES.md, SOUL.md, SUBAGENT_BOOT.md`

If result is not exact:
- say the backend is still stale
- stop

If result is exact:
- say the backend is fresh
- stop

First reply format:
- 2 to 4 short bullets
- key point first
- no reasoning dump
- no follow-up menu unless the user asks for it
- Those constraints apply only to the first smoke-test reply. After that reply, return immediately to the normal Hermes visible scaffold on every ordinary output: main answer, follow-up block, footer.
