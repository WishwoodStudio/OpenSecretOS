# MILESTONE-001 Review

**Status:** Analytical review of repository state as of this commit
boundary. Not promotional. Written to answer one question: is the
project becoming more capable, or just producing more documentation?
No new architecture, Workers, Runtime components, or specifications are
introduced by this document.

---

# 1. Objective

At the start of this iteration, the goal was to turn eighteen freeform
architecture drafts into an operating repository for Open Secret's video
production — one where the repository itself, not chat history, could
answer what's true, what's happening, and what should happen next (per
`docs/drafts/OS-001`'s own framing). That meant three things in
sequence: design the Engine's architecture and get it to survive its own
internal review; implement the smallest possible real vertical slice to
test whether the design actually holds up under construction; and then
use that slice on real, messy production material — not synthetic
demos — to find out what breaks.

# 2. What was actually built

By capability, not filename:

- **A reviewed, internally-consistent architecture.** `SPEC-001`
  consolidates the Engine/Runtime/Workers/`.claude` split, the
  Contract/Manifest/Production-Graph model, and five explicitly unresolved
  Open Questions — and it has not needed a single amendment since being
  baselined, despite everything built on top of it since (see §4).
- **The ability to specify a Worker completely before building it.**
  `SPEC-Director-Worker-v1` is implementation-grade: inputs, outputs,
  validation rules, failure conditions, and a Future Skill mapping — and
  it was later actually followed to build a real Skill (below), not just
  filed away.
- **A real, tested Repository Resolver.** Path resolution proven
  independent of shell working directory — not asserted, verified by
  invoking it from an unrelated directory and confirming identical
  output.
- **A real Manifest** that reports Demo Episode state from the actual
  filesystem — narrowly scoped to two artifacts, with a known,
  documented, still-unfixed responsibility-boundary issue (§4).
- **A written behavioral contract for Runtime components that don't exist
  yet.** `ACCEPTANCE-TESTS-Runtime-v1.md` defines Repository Resolver,
  Manifest, and Worker Dispatcher's required behavior in Given/When/Then
  form, ahead of Worker Dispatcher ever being implemented.
- **A real Director Package, produced twice, from real material.** The
  Luxury Destruction episode's Production Package was extracted into a
  Director Package by hand (v1, no canonical access), then regenerated
  once real canonical documents arrived (v2), with a full comparison
  report — proving the manual process could actually be repeated and
  produce a materially different, better-justified result the second
  time.
- **A real, tested, executable Director Skill.** Not a stub — code that
  locates inputs by content pattern (because `canonical/` has no fixed
  naming convention, discovered the hard way), detects stub/placeholder
  canonical documents automatically, writes the correct output structure,
  and mechanically validates its own output. Tested against real data:
  it independently rediscovered the exact Content Constitution stub a
  human had found by reading the file, using nothing but a generic
  length/pattern heuristic.
- **A full, real editorial production capability**, demonstrated on a
  second episode from scratch: three independently-evaluated hook
  structures varying one variable (reveal timing), a factual-precision
  editorial polish pass that caught a real factual error ("built" vs.
  "helped fund"), a mechanism-reveal script with disciplined one-fact-
  per-diagram-change pacing, and a caught, named demand-vs-return-
  mechanism causal gap.
- **Two new production artifact types, one already executed for real.**
  Research Fact Audit (designed, then run once — 13 claims, 0 verified)
  and Research Package (designed specifically to prevent the failure the
  audit found) — both deliberately kept outside `SPEC-001`, not yet
  Contracts.
- **A pure production-process description**, independent of any
  implementation detail (`PRODUCTION-FLOW-v1.md`), which itself surfaced
  three real naming/ownership gaps in the underlying architecture
  (Subtitle Package not in the Contract list, no name for rendered media,
  no publishing integration named anywhere).

# 3. Production evidence discovered

Only findings backed by an actual production attempt.

- **Missing Fact Audit.** Confirmed twice, independently: once in
  `episodes/the-giant-is-the-hostage/research-gap-report-45-percent-claim.md`
  and again in `docs/production-evidence/PE-001_Missing_Fact_Audit.md`.
  The episode's central statistic (45% of Microsoft's future cloud
  revenue depending on OpenAI) has no primary source anywhere in the
  available material. The system's actual behavior when it hit this gap
  is itself evidence, not just the gap: it stopped and reported the
  missing evidence rather than inventing an explanation or quietly
  softening the claim.
- **Missing Research Package.** The full Fact Audit
  (`episodes/the-giant-is-the-hostage/research/fact-audit-v1.md`) found
  this wasn't limited to the headline number — **10 of 13 audited claims
  were Unsupported**, including claims already locked into produced
  script lines (hosting, revenue share, equity stake). The upstream
  material was never a Research Package with claim-to-source mapping; it
  was an editorial comparison document that assumed its own factual
  defensibility.
- **Editorial Board limitations.** The Board's own document self-declares
  "No research performed. Both concepts assumed fully factually
  defensible." Concretely, this let facts from the *rejected* concept
  (Concept A: hosting, revenue share, equity stake, the $13B figure) get
  cross-borrowed into the *chosen* concept's actual production (Concept
  B) without their own sourcing ever being independently checked —
  confirmed in the Fact Audit as RFA-GIANT-004 through 008.
- **Director Skill validation behavior.** Confirmed working as intended,
  not just as designed: `check-canonical-doc.mjs` correctly flagged
  Content Constitution v4 as a stub and correctly confirmed the other
  four canonical documents as real, automatically and without hints,
  reproducing a finding a human had made by hand. `locate-inputs.mjs`
  correctly resolved all five real canonical documents despite
  inconsistent real-world filenames the design hadn't originally assumed.
  `validate-director-package.mjs` correctly passed a real, complete
  Director Package and correctly failed with accurate detail against a
  nonexistent one.
- **Canonical validation findings.** Once real canonical documents became
  available: the Luxury Destruction source package's own claimed
  canonical basis ("Duration Philosophy," no fixed runtime target) does
  not exist anywhere in the real Decision Log v2 or Visual Identity
  System v2 — both state a hard 58–59 second target, contradicting the
  source material's own justification for its ~76 second runtime. Set
  against that, most of the same package's other creative decisions
  (color use, typography, motion principles, the Purple Rule, Real
  Artifacts First) turned out to already match the real canonical text
  closely, without having had access to it at the time.

# 4. Architectural changes justified by production

Deliberately short. Most production evidence this iteration justified
new *artifacts*, not changes to `SPEC-001` itself — which has not been
amended since baseline.

- **Manifest-does-not-orchestrate is now evidence-confirmed, not just
  specified.** `SPEC-001` §7/§11 already stated that Manifest reports
  state and Worker Dispatcher decides execution. Building Manifest v1
  actually violated this (it still computes `activeWorker` and
  `nextExpectedArtifact` directly — confirmed still present in
  `engine/manifests/manifest.mjs` as of this review) before the
  violation was caught by review and formalized as a required behavior
  in `ACCEPTANCE-TESTS-Runtime-v1.md` (MF-6, explicitly marked
  "Currently violated"). This is real evidence *for* the existing
  principle, surfaced by a real attempt to build around it — but the
  code fix itself has not yet been applied. Listed here as justified,
  not as done.

No other `SPEC-001` amendment is justified by evidence gathered this
iteration. Everything else in §2 that looks architectural (Research Fact
Audit, Research Package) was deliberately designed to sit outside the
frozen architecture, not to change it.

# 5. Architectural ideas deliberately rejected

Insufficient evidence, not rejected on merit:

- **Fact Audit Worker** — the artifact it would produce was designed and
  run by hand instead, specifically to learn what the artifact needs to
  contain before automating its production.
- **Research Worker** — Research Package's *shape* was designed
  (`ARTIFACT-SPEC-Research-Package-v1.md`), but nothing produces one yet;
  no evidence exists yet on what a Worker doing this would actually need
  to do beyond what a human did by hand.
- **Worker Dispatcher implementation** — its required behavior is fully
  specified (acceptance tests), but not built. Building it now would mean
  encoding assumptions about dispatch logic that no real multi-Worker
  run has ever tested.
- **The Importer** (general external-input-handling mechanism,
  recommended in earlier architecture review) — Sprint 1 used manual
  seeding instead for its narrow two-artifact case; no second, different
  kind of external input has yet been handled to justify generalizing.
- **Populating all nine `engine/contracts/` schemas** — only the two
  Contracts Director Worker actually touches were populated; the other
  seven remain unbuilt because nothing has yet needed them.
- **Renaming the `higgsfield/` integration folder** to match Decision Log
  v2's actual named tools (Runway/Kling) — flagged explicitly as a
  finding in the Luxury Destruction comparison report, deliberately left
  alone because changing it is an Engine decision, not a production one.
- **Resolving the OS-016 "Confidence Assessment" vs. Fact Audit overlap**
  — flagged as an open question in the Fact Audit's own artifact spec,
  intentionally left unresolved pending a second real case.

# 6. Current production pipeline

As it actually exists today, not as designed:

1. A human selects a topic and produces editorial concept comparisons —
   entirely manual; no Worker exists for this step.
2. A human places source material directly into the repository
   (canonical documents, Production Packages, research files) — there is
   no Importer; every real input this iteration arrived by being placed
   directly into the correct location.
3. Canonical documents, once present, can be automatically checked for
   real content vs. placeholder status via the Director Skill's
   `check-canonical-doc.mjs` — the one point in the entire pipeline where
   a check that used to require a human reading a file by hand now
   happens in code.
4. A Script Package is extracted from source material by hand — no
   Editorial Worker exists.
5. A Director Package is produced either by hand (Luxury Destruction) or
   by following the Director Skill's procedure directly (its mechanical
   scripts handle input location, stub detection, output structure, and
   structural validation; the actual extraction and citation work is
   still performed by whoever — human or Claude — is executing the
   Skill, exactly as `SKILL.md` describes).
6. Editorial refinement (hook variants, polish, mechanism reveal) happens
   entirely as direct, chat-mediated human/AI collaboration, with
   artifacts saved at each step — no automation, no Runtime involvement.
7. A Research Fact Audit can be run by hand against whatever source
   material exists, following the new artifact spec, producing a
   claim-by-claim record.
8. When a gap is found (missing source, contradicted claim, missing
   document), it is recorded as production evidence in the episode
   workspace or `docs/production-evidence/` rather than patched over or
   used to justify an immediate architecture change.

Nothing currently connects these eight steps automatically. Every
transition is a manual instruction in a chat session. Exactly one piece
of real, reusable, tested code (the Director Skill's scripts) exists
inside this pipeline; everything else is either a human/AI-collaborative
process producing durable artifacts, or a narrowly-scoped implementation
(Repository Resolver, Manifest) proven only against the Demo Episode's
two-artifact case.

# 7. Current maturity assessment

- **Architecture:** mature relative to what has actually been tested
  against it. `SPEC-001` has absorbed a real implementation attempt
  (Manifest) and a real Skill build (Director Worker) without needing
  amendment. This is a meaningfully strong signal, but it reflects depth
  in a narrow slice, not breadth — most of the architecture (Contracts,
  Production Graph, five of seven Workers, Worker Dispatcher) remains
  entirely untested by any real attempt.
- **Production readiness:** low. One episode (Luxury Destruction) has a
  complete, real Director Package built from real source material and
  real canonical documents. A second episode (The Giant Is The Hostage)
  has real, rigorous editorial development but is currently and
  correctly stalled — its central claim has no verified source, and the
  pipeline halted rather than proceeding past that gap. Zero episodes
  have reached Production, Voice, QA, or Publishing.
- **Automation readiness:** low. Exactly one component (the Director
  Skill's mechanical scripts) is real, tested, reusable code operating
  without hand-holding. Repository Resolver is real but only exercised
  in the narrowest possible case. Manifest, Worker Dispatcher, and every
  Worker except Director remain either unbuilt or unautomated.
- **Editorial readiness:** the strongest area by a clear margin. Real
  hook-structure comparison, real factual-precision correction, real
  diagram-pacing discipline, and a real fact-audit process have all been
  demonstrated on genuine material, not toy examples. This entire
  capability is currently 100% manual/AI-collaborative, not automated —
  its strength is in the *process*, not in any code.

**Biggest remaining bottleneck: verified research, not architecture or
automation.** Every other capability now has at least one real, tested
proof point. Research does not. Nothing in this repository has ever
produced a properly-sourced claim from scratch — the one artifact
designed specifically to enable that (Research Package) has never been
used to produce one. This is also the exact thing currently blocking
real progress on the one episode still in active development.

# 8. Recommended next milestone

**Produce one real, sourced Research Package for "The Giant Is The
Hostage," by hand, and re-run the existing Research Fact Audit against
it.**

Not a Research Worker, not Runtime changes, not further architecture —
per this review's own §7 finding, none of those are the bottleneck.
This milestone directly tests the two artifacts designed but never used
in anger (`ARTIFACT-SPEC-Research-Package-v1.md`,
`ARTIFACT-SPEC-Research-Fact-Audit-v1.md`) against the exact real
conditions they were designed for, and it is the only currently-known
action that could actually unblock the one piece of real production work
sitting stalled in this repository right now. If a sourced Research
Package genuinely turns some of the 10 currently-Unsupported claims into
Verified or Partially Supported, that's real evidence the two-artifact
design works. If it doesn't — if primary sources for this specific topic
turn out not to exist — that's equally real evidence, just of a
different and still valuable kind. Either outcome teaches more than
building another Worker on top of an unproven foundation would.
