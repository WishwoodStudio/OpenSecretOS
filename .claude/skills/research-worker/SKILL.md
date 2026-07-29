---
name: research-worker
description: Transform a raw topic into a Research Package and Reveal Brief for a potential Open Secret episode. Use when the user says "Research this topic: ...", asks to research something for Open Secret / an episode, or asks to produce a Research Package or Reveal Brief.
---

# Research Worker

This Skill implements `workers/research-worker.md` (the ratified Contract)
directly. There is no `SPEC-Research-Worker-v1.md` yet — per that
Contract's own "Internal organization" section, the implementation-grade
specification "is the next step before any Skill is built, and is not yet
written." This Skill exists anyway, as a deliberately minimal experiment:
the smallest thing that makes "Research this topic: ..." actually route
to real Research Worker output instead of an unstructured answer. It is
not the complete version — see "Deliberate scope limits" below before
extending it.

If anything here conflicts with `workers/research-worker.md`, the
Contract wins; do not improvise around it.

## Mission

Transform a raw topic into an approved Reveal Brief: gather evidence
rigorously, separate fact from assumption, identify the underlying
mechanism rather than a surface observation, and select the single
strongest, best-defended reveal the evidence actually supports.

## What "Topic" means here

Per `docs/architecture/Architecture-Gap-Analysis-001.md` §4 Tier 2, a raw
Topic is deliberately informal, pre-pipeline intake — not a Contract, not
an Episode Workspace, not a Manifest entry. Whatever the user names after
"Research this topic:" (or the equivalent phrasing) is the Topic. No
special format is required or should be imposed on it.

## What "Research Package" means here

Per the Contract's "Owns" section, Research Package is **one document**
containing source log, open questions, and confidence assessment as
internal parts — not separate files — following OS-013's "one owner, one
schema, one lifecycle" principle, the same way Director Package bundles
Shot List, Continuity Notes, and Asset Manifest as internal parts of one
Contract. Reveal Brief is a second, distinct output — the Contract lists
it separately under both "Owns" and "Outputs."

## Reference precedent

`unsorted/Research_Dollar_Dominance_DRAFT.md` →
`unsorted/Research_Dollar_Dominance_Round2_DRAFT.md` →
`unsorted/Editorial_Review_Dollar_Dominance_DRAFT.md` →
`unsorted/Editorial_Board_Dollar_Concept_Selection_DRAFT.md` →
`unsorted/Reveal_Brief_v1.md` is the one complete, real research-to-reveal
chain this project has actually run (cited as such in `ADR-0002`). It
predates the Architecture v1.0 freeze, so its four-document split reflects
the *old* two-Worker boundary (research vs. editorial), not the current
one — do not reproduce that file split. Reproduce its **function**
(candidate mechanisms → stress-test against competing explanations →
comparative selection of the strongest reveal → a full Reveal Brief) as
internal sections of this Skill's single Research Package, consolidated
under the Contract's current, single-Worker ownership.

`unsorted/Reveal_Brief_v1.md` is the one fully-realized example of a
Reveal Brief in this repository. Match its actual section shape (Episode
Promise, Prior Belief, Belief Transformation, Reveal Architecture, Reveal
Moment, Proof Strategy, Memory, Twenty-Second Retelling, Scope Control,
Script Guardrails, Personal Stake, Appendix) rather than inventing a new
one.

## Procedure

1. **Identify the Topic** from the user's request. Do not ask for it to
   be reformatted into a Contract or Workspace shape — per the Contract,
   it deliberately isn't one.

2. **Check available canonical documents before using any of them.**
   Look for Mechanism Ladder, Content Constitution, and Decision Log in
   `canonical/`. Read whatever is found in full — do not skim for
   keywords, and do not assume a file has real content because it exists.
   `Content_Constitution_v4_DRAFT.md.docx` was found to be a one-line stub
   during Director Worker's own validation; treat anything similarly thin
   as unusable for citation and say so explicitly rather than citing it
   anyway. There is no automated check for this yet (unlike
   `director-worker`'s `check-canonical-doc.mjs`) — do this by direct
   reading.

3. **Gather evidence.** Use real search/fetch tools, not prior knowledge
   alone. Prefer primary sources over secondary commentary. Never invent a
   fact or a citation — if a claim can't be traced to a real source, say
   so plainly instead of smoothing over the gap.

4. **Separate fact, interpretation, and assumption explicitly** in the
   Research Package — as distinct, labeled categories, not blended prose.
   Flag uncertainty explicitly wherever it exists; do not round an
   unresolved question into a confident claim.

5. **Identify candidate mechanisms, plural.** Per the Mission, the goal is
   the underlying mechanism, not the first plausible surface explanation.
   Following the reference precedent's shape: list multiple candidate
   explanations, then stress-test the leading one against real competing
   explanations (what would have to be true for a rival explanation to
   win instead) before treating it as settled.

6. **Select the single strongest, best-defended reveal the evidence
   actually supports**, with an explicit "assume we are wrong" pass —
   what evidence would overturn this reveal, and does it exist. Do not
   select a reveal because it's the most dramatic; select it because it's
   the best-defended given step 5's stress test.

7. **Write the Research Package** as one document: findings, source log,
   open questions, confidence assessment, candidate-mechanism analysis,
   and the reveal-selection reasoning, all as internal sections.

8. **Write the Reveal Brief** as a second, separate document, matching
   `unsorted/Reveal_Brief_v1.md`'s section shape (see "Reference
   precedent" above).

9. **Mark the Reveal Brief's approval state explicitly, using the
   project's canonical artifact lifecycle** (`Draft → Generated →
   Reviewed → Approved → Archived`, per `SPEC-001` §19 / OS-014 — the
   same vocabulary already used in
   `episodes/luxury-destruction/director-package-v2/director-package.meta.json`'s
   `approvalState` field). Add a literal `**approvalState:**` header
   line to the Reveal Brief, in the same header block
   `unsorted/Reveal_Brief_v1.md` already uses for its own `**Status:**`
   and `**Governance:**` lines. This Skill always writes
   `**approvalState:** Generated` — never `Approved`. Per the Contract's
   Rules ("a Worker prepares a decision, it does not grant one" —
   `OS-015`) and `Reveal_Brief_v1.md`'s own precedent ("Claude does not
   self-ratify"), this field exists specifically so a later Worker
   invocation can check it as a real precondition, not just read prose
   describing intent — see `editorial-worker/SKILL.md`, which halts
   unless this field reads `Approved` and is the only place that field
   may be changed to `Approved`, on the human's explicit instruction.
   The Research Package does not get this field: it doesn't correspond
   to a named Human Gate (`SPEC-001` §18 — "not every artifact
   corresponds to a named Human Gate"); only the Reveal Brief is gated,
   by the Reveal gate.

10. **Where to write the output.** No Episode Workspace exists yet at this
    stage — Topic is deliberately pre-pipeline (see above), and Episode
    Selection is a separate, upstream human gate this Skill does not
    perform. The one real precedent for where this kind of pre-workspace
    material lives is `unsorted/`, where the entire reference chain above
    already sits. Nothing in this repository formally documents
    `unsorted/`'s purpose — follow this as observed convention, not a
    ratified rule, and say so in the report to the user rather than
    presenting it as settled.

11. **Report the result** — what was produced, which canonical documents
    were actually usable, every conflict or unresolved uncertainty found,
    and that human review (the Reveal gate) is still required before this
    becomes an Editorial Worker input.

## Explicit non-responsibilities

Same as `workers/research-worker.md`'s "Never Owns": no topic/Episode
Selection approval, no script writing. Also: no finalizing its own
approval, no rewriting canonical knowledge, no inventing facts or
citations, no bypassing the Reveal gate.

## Deliberate scope limits (read before extending this Skill)

This Skill intentionally does not include:

- **A faithful simulation of the seven named internal roles** (Question
  Framer, Researcher, Fact Auditor, Devil's Advocate, Mechanism Analyst,
  Reveal Selector, Lead Researcher). The Contract names them but states
  their design "was designed and approved separately and is not restated
  here." No document in this repository specifies what each role actually
  does, reads, or hands off — building that now would mean inventing
  implementation detail, not implementing an approved design. This Skill
  performs the Contract's Rules as one pass instead, and says so.
- **`SPEC-Research-Worker-v1.md`.** Director Worker's equivalent
  (`SPEC-Director-Worker-v1.md`) is 424 lines across 20 sections
  (execution sequence, validation rules, failure conditions, Definition
  of Done). Writing that is the correct long-term path, not the minimal
  one.
- **Mechanical validation scripts** analogous to `director-worker`'s
  `locate-inputs.mjs` / `check-canonical-doc.mjs` / `validate-*.mjs`.
  Research Package quality (fact/interpretation separation, source
  citation, reveal strength) is judgment-heavy in a way Director
  Worker's structural checks (duration math, required fields) aren't;
  what's mechanically checkable here should be identified from real
  output, not guessed at up front.

## If something doesn't fit this procedure

Same standing rule as `director-worker`: stop, document the specific
obstacle as production evidence, and do not change this Skill, the
Contract, or any Engine document to route around it. That decision
belongs to whoever reviews the evidence.
