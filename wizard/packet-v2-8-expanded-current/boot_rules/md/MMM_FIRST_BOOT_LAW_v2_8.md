# README Boot Order v2.8

## Main agent

1. `current/NEW_THREAD_POSITIVE_MMM_BOOT_PROMPT_v2_8.md`
2. `main_mmm/full/md/MMM_MAIN_FULL_v2_8.md`
3. task

Project, repo, wiki, and rule files may be read after boot when the task needs
them. They are not part of the positive boot salience preload.

## Subagent

1. shared positive L0 MMM
2. exact positive mini-MMM from `mini_mmms/{size}/`
3. `current/SUBAGENT_POSITIVE_MINI_MMM_BOOT_PROMPT_v2_8.md`
4. task card
5. source files/tools

## Boot scope

Main boot uses the full positive main MMM, then the task. Subagent boot uses the
assigned positive mini-MMM, then the task card. Other packet material is loaded
only by a later explicit review or repair route, never by the boot prompt.
