# PE-002 — Research Pipeline Retrospective

**Status:** Confirmed Production Evidence
**Date:** 2026-07-11
**Episode:** The Giant Is The Hostage
**Scope:** Research Package → Research Fact Audit → Claim Refinement.
No architecture, Worker, or Runtime design is proposed by this document.

---

# Summary

This is the first complete run of the pipeline PE-001 identified as
missing: a real Research Package, a Fact Audit run against it, and a
semantic-fidelity pass turning every Partially Supported finding into
something unambiguous. All three artifacts exist and are inspectable:
`research-package-v1.md`, `fact-audit-v2.md`, `claim-inventory-v3.md`.

---

# What worked

- **Separating "what was found" from "what it proves" held up under real
  use.** The Research Package recorded sources without judging them; the
  Fact Audit judged them separately. This mattered concretely: several
  claims (RFA-GIANT-001, 002, 006) had a source that supported *part* of
  the claim under a *different, more specific label* than the claim used
  (commercial RPO vs. "cloud revenue"; a narrow revenue-share scope vs. a
  general one). Judging this required a second pass with fresh eyes on
  precision, not just presence of a citation — exactly what the two-step
  design was for.
- **Real web research closed most of the gap.** Going in, 10 of 13 claims
  were Unsupported. After one real research pass, 8 of 10 factual claims
  had a citable, named source. The topic (a large, heavily-covered public
  company relationship) turned out to have real primary material sitting
  in the open — this was not a case where research was attempted and
  came up empty.
- **The audit correctly refused to reward "a source exists" as good
  enough.** Even with real sources in hand, the second audit
  (`fact-audit-v2.md`) still returned zero Verified claims, because it
  checked wording precision, not just citation presence. That's the
  artifact behaving as designed under real pressure to declare victory
  early.
- **Re-running the same artifact against a different input worked with
  no modification.** `ARTIFACT-SPEC-Research-Fact-Audit-v1.md` was
  written once, then executed twice — once against the Editorial Board
  document, once against the Research Package — without needing a single
  change to the artifact's structure or definitions.
- **Stating "no evidence found" plainly, instead of softening the claim,
  surfaced something a soft version would have hidden.** RFA-GIANT-010
  wasn't just unsupported — the one relevant primary statement found
  (Microsoft's CFO, on the record, downplaying concentration risk) leans
  *against* it. That distinction only became visible because the
  research was recorded honestly rather than smoothed into a generic
  "insufficient evidence" note.

# What failed

- **Zero claims reached Verified on first pass, for every single factual
  claim in the episode.** Not one of the ten original claims was written
  precisely enough to match a real source exactly. Every claim that
  eventually became Verified only got there by being narrowed — none by
  finding stronger evidence. This is a pattern across the whole set, not
  one bad claim.
- **Two claims could not be resolved even after real, successful
  research** (RFA-GIANT-007, RFA-GIANT-008 — the equity stake value and
  the $13B original investment). The blocker wasn't absence of sources —
  multiple independent secondary sources converged on the same figures —
  it was that the primary filing itself (Microsoft's SEC 10-Q) could not
  be read directly. SEC.gov returned HTTP 403 to automated fetching, and
  Microsoft's own investor-relations document mirror timed out twice.
  This is a concrete, repeatable access barrier, not a one-off.
- **Two claims were permanently unresolvable regardless of research
  quality** (RFA-GIANT-009, RFA-GIANT-010). Both were introduced during
  script drafting itself, after the Editorial Board comparison, with no
  research behind them at all. No amount of research or rewording after
  the fact fixes a claim that was invented downstream of where research
  happens — the order of operations, not the research effort, is what
  failed here.

# What surprised us

- **The central, most-suspected claim wasn't fabricated — it was
  mislabeled.** The 45% figure is real, specific, and traceable to a
  named Microsoft executive's exact words on an official earnings call.
  It just describes "commercial RPO," not "future cloud revenue" as the
  episode's hook states. The number wasn't invented; the metric name
  attached to it was wrong. That's a different — and more fixable —
  failure than the one originally suspected.
- **The size of the precision gap was larger than the presence of real
  sourcing would suggest.** Going from "no source at all" to "a named
  executive's exact quote" still wasn't enough to reach Verified, in
  every single case. That gap between "well-sourced enough for a
  documentary hook" and "verified under strict semantic fidelity" turned
  out to be consistent and large, not occasional.
- **Research access, not research existence, was the harder constraint.**
  For a well-covered public company topic, finding *some* real source was
  easy. Reading the actual primary document (the SEC filing itself) was
  the part that failed, twice, for tooling reasons unrelated to whether
  the underlying fact was true.
- **The one claim that couldn't be sourced was also the one claim the
  evidence pushed back on.** Not every unsupported claim is silent —
  at least once, the missing evidence turned out to be missing because
  the claim was already leaning the wrong way, not because no one had
  looked.

# What should change before the second episode

Only conclusions the above evidence actually supports — not new design:

- **Claims need to be checked against sources before drafting uses them,
  not after.** RFA-GIANT-009 and RFA-GIANT-010 are the two claims that
  proved permanently unfixable, and both share the same origin: they
  entered the episode after the point where anyone was checking sources.
  Every other claim, however imperfectly worded, at least traced back to
  something in the Editorial Board material and was eventually
  resolvable. Ordering, not effort, is the evidenced fix.
- **Claims should default to source-level precision, not rounded,
  dramatic language, at the point they're first written.** Every claim
  that became Verified did so by losing a qualifier ("purely," "the
  machines," "cloud revenue" generalized from "commercial RPO"). None
  needed a stronger source — they needed to have been narrower from the
  start. This suggests the drafting habit itself (round up for impact) is
  the recurring source of the gap, evidenced across essentially the
  entire claim set, not an isolated wording accident.
- **Whatever produces or checks a Research Package next needs a real
  answer for primary documents that block automated access.** This
  happened twice in one episode's research (SEC EDGAR, Microsoft's own
  investor-relations mirror) and stopped two claims from ever reaching
  Verified despite strong convergent secondary evidence. This is stated
  as an observed constraint, not a proposed fix — no mechanism is
  designed here.
- **Expect compound claims, not just imprecise ones.** Two of eight
  Partially Supported claims (RFA-GIANT-002, RFA-GIANT-006) turned out to
  bundle a well-evidenced core with a separately unevidenced extension,
  and had to be split into two claims rather than resolved as one. This
  happened often enough in a ten-claim set that it should be expected
  again, not treated as an edge case if it recurs.
