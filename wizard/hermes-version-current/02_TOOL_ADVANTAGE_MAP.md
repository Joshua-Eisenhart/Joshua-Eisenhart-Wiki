---
title: Hermes Tool Advantage Map
type: tool_map
runtime: hermes
created: 2026-05-04
updated: 2026-05-04
---

# Tool Advantage Map

Hermes's Wizard version should be built around Hermes tools, not around Codex's spawn-agent machinery.

## Core Hermes advantages

| Hermes surface | Wizard job | Truth boundary |
|---|---|---|
| `skills_list`, `skill_view`, `skill_manage` | load procedures, inspect prior playbooks, save reusable workflows | skill content is procedure, not proof that work ran |
| `memory` | durable user preferences and environment facts | memory can recall; it cannot prove current execution |
| `session_search` | recover prior sessions and decisions | recall is remembered context, not current state |
| `delegate_task` | bounded subagent fanout | only completed summaries/receipts count |
| `cronjob` | scheduled or recurring autonomous work | cron jobs run fresh sessions; prompt must be self-contained |
| `read_file`, `search_files`, `patch`, `write_file` | grounded file work and verification | reading proves file content only at read time |
| `terminal`, `process` | commands, tests, background jobs, readiness checks | process alive is not task done |
| `execute_code` | multi-step tool orchestration and audits | output is script result; still verify critical side effects |
| `web`, `browser` | current research and web interaction | browser state/online facts need fresh receipts |
| `send_message`, gateway delivery | deliver final artifacts/updates | side effects need explicit target/scope |
| profiles / `HERMES_HOME` | isolate agents, memory, skills, sessions | do not fragment profiles without a real independent boundary |
| MCP | dynamic external tool surfaces | MCP tool names and server availability must be checked |

## Recommended route mapping

- direct answer -> controller-local plus file/web/tool reads as needed
- critique/falsifier -> `delegate_task` only when separable and useful
- follow-up scout -> `delegate_task` or tool run, marked as scout not chosen execution
- durable watch -> `cronjob` only after explicit scope
- long autonomous mission -> separate Hermes process/profile/worktree if truly independent
- wiki/harness work -> file tools + execute_code audits + bounded delegation

## Tool-first rule

If Hermes can check a state with a tool, check it.

Examples:

- current file content -> `read_file`
- current file inventory -> `search_files`
- arithmetic/counts -> `execute_code` or terminal
- current date/system state -> terminal
- current web facts -> web/browser

## Anti-theater rule

Do not claim a Wizard lane just because Hermes has the toolset.
A toolset is capability, not execution.
