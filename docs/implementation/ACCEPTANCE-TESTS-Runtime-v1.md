# ACCEPTANCE-TESTS-Runtime-v1: Repository Resolver, Manifest, Worker Dispatcher

**Status:** Behavioral specification. Defines the expected behavior of
Runtime components before implementation exists to match it. This is
**not** unit test code and does not execute anything — it is the
contract implementation will be built and checked against.

**Scope:** Repository Resolver, Manifest, Worker Dispatcher only.
Explicitly excludes Workers (as their own behavior spec — a Worker name
appearing as a Dispatcher *decision output* below is not the same as
specifying that Worker's behavior), Production Graph, and Integrations.

**Governing documents:** `SPEC-001` §8 (Runtime Architecture, incl.
Repository Resolver), §9 (Worker Architecture / registry), §11
(Manifest).

**Relationship to existing code:** this document supersedes the Manifest
v1 implementation reviewed earlier this sprint. That implementation
currently violates the core rule below (it computes `activeWorker` and
`nextExpectedArtifact` directly, inside Manifest). This document is the
corrected target; the code has not yet been changed to match it. Each
scenario below notes whether current code already satisfies it.

## Core rule governing this entire suite

Manifest reports state. It never decides which Worker executes. Worker
Dispatcher makes execution decisions, using Manifest's state report plus
the Worker registry (`SPEC-001` §9) as its only inputs. Any scenario that
would require Manifest to output a Worker name, or Dispatcher to inspect
the filesystem directly instead of going through Manifest, is out of
contract.

---

## 1. Repository Resolver

**Contract:** Resolves a relative path to an absolute path anchored at
the canonical repository root. Pure path arithmetic — never infers the
root from the invoking process's working directory, and never checks
whether the resolved target exists (existence-checking belongs to
Manifest, not the Resolver).

### RR-1 — Repository can be resolved from any working directory

**Given** the Repository Resolver module is invoked as part of a running
process
**When** that process's current working directory is anything other than
the repository root, including a directory entirely outside the
repository
**Then** the Resolver must compute the same repository root regardless
of the invoking process's working directory
**Expected Result:** `REPO_ROOT`, and every path resolved from it, is
identical whether invoked from the repository root, a subdirectory, or
an unrelated directory elsewhere on disk.

*Implementation status: satisfied.* Verified manually — the current
resolver derives the root from its own file location (`import.meta.url`),
not `process.cwd()`, and was confirmed to produce the same result when
invoked from `C:\Users\Eugene` as from the repository root.

### RR-2 — Repository cannot be resolved

**Given** the Resolver module has been moved, copied, or is otherwise
running from a location where directory arithmetic from its own file
location no longer lands on a valid repository root (e.g., the computed
root has no `.git` directory and no root-level `README.md`)
**When** any path resolution is attempted
**Then** the Resolver must fail loudly with a clear error, not silently
return a plausible-looking but incorrect path
**Expected Result:** resolution raises an explicit error identifying
that the computed root does not look like a valid repository, rather
than returning a path that happens to exist but points somewhere wrong.

*Implementation status: not satisfied.* The current implementation has
no validation step — it always returns a computed path with no check
that the result is a real repository root. This scenario requires new
logic; it is not covered by existing code.

### RR-3 — Repository contains no episode

**Given** a valid, resolvable repository root
**When** the Resolver is asked to resolve a path for an episode ID that
does not exist under `episodes/`
**Then** the Resolver still returns a well-formed absolute path — it
does not check or care whether the target exists
**Expected Result:** a syntactically correct path is returned; the
caller, not the Resolver, is responsible for checking existence and
deciding what "no episode" means for its own purposes.

*Implementation status: satisfied by design.* The current Resolver has
no existence-checking logic at all, which is exactly the required
behavior here — not implementing existence-checking is the correct
contract, not a gap.

---

## 2. Manifest

**Contract:** Reports the current, observable state of one episode
workspace: which episode it is, and which of the artifacts this suite
currently recognizes (Script Package, Director Package) exist. Nothing
else. Manifest never names a Worker and never predicts what happens
next — both are out of contract.

Manifest's reported shape, for reference by the Dispatcher scenarios
below:

```
episode: <episode id>
artifacts:
  scriptPackage: present | absent
  directorPackage: present | absent
unrecognized: [ list of paths Manifest found but does not recognize ]
```

### MF-1 — Episode contains no production artifacts

**Given** an episode workspace with no `script/script-package.md` and no
non-empty `director-package/` directory
**When** Manifest is asked to report state for that episode
**Then** it reports both artifacts as absent
**Expected Result:** `{ episode: <id>, artifacts: { scriptPackage:
absent, directorPackage: absent }, unrecognized: [] }`.

*Implementation status: satisfied.* Verified against the actual Demo
Episode workspace in its current, real (un-seeded) state.

### MF-2 — Script exists

**Given** `script/script-package.md` exists, and `director-package/` is
absent or empty
**When** Manifest reports state
**Then** it reports Script Package present, Director Package absent
**Expected Result:** `{ artifacts: { scriptPackage: present,
directorPackage: absent } }`.

*Implementation status: satisfied.* Verified with a throwaway test file
during the Manifest v1 review, then removed.

### MF-3 — Script + Director Package exist

**Given** both `script/script-package.md` and a non-empty
`director-package/` exist
**When** Manifest reports state
**Then** it reports both artifacts present
**Expected Result:** `{ artifacts: { scriptPackage: present,
directorPackage: present } }`.

*Implementation status: satisfied.* Verified the same way as MF-2.

### MF-4 — Unknown artifact exists

**Given** the episode workspace contains something that isn't
`script/script-package.md` or `director-package/` — e.g., a stray file
inside `script/`, or an unexpected top-level folder like
`voice-package/`
**When** Manifest reports state
**Then** it reports the two known artifacts' presence/absence as normal,
and additionally lists the unrecognized item rather than silently
ignoring it or throwing
**Expected Result:** `{ artifacts: {...}, unrecognized:
["episodes/<id>/voice-package"] }` (or equivalent) — Manifest never
crashes on, and never silently drops, something it doesn't recognize.

*Implementation status: not satisfied.* The current implementation only
checks the two known paths and has no concept of "unrecognized" content.

### MF-5 — Artifact missing (partially present is still absent)

**Given** `director-package/` exists as a directory but is empty, or
`script/` exists but `script-package.md` inside it does not
**When** Manifest reports state
**Then** the corresponding artifact is reported as absent, not present
**Expected Result:** an empty or malformed artifact location is treated
identically to a missing one — presence means the expected file or
non-empty directory actually exists, not just that its parent folder
does.

*Implementation status: satisfied.* The current implementation already
checks `readdirSync(...).length > 0` for Director Package rather than
just directory existence.

### MF-6 — Manifest never reports a Worker or a next step (negative scenario)

**Given** any episode state at all
**When** Manifest reports state
**Then** the report contains no field naming a Worker and no field
predicting a next artifact
**Expected Result:** the reported shape is exactly `{ episode, artifacts,
unrecognized }` — nothing more. Any implementation that adds an
`activeWorker` or `nextExpectedArtifact` field violates this contract.

*Implementation status: not satisfied.* The current Manifest v1
implementation outputs `activeWorker` and `nextExpectedArtifact`
directly — this is precisely the violation identified in this sprint's
architecture review, and the reason this document exists.

---

## 3. Worker Dispatcher

**Contract:** Decides which Worker, if any, should execute next, using
Manifest's state report and the Worker registry (`SPEC-001` §9) as its
only inputs. Never inspects the filesystem directly — everything it
knows about episode state comes through Manifest.

### WD-1 — Script Package present, Director Package missing → selects Director Worker

**Given** a Manifest report showing `scriptPackage: present,
directorPackage: absent`
**When** the Dispatcher is asked to determine the next executable Worker
**Then** it consults the Worker registry, finds Director Worker's
declared input (Script Package) satisfied and its declared output
(Director Package) not yet produced
**Expected Result:** Dispatcher selects Director Worker and reports that
selection — it does not itself generate a Director Package or perform
any of Director Worker's work.

*Implementation status: not satisfied.* Worker Dispatcher does not exist
yet as code; this decision logic currently lives, incorrectly, inside
Manifest v1, and needs to move here.

### WD-2 — Script + Director Package present → "no executable worker"

**Given** a Manifest report showing both artifacts present
**When** the Dispatcher is asked to determine the next executable Worker
**Then** it finds no registered Worker, within this suite's in-scope
pair, whose output is still missing
**Expected Result:** Dispatcher reports "no executable worker" as a
normal, valid terminal state — not an error. This means the in-scope
portion of the pipeline is complete, and is clearly distinct from WD-3's
refusal below.

*Implementation status: not satisfied* — same reason as WD-1.

### WD-3 — Inconsistent state → Dispatcher refuses execution

**Given** a Manifest report that violates the pipeline's known
dependency order — e.g., `scriptPackage: absent, directorPackage:
present` (a Director Package cannot legitimately exist without the
Script Package it was built from)
**When** the Dispatcher is asked to determine the next executable Worker
**Then** it detects that this state cannot arise through normal
execution and does not attempt to select or run any Worker
**Expected Result:** Dispatcher explicitly refuses execution and reports
the specific inconsistency (which artifact relationship was violated) —
an abnormal outcome requiring investigation, clearly distinguished from
WD-2's normal "nothing to do" outcome.

*Implementation status: not satisfied* — same reason as WD-1.

### WD-4 — Neither artifact present → selects Editorial Worker *(added scenario)*

**Given** a Manifest report showing both artifacts absent
**When** the Dispatcher is asked to determine the next executable Worker
**Then** it finds Editorial Worker's declared output (Script Package)
not yet produced, with no unmet input dependency blocking it
**Expected Result:** Dispatcher selects Editorial Worker. Included
because it's the natural first step of the same in-scope pipeline WD-1
and WD-2 already cover — leaving it unspecified would leave a gap at the
very start of the sequence.

*Implementation status: not satisfied* — same reason as WD-1.

### WD-5 — Manifest reports an unrecognized artifact alongside normal state *(added scenario)*

**Given** a Manifest report where `artifacts` is well-formed but
`unrecognized` is non-empty (per MF-4)
**When** the Dispatcher is asked to determine the next executable Worker
**Then** it makes its decision based on the known `artifacts` field
only, and surfaces the unrecognized item in its own report rather than
silently discarding it or refusing execution outright
**Expected Result:** an unrecognized item is a visibility concern, not
automatically a WD-3-style inconsistency — Dispatcher proceeds normally
on the known state, but the unrecognized item must be traceable in its
output.

*Implementation status: not satisfied* — depends on MF-4 existing first.

---

## Summary: what this reveals about current implementation

| Scenario | Status |
|---|---|
| RR-1, RR-3 | Already satisfied |
| RR-2 | Not built — Resolver has no validation/failure path |
| MF-1, MF-2, MF-3, MF-5 | Already satisfied |
| MF-4 | Not built — no "unrecognized" reporting |
| MF-6 | **Currently violated** — Manifest v1 outputs `activeWorker`/`nextExpectedArtifact`, which this suite defines as out of contract |
| WD-1 through WD-5 | Not built — Worker Dispatcher does not exist yet |

This document defines the target only. It implements nothing, and no
file besides this one was created or changed to produce it.
