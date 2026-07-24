# Research Fact Audit — The Giant Is The Hostage (v2)

Second production execution of `docs/specifications/ARTIFACT-SPEC-Research-Fact-Audit-v1.md`,
same structure as v1, run against a different upstream input:
`episodes/the-giant-is-the-hostage/research/research-package-v1.md`
instead of the original Editorial Board document. The artifact itself is
unchanged; only the input and the resulting judgments are new.

## Header

| Field | Value |
|---|---|
| Artifact ID | `fact-audit-the-giant-is-the-hostage-v2` |
| Episode ID | `the-giant-is-the-hostage` |
| Version | 2 |
| Status | Generated |
| Owner Worker | Fact Audit Worker (not yet designed — produced by hand, as in v1) |
| Input Dependencies | `episodes/the-giant-is-the-hostage/research/research-package-v1.md` (v1) — this episode now has a real Research Package to audit against, closing the gap v1 of this audit identified |
| Output Consumers | Editorial Worker, Director Worker, QA Worker (none implemented) |
| Last Updated | 2026-07-11 |
| Approval State | Draft |

---

## 1. Updated verification counts

| Status | v1 (against Editorial Board doc) | v2 (against Research Package) |
|---|---|---|
| Verified | 0 | **0** |
| Partially Supported | 0 | **8** |
| Unsupported | 10 | **2** |
| Editorial Interpretation | 3 | 3 (unchanged) |

Zero claims reached full **Verified** status. This is stated plainly, not
softened: every claim that now has real sourcing behind it also has a
genuine, specific gap between how the claim is worded and what the
source actually says — a rounded or broadened figure, a narrower
qualifier the claim omits, or a specific detail that traces to secondary
reporting rather than a primary document I read directly. Eight of ten
factual claims moved from no evidence at all to real evidence with a
named, specific precision gap. That is the accurate description of what
changed — not "verified," not "still unsupported."

## 2. Which claims changed status

All eight moved Unsupported → Partially Supported. None reached Verified.
None regressed.

| Claim | v1 | v2 | Why not Verified |
|---|---|---|---|
| RFA-GIANT-001 (45% figure) | Unsupported | Partially Supported | Source (Microsoft CFO, Q2 FY26 earnings call) confirms 45% of **commercial RPO**, not "cloud revenue" as the claim states — a related but distinct accounting metric. |
| RFA-GIANT-002 (multi-year contract) | Unsupported | Partially Supported | The 2.5-year duration figure is a blended average across all of Microsoft's commercial RPO, not OpenAI-specific; the 2030/2032 dates come from secondary reporting only. |
| RFA-GIANT-003 (quarterly profit swing) | Unsupported | Partially Supported | Microsoft's own $3.1B disclosure directly supports the dollar magnitude and quarterly timing, but the claim's word "purely" overclaims — Microsoft's profit is affected by many factors, and the source doesn't establish OpenAI as the *sole* driver of its profit swings generally, only of this one disclosed item. |
| RFA-GIANT-004 (ChatGPT has to keep paying) | Unsupported | Partially Supported | Source confirms Azure hosts OpenAI's API infrastructure; it does not itself state a "has to keep paying" billing relationship — that's a reasonable but uncited inference from the hosting fact. |
| RFA-GIANT-005 (Microsoft owns the machines) | Unsupported | Partially Supported | Source explicitly narrows this to "stateless OpenAI APIs" specifically, and separately discloses that Microsoft's broader right of first refusal as compute provider was *removed* in October 2025 — the claim's general phrasing overstates a relationship the primary source itself describes as narrower and non-exclusive outside that one case. |
| RFA-GIANT-006 (Microsoft takes a cut of revenue) | Unsupported | Partially Supported | Microsoft's own blog confirms a revenue-share arrangement exists, but its exact wording ties the shared revenue specifically to "partnerships between OpenAI and other cloud providers" — narrower than "a cut of OpenAI's revenue" generally. The broader 20%-of-all-revenue figure comes from secondary reporting only. |
| RFA-GIANT-007 (equity stake worth many times original) | Unsupported | Partially Supported | The ~27% stake and roughly 10x value multiple are well-corroborated directionally, but the specific $135B valuation figure is secondary reporting on deal terms, not confirmed against a primary filing. |
| RFA-GIANT-008 ($13B original investment) | Unsupported | Partially Supported | Multiple independent secondary sources cite the same figure from the same Microsoft 10-Q consistently — real convergent evidence — but I never read the primary filing itself (SEC EDGAR returned HTTP 403; Microsoft's own filing mirror timed out twice), so this stops short of the artifact's own "named primary source" standard for Verified. |

## 3. Which claims remain Unsupported

RFA-GIANT-009 and RFA-GIANT-010. Both unchanged from v1.

## 4. Why they remain Unsupported

- **RFA-GIANT-009** ("These aren't handshake deals. They're contracts
  running years ahead.") The Research Package itself records this claim
  as "not independently sourced... a dramatized restatement of
  RP-GIANT-002." Its general premise (multi-year contracts exist) now has
  partial support through RFA-GIANT-002, but its specific added content —
  the explicit contrast against "handshake deals" — was never checked
  against any source at all, in either audit. Inheriting a neighboring
  claim's partial support is not the same as being sourced itself; this
  entry stays Unsupported on its own terms.
- **RFA-GIANT-010** ("Walk away, and Microsoft breaks its own growth
  promise.") No source was found in the new research confirming Microsoft
  made a specific growth commitment to investors contingent on the OpenAI
  relationship. More significant than a bare absence: the one relevant
  primary statement found — CFO Amy Hood, on the same earnings call that
  sourced the 45% figure, responding to a direct question about
  concentration risk — actively emphasized portfolio diversification and
  resilience rather than dependency. The available evidence leans against
  this claim, not merely away from it.

## 5. Is the episode ready to proceed to the Editorial Board?

**Conditionally — not as currently worded.**

The evidentiary picture improved substantially: from a script built on
zero sourced claims to one where 8 of 10 factual claims have real,
citable primary-source grounding. That is genuine progress, not just
more paperwork — it's the difference between "we assumed this" and "here
is what a named Microsoft executive said on the record, and here is
exactly how our claim differs from what they said."

But readiness has two separate conditions, and only one is met:

1. **Evidence exists.** Met, for 8 of 10 claims.
2. **The claims as currently worded in the produced script
   (`opening-00-15-version-b-FINAL.md`, `opening-00-15-30-mechanism-reveal-v1.md`)
   match what the evidence actually supports.** Not met. Every
   Partially Supported claim above is partial specifically because the
   script's wording is broader or more rounded than the source — "cloud
   revenue" vs. "commercial RPO," "the machines it runs on" vs.
   "stateless API infrastructure specifically," "purely" vs. "a
   contributing, disclosed factor." None of these gaps require new
   research to close. They require the claims to be reworded to match
   what was actually found — which is editorial work, and out of scope
   for this audit to perform.

**Recommendation:** the two Unsupported claims (RFA-GIANT-009,
RFA-GIANT-010) should not proceed to the Editorial Board as currently
worded — 010 in particular, given the available evidence leans against
it, not just away from it. The eight Partially Supported claims can
proceed, but only if whoever does the next editorial pass tightens each
one's wording to match its actual source precisely, rather than treating
"partially supported" as good enough to leave as-is. This audit does not
perform that tightening — it only identifies, precisely, where it's
needed.

---

No claim's status in this document was inflated or deflated relative to
what `research-package-v1.md` actually contains. `research-package-v1.md`
itself was not modified to produce this audit. Neither was `SPEC-001`,
`ARTIFACT-SPEC-Research-Fact-Audit-v1.md`, nor `ARTIFACT-SPEC-Research-Package-v1.md`.
