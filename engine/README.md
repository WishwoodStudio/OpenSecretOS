# engine/

## Purpose
The deterministic, **AI-provider-agnostic** core of the operating system —
the mechanisms that make production repeatable and machine-resolvable,
independent of Claude Code or any other specific AI runtime.

## Ownership
Engine mechanics are structural/schema decisions, not editorial ones, and
not Claude-specific ones. Nothing here should need to change if the AI
runtime driving the system changes.

## Subfolders

- **`contracts/`** — the typed interface each production artifact must
  satisfy (Research Package, Script Package, Director Package, etc., per
  the Production Contracts). Workers exchange typed artifacts, never
  free-form chat; this is where that typing lives. **Interface**, not
  instance.
- **`artifacts/`** — the versioned-artifact registry: lifecycle state
  (Draft → Generated → Reviewed → Approved → Archived) for actual artifact
  instances. **Instance registry**, not interface.
- **`graph/`** — the production graph: how artifacts depend on each other,
  and the invalidation rule (an upstream change marks dependents Outdated).
- **`manifests/`** — manifest-based execution: the schema for describing
  "what should run," and how it's resolved.

## What belongs here
Schemas, contracts, and mechanism definitions that apply across every
episode and would survive a change of AI runtime.

## What must never be stored here
- Anything Claude-Code-specific, including Skills (belongs in
  `.claude/skills/`)
- Actual episode content or artifacts (belongs in `episodes/`)
- Canonical project-behavior documents like the Constitution (belongs in
  `canonical/`)
- Anything specific to a single integration provider (belongs in
  `integrations/`)
