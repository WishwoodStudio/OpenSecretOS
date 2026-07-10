# runtime/

## Purpose
Defines how a request gets executed against the repository: resolving
paths, resolving current production state, loading only the context a task
needs, and dispatching to the right Worker. These are runtime *concepts* —
currently implemented via Claude Code, but designed to outlive that
specific choice. `.claude/` is where the Claude-Code-specific implementation
of these concepts lives; this folder defines the contracts they must
satisfy.

## Ownership
Runtime behavior is infrastructure, set deliberately rather than
improvised per session.

## Subfolders

- **`repository-resolver/`** — owns path resolution against the canonical
  repository root. Never infers structure; never trusts shell/session
  working directory.
- **`context-loader/`** — the Context Loading System: which documents a
  given task type requires, so the runtime never reads the full repository
  by default.
- **`worker-dispatcher/`** — routes a resolved task to the correct Worker
  (per the `workers/` registry) and its current implementation.
- **`state-manager/`** — resolves current production state from the
  repository (episode status, artifact/graph state) before any Worker is
  invoked.

## What belongs here
Rules and configuration governing *how* the runtime behaves.

## What must never be stored here
- `CLAUDE.md` itself — lives at the repository root, not created yet, and
  points into this folder rather than duplicating it
- Claude-Code-specific implementation detail (belongs in `.claude/`)
- Episode data, canonical documents, or worker prompt content
- Anything provider-specific (belongs in `integrations/`)
