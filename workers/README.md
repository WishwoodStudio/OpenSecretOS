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
| Research Worker | Topic / existing workspace | Research Package, Source Log |
| Editorial Worker | Research Package, canonical docs | Reveal Brief, Script Package |
| Director Worker | Script, Visual Identity, Playbook | Director Package, Shot List, AI Prompt Packages, Asset Manifest |
| Voice Worker | Script | Voice Package |
| QA Worker | All production artifacts | QA Report |
| Knowledge Worker | Postmortems | Canonical change proposals only |
| Publishing Worker | Approved production artifacts | Published Episode |

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
