# workers/

## Purpose
The specialist worker registry. Workers are specialists — they consume
canonical knowledge and produce artifacts, but never own the production
pipeline and never define project rules. This folder holds the *contract*
for each worker (provider-agnostic); the *implementation* of a worker as a
Claude Code Skill — including its prompt content — lives in
`.claude/skills/` once authorized.

## Registry

| Worker | Inputs | Outputs |
|---|---|---|
| Research Worker | Topic | Research Package, Reveal Brief |
| Editorial Worker | Reveal Brief, canonical docs (Research Package referenced) | Script Package |
| Director Worker | Script, Visual Identity, Playbook | Director Package, Shot List, AI Prompt Packages, Asset Manifest |
| Voice Worker | Script | Voice Package |
| QA Worker | All production artifacts | QA Report |
| Knowledge Worker | Postmortems | Canonical change proposals only |
| Publishing Worker | Approved production artifacts | Published Episode |

As of the Architecture v1.0 freeze
(`docs/adr/ADR-0002-Architecture-v1.0-Freeze.md`), Reveal Brief moved from
Editorial Worker to Research Worker. Research Worker and Editorial
Worker now each have a full contract file in this folder —
`research-worker.md` and `editorial-worker.md` — promoted from
`docs/drafts/OS-016` and `OS-017`; this table is a summary of them, not a
duplicate source of truth. Director, Voice, QA, Knowledge, and Publishing
Worker remain defined only by this table and their respective source
drafts, not yet promoted.

## What belongs here
Worker contracts/registry entries — what each worker owns, consumes, and
produces.

## What must never be stored here
- Worker *implementation* (Skills, including prompt content) — belongs in
  `.claude/skills/` once authorized
- Episode artifacts a worker produces (belong in `episodes/`)

Director Worker now has an implementation under
`.claude/skills/director-worker/`; no other worker implementations exist
yet.
