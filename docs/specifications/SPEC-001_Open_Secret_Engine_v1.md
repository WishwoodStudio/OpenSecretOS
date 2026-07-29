# SPEC-001: Open Secret Engine (v1)

**Status:** Consolidated specification — documents architecture already
established; introduces no new architecture.
**Purpose of this document:** the single source of truth for what has
been decided about Open Secret Engine as of this session. Every statement
below is either already written in a repository document or was reached
through architecture review conducted during this session and is being
recorded here for the first time, per this repository's own rule that
nothing important may live only in conversation (OS-003's Golden Rule).
Nothing in this document is new architecture — where a real decision is
still open, it is listed in **Open Questions**, not resolved here.

**Source key**, used throughout:
- *Repository document* — an existing file in this repository (a draft, a
  spec, a README).
- *ADR* — `docs/adr/ADR-0001-Initial-Repository-Architecture.md`.
- *Architecture Review* — reasoning conducted and concluded during this
  session (Gap Analysis 001, the Importer-hypothesis evaluation, the
  Director Worker specification, the Readiness Assessment), captured here
  because it previously existed only in conversation.
- *Production evidence* — observed outcomes from real production runs.
  **Not cited anywhere in this document** — no episode has yet been
  produced, so no production evidence exists yet. This is itself recorded
  under Current Known Gaps.

## What is Open Secret Engine?

Open Secret Engine is the production operating system for Open Secret's
media business — not the repository that stores it, but the operating
discipline the repository encodes. It is the set of rules by which
production work is planned, executed, and tracked: Workers exchange only
typed Contracts, execution is driven by Manifests, dependencies are
tracked as a Production Graph, and every meaningful action produces or
updates a versioned artifact — all orchestrated by a Runtime that
determines what happens next from current production state rather than
conversation history, and all subject to a human Editor-in-Chief's final
authority.

---

## 1. Vision

**Decision:** Open Secret Engine exists to turn Open Secret's production
process from a collection of prompts and documents into an operating
system — one where the repository itself, not chat history, can answer
what is true, what is happening, and what should happen next. Automation
is a consequence of this, not the objective; the objective is to automate
deterministic production work while preserving human editorial control
over strategic and creative decisions.

**Rationale:** A repository that depends on conversational memory cannot
be resumed correctly after time has passed, and cannot scale past one
person's recall of prior decisions.

**Source:** Repository document (`docs/drafts/OS-001_OpenSecretOS_Vision_and_Design_Principles.md`).

**Decision:** The system's Core Principle: the repository is the
operating system; Claude Code (or whichever AI runtime is in use) is the
runtime that executes it; canonical documents define behavior; Skills
execute specialized work; external tools provide capabilities; the human
remains Editor-in-Chief.

**Rationale:** Same source as above — this is the layering that makes
"automation without losing human authority" concrete.

**Source:** Repository document (OS-001).

**Note on naming:** the source drafts refer to the system as "Open Secret
OS." The repository as actually built refers to itself as "Open Secret
Engine" (its own root `README.md`). Both names refer to the same system;
this document uses "Open Secret Engine" throughout, matching the
repository's current self-description.

**Source:** ADR (repository naming as constructed).

## 2. Scope

**Decision:** In scope, as already built or specified: the repository's
top-level architecture (Engine, Runtime, Workers, `.claude/`, Canonical
Knowledge, `docs/`, Episode Workspaces, Integrations, Assets, Output,
Archive); a Contract-mediated communication discipline between Workers; a
manifest-based execution model; a production-graph dependency model; a
Context-Loader-based context assembly discipline; a Worker registry; and
one fully-specified Worker (Director Worker) demonstrating the
implementation-specification format future Workers will follow.

**Rationale:** This is the set of decisions that has actually been made
and recorded, as opposed to implied or assumed.

**Source:** ADR; Architecture Review (this session's construction work).

**Decision:** Explicitly not yet in scope: any Claude Skill
implementation, any ratified Canonical document, any real episode
production, and any populated Contract, Manifest, or Production Graph
schema (all exist only as empty scaffolding today).

**Rationale:** Repeated explicit instruction throughout this session drew
this line consistently (do not create Skills, do not create CLAUDE.md, do
not implement Workers); recording it here makes the boundary a documented
fact rather than an inferred one.

**Source:** Architecture Review (this session).

## 3. Non-goals

**Decision:** Open Secret Engine does not replace human judgment; the
human remains Editor-in-Chief and sole authority over editorial and
investment decisions.

**Source:** Repository document (OS-001).

**Decision:** Workers never own the production pipeline and never define
project rules — they are specialists that consume canonical knowledge and
produce artifacts, nothing more.

**Source:** Repository document (`docs/drafts/OS-008_Worker_Architecture.md`).

**Decision:** No repository-level `prompts/` directory exists. Worker
prompt content, once Workers are implemented as Skills, is that Skill's
own implementation detail and lives under `.claude/skills/`, not as a
standalone repository artifact.

**Rationale:** A separate top-level prompts directory would create two
possible places defining "how a Worker behaves," with no principled rule
for which one wins — an ambiguity judged not worth the folder.

**Source:** ADR.

**Decision:** The Engine does not consume external/raw production
material directly.

**Rationale:** Established during this session's architecture review as
the resolution to the "Production Package" gap (see §10, §11, §21) — kept
brief here as a non-goal statement; the full reasoning is under Manifest
and Current Known Gaps.

**Source:** Architecture Review (this session).

## 4. Engineering Principles

**Decision:** Repository First — the repository is the single source of
truth; external stores (e.g. Google Drive) become archive; any AI client's
own project instructions are bootstrap only, not a knowledge store.

**Source:** Repository document (OS-001).

**Decision:** Knowledge Before Execution — behavior originates from
canonical documents; nothing is improvised as project rule.

**Source:** Repository document (OS-001).

**Decision:** Load Only What Is Required — context is assembled
dynamically per task; reading the full repository by default is
prohibited.

**Source:** Repository document (OS-001; elaborated in OS-006).

**Decision:** Deterministic Before Intelligent — repeatable behavior is
represented as rules; reasoning is reserved for genuinely editorial work.

**Source:** Repository document (OS-001).

**Decision:** One Responsibility — every Skill (and, as applied during
this session, every repository component) owns one responsibility; no
component owns the complete pipeline.

**Rationale:** This principle was the specific justification, during this
session, for separating Contracts from Artifacts and for splitting Runtime
into four named components rather than one undifferentiated folder.

**Source:** Repository document (OS-001); ADR.

**Decision:** Everything Becomes an Artifact — nothing important lives
only in chat history.

**Rationale:** This principle is the direct justification for this
document's own existence: it exists specifically to move decisions that
were made in conversation into the repository.

**Source:** Repository document (OS-001); ADR.

**Decision:** Production State Drives Execution — the repository's current
state determines the next action, not chat history.

**Source:** Repository document (OS-001; elaborated in OS-005's state
machine).

**Decision:** Replaceable Automation — every external tool, and by
extension every AI runtime, must be replaceable without redesigning the
system.

**Rationale:** This is the specific principle behind keeping `engine/`
provider-agnostic and isolating Claude-specific implementation under
`.claude/`.

**Source:** Repository document (OS-001); ADR.

**Decision:** Human Authority — editorial and investment decisions always
belong to the human.

**Source:** Repository document (OS-001).

## 5. Repository Architecture

**Decision:** The repository is organized around ten top-level concepts:
`engine/`, `canonical/`, `episodes/`, `workers/`, `runtime/`, `.claude/`,
`docs/`, `integrations/`, `assets/`, `output/`, `archive/`.

**Rationale:** Each directory maps to one production responsibility;
empty directories were avoided unless a specific named requirement
justified them (documented per-directory in each directory's own
`README.md`).

**Source:** ADR; repository document (root `README.md` and each
directory's `README.md`).

**Decision:** `docs/` is subdivided into `drafts/` (unratified source
material — currently the eighteen original architecture drafts, `OS-001`
through `OS-018`), `architecture/`, `specifications/`, `adr/`, and
`principles/`.

**Rationale:** Distinguishes prose *about* the system (docs) from the
system's actual structure (engine/runtime/workers), and distinguishes
ratified from unratified material within docs itself.

**Source:** ADR; repository document (`docs/README.md`).

## 6. Engine Architecture

**Decision:** `engine/` holds `contracts/`, `artifacts/`, `graph/`, and
`manifests/` — the deterministic, AI-provider-agnostic core: typed
interfaces (Contracts), the versioned-instance registry (Artifacts), the
dependency graph (Graph), and manifest-based execution (Manifests).

**Rationale:** `contracts/` and `artifacts/` were deliberately separated —
a Contract is an interface/schema, an Artifact is a versioned instance of
one; conflating them would violate One Responsibility.

**Source:** ADR; repository document (`engine/README.md`).

**Decision:** `engine/` contains no Claude-specific (or any other
AI-runtime-specific) concept. Skills, once authorized, live under
`.claude/skills/`, not `engine/skills/`.

**Rationale:** Direct application of Replaceable Automation — `engine/`
must survive a change of AI runtime unmodified.

**Source:** ADR.

**Decision:** The Engine never consumes external/raw artifacts directly.

**Rationale:** Established through this session's comparative review of
two competing resolutions to the "Production Package" gap (see §21). The
Engine only ever operates on Manifests, Contracts, and Artifacts that have
already passed through an Importer boundary — a concept validated by this
session's review but not yet implemented (§21).

**Source:** Architecture Review (this session).

## 7. Execution Model

This section describes how work moves through the Engine end to end,
using only the components already defined elsewhere in this document. It
introduces no new component and states no new decision — it is the
sequence those components already imply, read together.

1. **External input arrives.** Material originating outside the
   Contract-mediated system (see §11, Manifest) enters at this boundary.
2. **Path resolution.** The Repository Resolver (§8) resolves all
   relevant paths against the canonical repository root before anything
   else happens.
3. **State resolution.** The State Manager (§8) resolves the current
   production state of the relevant episode workspace (§16), determining
   what stage of the episode state machine it is in.
4. **Context assembly.** The Context Loader (§8, §13) assembles exactly
   the task-specific documents required for the work about to happen —
   no more.
5. **Manifest reference.** External input, once translated by an Importer
   (§11), or an existing in-repository reference, is expressed as a
   Manifest declaring which specific Contract versions (§10) are in scope
   for this invocation.
6. **Dispatch.** The Worker Dispatcher (§8) invokes the Worker (§9) whose
   registry entry matches the work described by the Manifest.
7. **Worker execution.** The Worker produces one or more Contract-typed
   Artifacts (§10, §19), following only its own declared inputs/outputs —
   it does not decide what context to load or which Contracts it may
   write to.
8. **Validation.** The resulting Artifact progresses through its
   lifecycle (§19): Draft → Generated → Reviewed, gated by whatever
   validation the Worker's own specification defines.
9. **Human approval, where applicable.** If the work produced touches one
   of the five named Human Gates (§18), the Artifact awaits human approval
   before advancing to Approved; otherwise it advances once Reviewed, per
   §18's distinction between artifact-level review and named gates.
10. **Graph update.** The Production Graph (§12) is updated to reflect the
    new Artifact and its declared upstream/downstream edges; any
    dependent Artifacts affected by an upstream change are marked
    Outdated.
11. **Persistence.** The completed Artifact is written to its owning
    location — the episode workspace (§16) or, for Canonical material,
    `canonical/` (§15) via the Knowledge Worker only.
12. **Report.** The Runtime reports the next available action, determined
    from the repository's current state (§4's "Production State Drives
    Execution"), not from conversation history.

This is the complete lifecycle from initial input to completed artifact.
No step here introduces a component not already named in §6, §8, §9,
§10, §11, §12, §13, §15, §16, §18, or §19.

**Source:** Synthesis of already-established content — Repository
document (OS-010's runtime flow); Architecture Review (this session's
Importer/Manifest decision, §11); repository document
(`docs/specifications/SPEC-Director-Worker-v1.md`, whose own §9 "Runtime
execution sequence" and §10 "Artifact generation pipeline" instantiate
this same general model for one specific Worker). No new architectural
decision is made in this section.

## 8. Runtime Architecture

**Decision:** The general runtime flow is: receive request → resolve
current production state → ask the Context Loader for required documents
→ invoke the appropriate Worker(s) → produce artifacts → update the
Production Graph → persist outputs → report next available actions.

**Source:** Repository document (`docs/drafts/OS-010_Runtime_Architecture.md`).

**Decision:** Runtime rules: never infer repository structure; never
bypass Canonical Knowledge; never edit Canonical documents directly; every
meaningful action creates or updates an artifact.

**Source:** Repository document (OS-010).

**Decision:** `runtime/` is subdivided into four named components:
`repository-resolver/`, `context-loader/`, `worker-dispatcher/`, and
`state-manager/`, each mapping to one step of the general runtime flow
above.

**Rationale:** The general flow names four distinct responsibilities that
were previously collapsed into a single undifferentiated folder; splitting
them applies One Responsibility at the runtime layer.

**Source:** ADR; repository document (`runtime/README.md`).

**Decision:** Runtime concepts are themselves provider-agnostic —
currently implemented via Claude Code, but designed to outlive that
specific choice. `.claude/` holds the current, concrete implementation of
these concepts; `runtime/` defines the contracts they must satisfy.

**Source:** ADR; repository document (`runtime/README.md`).

### Repository Resolver

**Decision:** `runtime/repository-resolver/` owns path resolution against
the canonical repository root. It never infers repository structure and
never trusts a shell or session's current working directory.

**Rationale:** This component was not named in any source draft. It was
added because of an operating rule established directly during this
session: the AI runtime's own shell working directory was found to be
unreliable (it is reset by the host application after every command), so
every path must be resolved against the canonical repository root
explicitly rather than assumed. OS-010's existing rule — "never infer
repository structure" — already implied this requirement; this session
made it an explicit, named runtime component.

**Source:** ADR; Architecture Review (this session's operating experience).

### Execution States

The Runtime moves through the following execution states while carrying
out the lifecycle described in §7 (Execution Model):

- **Idle** — no request is being processed.
- **Resolving** — the Repository Resolver and State Manager are resolving
  paths and current production state (Execution Model steps 2–3).
- **Loading Context** — the Context Loader is assembling the
  task-specific profile (Execution Model step 4).
- **Executing Worker** — the Worker Dispatcher has invoked a Worker,
  which is producing Artifacts (Execution Model steps 6–7).
- **Waiting Human Approval** — execution is paused at one of the five
  named Human Gates (§18), pending the human's decision.
- **Completed** — the request's Artifacts have been persisted and the
  Production Graph updated (Execution Model steps 10–12).
- **Blocked** — execution halted on a failure condition and could not
  complete.

These are Runtime execution states only. They are not Artifact states
(§19 — Draft, Generated, Reviewed, Approved, Archived, Outdated, Blocked,
Deprecated) and not Human Gates (§18 — Episode Selection, Reveal, Script
Lock, Final QA, Publication). Note in particular that "Blocked" names both
a Runtime execution state and, separately, an Artifact state (§19); the
two are related but distinct — an Artifact is Blocked when it cannot
progress through its own lifecycle, while the Runtime is Blocked when a
specific invocation cannot proceed. One does not imply the other.

**Source:** Architecture Review (this session — states supplied directly
in this editorial instruction, mapped onto the already-established
Execution Model and existing Runtime flow; no new component introduced).

## 9. Worker Architecture

**Decision:** Workers are specialists: they consume canonical knowledge
and produce artifacts, never own the production pipeline, and never
define project rules. The registry (`workers/`) holds each Worker's
contract — inputs and outputs — not its implementation.

**Source:** Repository document (OS-008); repository document
(`workers/README.md`).

**Decision:** The current Worker registry: Research Worker (Topic →
Research Package, Reveal Brief), Editorial Worker (Reveal Brief,
canonical docs → Script Package; Research Package remains a referenced,
non-trigger dependency for fact-checking), Director Worker (Script,
Visual Identity, Playbook → Director Package, Shot List, AI Prompt
Packages, Asset Manifest), Voice Worker (Script → Voice Package), QA
Worker (all production artifacts → QA Report), Knowledge Worker
(Postmortems → canonical change proposals only), Publishing Worker
(approved artifacts → Published Episode).

**Rationale:** Reveal Brief ownership moved from Editorial Worker to
Research Worker as of the Architecture v1.0 freeze — an explicit,
human-approved architectural decision, not drift. Justified by this
repository's own production evidence (the real Dollar Dominance
research-to-reveal chain and `the-giant-is-the-hostage`'s
reveal-stage-before-script workspace both show reveal-selection
happening entirely on the research side, before scripting begins) and by
One Responsibility (finding the strongest reveal requires holding the
full research corpus; scripting is a distinct prose/pacing craft applied
to an already-decided reveal).

**Source:** `workers/research-worker.md`, `workers/editorial-worker.md`
(promoted from OS-016/OS-017, superseding this entry's prior citation of
them as drafts); `docs/adr/ADR-0002-Architecture-v1.0-Freeze.md`.

**Decision:** Worker *implementation*, including all prompt content, is
deferred to `.claude/skills/<worker-name>/` and does not exist yet for any
Worker.

**Source:** ADR; repository document (`workers/README.md`, `.claude/README.md`).

**Decision:** Director Worker is the first Worker to receive a complete
implementation-grade specification (`docs/specifications/SPEC-Director-Worker-v1.md`),
establishing the format future Worker specifications should follow:
Mission, Responsibilities, Explicit Non-Responsibilities, Inputs, Outputs,
Contracts consumed/produced, Context Loader profile, Runtime execution
sequence, Artifact generation pipeline, Validation rules, Failure
conditions, Human approval gates, Integration points, Manifest/Graph
updates, Logging, Error recovery, Definition of Done, Future Skill
mapping.

**Rationale:** Demonstrates that OS-013's Contract discipline and OS-006's
Context Loader profile can be operationalized into an implementation-grade
document without inventing new architecture — the specification only
resolves ambiguity (e.g., "Production Package" for Director Worker's
purposes) by tracing every input/output to a named Contract or Canonical
document.

**Source:** Repository document (`docs/specifications/SPEC-Director-Worker-v1.md`).

## 10. Contracts

**Decision:** Every Contract has one owner, one schema, one lifecycle,
declares its upstream dependencies, and declares its downstream consumers.
Workers communicate only through Contracts, never free-form exchange.

**Source:** Repository document (`docs/drafts/OS-013_Production_Contracts.md`).

**Decision:** Nine Initial Contracts are named: Research Package, S9
Scorecard, Reveal Brief, Script Package, Director Package, Voice Package,
QA Package, Publishing Package, Postmortem Package.

**Source:** Repository document (OS-013).

**Decision:** `engine/contracts/` is the intended physical home for these
Contracts as real, checkable schemas. As of this document, it contains no
populated schemas — the only place any Contract is actually defined is as
prose inside an unratified draft.

**Rationale:** This absence was identified as the primary root cause of
the "Production Package" gap: there is currently no mechanism by which a
Worker specification (or a person) can check a term against an
authoritative registry, only a manual cross-read of OS-013.

**Source:** Architecture Review (this session, Gap Analysis 001).

**Decision:** OS-013's governing rule — "Workers communicate only through
these contracts" — is scoped to inter-Worker exchange (one Worker's output
becoming another's input). It does not, on its own text, state whether
genesis input (material with no producing Worker, originating outside the
system) is exempt.

**Rationale:** This scoping ambiguity is precisely what allowed
"Production Package" — a term with no producing Worker — to be used
informally in `OS-016_Research_Worker.md` without being reconciled against
the Contract list.

**Source:** Architecture Review (this session, Gap Analysis 001).

## 11. Manifest

**Decision:** The architecture must support manifest-based execution —
describing, for a given piece of work, what should run.

**Source:** Architecture Review (this session — stated directly as a
repository-skeleton requirement during construction).

**Decision:** `engine/manifests/` is the intended physical home for this
schema. As of this document, it is empty — no manifest schema has been
defined.

**Source:** Architecture Review (this session, Gap Analysis 001;
confirmed again in Readiness Assessment 001).

**Decision:** External material never reaches a Manifest, a Contract, or
a Worker directly. It is first translated by an Importer — a boundary
component that converts an External Artifact into a reference a Manifest
can declare. The Manifest itself only declares a reference bundle of
specific Contract versions in scope for a given Worker invocation; it does
not perform translation itself.

**Rationale:** Chosen over letting Manifest absorb translation directly,
which would have given Manifest two responsibilities in violation of One
Responsibility (§4) and coupled external format changes into the Engine's
own schema. An Importer isolates that volatility the same way
`integrations/` already isolates the Engine from external AI services on
the outbound side.

**Source:** Architecture Review (this session).

**Decision:** The Importer has not been built, named as a repository
directory, or given its own specification.

**Source:** Architecture Review (this session).

## 12. Production Graph

**Decision:** Production is modeled as a dependency graph rather than a
linear checklist. Every artifact declares its inputs and outputs; when an
upstream artifact changes, every dependent artifact becomes Outdated until
regenerated.

**Source:** Repository document (`docs/drafts/OS-007_Production_Graph.md`).

**Decision:** The Initial Graph: Topic → Research → Reveal Brief → Script.
Script produces Director Package, Voice Package, and Subtitle Package.
Director Package produces Higgsfield Prompts, HyperFrames Prompts, and
Asset Manifest. Director Package and Voice Package together produce QA
Package. QA Package produces Publishing Package. Publishing Package
produces Published Episode. Postmortem feeds back into Canonical Knowledge
through Knowledge Worker only.

**Source:** Repository document (OS-007).

**Decision:** `engine/graph/` is the intended physical home for this
graph's actual state. As of this document, it is empty.

**Source:** Architecture Review (this session, Readiness Assessment 001).

## 13. Context Loading

**Decision:** The Context Loader assembles task-specific context before
any Worker begins execution. Workers never decide what to load — that
responsibility belongs to the Context Loader alone. Loading the entire
repository by default is prohibited.

**Source:** Repository document (`docs/drafts/OS-006_Context_Loading_System.md`).

**Decision:** Six task-type profiles are currently named: S9 Review
(Constitution §9, Mechanism Ladder, S9 Scorecard), Reveal Development
(Constitution §10, Mechanism Ladder, editorial Decision Log), Script
Production (Constitution, Reveal Brief, Production Playbook, Production
Postmortem), Director Package (Visual Identity, Production Playbook,
Current Script, Current Workspace), Voice (Voice Package, Script,
Production Playbook), and QA (only documents relevant to validation).

**Source:** Repository document (OS-006).

**Decision:** The Director Package profile was validated in practice by
`SPEC-Director-Worker-v1`, which adopted it exactly as its Context Loader
profile without modification.

**Source:** Repository document (`docs/specifications/SPEC-Director-Worker-v1.md`, §8).

**Decision:** No profile currently exists for Production Package
generation or import.

**Source:** Architecture Review (this session, Readiness Assessment 001).

## 14. Knowledge Architecture

**Decision:** Knowledge is organized into four layers: Canonical (defines
behavior — Constitution, Decision Log, Production Playbook, Visual
Identity, Mechanism Ladder), Operational (supports active production —
Episode Workspaces, Production Packages within them, Research, QA),
Reference (reusable but non-authoritative — external research, templates,
AI experiments), and Archive (historical record only, never loaded
automatically).

**Source:** Repository document (`docs/drafts/OS-004_Knowledge_Architecture.md`).

**Decision:** Promotion moves one direction only: Reference → Operational
→ Canonical, and requires production evidence. Ideas are never promoted
directly into Canonical.

**Source:** Repository document (OS-004).

**Decision:** The repository maps these layers as: `canonical/` (Layer 1),
`episodes/` (Layer 2), `docs/` mostly Layer 3 (with `docs/adr/` carved out
specifically for engineering decisions, distinct from Canonical's future
Decision Log, which records editorial/business decisions), and `archive/`
(Layer 4).

**Source:** ADR; repository document (`docs/README.md`).

## 15. Canonical Documents

**Decision:** Only Canonical documents may define rules. They are
immutable except through the Knowledge Worker, and promotion into
`canonical/` requires production evidence.

**Source:** Repository document (OS-004); repository document
(`canonical/README.md`).

**Decision:** The named Canonical documents are Constitution, Decision
Log, Production Playbook, Visual Identity, and Mechanism Ladder.

**Source:** Repository document (`docs/drafts/OS-002_System_Architecture.md`;
`docs/drafts/OS-004_Knowledge_Architecture.md`).

**Decision:** `canonical/` currently contains no ratified documents.

**Source:** Architecture Review (this session, confirmed via repository
inspection).

## 16. Episode Workspaces

**Decision:** The Episode Workspace is the primary production object.
Every episode has exactly one workspace; everything related to that
episode lives inside it; nothing episode-related exists outside its
workspace except Canonical documents.

**Source:** Repository document (`docs/drafts/OS-005_Episode_Workspace_Specification.md`).

**Decision:** Required components per episode: Metadata, Research,
Sources, Reveal Brief, Script, Director Package, Voice Package, Assets,
QA, Output, Postmortem.

**Source:** Repository document (OS-005).

**Decision:** The episode state machine: Idea → Research → Episode
Selection → Reveal → Script → Direction → Production → QA → Publish →
Postmortem. Claude determines the next step from current state, not chat
history.

**Source:** Repository document (OS-005).

**Decision:** `episodes/` currently contains no episode workspaces. No
workspace exists for the reference episode examined during this session's
Readiness Assessment ("Luxury Destruction").

**Source:** Architecture Review (this session, Readiness Assessment 001).

## 17. Integrations

**Decision:** Workers never call external tools directly — they submit
standardized requests to the Integration Layer, so any provider can be
replaced without changing a Worker. Each integration receives an input
artifact, configuration, and an output destination, and returns a
generated artifact, metadata, an execution log, and failure state. No
business logic lives inside an integration.

**Source:** Repository document (`docs/drafts/OS-009_Integration_Layer.md`).

**Decision:** Initial providers: Higgsfield (video generation, camera
execution), HyperFrames (image generation, keyframe creation), ElevenLabs
(voice synthesis). Additional providers are added as sibling folders.

**Source:** Repository document (OS-009); repository document
(`integrations/README.md`).

**Decision:** Director Worker does not call Higgsfield or HyperFrames
directly. It produces prompt packages that a later Production-stage step
supplies to those integrations as their input artifact.

**Source:** Repository document (`docs/specifications/SPEC-Director-Worker-v1.md`, §14).

**Decision:** No integration adapter is implemented. All three provider
folders are empty.

**Source:** Architecture Review (this session).

## 18. Human Approval Gates

**Decision:** Exactly five named Human Gates exist: Episode Selection,
Reveal, Script Lock, Final QA, Publication. Only the human (Eugene) may
approve these. Workers prepare decisions; they do not finalize them.

**Source:** Repository document (`docs/drafts/OS-015_State_Management.md`).

**Decision:** Not every artifact corresponds to a named Human Gate. A
Director Package, for example, is bounded between two gates (Script Lock
upstream, Final QA downstream) without being a gate itself; its own
progression from Generated to Reviewed is satisfied by automated
validation, not a human decision, and it only reaches Approved status
transitively once Final QA passes.

**Rationale:** Verified directly while writing `SPEC-Director-Worker-v1` —
the general artifact lifecycle (OS-014) applies to every artifact, but
that is a separate mechanism from the five specifically-named Human Gates,
and conflating them would have invented a sixth gate not present in any
source document.

**Source:** Repository document (`docs/specifications/SPEC-Director-Worker-v1.md`, §13).

## 19. Versioning

**Decision:** Every artifact exposes Artifact ID, Episode ID, Version,
Status, Owner Worker, Input Dependencies, Output Consumers, Last Updated,
and Approval State.

**Source:** Repository document (`docs/drafts/OS-014_Artifact_Specification.md`).

**Decision:** Artifact states progress Draft → Generated → Reviewed →
Approved → Archived, with Outdated, Blocked, and Deprecated as additional
possible states.

**Source:** Repository document (OS-014).

**Decision:** Artifacts are immutable after approval. A revision creates a
new version rather than overwriting history.

**Source:** Repository document (OS-014).

**Decision:** No concrete identifier or naming scheme has been defined
that maps this abstract discipline onto real version identifiers (e.g.
what distinguishes a "`_v2`" from a "`_v1`" in practice).

**Source:** Architecture Review (this session, Readiness Assessment 001).

## 20. ADR Process

**Decision:** Architecture Decision Records are numbered, immutable once
accepted, and superseded by a new ADR rather than edited in place. They
record engineering decisions about the repository/system itself, distinct
from Canonical's future Decision Log, which records editorial/business
decisions about the show.

**Source:** Repository document (`docs/README.md`).

**Decision:** `ADR-0001` is the first instance of this process, recording
the decisions made while constructing the repository skeleton (the
Engine/Runtime/Workers split, provider-agnostic Engine, Claude-specific
implementation under `.claude/`, Contracts as first-class, the four named
Runtime components, the removal of `prompts/`, and the Knowledge
Architecture mapping), and explicitly states that it sets the precedent
for recording future engineering decisions the same way.

**Source:** ADR.

**Decision:** This document (SPEC-001) is not itself an ADR — it is a
consolidation of decisions already made (several of them via ADR-0001,
others via this session's architecture-review documents). Where a
decision recorded here (§11, §6, §21) has not yet been formalized as its
own ADR, that is listed as a gap, not resolved by this document.

**Source:** Architecture Review (this session).

## 21. Current Known Gaps

Factual, unresolved-but-not-decided-here gaps, consolidated from Gap
Analysis 001 and Readiness Assessment 001:

- `engine/contracts/` contains no populated Contract schemas — the nine
  Initial Contracts exist only as prose in an unratified draft (§10).
- `engine/manifests/` contains no manifest schema, including no
  input-reference-bundle field for Importer output (§11).
- `engine/graph/` contains no populated graph state (§12).
- `canonical/` contains no ratified documents of any kind (§15).
- `episodes/` contains no episode workspaces (§16).
- `.claude/skills/` contains no Worker implementations (§9).
- `integrations/{higgsfield,hyperframes,elevenlabs}/` contain no adapter
  implementations (§17).
- No Context Loader profile exists for Production Package generation or
  import (§13).
- The Importer concept — validated through this session's architecture
  review (§11) — exists nowhere in the repository as its own file, folder,
  or specification prior to this document. This document is the first
  place it has been written down.
- No concrete artifact versioning/identifier scheme exists beyond OS-014's
  abstract discipline (§19).
- No production evidence exists anywhere in the repository, because no
  episode has yet been produced. Every source citation in this document is
  therefore either a Repository document, an ADR, or an Architecture
  Review — never Production evidence.

---

## Open Questions

Genuinely unresolved forks — not implementation gaps, but decisions this
session did not make and this document does not make on its behalf.

### 1. Who owns Production Package import — a Worker, or the Runtime itself?

**Why unresolved:** No Worker in the current registry (§9) claims this
responsibility. OS-016 associates the term with Research Worker's *input*
side only, not its output. An Importer (§11) behaves more like a
deterministic translation mechanism — comparable to the Context Loader, a
Runtime service every Worker depends on — than like a specialist Worker
exercising editorial judgment.

**Competing options:**
(a) Importer is Runtime-level machinery, invoked automatically ahead of
Worker Dispatch, the same way Context Loader runs before a Worker is
invoked.
(b) Importer is a tool a Worker (existing or new) invokes deliberately,
exercising judgment over its output before treating it as usable.

**What production evidence would resolve this:** a real case showing
whether human/editorial judgment is ever needed when importing external
material — e.g., whether an imported Production Package sometimes needs to
be rejected, corrected, or interpreted rather than mechanically accepted.
If judgment is regularly needed, this favors (b); if the process is
consistently mechanical, this favors (a).

### 2. Should all nine Contracts be populated in `engine/contracts/` at once, or incrementally?

**Why unresolved:** Gap Analysis 001 recommended populating the registry
but did not decide the order or pace. `SPEC-Director-Worker-v1` only
strictly required Script Package and Director Package to exist as real
schemas.

**Competing options:**
(a) Populate all nine upfront, for internal consistency across the whole
Contract set from day one.
(b) Populate incrementally, driven by whichever Worker specification needs
a given Contract next.

**What production evidence would resolve this:** building at least two
more Worker specifications under the incremental approach and observing
whether their Contract definitions drift or require rework once compared
against each other — if drift occurs, this favors (a).

### 3. Should an Importer's translation output be its own persisted, versioned artifact?

**Why unresolved:** OS-001's "Everything Becomes an Artifact" principle
suggests yes; but the Importer hypothesis as evaluated this session only
specified `External Artifact → Importer → Manifest`, without stating
whether the intermediate translation step itself needs to be recorded, and
persisting every import unconditionally may be unwarranted overhead for
trivial cases (e.g., a bare Topic string).

**Competing options:**
(a) Every Importer run produces its own persisted, versioned artifact,
fully auditable after the fact.
(b) Only the resulting Manifest reference is persisted; the translation
itself is a transient computation.

**What production evidence would resolve this:** a real case where someone
needs to audit or debug why an import was interpreted a particular way
after the fact. If that need arises, this favors (a); if it never comes
up in practice, this favors (b).

### 4. What concrete scheme should artifact version identifiers follow?

**Why unresolved:** OS-014 establishes the rule (immutable after approval,
revision creates a new version) but never defines the identifier format
itself (what a "`_v2`" actually means mechanically).

**Competing options:**
(a) Sequential per-artifact integers (v1, v2, v3…).
(b) Content-hash-based identifiers.
(c) Timestamp-based identifiers.

**What production evidence would resolve this:** observing whether humans
need to reference versions by memorable sequence (favoring (a)) versus
whether the system needs tamper-evidence or deduplication guarantees
(favoring (b)) — this becomes decidable only once real revisions start
occurring in production.

### 5. Does OS-013's Contract-only communication rule need a formal amendment, or is Manifest-mediated import sufficient?

**Why unresolved:** Gap Analysis 001 identified that OS-013's rule doesn't
explicitly say whether genesis/external input is exempt from being a
Contract. The Importer hypothesis (§11) offers a working resolution
(external input becomes a Manifest reference, never a Contract), but this
has been reasoned through, not formally written into OS-013 or a
superseding document as an amendment.

**Competing options:**
(a) Leave OS-013 as-is and treat the Importer→Manifest pattern as the
de facto scoping clarification, recorded here and in a future ADR.
(b) Formally amend OS-013 (once it is promoted out of `docs/drafts/`) to
state explicitly that its rule governs inter-Worker exchange only.

**What production evidence would resolve this:** whether any Worker, in
practice, ever needs stronger typing guarantees on external input than a
Manifest reference provides. If a Worker's correctness depends on that
input having full Contract-level guarantees, this favors (b).
