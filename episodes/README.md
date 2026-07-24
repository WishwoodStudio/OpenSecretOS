# episodes/

## Purpose
Episode Workspaces — the primary production object. Every episode has
exactly one workspace, and everything related to that episode lives inside
it. Nothing episode-related exists outside its workspace except canonical
documents.

## Ownership
Owned jointly by whichever Worker is currently active on that episode's
production stage; overall state ownership follows the episode's status
(Idea → Research → Selected → Reveal Ready → Script Ready → Direction Ready
→ Production Ready → QA Passed → Published → Postmortem Complete).

## Structure (per episode, once created)
Each episode subfolder holds: Metadata, Research, Sources, Reveal Brief,
Script, Director Package, Voice Package, Assets, QA, Output, Postmortem.

## What belongs here
Exactly one subfolder per episode, containing only that episode's own
production artifacts.

## What must never be stored here
- Canonical documents (belongs in `canonical/`)
- Cross-episode/reusable assets (belongs in `assets/`)
- Anything not tied to a specific episode

This folder currently holds five episode workspaces (`demo-episode`,
`episode-004`, `episode-005`, `luxury-destruction`,
`the-giant-is-the-hostage`) at various production stages, from early
research through fully assembled video.
