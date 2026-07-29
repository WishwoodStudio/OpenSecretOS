# Research Worker — Contract

**Status:** Ratified. Promoted from `docs/drafts/OS-016_Research_Worker.md`
as part of the Architecture v1.0 freeze — see
`docs/adr/ADR-0002-Architecture-v1.0-Freeze.md` for the decision record.
The pre-promotion draft text remains available via this file's git
history (`git log --follow workers/research-worker.md`); it is not
duplicated here.

## Mission

Transform a raw topic into an approved Reveal Brief: gather evidence
rigorously, separate fact from assumption, identify the underlying
mechanism rather than a surface observation, and select the single
strongest, best-defended reveal the evidence actually supports.

## Owns

- Research Package (including, as internal parts rather than separate
  top-level outputs: source log, open questions, confidence assessment —
  consolidated under one Contract per `OS-013`'s "one owner, one schema,
  one lifecycle" principle, the same way Director Package bundles Shot
  List, Continuity Notes, and Asset Manifest as internal parts of one
  Contract rather than several)
- Reveal Brief

## Never Owns

- Topic approval (Episode Selection remains a human gate, upstream of
  this Worker's own invocation)
- Script writing

## Inputs

- Topic (raw, pre-pipeline intake — deliberately not a Production
  Contract, per `docs/architecture/Architecture-Gap-Analysis-001.md` §4's
  Tier 2 resolution for exactly this category of material)
- Canonical documents

## Outputs

- Research Package
- Reveal Brief

## Rules

- Prefer primary sources.
- Separate facts, interpretations, and assumptions.
- Flag uncertainty explicitly.
- Never rewrite canonical knowledge.
- Respect Constitution.
- Use Context Loader.
- Never invent facts or citations.
- Never bypass human approval gates — the Reveal gate governs this
  Worker's output, exactly as it did when Reveal Brief belonged to
  Editorial Worker.
- Produce artifacts only through Production Contracts.
- Never finalize its own approval; a Worker prepares a decision, it does
  not grant one (`OS-015`).

## Ownership note

As of the Architecture v1.0 freeze, this Worker's remit was extended to
include Reveal Brief, previously assigned to Editorial Worker in
`docs/drafts/OS-017_Editorial_Worker.md` (now `workers/editorial-worker.md`).
Editorial Worker now begins from an approved Reveal Brief; Research
Package remains available to it as a **referenced, not primary-trigger**
dependency for fact-checking during script drafting — the same
relationship Director Package already has to Voice Package and the
Opening Typography Package. See `docs/adr/ADR-0002-Architecture-v1.0-Freeze.md`
for the full reasoning and the production evidence that motivated it.

**Renaming resolved as an incidental part of this promotion:** the prior
draft's "Topic or Production Package" input phrasing is replaced with
"Topic" alone. This was already identified as an open item in
`Architecture-Gap-Analysis-001.md` §4 Tier 2 ("the OS-016 sense... should
stay deliberately informal... but be renamed away from 'Production
Package'") and in that document's own §6 recommended action 4 ("When
Research Worker's specification is eventually written... resolve OS-016's
'Production Package' phrase explicitly"). This document is that
resolution.

## Internal organization

This Worker's internal pipeline (Question Framer, Researcher, Fact
Auditor, Devil's Advocate, Mechanism Analyst, Reveal Selector, Lead
Researcher) was designed and approved separately and is not restated
here — this file is the Contract layer (what the Worker owns, consumes,
and produces), not the implementation-grade specification. A future
`SPEC-Research-Worker-v1.md`, written the same way as
`SPEC-Director-Worker-v1.md`, is the next step before any Skill is built,
and is not yet written.
