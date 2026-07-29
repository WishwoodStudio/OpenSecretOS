---
name: editorial-worker
description: Transform an approved Reveal Brief into a Script Package for an Open Secret episode. Use when the user asks to write the script, produce a Script Package, or continue production after a Reveal Brief has been approved.
---

# Editorial Worker

This Skill implements `workers/editorial-worker.md` (the ratified
Contract) directly. There is no
`SPEC-Editorial-Worker-Script-Pipeline-v1.md` yet — per that Contract's
own "Internal organization" section, the implementation-grade
specification "is the next step before any Skill is built, and is not
yet written." This Skill exists anyway, scoped the same way
`research-worker/SKILL.md` was: the smallest thing that makes an
approved Reveal Brief actually produce a Script Package, with the
Reveal gate enforced as a real precondition rather than a remembered
intention.

If anything here conflicts with `workers/editorial-worker.md`, the
Contract wins; do not improvise around it.

## Mission

Transform an approved Reveal Brief into a production-ready Script
Package.

## Required input

A Reveal Brief — per the Contract's Inputs, "approved/locked, post-Reveal
human gate." If the user's request doesn't name a specific Reveal Brief
file and more than one plausible candidate exists (e.g. several files
under `unsorted/`), ask which one rather than guessing.

Research Package is a **referenced, not primary-trigger** dependency
(per the Contract's "Ownership note") — read it for claim-traceability
during drafting, but it does not gate this Skill's invocation and is not
what step 1 below checks.

## Procedure

1. **Read the Reveal Brief's `**approvalState:**` header field** — the
   field `research-worker/SKILL.md` writes as `Generated` and never as
   `Approved`.

2. **Halt if `approvalState` is not exactly `Approved`.** Do not draft
   any part of the Script Package — not an outline, not a placeholder.
   Report the Reveal Brief's current `approvalState` plainly and state
   that Editorial Worker cannot proceed until it reads `Approved`. Ask
   the human directly whether to approve it now. This mirrors
   `director-worker/SKILL.md` step 3's halt-on-unmet-precondition
   pattern.

3. **Continue only after explicit human approval.** "Explicit" means the
   human's own clear words approving *this* Reveal Brief — never inferred
   from silence, a topic change, or an ambiguous reply. On explicit
   approval, update the Reveal Brief's `**approvalState:**` field to
   `Approved` via a direct edit before proceeding. This is the only
   place that field may become `Approved`, and the only trigger for it —
   this Skill does not self-approve (`OS-015`: "a Worker prepares a
   decision, it does not grant one"), and does not treat approval of
   something else as approval of this gate.

4. **Once `approvalState: Approved` is confirmed** (found already
   Approved on first read, or just set per step 3), read the Reveal
   Brief in full, plus the Research Package it references, for
   claim-traceability material.

5. **Check available canonical documents before using any of them.**
   Look for Visual Identity, Production Playbook, Content Constitution,
   and Decision Log in `canonical/`. Read whatever is found in full — do
   not skim, and do not assume a file has real content because it
   exists (`Content_Constitution_v4_DRAFT.md.docx` was found to be a
   one-line stub during Director Worker's own validation; treat
   anything similarly thin as unusable for citation and say so
   explicitly).

6. **Draft the Script Package.** Prose script and narration, tracing
   every factual claim back to the Reveal Brief and/or Research Package.
   Never invent a fact not present in either. Never modify the Reveal
   Brief this Skill consumes (explicit Contract Rule) — the Script
   Package is a new, separate artifact.

7. **Report the result** — what was produced, which canonical documents
   were actually usable, any claim that could not be traced to a source,
   and that Script Lock (the next named Human Gate) still governs before
   this Script Package is production-ready. Mark the Script Package
   `Generated`, not `Approved` — same discipline as step 2/3 above,
   applied to this Skill's own output this time.

## Explicit non-responsibilities

Same as `workers/editorial-worker.md`'s Rules: no research, no reveal
selection (that decision belongs to the already-approved Reveal Brief),
no modifying the Reveal Brief, no bypassing the Reveal gate or Script
Lock, no self-approval, no inventing facts.

## Deliberate scope limits (read before extending this Skill)

This Skill intentionally does not include a faithful simulation of the
internal pipeline named in `workers/editorial-worker.md` (Script Writer,
Compliance & Fact-Checker, General Audience Reviewer, Retention Editor,
Critical Reviewer, Lead Editor — the Contract states the latter three
"run as isolated subagents"). That design "was designed and approved
separately and is not restated" in the Contract, and no document in this
repository specifies what each stage actually does. Building that now
would mean inventing implementation detail, and would mean simulating
sub-agents — both outside this experiment's scope. This Skill performs
the Contract's Rules as one pass instead, and says so.

## If something doesn't fit this procedure

Same standing rule as `director-worker` and `research-worker`: stop,
document the specific obstacle as production evidence, and do not change
this Skill, the Contract, or any Engine document to route around it.
That decision belongs to whoever reviews the evidence.
