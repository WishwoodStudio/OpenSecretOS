# Architecture Gap Analysis 001: "Production Package" has no Contract

**Status:** Analysis — no architectural or specification changes applied
**Trigger:** Writing `docs/specifications/SPEC-Director-Worker-v1.md` required a
precise definition of "Production Package," which does not exist as a named
Production Contract, Canonical document, or Workspace component anywhere in
the repository or its source drafts.
**Scope:** Analysis only. This document changes no existing file and
implements no recommendation.

---

## 1. Root cause

Two compounding structural gaps, not one:

**1a. `engine/contracts/` is empty.** OS-013 lists nine Initial Contracts in
prose, inside a Draft-status document. That list has never been
transcribed into `engine/contracts/` as actual schema files. The only
"source of truth" for what counts as a valid Contract is a paragraph in
`docs/drafts/OS-013_Production_Contracts.md` — a document this repository's
own `docs/drafts/README.md` explicitly describes as unratified. There is,
today, no place in the repository where a Worker specification (or a
human) can mechanically check "is this noun a real Contract?" The check I
performed while writing `SPEC-Director-Worker-v1` was a manual, prose-level
cross-reference against OS-013 — the same kind of manual check anyone
writing OS-016 could have done, and evidently didn't.

**1b. OS-013's governing rule is scoped ambiguously.** OS-013 states
"Workers communicate only through these contracts" and "Workers never
exchange free-form chat." This rule clearly governs *inter-Worker*
exchange — Worker A's output becoming Worker B's input. It says nothing
about the *first* input into the pipeline: material that originates
outside any Worker (a human-supplied topic, an externally-sourced brief).
Because the rule's scope was never made explicit, it's undecidable from
the drafts alone whether genesis/external input is supposed to be a
Contract too, or is legitimately exempt. "Production Package" was coined
into exactly that undecided space.

Neither gap is a drafting mistake in one document — both are the absence
of a mechanism (a populated registry, a scoping rule) that would have
caught the drift automatically instead of requiring a human to notice it
while writing unrelated, unrelated-seeming implementation work.

## 2. Why this inconsistency appeared

Concrete causal chain, in order:

1. `OS-013_Production_Contracts.md` was written, establishing nine named
   Contracts (Research Package, S9 Scorecard, Reveal Brief, Script
   Package, Director Package, Voice Package, QA Package, Publishing
   Package, Postmortem Package).
2. `OS-016_Research_Worker.md` was written afterward and needed to
   describe Research Worker's possible inputs. It wrote "Topic or
   Production Package" — a natural, readable English phrase — without
   cross-checking it against OS-013's list. Nothing in the drafting
   process required that check; the eighteen drafts were written as a
   sequence of individually coherent documents, not validated against
   each other as a set. (`docs/drafts/README.md`, written during this
   repository's construction, now documents that these are unratified and
   individually coherent at best — this gap analysis is evidence for why
   that caution belongs there.)
3. The term read naturally enough that it was picked up a second time,
   independently, in the live instruction that asked for the Director
   Worker specification — but used to mean something different: not
   "externally-sourced pre-selection material" (OS-016's apparent sense)
   but "the current, already-in-pipeline bundle a downstream Worker acts
   on" (the sense needed for Director Worker). Two distinct meanings now
   share one informal name, in two different places, neither formally
   defined.
4. The gap stayed invisible through this repository's entire architecture
   phase — skeleton design, the Engine/Runtime/Workers split, Contracts
   being promoted to first-class, and ADR-0001 — because none of that work
   required resolving what any *specific* Worker's inputs concretely are.
   Architecture-level work operates one level of abstraction above this
   question.
5. It became unavoidable only when `SPEC-Director-Worker-v1` was written,
   because an implementation-grade specification's own stated bar —
   "someone else should be able to implement the Worker without making
   architectural decisions" — cannot be met while a required input is a
   colloquial phrase instead of a named, schema-bearing thing. The spec
   didn't introduce the gap. It was the first artifact in this repository
   rigorous enough to be unable to paper over it.

## 3. Alternative architectural solutions

Evaluated against what "Production Package" is actually being asked to
mean in its two observed usages (OS-016's pre-pipeline intake vs. the
Director Worker task's in-pipeline reference bundle):

**A. A new Contract (a tenth entry in OS-013's list).**
Contracts have one owner and are produced by exactly one Worker (OS-013's
Contract Principles). Neither observed usage of "Production Package" has a
single producing Worker: the OS-016 sense comes from outside the Worker
system entirely (no Worker produces it); the Director-stage sense is a
*derived combination* of Script Package plus canonical documents, not
something any Worker generates fresh. Forcing either into a flat Contract
means either inventing a phantom "owner" or violating the one-owner rule
on day one of using it.

**B. A Workspace (folded into Episode Workspace, OS-005).**
Fits the Director-stage sense loosely — that usage is, in effect, "the
readable parts of the current episode workspace." Fits the OS-016 sense
poorly — that usage can precede a workspace's existence (it can be part of
what *causes* a workspace to be created, per OS-016's "Topic or Production
Package" framing as alternative starting points). A single concept can't
sit both inside and logically prior to the container it's supposed to be
folded into.

**C. A Manifest (`engine/manifests/`).**
Fits the Director-stage sense well: manifest-based execution already needs
to describe, for any given Worker invocation, which specific artifact
*versions* it operates on. "Script Package (v3) + Visual Identity (v1) +
Production Playbook (v2)" is exactly a reference bundle, not new content —
which is what a manifest is for. It also composes for free with the
existing invalidation mechanism (OS-007): if a referenced version changes,
downstream is already marked Outdated without the reference bundle itself
needing versioning logic of its own. Does not fit the OS-016 sense at all
— there's nothing yet in the system to reference.

**D. A Composite Artifact (its own bundled, denormalized artifact type).**
Could represent either sense by physically copying/bundling referenced
content into one object. Rejected on inspection: it re-introduces a
synchronization problem that Manifest-by-reference avoids for free — a
Composite Artifact holding a copy of Script Package content would need its
own staleness/versioning logic to detect when its source has moved on,
duplicating what OS-007's graph already does for referenced artifacts.
Doable, but the wrong default given a simpler existing mechanism handles
the same job.

**E. Something else: retire the term; require every specification to name
real Contracts, Canonical documents, or Workspace components directly.**
This is what `SPEC-Director-Worker-v1` §4 already did in practice (defining
"Production Package," for Director Worker's purposes, as "Script Package +
Visual Identity + Production Playbook" and stating explicitly that this is
not a new Contract). It resolves the *symptom* in one document. It does
not resolve the *mechanism gap* from §1 — nothing stops a future document
from coining another ambiguous noun the same way OS-016 did, because the
registry that would catch it (§1a) still wouldn't exist.

## 4. Recommended solution

Two tiers — a systemic fix and a specific one. Neither is implemented by
this document.

**Tier 1 — systemic, addresses §1 directly:**
Populate `engine/contracts/` with the nine Contracts named in OS-013 as
actual schema files (not prose), and adopt a governance rule — a new entry
under `docs/principles/` once populated — that no Worker specification may
reference an artifact-like noun that does not resolve to an entry in
`engine/contracts/`, a document in `canonical/`, or a named component of
the Episode Workspace (OS-005). This turns the check that caught this gap
from "a human happened to notice while writing an unrelated spec" into
something checkable against real, present data.

**Tier 2 — specific, resolves "Production Package" itself:**
The term names two different things and should stop being one term.

- The Director-stage sense (a specific Worker invocation's resolved
  bundle of input Contract *versions*) becomes part of the **Manifest**
  schema (`engine/manifests/`) — Option C. Every manifest entry that
  triggers a Worker run should carry this reference bundle as a defined
  field, not as a bespoke definition re-derived per Worker spec the way
  `SPEC-Director-Worker-v1` §4 currently has to.
- The OS-016 sense (material that precedes the Contract-mediated pipeline
  entirely — comparable to "Topic," which nobody is proposing needs to
  become a Contract either) should stay **deliberately informal**, per
  Option E, but be renamed away from "Production Package" so it stops
  colliding with the now-formalized Director-stage sense. It's a
  legitimate concept — pre-pipeline intake — it just isn't a Contract, a
  Workspace, or a Manifest; it's raw material that hasn't entered the
  typed system yet, structurally different from anything OS-013 governs.

**Direct answer to the five-way question:** Production Package should
become **a field within the Manifest concept** (Option C) for its
in-pipeline sense, and should **not be formalized at all** (Option E,
renamed) for its pre-pipeline sense. It should not become a Contract or a
Composite Artifact, and folding it into Workspace (Option B) doesn't fit
either of its actual usages once they're examined separately.

## 5. Consequences

- `engine/manifests/`'s eventual schema now has a concrete, non-optional
  requirement it didn't clearly have before: an input-reference-bundle
  field. This should be settled before any Worker (Director or otherwise)
  is implemented as a Skill, or every Worker will independently reinvent
  its own version of §4's ad hoc resolution.
- `SPEC-Director-Worker-v1` §4 is now known to be a temporary, local
  resolution rather than a permanent one. It is correct as written today
  (it doesn't contradict anything and the spec explicitly flags it as a
  definition, not a new Contract) but it will need to be revised once the
  Manifest schema exists, to reference that schema instead of restating
  its own bespoke definition. Per this task's instructions, that revision
  is not made now.
- OS-016 is now known to contain an unresolved ambiguity, but as an
  unratified draft (`docs/drafts/`) it is not edited directly — the
  correction belongs in whatever document eventually promotes Research
  Worker's specification out of `docs/drafts/`, informed by this analysis.
- Until Tier 1 is acted on, this exact failure mode — an informal noun
  used in a Worker-facing instruction with no registry to check it
  against — can recur with any other term, for any other Worker. This gap
  analysis closes one instance; it does not close the mechanism that
  produced it.

## 6. Required changes to existing specifications

None are made by this document. If Tier 1 and Tier 2 above are approved,
the following would need to happen (listed for visibility, not executed):

1. Create schema files under `engine/contracts/` for each of OS-013's nine
   Initial Contracts.
2. Define an input-reference-bundle field as part of the (not-yet-written)
   manifest schema in `engine/manifests/`.
3. Add a terminology-governance principle to `docs/principles/` once that
   folder is populated, formalizing the check described in Tier 1.
4. When Research Worker's specification is eventually written (its own
   `SPEC-Research-Worker-v*.md`, not yet created), resolve OS-016's
   "Production Package" phrase explicitly, renamed to avoid collision with
   the now-formalized Director-stage sense.
5. Revise `SPEC-Director-Worker-v1` §4 to reference the Manifest schema's
   input-reference-bundle field once it exists, rather than its current
   local definition — a follow-up spec revision, not part of this
   analysis.

No file other than this one has been created or modified to produce this
analysis.
