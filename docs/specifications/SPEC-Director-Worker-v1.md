# SPEC: Director Worker (v1)

**Status:** Draft — implementation specification, not yet a Claude Skill
**Spec ID:** SPEC-Director-Worker-v1
**Owner Worker:** Director Worker
**Source documents:** OS-001, OS-002, OS-004, OS-005, OS-006, OS-007,
OS-008, OS-009, OS-010, OS-013, OS-014, OS-015, OS-017, OS-018

This document is the complete implementation specification for the
Director Worker. It is written so that someone else can implement the
future Claude Skill without making any architectural decision of their
own — every decision below is either drawn directly from an existing
architecture draft (cited inline) or is an implementation-level detail
required to make those drafts concrete, explicitly flagged as such.

Where a decision would require inventing architecture that belongs to a
different component's own specification (the schema of `engine/manifests/`
or `engine/graph/`, for example), this document states Director Worker's
*obligation* toward that component and marks the component's internal
schema as out of scope, rather than inventing it here.

---

## 1. Mission

Convert an approved Script Package into a complete, deterministic
production package — the shot-by-shot plan, tool-ready prompts, camera
language, continuity notes, and asset requirements needed to move an
episode from Direction into Production (OS-018, OS-005).

Colloquially: Director Worker transforms an approved Production Package
(concretely: the Script Package plus required canonical context) into
deterministic production artifacts. It does not originate content — it
translates an already-locked script into instructions concrete enough for
Integrations and human production staff to execute without further
interpretation.

## 2. Responsibilities

- Read the approved Script Package and derive a shot-by-shot plan (OS-018).
- Generate camera language and continuity notes per shot (OS-018).
- Generate tool-ready AI Prompt Packages, one set per target integration
  (Higgsfield for video/camera, HyperFrames for image/keyframe) (OS-018,
  OS-007, OS-009).
- Generate an Asset Manifest describing every asset the shot list requires
  (OS-018, OS-007).
- Assemble the above into the single Director Package contract (OS-013)
  and write it into the episode's workspace (OS-005).
- Follow Visual Identity in every generated prompt and camera decision
  (OS-018).
- Produce artifacts deterministically: the same Script Package, Visual
  Identity, and Production Playbook must yield the same shot structure,
  continuity notes, and asset requirements on every run (OS-018 — "Generate
  deterministic production artifacts").
- Update the Production Graph and manifest state to reflect that the
  Director Package now exists and what it produces downstream (OS-007,
  OS-010 — "every meaningful action creates or updates an artifact").

## 3. Explicit non-responsibilities

Director Worker does **not**:

- Write or rewrite scripts. It consumes the Script Package as immutable
  input (OS-018 — "Never modify the script").
- Perform research. Research Package is Research Worker's output and is
  only read, never generated, by Director Worker (OS-016, OS-008).
- Make editorial decisions. Reveal framing, script content, and narrative
  judgment belong to Editorial Worker and the human (OS-017, OS-015).
- Define project rules or own the production pipeline. Per OS-008, Workers
  are specialists, never pipeline owners.
- Call Integration APIs directly to generate final media. It produces
  tool-ready prompt packages; actual generation is a separate runtime step
  that invokes Higgsfield/HyperFrames using Director Worker's output as
  their input artifact (OS-009 — see §14).
- Finalize approval decisions. Like every Worker, it prepares artifacts for
  review; only a human finalizes an approval gate (OS-015 — "Workers
  prepare decisions. They do not finalize them.").
- Bypass or edit Canonical Knowledge. It reads Visual Identity and
  Production Playbook but never writes to `canonical/` (OS-010 — "Never
  bypass Canonical Knowledge," "Never edit Canonical documents directly").
- Decide what context to load. Context assembly is the Context Loader's
  responsibility, not the Worker's (OS-006 — "Workers never decide what to
  load.").
- Invent visual or narrative facts not present in the Script or Visual
  Identity. Atmosphere may be AI-generated; information must come from
  real artifacts (OS-018 — "AI generates atmosphere. Real artifacts carry
  information.").

## 4. Inputs

| Input | Kind | Source |
|---|---|---|
| Script Package | Production Contract | `episodes/<episode-id>/script/` — produced by Editorial Worker, must be in Script-Locked / Approved state (OS-015, OS-017) |
| Visual Identity | Canonical document | `canonical/` (once ratified) |
| Production Playbook | Canonical document | `canonical/` (once ratified) |
| Current Episode Workspace state | Operational context | `episodes/<episode-id>/` — episode metadata and any prior artifacts needed for continuity |

"Production Package," as used loosely in this system's earlier drafts
(OS-016), resolves concretely for Director Worker to: **the approved
Script Package plus the required canonical context (Visual Identity,
Production Playbook)**. This is not a new Contract — it is this
specification's precise definition of the informal term, so that it does
not get reinterpreted differently by whoever implements the Skill.

## 5. Outputs

Per OS-018, Director Worker's output is a shot-by-shot plan, tool-ready
prompts, camera language, continuity notes, and asset requirements. These
are produced as one composite artifact — the Director Package — with the
following internal structure:

```
episodes/<episode-id>/director-package/
├── director-package.meta.json     (Artifact Specification metadata, §6/§14 of OS-014)
├── shot-list.md                   (shot-by-shot plan, camera language, continuity notes)
├── asset-manifest.md              (every asset the shot list requires)
└── prompts/
    ├── higgsfield/                (tool-ready video/camera prompts, one file per shot)
    └── hyperframes/               (tool-ready image/keyframe prompts, one file per shot)
```

This directory layout is an implementation-level detail of this spec, not
a new top-level repository decision — it lives entirely inside the
episode workspace location `episodes/<episode-id>/` already designated for
the Director Package by OS-005.

## 6. Production Contracts consumed

Per OS-013's Initial Contracts list, exactly one formal Contract is read:

- **Script Package** — must exist, must be in an Approved/Locked state
  (post "Script Lock" human gate, OS-015). Director Worker treats it as
  immutable.

Visual Identity and Production Playbook are Canonical documents, not
Production Contracts — they are read as canonical context, not as typed
inter-Worker artifacts (OS-013 vs OS-004).

## 7. Production Contracts produced

Exactly one formal Contract is produced, per OS-013's Initial Contracts
list:

- **Director Package** — a composite artifact bundling Shot List,
  Continuity Notes, Asset Manifest, and AI Prompt Packages (subdivided by
  target integration: Higgsfield, HyperFrames). OS-018 lists these as
  things Director Worker "Owns"; OS-007's Production Graph shows them as
  what "Director Package produces" downstream. This spec treats them as
  one Contract with defined internal parts (§5), rather than as separate
  top-level Contracts, so that Director Package retains "one owner, one
  schema, one lifecycle" (OS-013 Contract Principles).

Declared per OS-013's contract principles:

- **Upstream dependency:** Script Package
- **Downstream consumers:** Voice Worker and QA Worker do not consume
  Director Package directly per OS-007's graph (Voice Package derives from
  Script independently); QA Worker consumes Director Package as part of
  "all production artifacts" (OS-008) for Final QA. The Higgsfield and
  HyperFrames integrations consume the Director Package's prompt packages
  as their input artifact during the Production stage (OS-009, §14).

## 8. Context Loader profile

Per OS-006's explicit "Director Package" loading strategy, the Context
Loader must assemble exactly:

- Visual Identity
- Production Playbook
- Current Script (the episode's Script Package)
- Current Workspace (the episode's workspace state)

Director Worker must not load anything beyond this profile itself — context
assembly is the Context Loader's responsibility (`runtime/context-loader/`),
not the Worker's (OS-006). If Director Worker finds it needs a document
outside this profile to do its job, that is a signal the profile itself
needs to be revised (a Context Loader change), not that the Worker should
read the document directly.

## 9. Runtime execution sequence

Specializes OS-010's general runtime flow for a Director Worker
invocation, using the four named runtime components built in this
repository (`runtime/repository-resolver/`, `runtime/context-loader/`,
`runtime/worker-dispatcher/`, `runtime/state-manager/`):

1. **Receive request** — a request to direct a specific episode (by
   episode ID) arrives at the runtime.
2. **Resolve current production state** (State Manager) — confirm the
   episode's status is at or past "Script Ready" per OS-005's state
   machine, and that Script Package is in Approved/Locked state (OS-015).
   If not, halt (§12).
3. **Resolve paths** (Repository Resolver) — resolve the episode workspace
   path and canonical document paths against the repository root; never
   infer or assume a working directory (per this repository's own
   operating rule and OS-010's "never infer repository structure").
4. **Load context** (Context Loader) — assemble exactly the profile in §8.
5. **Dispatch** (Worker Dispatcher) — invoke Director Worker with the
   loaded context.
6. **Run the artifact generation pipeline** (§10).
7. **Validate output** (§11). If validation fails, do not persist as
   Approved; follow §12/§18.
8. **Persist outputs** — write the Director Package to
   `episodes/<episode-id>/director-package/` (§5).
9. **Update manifest and graph state** (§15, §16).
10. **Log the run** (§17).
11. **Report next available actions** — per OS-010 step 8, e.g. surface
    that the episode is now eligible for the Production stage.

## 10. Artifact generation pipeline

Internal sequence once context is loaded (step 6 above). Each stage is
deterministic given the same inputs (OS-018):

1. **Parse** the Script Package into scenes/beats.
2. **Derive the Shot List** — one shot-by-shot plan entry per beat,
   including camera language, sourced from script structure plus Visual
   Identity's camera/visual rules. This is a rule-driven derivation, not
   free interpretation.
3. **Derive Continuity Notes** — cross-shot continuity constraints (recurring
   subjects, locations, props, lighting continuity) tracked across the
   shot list.
4. **Derive the Asset Manifest** — every asset (existing or to-be-generated)
   the shot list requires, cross-referenced against `assets/` for
   already-available shared assets before assuming new generation is
   needed.
5. **Generate AI Prompt Packages** — for each shot, produce a tool-ready
   prompt for the applicable integration (Higgsfield for video/camera
   shots, HyperFrames for image/keyframe shots), constrained by Visual
   Identity. Per OS-018's rule, AI may generate the atmospheric language
   inside a prompt; it may not invent the information the prompt encodes
   (subject, action, continuity constraints) — that information must trace
   back to the Script Package or Visual Identity.
6. **Assemble** shot list, continuity notes, asset manifest, and prompt
   packages into the Director Package structure (§5), with metadata
   populated per OS-014's Artifact Specification (Artifact ID, Episode ID,
   Version, Status, Owner Worker = Director Worker, Input Dependencies =
   Script Package, Output Consumers = QA Worker + Higgsfield/HyperFrames
   integrations, Last Updated, Approval State).

## 11. Validation rules

Before a Director Package may be persisted with Status = Generated (OS-014):

- Script Package input must be unchanged on disk at the end of the run
  (byte-for-byte) — enforces "never modify the script" (OS-018).
- Every shot in the Shot List must reference a valid beat in the source
  Script Package (no orphaned shots).
- Every asset in the Asset Manifest must be referenced by at least one
  shot (no unused asset requirements).
- Every generated prompt must declare which Visual Identity rule(s) it
  follows, or explicitly note none applied (traceability, not invention).
- Director Package metadata must satisfy OS-014's required Artifact
  Metadata fields in full — a Director Package missing any required field
  is invalid.
- Output must not include any field or content that only Canonical
  documents may define (i.e., the Worker cannot invent a new visual rule
  not present in Visual Identity; it must cite the existing rule or defer).

## 12. Failure conditions

Director Worker must halt without producing a persisted Director Package
if:

- Script Package does not exist, or exists but is not in an
  Approved/Locked state (Script Lock gate not yet passed, OS-015).
- Visual Identity or Production Playbook cannot be resolved (not yet
  ratified in `canonical/`, or path resolution fails).
- The episode's current state (per State Manager) precedes "Script Ready"
  in OS-005's state machine.
- Any Validation Rule in §11 fails.
- The Repository Resolver cannot resolve paths against the canonical
  repository root (per this repository's path-resolution rule).

On any failure condition, no artifact is written as Generated/Approved;
see §18 for recovery behavior.

## 13. Human approval gates

Per OS-015, the five named Human Gates are Episode Selection, Reveal,
Script Lock, Final QA, and Publication. **Director Package is not itself
one of these five gates** — this specification does not invent a sixth.

Two human checkpoints bound Director Worker's execution instead:

- **Upstream:** Script Lock must already be passed before Director Worker
  may run at all (§4, §12) — this is the human's approval of the input,
  not of Director Worker's output.
- **Downstream:** Final QA is the human gate at which Director Package's
  correctness is ultimately checked, as part of "all production artifacts"
  that QA Worker consumes (OS-008).

Between those two gates, Director Package still passes through the general
artifact lifecycle from OS-014 (Draft → Generated → Reviewed → Approved).
"Reviewed" here is satisfied by passing §11's Validation Rules — an
automated, deterministic check performed by the Worker itself, not a named
Human Gate. This specification does not treat automated validation as
equivalent to human approval; it only advances the artifact from Generated
to Reviewed, never to Approved. Approved status for a Director Package is
only reached transitively, once Final QA passes.

## 14. Integration points

Director Worker does not call Higgsfield or HyperFrames directly (§3). It
produces prompt packages structured to be consumed as the *input artifact*
in a later Integration Contract invocation (OS-009):

- **Higgsfield** — receives the Higgsfield Prompt Package (video/camera
  shots) as its input artifact during the Production stage; responsible
  for video generation and camera execution (OS-009).
- **HyperFrames** — receives the HyperFrames Prompt Package (image/keyframe
  shots) as its input artifact during the Production stage; responsible
  for image generation and keyframe creation (OS-009).

Per the Integration Contract (OS-009), each integration returns a
generated artifact, metadata, an execution log, and failure state — all
consumed by a later Production-stage step, not by Director Worker. No
business logic for either integration lives inside Director Worker or
inside `integrations/`.

## 15. Manifest updates

`engine/manifests/` owns manifest-based execution; its internal schema is
that component's own specification and is out of scope here. Director
Worker's obligation toward it:

- Director Worker's invocation must be describable as a manifest entry
  (what should run, for which episode) before execution begins.
- On completion (success or failure), Director Worker must report its
  execution result back to the manifest record that triggered it, so the
  manifest reflects whether the run produced a valid Director Package.
- Director Worker must not silently run outside of a manifest-tracked
  invocation — every run is traceable to a manifest entry (supports OS-010
  — "every meaningful action creates or updates an artifact").

## 16. Production Graph updates

`engine/graph/` owns the production graph's internal schema, out of scope
here. Director Worker's obligation toward it, per OS-007:

- On successful completion, mark the Script → Director Package edge as
  satisfied.
- Register Director Package's own downstream edges: Director Package →
  Higgsfield Prompts, Director Package → HyperFrames Prompts, Director
  Package → Asset Manifest (per OS-007's stated graph).
- Director Worker does not itself need to handle invalidation propagation
  — that is the graph's automatic behavior (OS-007's Core Rule: an
  upstream change marks dependents Outdated). Director Worker only needs
  to correctly register what it consumed and what it produced.

## 17. Logging

Exact log schema belongs to the runtime's own specification and is out of
scope here. Director Worker's obligation: every invocation must log at
minimum the episode ID, Script Package version consumed, start/end time,
Validation Rule results (§11), final artifact state reached, and — on
failure — which Failure Condition (§12) was hit. This mirrors what the
Integration Contract already requires of integrations (an execution log
per invocation, OS-009), applied consistently to the Worker itself.

## 18. Error recovery

- A failed run (any §12 condition) must not leave a Director Package in
  Generated, Reviewed, or Approved state. If a partial artifact was
  written during the pipeline, it must be marked Draft or removed, never
  left ambiguous.
- A failed run must not update the Production Graph as though it
  succeeded (§16 updates only occur after §11 validation passes).
- A failed run is not automatically retried by the Worker itself; retry is
  a runtime/manifest-level decision (OS-010's flow, "report next available
  actions" — a failed Director Worker run reports that Direction remains
  outstanding, not that it will retry unprompted).
- If Script Package changes after a Director Package was already
  Generated/Approved, the existing Director Package becomes Outdated per
  OS-015's automatic invalidation rule ("If Script changes: Director
  Package → Outdated"). Director Worker does not need special logic for
  this — it is the graph's behavior — but a subsequent Director Worker run
  against the new Script Package must treat the prior Director Package as
  superseded, not silently overwrite it (OS-014 — revision creates a new
  version rather than overwriting history).

## 19. Definition of Done

A Director Worker run is complete when all of the following hold:

- [ ] Script Package was read but not modified (byte-identical before/after).
- [ ] Shot List, Continuity Notes, Asset Manifest, and both Prompt Packages
      exist under `episodes/<episode-id>/director-package/` per §5.
- [ ] All §11 Validation Rules pass.
- [ ] Director Package metadata satisfies OS-014's required fields in full.
- [ ] Director Package reaches at least "Reviewed" status (§13); "Approved"
      is out of scope for this Worker and occurs only via Final QA.
- [ ] The manifest entry that triggered the run is updated with the result
      (§15).
- [ ] The production graph reflects the new Director Package node and its
      declared downstream edges (§16).
- [ ] A log entry exists for the run (§17).
- [ ] If any condition above was not met, the run is not Done — it is
      Failed, per §12/§18, and no Director Package is left in a state that
      claims otherwise.

## 20. Future Skill mapping

This specification is what `.claude/skills/director-worker/` must
implement once Skills are authorized (per this repository's own
`.claude/README.md` and `workers/README.md`, which state that Worker
implementation — including prompt content — belongs there, not in
`workers/` or `engine/`).

Suggested (non-binding, implementation-level) mapping for whoever builds
the Skill:

| Spec section | Skill responsibility |
|---|---|
| §8 Context Loader profile | The Skill's declared required-context inputs |
| §10 Artifact generation pipeline | The Skill's main procedure |
| §11 Validation rules | The Skill's self-check before returning |
| §12 Failure conditions | The Skill's precondition checks / early exits |
| §15, §16 | Calls the Skill must make into the manifest/graph systems |
| §17 | The Skill's logging calls |

This mapping does not authorize building the Skill. It only records where
each part of this specification is expected to land once building it is
authorized.
