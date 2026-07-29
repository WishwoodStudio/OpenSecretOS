# Readiness Assessment 001: Production Package Generator

**Status:** Assessment only — no code, Skills, Workers, or Production
Package generated.
**Reference episode:** Luxury Destruction
**Reference artifact:** `OS_Production_Package_LuxuryDestruction_v2`
**Question:** Does the current repository architecture contain enough
structure to build a deterministic Production Package Generator?

---

## Scope limitation, stated up front

This assessment did not access the actual contents of
`OS_Production_Package_LuxuryDestruction_v2`. Per the standing instruction
not to search for Open Secret files outside the canonical repository root
(`C:\Projects\OpenSecretOS`) without explicit direction, no search was
performed elsewhere for it. A search *within* the repository root found no
trace of it, and `episodes/` contains no workspace for Luxury Destruction:

```
episodes/          → empty except README.md
(no match for "luxury" or "ProductionPackage" anywhere in the repo)
```

This means the assessment below can evaluate **structural readiness** —
whether the architecture has a place for this artifact and a defined
process to produce it — but cannot evaluate **content fidelity**, i.e.
whether that process, once built, would actually reproduce this specific
artifact correctly. That second question is unanswerable without seeing
the artifact, and is out of scope for an architecture-only exercise
regardless.

---

## 1. What information already exists?

- **The term itself is attested, but only loosely.** `docs/drafts/OS-016_Research_Worker.md`
  (since promoted to `workers/research-worker.md`, which resolved this
  exact phrasing per its own "renaming resolved" note — see
  `docs/adr/ADR-0002-Architecture-v1.0-Freeze.md`)
  listed "Topic or Production Package" as alternative Research Worker
  inputs — the only place any source draft uses the phrase.
- **Two prior analyses of this exact gap already exist in the repository:**
  `docs/architecture/Architecture-Gap-Analysis-001.md` (root-caused the
  missing Contract) and this session's evaluation of the Importer
  hypothesis (`External Artifact → Importer → Manifest → Workers →
  Artifacts`) — **but that hypothesis's conclusion has not been written to
  any file.** It exists only as conversational analysis. This is itself a
  finding, addressed in §7.
- **Episode Workspace Specification** (`OS-005`) defines the required
  components of an episode workspace (Metadata, Research, Sources, Reveal
  Brief, Script, Director Package, Voice Package, Assets, QA, Output,
  Postmortem) — a partial model of what an episode's materials look like,
  though it does not name "Production Package" as one unified artifact.
- **Production Contracts** (`OS-013`) defines nine named Contracts and the
  discipline they must follow (one owner, one schema, one lifecycle,
  declared upstream/downstream) — establishing the *rules* a Production
  Package's constituent parts would need to follow, even though Production
  Package itself isn't on that list.
- **`SPEC-Director-Worker-v1.md`** exists as a real implementation-grade
  spec, useful as a template for the shape a future Production Package
  Generator spec would need to take — but it explicitly does not produce
  or consume a Production Package; it consumes Script Package and produces
  Director Package.
- **The repository skeleton itself** — `engine/{contracts,artifacts,graph,manifests}`,
  `runtime/{repository-resolver,context-loader,worker-dispatcher,state-manager}`,
  `workers/`, `episodes/` — exists as scaffolding with documented
  *intended* responsibilities (via README files), but no implementation.

## 2. What information is missing?

- No episode workspace for Luxury Destruction.
- No ratified canonical documents (`canonical/` is empty) — no Visual
  Identity, Production Playbook, Constitution, Decision Log, or Mechanism
  Ladder exists to validate a generated package against.
- No populated Contract schemas in `engine/contracts/` (still prose-only
  inside an unratified draft — the root cause identified in Gap Analysis
  001, still unresolved).
- No Manifest schema in `engine/manifests/`.
- **No Importer concept exists anywhere in the repository as a file** —
  not a folder, not a spec, not even a stub. It exists only in this
  conversation.
- No definition of what fields/sections a "Production Package" actually
  contains — neither the source drafts nor this repository's built
  architecture specify its shape. Only its *name* and *rough function*
  (an external, pre-pipeline bundle) have been discussed.
- No versioning scheme mapping OS-014's abstract "revision creates a new
  version" rule onto a concrete naming convention — nothing in the
  repository explains what distinguishes `_v2` from `_v1`, or what a
  version boundary means for this artifact type.
- No Worker or Runtime component has any implementation to run — every
  relevant folder is an empty scaffold with a descriptive README only.

## 3. Which documents would be loaded?

Two answers, because the loading strategy itself is incomplete:

**What OS-006's Context Loading System actually defines today:** nothing.
OS-006 names six task-type profiles (S9 Review, Reveal Development, Script
Production, Director Package, Voice, QA). "Production Package
generation/import" is not one of them. There is no profile to consult —
this is itself a gap, not just an omission in this report.

**What would plausibly need to be loaded, inferred from adjacent
material** (not an authoritative profile, since none exists):
`OS-005` (Episode Workspace Specification), `OS-013` (Production
Contracts), `OS-016` (Research Worker, the only draft naming this term),
`Architecture-Gap-Analysis-001.md`, and the not-yet-written Importer
decision. Canonical documents (Visual Identity, Production Playbook) would
also be needed to validate output, but don't exist yet to load.

## 4. Which Contracts would participate?

Under the Importer hypothesis (this session's recommended, but unwritten,
conclusion), the Production Package itself is **not** a Contract — it is
external material that would pass through an Importer to produce a
Manifest referencing real Contracts. Depending on what the actual
reference artifact contains (unknown here), the resulting Manifest might
reference Research Package, Reveal Brief, and/or Script Package.

In practice, **none of the nine Contracts can participate in an
enforceable sense today**, because none exist as real schemas —
`engine/contracts/` is empty. Any reference to "the Script Package
Contract participates" is only true at the level of naming, not at the
level of anything that could be checked or validated.

## 5. Which Runtime components would execute?

All four, conceptually — none actually implemented:

| Component | Role in this task | Status |
|---|---|---|
| Repository Resolver | Resolve/create the Luxury Destruction workspace path | Empty scaffold |
| Context Loader | Assemble the (non-existent) profile for this task | Empty scaffold; no profile defined (§3) |
| Worker Dispatcher | Dispatch to the owning Worker | Empty scaffold; **no Worker to dispatch to** (§6) |
| State Manager | Resolve current episode state | Empty scaffold; no state exists — the episode isn't even at "Idea" stage in this repository |

## 6. Which future Worker would own this task?

**Unresolved, and this assessment should not paper over that.**

- Not Director Worker — explicitly scoped away in
  `SPEC-Director-Worker-v1` §3 (consumes Script Package, does not import
  external material).
- Not Research Worker as currently specified — OS-016 lists "Production
  Package" only as an *alternate input* Research Worker might receive, not
  something it generates. Its actual outputs (OS-016) are Research Package
  and Source Log.
- No other Worker in the OS-008 registry claims this responsibility.

More importantly, it's not clear this is a **Worker's** job at all. A
Worker (OS-008) is a specialist exercising editorial/production judgment.
An Importer, as hypothesized in this session, is a deterministic
translation mechanism — closer in kind to the Context Loader (a Runtime
service every Worker depends on) than to a specialist Worker. If that's
correct, the honest answer is: **ownership shouldn't default to "some
Worker" at all — it's an open architectural question whether Production
Package handling belongs to the Runtime layer (as Importer machinery,
analogous to Context Loader) or to a Worker that invokes an Importer as a
tool.** Research Worker is the closest existing candidate by association
(OS-016), but nothing currently on record assigns it this responsibility,
and assigning it by default would be inventing architecture this exercise
was told not to invent.

## 7. What prevents the repository from generating the Production Package today?

In dependency order:

1. No episode workspace exists for Luxury Destruction.
2. No canonical documents are ratified — nothing to validate against.
3. `engine/contracts/` has no populated schemas.
4. `engine/manifests/` has no schema — there is nowhere for an Importer's
   output to land even conceptually.
5. **The Importer concept — this session's own recommended resolution —
   does not exist in the repository as a file.** It is not committed, not
   drafted, not even stubbed. The single most relevant piece of
   architecture for this exact task currently lives only in conversation
   history, which this repository's own philosophy (OS-003's Golden Rule)
   identifies as exactly the failure mode the repository exists to
   prevent.
6. No Runtime component or Worker has any implementation.
7. No Context Loader profile exists for this task type.
8. Ownership (§6) is unresolved.
9. The actual target shape is unknown to this repository — no document
   anywhere describes what fields `OS_Production_Package_LuxuryDestruction_v2`
   actually contains, and this assessment did not have access to it (see
   scope limitation above).

## 8. What is the MINIMUM additional implementation required before this becomes executable?

Ordered by strict dependency, not by effort:

1. **Commit the Importer decision to a real file** (an ADR and/or a
   specification) so it is part of the repository's persisted knowledge
   rather than conversational memory. Nothing below is buildable on a
   decision that doesn't exist yet in writing.
2. **Define a minimal Manifest schema** in `engine/manifests/` — at least
   enough to represent a reference bundle of specific Contract versions,
   since an Importer has nowhere to write its output without this.
3. **Populate the specific Contracts this artifact plausibly touches** in
   `engine/contracts/` (most likely Research Package, Reveal Brief, Script
   Package — not necessarily all nine immediately).
4. **Create the Luxury Destruction episode workspace** under `episodes/`,
   per OS-005's rule that episode material lives nowhere else.
5. **Resolve ownership** (§6) — explicitly decide whether this is Runtime
   machinery or a Worker responsibility, and record the decision.
6. **Define a Context Loader profile** for this task type, per OS-006's
   existing pattern, once ownership is settled.
7. **Write an Importer specification** (a `SPEC-*` document, following the
   template `SPEC-Director-Worker-v1.md` already establishes) — this is
   the actual generator spec, and is explicitly out of scope for this
   assessment.
8. Only after 1–7 does the repository have real (not merely described)
   architecture to attempt reproducing the actual reference artifact —
   and even then, step 7 cannot be written accurately without someone
   who has seen `OS_Production_Package_LuxuryDestruction_v2` supplying its
   real shape, which this assessment was not given.

---

## Bottom line

The repository has the right *surrounding* architecture — Contracts,
Manifests, Runtime components, and Worker registry all have a designated
place waiting for this concept — but has not yet built the specific piece
this task needs (the Importer), has not persisted the decision that this
session already reached about it, and has not resolved who is responsible
for invoking it. The gap is not "missing folders." It is: **one
architectural decision made this session was never written down, and
everything downstream of it is consequently still hypothetical.**
