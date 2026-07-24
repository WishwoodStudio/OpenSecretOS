# SPRINT-001: First Vertical Slice — Production Package → Director Package

**Status:** Planning only. No implementation has been performed.
**Phase:** Implementation Phase (architecture frozen per `SPEC-001`; this
plan implements it, it does not extend it).
**Reference episode:** Demo Episode — a minimal, synthetic episode that
exists solely to exercise the execution path. Content quality is not the
objective; a real episode is deliberately not used for this sprint.
**Governing documents:** `docs/specifications/SPEC-001_Open_Secret_Engine_v1.md`,
`docs/specifications/SPEC-Director-Worker-v1.md`.

Every task below implements something already decided in `SPEC-001` or
`SPEC-Director-Worker-v1`. Where this sprint has to make a choice neither
document settled (e.g., a concrete file format), that choice is called out
explicitly as an *implementation convenience*, not an architectural
decision — none of `SPEC-001`'s five Open Questions are resolved by this
plan or by executing it.

---

## 1. Sprint Goal

Prove that Open Secret Engine can execute one complete production cycle:

```
Production Package → Context Loader → Director Worker → Director Package
```

end-to-end, using the smallest possible Production Package (Script
Package + minimal canonical context, per `SPEC-Director-Worker-v1` §4's
existing definition of that term) that still exercises every step of the
path. This sprint proves the *pipeline shape* works. It does not prove
Director Worker handles real script complexity, and it does not produce
anything publishable — both are explicitly out of scope (see Risks, §9).

## 2. Acceptance Criteria

- A Director Package exists on disk for `episodes/demo-episode/` and
  satisfies every Validation Rule in `SPEC-Director-Worker-v1` §11.
- The Director Package was produced by actually invoking the Repository
  Resolver, State Manager, Context Loader, and Worker Dispatcher
  (`SPEC-001` §8) — not hand-assembled or simulated.
- Exactly two Contracts are populated as real schemas in
  `engine/contracts/`: Script Package and Director Package. No other
  Contract is populated by this sprint.
- `engine/graph/` reflects the new Script Package → Director Package edge
  (`SPEC-001` §12).
- The source Script Package file is byte-identical before and after the
  run (`SPEC-Director-Worker-v1` §11 — "never modify the script").
- No file outside this sprint's task list (§3 below) was modified.
- No decision in `SPEC-001` changed, and none of its five Open Questions
  were resolved as a side effect of implementation choices made here.

## 3. Required implementation tasks

Grouped by concern. Every task is independently implementable, testable,
and committable on its own. Compared to the previous version of this
plan, every task that existed only to source or wait on a real episode's
content has been removed or replaced with a self-contained equivalent —
noted inline as **(changed)**.

### Group A — Fixture bootstrapping (episode-scoped stand-ins for canonical context)

**(revised)** These fixtures do not live in `canonical/` and do not live
in `docs/`. `canonical/README.md` forbids storing anything not ratified
there — confirmed while attempting A1, see the architecture-conflict note
below — and Runtime/Worker code must not depend on anything inside
`docs/`, since that directory is documentation, not working data. Per the
separation established for this sprint (*documentation belongs in
`docs/`; working data belongs in `episodes/`*), both fixtures instead live
under the Demo Episode's own workspace, at
`episodes/demo-episode/fixtures/`. This keeps `canonical/` genuinely
empty until real ratification happens, exactly as its README promises,
and keeps Runtime/Worker dependencies confined to `episodes/`.

**A1. Minimal Visual Identity fixture**
Create `episodes/demo-episode/fixtures/visual-identity.md` with the
smallest content that gives Director Worker's prompt generation
(`SPEC-Director-Worker-v1` §10 step 5) something concrete to cite — a
single camera-language rule is enough. Content quality is explicitly not
the objective this sprint.
*Test:* file exists, is loadable by the Context Loader task (D3).
*Explicitly not* a ratified Canonical document (`SPEC-001` §15) and
explicitly not stored in `canonical/` — a labeled, episode-scoped
placeholder for this sprint only.

**A2. Minimal Production Playbook fixture**
Same treatment as A1, for
`episodes/demo-episode/fixtures/production-playbook.md`.
*Test:* same as A1.

### Group B — Contract schemas (only the two this sprint needs)

**B1. Script Package contract schema**
Create `engine/contracts/script-package.md` defining the concrete shape a
Script Package file must have (scene/beat structure) plus the Artifact
Metadata fields required by `SPEC-001` §19. Unchanged from the previous
plan — this task never depended on which episode it would later apply to.
*Test:* schema is concrete enough that a human could author a conforming
Script Package from it alone.
*Implementation convenience:* Markdown, matching every other document in
this repository.

**B2. Director Package contract schema**
Create `engine/contracts/director-package.md`, defining the composite
structure specified in `SPEC-Director-Worker-v1` §5 and §7. Unchanged.
*Test:* every field `SPEC-Director-Worker-v1` §10 step 6 says must be
populated has a place in this schema.
*Depends on:* none.

### Group C — Demo Episode workspace bootstrapping

**C1. Demo Episode workspace skeleton (trimmed)**
Create `episodes/demo-episode/` with a `metadata.md` file recording
episode ID, title, and current state ("Script Ready", per `SPEC-001`
§16's state machine). **(changed: create only `script/` and
`director-package/` — the other required components named in `SPEC-001`
§16 (`research/`, `sources/`, `reveal-brief/`, `assets/`, `qa/`,
`output/`, `postmortem/`) add nothing to proving this path and are
dropped from this sprint. Full OS-005 compliance for a workspace's shape
is deferred to whichever sprint first runs a real episode.)**
*Test:* workspace exists; `metadata.md` correctly reports "Script Ready."

**C2. Author a minimal synthetic Script Package (changed: no longer blocked)**
Write a deliberately small Script Package directly into
`episodes/demo-episode/script/script-package.md` — two shots is enough to
exercise shot-list derivation, one continuity element shared across both
shots to exercise continuity-note derivation, and one asset referenced by
a shot to exercise asset-manifest derivation. Content is invented for this
sprint; it does not need to resemble real Open Secret material.
*Test:* file conforms to the B1 schema; State Manager (D2) reads it and
reports "Script Ready."
*No external dependency.* This replaces the previous plan's Task C2,
which required sourcing real content from outside the repository and was
this sprint's single blocking risk. That blocker no longer exists.

### Group D — Minimal Runtime implementation

**D1. Repository Resolver**
Unchanged from the previous plan — implement a small module that resolves
any relative path against the canonical repository root, per `SPEC-001`
§8's Repository Resolver subsection.
*Test:* resolves correctly regardless of the invoking process's current
working directory.
*Depends on:* none.

**D2. State Manager**
Unchanged. Implement a small module that reads an episode's `metadata.md`
(C1) and reports its current state.
*Test:* given C1's workspace, correctly reports "Script Ready."
*Depends on:* C1, D1.

**D3. Context Loader — Director Package profile only**
Unchanged. Implement the single profile named in `SPEC-001` §13.
*Test:* given A1, A2, C1, C2 all present, returns exactly those four
documents and nothing else.
*Depends on:* A1, A2, C1, C2, D1.

**D4. Minimal Manifest schema + one manifest entry**
Unchanged in mechanism — define a minimal shape in `engine/manifests/`
and create one concrete manifest entry referencing this sprint's Script
Package version and the fixture versions.
*Test:* the manifest entry unambiguously identifies every input this run
depends on.
*Depends on:* B1, B2.
*Explicitly out of scope:* a general Importer (`SPEC-001` Open Question 1
remains open).

**D5. Worker Dispatcher (minimal)**
Unchanged. Reads a manifest entry (D4) and invokes Director Worker (E1)
with the context assembled by D3.
*Depends on:* D3, D4.

**D6. Minimal Production Graph schema + update**
Unchanged. Define a minimal shape in `engine/graph/` sufficient to record
one edge and mark it satisfied after a successful run.
*Depends on:* B2.

### Group E — Director Worker implementation

**E1. Director Worker as a Claude Skill**
Unchanged. Implement `.claude/skills/director-worker/`, following
`SPEC-Director-Worker-v1` §10 exactly.
*Test:* given a conforming Script Package (C2) and loaded context (D3),
produces a Director Package matching the B2 schema.
*Depends on:* B1, B2, D3.

**E2. Validation Rules**
Unchanged. Implement `SPEC-Director-Worker-v1` §11 as automated checks.
*Test:* a deliberately malformed Script Package causes the correct
Validation Rule to fail, not a silent pass.
*Depends on:* E1.

**E3. Failure condition handling**
Unchanged. Implement `SPEC-Director-Worker-v1` §12's failure conditions as
explicit early exits.
*Test:* each failure condition, triggered individually, halts without
writing a Director Package.
*Depends on:* E1.

### Group F — End-to-end wiring and proof (changed: merged)

**F1. Wire the pipeline and run it against the Demo Episode**
Connect D1 → D2 → D3 → D4 → D5 → E1 into one runnable sequence matching
`SPEC-001` §7 (Execution Model) steps 2–11, and execute it against C2's
content in the same task. **(changed: the previous plan split this into
"wire against a stub" (F1) and "run against real content" (F2), because
real content was a separately-blocked resource arriving later. Since C2 is
now already the minimal, self-contained input, that distinction no longer
means anything — there is only one run to prove.)**
*Test:* all Acceptance Criteria (§2) are met.
*Depends on:* D1–D6, E1–E3, C2.

## 4. Task dependencies

```
A1 ─┐
A2 ─┼─→ D3 ─→ D5 ─┐
C1 ─┼─→ D2         │
C2 ─┘              │
              D4 ──┤
B1 ─┬─→ D4          ├─→ F1
B2 ─┼─→ D4, D6      │
    └─→ E1          │
D1 ─────────────────┘
E1 ─→ E2, E3 ────────→ F1
```

No task in Group D, E, or F can complete before its Group A/B/C
prerequisites exist. There is no longer a critical-path blocker outside
this repository — every task can be completed by implementation work
alone.

## 5. Expected artifacts

- `episodes/demo-episode/` — populated workspace (metadata, script,
  director-package only — see C1)
- `episodes/demo-episode/director-package/director-package.meta.json`,
  `shot-list.md`, `asset-manifest.md`, `prompts/higgsfield/`,
  `prompts/hyperframes/` — per `SPEC-Director-Worker-v1` §5
- One manifest entry in `engine/manifests/`
- One graph edge in `engine/graph/`
- A log entry for the run (`SPEC-Director-Worker-v1` §17)

## 6. Files to create

```
episodes/demo-episode/fixtures/visual-identity.md        (A1)
episodes/demo-episode/fixtures/production-playbook.md     (A2)
engine/contracts/script-package.md                      (B1)
engine/contracts/director-package.md                    (B2)
episodes/demo-episode/metadata.md                        (C1)
episodes/demo-episode/script/script-package.md            (C2)
runtime/repository-resolver/resolver.mjs                 (D1)
runtime/state-manager/state-manager.mjs                  (D2)
runtime/context-loader/director-package-profile.mjs       (D3)
engine/manifests/{schema.md, demo-episode-director-001.md} (D4)
runtime/worker-dispatcher/dispatcher.mjs                  (D5)
engine/graph/{schema.md, demo-episode.md}                  (D6)
.claude/skills/director-worker/SKILL.md                   (E1)
.claude/skills/director-worker/scripts/*.mjs               (E1, E2, E3)
episodes/demo-episode/director-package/*                   (F1 output)
```

*Implementation convenience:* `.mjs` (Node.js) is proposed for runtime and
Skill logic, matching the only precedent already present in this
environment and the fact that Node.js is already installed on this
machine. A scripting-language choice, not part of the Engine's
architecture.

## 7. Runtime components involved

Repository Resolver, State Manager, Context Loader (Director Package
profile only), Worker Dispatcher — the four named in `SPEC-001` §8. No
Human Gate fires in this sprint: per `SPEC-001` §18, Director Package sits
between Script Lock (assumed passed for the demo script) and Final QA
(out of scope — this sprint stops at Director Package).

## 8. Contracts involved

Script Package (consumed) and Director Package (produced) — the only two
named in `SPEC-Director-Worker-v1` §6/§7. The other seven Contracts named
in `SPEC-001` §10 are untouched by this sprint.

## 9. Risks

- **This sprint proves mechanism, not content-readiness.** A synthetic
  two-shot script cannot exercise everything a real episode's script
  would (long continuity chains, many scenes, ambiguous beats). Passing
  this sprint proves the pipeline shape works; it does not mean Director
  Worker is ready for a real episode. A follow-up sprint against a real
  episode is still required before Director Worker is considered
  production-ready, and should be scoped separately once this one is
  done.
- **Fixtures are not real canonical content.** The Director Package this
  sprint produces is validated against placeholder Visual
  Identity/Playbook fixtures living under
  `episodes/demo-episode/fixtures/` (A1, A2), not ratified documents from
  `canonical/`. Must not be mistaken for a publishable artifact.
- **Determinism is asserted, not yet verified.** `SPEC-Director-Worker-v1`
  §2 requires deterministic output, but E1's implementation, if it uses an
  LLM for prompt-language generation, may not produce byte-identical
  output across runs even when the underlying shot structure stays fixed.
  Whether "deterministic" needs to mean byte-identical or just
  structurally-repeatable is a real implementation question worth
  surfacing in review, not something this plan resolves.
- **Ad hoc file formats.** B1, B2, D4, and D6 each make a small,
  unavoidable format choice that `SPEC-001` deliberately left
  unspecified. None require an ADR individually, but if a second Worker's
  implementation makes incompatible choices, reconciling them later is
  real (if small) rework.
- **Scope creep.** Every Group D task is deliberately minimal — a
  temptation exists to build general-purpose infrastructure (a real
  Importer, all nine Contracts, a full Manifest system) while already in
  the code. Doing so would silently resolve `SPEC-001`'s Open Questions
  through implementation rather than through evidence.

## 10. Definition of Done

- [ ] Every task in §3 is committed separately, in dependency order.
- [ ] `episodes/demo-episode/director-package/` contains a complete
      Director Package (shot list, continuity notes, asset manifest, both
      prompt packages).
- [ ] Every `SPEC-Director-Worker-v1` §11 Validation Rule passes for this
      run.
- [ ] `engine/graph/` shows the Script Package → Director Package edge as
      satisfied, plus Director Package's own declared downstream edges.
- [ ] The manifest entry that triggered the run records its result.
- [ ] A log entry exists for the run.
- [ ] The source Script Package file is verified byte-identical
      before/after the run.
- [ ] Visual Identity/Playbook fixtures live under
      `episodes/demo-episode/fixtures/`, not in `canonical/` or `docs/`,
      and are clearly marked as non-ratified placeholders.
- [ ] No file outside this sprint's task list was modified.
- [ ] None of `SPEC-001`'s five Open Questions were resolved, implicitly
      or explicitly, by any implementation choice made in this sprint.
- [ ] If any of the above is not true, the sprint is not Done — it is
      Blocked, and the specific blocker is what's reported, not a partial
      success framed as complete.
