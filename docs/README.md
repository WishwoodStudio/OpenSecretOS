# docs/

## Purpose
Prose *about* the system — why it's built the way it is — as distinct from
`engine/`, `runtime/`, and `workers/`, which *are* the system. Nothing here
defines runtime behavior by itself; `canonical/` is the only place that can
define binding rules.

## Subfolders

- **`drafts/`** — documents that exist but haven't been ratified into any
  category below yet. The 18 original Open Secret OS architecture drafts
  (`OS-001` … `OS-018`) live here now, in one batch, exactly as they were
  written. Sorting an individual draft into `architecture/`,
  `specifications/`, or `principles/` — or promoting it into `canonical/`
  — is a ratification decision, not an automatic move.
- **`architecture/`** — ratified, high-level descriptions of how the system
  is put together and why (the "why" behind `engine/`, `runtime/`,
  `workers/`).
- **`specifications/`** — ratified, detailed specs for a single concept
  (e.g. what an Episode Workspace must contain, what an Artifact must
  expose). The spec is the prose contract; `engine/` and `episodes/` hold
  its structural implementation.
- **`adr/`** — Architecture Decision Records: numbered, immutable-once-
  accepted records of a specific *engineering* decision about this
  repository/system (context, decision, consequences). Superseded by a new
  ADR, never edited in place. Distinct from `canonical/`'s future Decision
  Log, which records *editorial/business* decisions about the show itself.
- **`principles/`** — engineering principles governing how this repository
  and its engine are built and operated (e.g. "load only what context is
  required," "deterministic before intelligent"). Distinct from
  `canonical/`, which governs the *show's* editorial/production behavior,
  not the *system's* engineering conventions.

## What must never be stored here
- Binding production rules (belong in `canonical/`, once ratified)
- Episode content
- Worker implementation or prompt content

`drafts/` holds the 18 original unratified architecture drafts.
`architecture/`, `specifications/`, and `adr/` are now populated with
promoted/working content; `principles/` remains empty, awaiting content.
