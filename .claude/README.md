# .claude/

## Purpose
The Claude-Code-specific integration point. Everything the *current* AI
runtime needs that isn't a portable engine/runtime concept lives here.

## Ownership
Runtime-implementation detail — replaceable as a unit if the AI runtime
ever changes, without touching `engine/`, `runtime/`, or `workers/`.

## Subfolders
- **`skills/`** — home for Worker implementations as Claude Code
  Skills (`SKILL.md` + supporting files). A Skill's prompt content lives
  inside its own skill folder here, not in a separate repository-level
  prompts directory. Currently holds one Skill implementation,
  `director-worker/` (Director Worker).

`CLAUDE.md` will live at the repository root (Claude Code's required
location for auto-loading), not inside this folder.

## What belongs here
Claude-Code-specific configuration and Skill implementations only.

## What must never be stored here
- Provider-agnostic mechanics (belong in `engine/`)
- Worker *contracts* (belong in `workers/`)
- Anything that should still make sense if Claude Code is replaced
