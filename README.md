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

**Architecture v1.0 (Frozen)** as of 2026-07-24 — see
`docs/adr/ADR-0002-Architecture-v1.0-Freeze.md`. Further architectural
redesign is deferred until real implementation or production experience
demonstrates a concrete deficiency; improvements are tracked as backlog
items, not immediate redesigns.

`docs/drafts/` holds 16 of the original 18 architecture drafts, not yet
ratified — `OS-016` and `OS-017` were promoted into `workers/` as part of
the freeze. `canonical/` holds working documents (Decision Log, Visual
Identity System, Production Playbook, Mechanism Ladder, and two items
still in draft/placeholder state — see `canonical/README.md`). `episodes/`
holds several episode workspaces at various production stages, from early
research through fully assembled video. A first Worker implementation
(Director Worker) exists under `.claude/skills/`; Research Worker and
Editorial Worker have ratified contracts under `workers/` but no Skill
implementation yet. `CLAUDE.md` still does not exist.
