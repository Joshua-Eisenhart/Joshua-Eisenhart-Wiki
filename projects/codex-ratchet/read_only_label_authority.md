last_updated: 2026-04-17T15:17:19-07:00

# READ ONLY label authority

This project treats any folder or file name containing `READ ONLY` as an explicit owner scope boundary and frozen reference surface.

## Rule

- Without an owner instruction that explicitly names that surface, do not move, rename, delete, rewrite, or bulk-substitute through it.
- Reading the contents, citing them, or mining ideas into a new derived note is allowed; touching the labeled source surface is not.
- Instructions that name folders A and B do not authorize work on related folder C. Unnamed folders stay out of scope by default.
- Before any path-edit or refactor pass, list every folder to touch and compare that list against the owner instruction.

## Evidence

- Memory feedback: `feedback_respect_read_only_labels.md`
- Repo revert: `1b3f16af15882c68024017b31eb011e080bccf42`
