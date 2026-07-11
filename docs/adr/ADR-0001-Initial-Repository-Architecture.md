# ADR-0001: Initial Repository Architecture

**Status:** Accepted
**Date:** 2026-07-10

This record documents *why* the repository is shaped the way it is. It is
not a changelog of what was created — it is the reasoning a future
maintainer (human or AI) needs in order to extend this system without
breaking its intent.

---

## Context

Open Secret Engine exists to turn Open Secret's production process from a
collection of prompts and chat history into an operating system: a
repository that can answer "what is true, what is happening, what should
happen next" from its own contents alone, and that a Claude Code session
can resume correctly after weeks with no memory of prior conversations.

Eighteen architecture drafts (`OS-001` through `OS-018`) were written
first, outside any repository, to think through the system before
building it. This ADR records the decisions made when those drafts were
turned into an actual repository structure — including several places
where the repository diverges from what the drafts originally proposed,
and why.

---

## Decisions

### 1. Repository philosophy

The repository is the operating system, not documentation or a file
cabinet for it (OS-003). Every directory exists because a production
process requires it; nothing is created "because it might be useful." This
governed every decision below: several folders proposed in the original
drafts (a flat `docs/` with a single `architecture/` subfolder, a
top-level `prompts/`) were changed or dropped because they didn't hold up
against this standard once examined concretely.

The corollary — the Golden Rule from OS-003 — is that if losing a chat
would lose important project knowledge, that knowledge belongs in the
repository, not in conversation history. This is why the drafts were
copied into the repository (`docs/drafts/`) rather than left to live only
as files on someone's Downloads folder, and why this ADR exists at all:
the reasoning behind the structure needs to survive independent of the
conversation that produced it.

### 2. Separation of Engine / Runtime / Workers

The system is split into three layers with distinct, non-overlapping
questions each one answers:

- **`engine/`** — *what is the machinery?* Versioned artifacts, the
  production graph, contracts, manifest execution. Pure mechanism.
- **`runtime/`** — *how does a request get executed against that
  machinery?* Path resolution, context loading, state resolution, worker
  dispatch. Process, not mechanism.
- **`workers/`** — *who does the work?* A registry of specialist roles and
  their input/output contracts — not their implementation.

This split exists because each layer changes for different reasons and at
different rates. The engine's schemas should be stable for years. The
runtime's execution flow may evolve as the system matures (OS-006
explicitly anticipates the Context Loader becoming a full dependency
resolver). The worker registry changes whenever the business adds or
reshapes a production role. Collapsing these into one undifferentiated
structure would mean a change to any one reason for change risks
disturbing the other two.

### 3. Provider-agnostic Engine

`engine/` contains no reference to Claude, Claude Code, or any specific AI
runtime. This directly implements the "Replaceable Automation" principle
from OS-001: every external tool — and by extension every AI runtime —
must be replaceable without redesigning the OS. If Open Secret Engine is
still running in five years, it is likely running on different AI
infrastructure than it started on; `engine/` is the part of the system
that must not care.

This is the specific reason Skills were relocated out of `engine/` during
review (see decision 4) — a Claude Code Skill is not a neutral concept,
and its presence inside `engine/` would have quietly coupled the
provider-agnostic core to one vendor's implementation format.

### 4. Claude-specific implementation under `.claude/`

`.claude/` is the single, explicit boundary where the current AI runtime's
implementation detail lives — currently just `skills/`, reserved for
Worker implementations once authorized. This restores what the original
`OS-012` draft proposed (`.claude/CLAUDE.md`, `.claude/skills/`,
`.claude/workers/`) after an intermediate pass had drifted from it by
inventing `engine/skills/` instead.

The practical test applied throughout: would this survive a change of AI
runtime? If not, it belongs under `.claude/`, not `engine/` or `runtime/`.
`CLAUDE.md` itself is deliberately not placed inside `.claude/` — it will
live at the repository root, because that is where Claude Code's own
auto-loading convention expects it, and this repository does not fight
that convention.

### 5. Contracts as first-class architecture

`engine/contracts/` was added as a sibling to `engine/artifacts/` after
recognizing a distinction the original drafts named but didn't structurally
separate: OS-013 states that Workers exchange typed production artifacts,
never free-form chat. The *type* an artifact must satisfy (a contract) and
the *lifecycle state* of an actual instance of that type (the artifact
registry) are different concerns — one is a schema, the other is a state
machine. Merging them would make it unclear, for any given piece of
information, whether you were looking at a rule or a record. Every Worker
in the system depends on this distinction being unambiguous, since
contracts are literally the interface layer between Workers, Integrations,
and Artifacts (OS-013) — this is not a minor organizational nicety, it is
what makes multi-worker production safe.

### 6. Runtime components

`runtime/` was split into four named parts — `repository-resolver/`,
`context-loader/`, `worker-dispatcher/`, `state-manager/` — because OS-010's
runtime flow (receive request → resolve state → load context → invoke
worker → produce artifacts → update graph → persist → report) names four
distinct responsibilities that were previously collapsed into a single
undifferentiated `context/` folder.

`repository-resolver/` in particular was not named in any of the original
eighteen drafts. It was added because of an operating rule established
directly during this repository's construction: the shell's working
directory cannot be trusted and every path must be resolved against the
canonical repository root rather than inferred. OS-010's own runtime rule
— "never infer repository structure" — already implied exactly this
requirement; giving it a named component makes an implicit rule into an
explicit, addressable one.

### 7. Why `prompts/` was intentionally removed

The original proposal (OS-012) included a top-level `prompts/` directory.
It was removed after concluding that a Worker's prompt content, once
Workers are implemented as Claude Code Skills, *is* that Skill's
implementation — it has no meaning independent of the Skill that uses it.
A separate top-level `prompts/` would have created two possible locations
for "how does this Worker behave" with no principled rule for which one
wins, and drift between the two was not a hypothetical risk but a near
certainty over years of iteration.

No replacement placeholder was created. There is no Skill implementation
yet, so there is nothing today that needs a prompts location; when Skills
are authorized, prompt content will live inside each Skill's own folder
under `.claude/skills/<worker-name>/`. If a genuinely cross-worker reusable
prompt fragment emerges later, that will be a decision made with real
content in hand, not a structural bet made in advance of any evidence for
it.

### 8. Knowledge organization

Knowledge is organized into four layers (OS-004): **Canonical** (defines
behavior), **Operational** (active production — episode workspaces),
**Reference** (reusable but non-authoritative), and **Archive** (historical
only). This repository maps that directly:

- `canonical/` — Layer 1. Only documents here may define rules. Empty
  today; nothing has been ratified.
- `episodes/` — Layer 2, the operational layer, structured per OS-005.
- `docs/` — mostly Layer 3 (reference material *about* the system), with
  one addition: `docs/adr/`, which records *engineering* decisions (like
  this one) as distinct from `canonical/`'s future Decision Log, which will
  record *editorial/business* decisions about the show itself. Conflating
  these two kinds of decision record was judged a worse long-term outcome
  than adding one extra folder.
- `archive/` — Layer 4, never loaded automatically.

`docs/drafts/` holds the eighteen source documents as a single, unsorted
batch rather than pre-sorted into `architecture/` / `specifications/` /
`principles/`. Every one of them currently carries `Status: Draft v0.1` in
its own header; sorting them into a ratified category is a promotion
decision requiring human judgment (per OS-004's promotion rule: Reference
→ Operational → Canonical, requiring production evidence, never a direct
promotion), not something to be inferred from a document's working title.

### 9. Design principles that guided these decisions

Three principles from OS-001 were applied repeatedly enough during review
to call out explicitly:

- **Replaceable Automation** — motivated the entire Engine/`.claude` split
  (decisions 3 and 4).
- **One Responsibility** — motivated splitting `runtime/` into four named
  components and separating `contracts/` from `artifacts/` (decisions 5
  and 6), rather than letting one folder quietly grow multiple jobs.
- **Everything Becomes an Artifact / nothing important lives only in chat
  history** — motivated committing the eighteen drafts into `docs/drafts/`
  and writing this ADR, so that the reasoning behind the repository's
  shape survives independently of the conversation that produced it.

---

## Consequences

- Extending the system now has a clear rule of thumb: ask whether a new
  concept would survive a change of AI runtime. If yes, it belongs in
  `engine/` or `runtime/`; if no, it belongs in `.claude/`.
- `docs/drafts/` will accumulate documents faster than they get promoted
  unless someone actively curates it; that curation is Knowledge Worker's
  job once it exists; until then, `docs/drafts/` is expected to be the
  largest, least organized folder in the repository, by design.
- Because `prompts/` was removed rather than left empty, a future
  contributor proposing prompt-related structure again should re-read
  decision 7 rather than assume the omission was accidental.
- This ADR itself sets the precedent that engineering decisions about the
  repository are recorded here, going forward, rather than only in
  conversation.
