# docs/drafts/

## Purpose
Holding area for documents that exist but have not been ratified into
`architecture/`, `specifications/`, `adr/`, `principles/`, or `canonical/`.

## Contents
16 of the 18 original Open Secret OS architecture drafts remain here,
unmodified from their source:

`OS-001` through `OS-015`, and `OS-018` — vision, system architecture,
repository philosophy, knowledge architecture, episode workspace spec,
context loading, production graph, worker architecture, integration
layer, runtime architecture, CLAUDE.md spec, repository structure,
production contracts, artifact spec, state management, and the Director
worker definition.

All 16 carry `Status: Draft v0.1` in their own headers — none are
ratified.

`OS-016` (Research Worker) and `OS-017` (Editorial Worker) were promoted
into `workers/` (as `research-worker.md` and `editorial-worker.md`) as
part of the Architecture v1.0 freeze — see
`docs/adr/ADR-0002-Architecture-v1.0-Freeze.md`. Their pre-promotion text
is preserved in this file's git history, per the rule below, rather than
duplicated here.

## What must never be stored here
- Anything already ratified (move it to its proper category instead)
- New content authored directly here — this folder is for drafts *brought
  in*, not a default place to write new proposals
