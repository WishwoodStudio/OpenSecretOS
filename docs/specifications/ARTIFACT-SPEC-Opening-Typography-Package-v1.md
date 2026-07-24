# ARTIFACT-SPEC: Opening Typography Package v1

**Status:** Proposed — not yet ratified, not added to `canonical/`, not
added to `SPEC-001` or `SPEC-Director-Worker-v1`. This document lives
here, alongside the other artifact specs written the same way
(`ARTIFACT-SPEC-Research-Fact-Audit-v1.md`,
`ARTIFACT-SPEC-Research-Package-v1.md`), for the same reason: it's a
new, narrow artifact type discovered through real production, proposed
for review, not silently folded into an existing canonical document.

**Promoted to a standalone artifact (this revision):** earlier drafts of
this spec recommended Opening Typography Package live as a sub-section
of the Director Package's Typography Package. On review, that's wrong
for the same reason Voice Package and the CapCut Assembly Package aren't
sub-sections of Director Package either: it's a distinct artifact with
its own lifecycle, own version history, and its own single owner. It is
now specified as a standalone artifact, produced once per episode,
independently versioned, that the Director Package *references* as an
input dependency rather than *contains*. See §5.

**What this is not:** a redesign of the Visual Identity System. Every
rule below is either a direct citation of an existing rule already in
`Visual Identity System v2`, or explicitly marked as new and justified
on its own.

---

## 1. Problem this addresses

Every episode already has a typographic hook — Hook Pattern 1 ("The
Impossible Number," `Visual Identity System v2` §5) already governs
*what* the opening number-card says. What doesn't exist anywhere is a
spec for *how* that first card behaves in its first frames specifically
— its fade timing, its exact placement, and its treatment as distinct
from every other typography card in the episode. In practice, the
opening card has been using the same generic build-in as every other
card (`Visual Identity System v2` §6: opacity 0→100 over 200–300ms).
That's correct for a card interrupting a shot already in progress. It's
the wrong choice for the literal first frame of the episode, where a
0.2–0.3s fade means the frame most likely to be seen by a scrolling
thumb — frame zero — carries no legible text at all.

## 2. Opening Typography Package — reusable specification

| Requirement | Rule |
|---|---|
| Appears within 1–2s | Number line present from **frame 0**, not merely "by 2 seconds" |
| Communicates the contradiction/surprising fact | Content = the episode's Hook Pattern 1 number (§5) — this package doesn't choose the content, it packages the display of whatever number the Hook Rule already selected |
| Very few words | Two lines only: Line 1 = the number (display size), Line 2 = a 2–5 word action/consequence phrase |
| Integrates with the first shot, doesn't replace it | Overlay only — the AI shot underneath stays fully visible; consistent with Documentary Hybrid (§2: AI footage itself carries no legible text) |
| Readable on TikTok/Reels/Shorts | Placement respects platform safe zones (below), sized for mobile legibility |
| Follows existing typography/color rules | Space Grotesk ExtraBold (number) / Inter Medium (action line); Primary `#EDEAE2` — no new color introduced |

**The one new rule, not previously specified anywhere, proposed here
explicitly:** the number line's entrance is **not** the standard 200–300ms
build-in. It should be present at or near full opacity from frame 0 (a
fast ~100ms settle at most, not a fade a scrolling viewer can outrun).
Justification: the standard build-in rule was designed for cards that
interrupt an already-rolling shot mid-episode; the opening card is
competing with a thumb mid-scroll, a different job with a different
timing requirement. This is the only place this package departs from an
existing rule, and it departs by *tightening*, not replacing, the
existing motion language (still opacity-based, still fast, still no new
easing/effect introduced).

**Placement:** left third of frame (already reserved — the AI Generation
Package convention for opening/establishing blocks already specifies
"left third empty for typography," e.g. Block A's own composition spec —
this package is filling a slot the shot-generation prompts were already
designed to leave open). Vertically: upper-middle, roughly 35–45% from
the top — clear of both the top status-bar-adjacent zone and the bottom
~20% / right ~15% where TikTok, Reels, and Shorts all place their own UI
chrome (like/comment/share, caption line, username).

## 3. Applied to Luxury Destruction

This uses the episode's own already-locked hook content verbatim — no
new wording. `script-package-v3.md` and `capcut-assembly-package-v1.md`
are not modified; this section documents how the package's *treatment*
rules apply to content that already exists.

0. **Artifact identity:** `opening-typography-package-luxury-destruction-v1`
   — same naming convention as `voice-package-luxury-destruction-v1` and
   `capcut-assembly-package-luxury-destruction-v1`, one more standalone,
   independently-versioned per-episode artifact, not a field inside
   another one.
1. **Specification:** Hook Pattern 1 (Impossible Number), two-line
   number + action structure, frame-0 presence, left-third placement,
   platform-safe positioning.
2. **Exact wording (unchanged, from the locked script):**
   - Line 1: **"£28.6 MILLION"**
   - Line 2: **"Of its own clothes. Burned."**
3. **Font treatment:** Line 1 — Space Grotesk ExtraBold, display size
   (largest text in the episode alongside the reveal caption). Line 2 —
   Inter Medium, secondary size, positioned directly beneath Line 1.
   Both Primary `#EDEAE2` (`Visual Identity System v2` §3/§4) — no
   amber/red/purple use here; those colors are reserved for money-flow,
   cost/loss, and the single mechanism-reveal moment respectively, none
   of which this beat is.
4. **Timing (matches the already-locked shot-list exactly, not
   changed):** Line 1 present 0:00–0:02. Line 2 present 0:02–0:05,
   holding until the hard cut into Beat 2 at 0:05.
5. **Animation:** Line 1 — present from frame 0 at (or within ~100ms of)
   full opacity, per the one new rule above. Line 2 — standard build-in
   (opacity 0→100, 4–8px upward translate, 200–300ms), since by 0:02 the
   episode is no longer competing with the scroll-past moment.
6. **Placement:** left third of Block A's frame, ~35–45% from top —
   matching the negative space Block A's own generation prompt already
   reserved ("left third empty for typography," per
   `prompts/higgsfield/block-a.md`).
7. **Rationale:** every element above already existed in some form —
   the content (Hook Pattern 1's number), the colors (Primary), the
   fonts (Space Grotesk/Inter per the established hierarchy), the
   placement (Block A's own reserved negative space). What was missing
   was a name and a rule tying them together specifically for frame
   zero, plus the one deliberate timing tightening justified by
   scroll-stopping legibility on the three named platforms. Nothing
   here overrides the Hook Rule (§5, first surprise within 3 seconds) —
   it makes the same beat land closer to frame 0 than "by 2 seconds"
   already required.

## 4. Relationship to the Director Package

The Director Package **references** this artifact; it does not own it.
Concretely: `director-package-v*/asset-manifest.md` should cite the
Opening Typography Package by artifact ID as an input dependency for
Beat 1 (the same way it already cites the diagram and the real-artifact
crops as dependencies rather than embedding their content), and the
shot list's Beat 1 entry should point to it rather than re-describing
its timing/placement inline. This mirrors exactly how Voice Package and
the CapCut Assembly Package already relate to Director Package in this
repository — each is produced once, independently, and Director Package
consumes it by reference. Nothing about `director-package-v3/` needs to
change to reflect this for Luxury Destruction specifically, since §3
above already documents the package's content without having written it
into any Director Package file.

## 5. Repository location

**Per-episode instance:** its own top-level folder inside the episode
workspace, a sibling of `script/`, `voice/`, `assembly/`, and
`director-package-v*/` — not nested inside any of them:

```
episodes/<episode-id>/opening-typography/
  opening-typography-package-v1.md
```

For Luxury Destruction, that's
`episodes/luxury-destruction/opening-typography/opening-typography-package-v1.md`
— not created by this document (per instruction, only the specification
is updated here), but this is the path a future write of §3's content
should target.

**Specification (this document):** stays in `docs/specifications/`,
unchanged location — consistent with `ARTIFACT-SPEC-Research-Package-v1.md`
and `ARTIFACT-SPEC-Research-Fact-Audit-v1.md`, which define artifact
types the same way without living inside any episode folder themselves.

**Not recommended:** adding this to `canonical/` or merging it into
`Visual Identity System v2`. That document is canonical and ratified;
this is one production team's proposed pattern, tested on exactly one
episode, and should earn its way into canonical status through review —
not be added by this document unilaterally.
