# Open Secret Engine

This repository is the long-term operating system for the Open Secret media
business. It is not documentation and not a file cabinet — every directory
exists because a production process requires it.

`CLAUDE.md` (the runtime bootstrap file) does not exist yet. Until it does,
this README is the entry point for orientation.

## Top-level layout

| Directory | Role |
|---|---|
| `engine/` | AI-provider-agnostic core: contracts, versioned artifacts, the production graph, manifest-based execution. |
| `runtime/` | How a request gets executed: repository resolution, context loading, worker dispatch, state resolution. Provider-agnostic concepts; `.claude/` holds the current implementation. |
| `.claude/` | Claude-Code-specific integration point — Skills (future worker implementations) and other Claude-only glue. |
| `canonical/` | Documents that define show behavior (Constitution, Decision Log, Playbook, Visual Identity, Mechanism Ladder). Nothing here is provisional. |
| `docs/` | Prose about the system: drafts, ratified architecture, specifications, ADRs, engineering principles. |
| `episodes/` | Episode Workspaces — the primary production unit. One subfolder per episode. |
| `workers/` | The specialist worker registry (contracts only — implementation lives in `.claude/skills/`). |
| `integrations/` | Adapters to external AI/production services (Higgsfield, HyperFrames, ElevenLabs, future providers). |
| `assets/` | Shared/brand assets used across episodes. |
| `output/` | Final, publish-ready or published episode output. |
| `archive/` | Historical record only. Never loaded automatically. |

See each directory's own `README.md` for what belongs there, what must
never be stored there, and who owns it.

## Status

Skeleton stage. `docs/drafts/` holds the 18 original architecture drafts,
not yet ratified. No canonical documents, no CLAUDE.md, no Skills, and no
production content have been created yet.
