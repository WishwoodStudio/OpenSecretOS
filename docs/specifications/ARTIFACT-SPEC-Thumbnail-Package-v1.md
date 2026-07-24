# ARTIFACT-SPEC: Thumbnail Package v1

**Status:** Proposed — not yet ratified, not added to `canonical/`, not
added to `SPEC-001` or `SPEC-Director-Worker-v1`. Written the same way
as `ARTIFACT-SPEC-Research-Fact-Audit-v1.md`,
`ARTIFACT-SPEC-Research-Package-v1.md`, and
`ARTIFACT-SPEC-Opening-Typography-Package-v1.md`: a new, narrow artifact
type discovered through real production, proposed for review.

**Standalone from the outset:** per the same reasoning
`ARTIFACT-SPEC-Opening-Typography-Package-v1.md` was revised to (§ that
document's "Promoted to a standalone artifact"), this is specified
directly as a standalone artifact — own lifecycle, own version, own
repository location — that the Director Package *references*, not
owns. See §9.

**What this is not:** a redesign of the Visual Identity System, and not
a second copy of the Opening Typography Package. A thumbnail is seen
*before* a viewer commits to pressing play — no motion, no audio, no
narration, often at a few hundred pixels in a crowded feed. Opening
Typography works inside video the viewer already chose to watch. This
artifact is specified separately because the job is genuinely different,
not because the visual language changes.

---

## 1. Thumbnail objective — why a viewer should stop

Everything else in this show's typography exists to land a beat *after*
someone is already watching. A thumbnail has to do something Hook
Pattern 1 (`Visual Identity System v2` §5) was never asked to do:
work with zero motion, zero audio, and zero narration, competing against
every other tile in a feed or grid. The objective is narrower than "hook
the viewer" — it's *make the central contradiction legible as a still
image alone*, so someone deciding whether to tap already knows the shape
of the surprise before they do.

For Luxury Destruction, that contradiction is: a luxury brand destroyed
a large, specific amount of money's worth of its own product, on
purpose. The thumbnail's one job is making that register in under a
second, using the same number the episode itself already uses to do the
same job in motion.

## 2. Primary visual composition

**Base:** the show's own boutique-interior register (`Block A`), not a
new scene. Reusing the already-generated/approved establishing shot
(or a still pulled from it — see §7) keeps the thumbnail visually
continuous with the video it represents, rather than promising a
different show than the one that plays.

**Deliberately not shown:** literal destruction, fire, or damage
imagery. The Visual Identity System's own philosophy (§1: "Analytical...
Quiet confidence. No hype energy") already rules this out — showing
something dramatic to match the word "Burned" would be exactly the
"hype energy" the existing identity is built against. The tension this
thumbnail relies on is the *contrast* between a calm, elegant,
documentary-still boutique image and a shocking number sitting on top of
it — the image stays restrained; the text carries the shock.

**Composition:** same framing logic as Block A's own generation spec —
racks receding into shallow depth of field, negative space reserved on
the left third for the headline (`prompts/higgsfield/block-a.md`'s
existing composition note, reused here rather than re-specified).

## 3. Exact headline text

**Design principle (added following first production review):**

> The opening thumbnail headline should communicate the strongest
> literally true fact available in the episode, even if it is initially
> surprising. The explanation belongs to the video, not the thumbnail.

This replaces the previous headline rationale, which selected wording
mainly for brevity and continuity with the Opening Typography Package.
The principle requires the same wording to now be justified on its own
terms: is it the *strongest available true fact*, not merely a short,
convenient one.

**Candidates evaluated, all sourced from the locked script and its
underlying disclosures — none invented for this exercise:**

| Candidate | True? | Strongest available? | Verdict |
|---|---|---|---|
| **£28.6 million, burned** (Beat 1) | Yes — Burberry's own 2017/18 disclosure; the show's own QA rules already confirm "burned" is the accurate verb specifically for Burberry's method (incineration), distinct from Richemont's | Standalone-complete: no qualifier needed to avoid misstating scope or timing | **Selected** |
| £90 million, over five years (Beat 2) | Yes | Larger number, but *only* accurate with "over five years" attached — compressed to thumbnail length without that qualifier, it misstates a five-year cumulative total as a single event | Rejected — fails the accuracy half of the principle at the length the format allows |
| €481 million, Richemont/Cartier (Beat 3) | Yes | Larger number still, but the show's own established QA rule requires "took apart," not "burned," for this company's method — a thumbnail short enough to pair a big number with "BURNED" would misattribute both the actor (Cartier vs. its parent Richemont) and the method | Rejected — the only candidate that risks an actual factual error at thumbnail brevity, not just a lost nuance |
| The mechanism itself ("destroying it is cheaper") | Yes, but only once the video has explained *why* | Would be the most surprising claim if it landed — but requires context the thumbnail doesn't have room for | Rejected — this is exactly what the principle's second sentence excludes: the explanation belongs to the video |

**Recommended headline, confirmed under the new principle rather than
carried over unchanged by default:**

- Line 1 (large): **"£28.6 MILLION"**
- Line 2 (short): **"BURNED."**

Both words are already locked in the script's Beat 1 VO and already
used in the Opening Typography Package's Line 2 ("Of its own clothes.
Burned."). Of the four candidates actually compared, it's the only one
that's both maximally surprising *and* fully accurate standalone, with
no qualifier the thumbnail's length can't afford to include.

## 4. Typography treatment

Space Grotesk ExtraBold for both lines — thumbnail text has no room for
a secondary, smaller-weight line the way in-episode cards do; both lines
need to read at a glance. Color: Primary `#EDEAE2` on the dark boutique
background, per `Visual Identity System v2` §3/§4 — not Amber, even
though Amber is the system's "money" color elsewhere: Amber specifically
means *recovered* money in the existing color system (the diagram's
`$490 recovered` bar). This number is destroyed money, the opposite
case — using Amber here would borrow a color that already carries a
different, specific meaning. Primary avoids that collision.

Scale: headline should occupy roughly 35–45% of frame height combined —
substantially larger proportionally than any in-video typography card,
because a thumbnail is viewed at a fraction of the size and for a
fraction of the time.

## 5. Safe placement

Left third of frame (same reserved negative space as Block A itself),
vertically centered to slightly upper. Kept clear of:
- **Bottom ~20–25%** — where TikTok, Shorts, and Reels all place feed
  chrome (captions, like/comment/share, duration badges, view counts
  depending on surface).
- **Top ~10%** — where some grid/shelf views place profile or
  notification overlays.

This is the same safe-zone reasoning already established in the Opening
Typography Package spec, applied to a static frame instead of a moving
one — the constraint doesn't change based on whether the frame moves.

## 6. Image generation brief (Higgsfield or equivalent)

If generating a dedicated still rather than pulling one from existing
footage (§7), reuse Block A's own approved prompt almost unchanged —
deliberately, not as a new creative brief:

> Upscale clothing boutique interior, garment racks in soft focus, warm
> ambient light, no legible signage. Documentary-grade stillness, not
> fashion-ad energy — quiet, controlled mood with a slightly cold
> undertone beneath the warmth. Warm key light, cool rim light, low
> contrast. Racks receding into shallow depth of field, left third of
> frame empty. No legible text, no logos, no brand patterns, no faces,
> no fast motion, no lens flares.

Differences from Block A's video prompt, both mechanical, not creative:
drop the camera-movement line (a still needs none), and request a
portrait still image rather than a video duration/fps. Model/parameter
selection (which Higgsfield image model, aspect ratio, resolution) isn't
specified here — that needs a live check against Higgsfield's current
image-model catalog before submission, the same way the video model
selection for Blocks A–E was verified against the real tool rather than
assumed.

## 7. Editing instructions if manual composition is preferred

The lower-cost, zero-new-generation option: extract a still frame
directly from the already-rendered `block-a_v1_seedance2mini.mp4`
(`assets/Generated/block-A/`) at a moment where the push-in hasn't
progressed far enough to lose the left-third negative space, then
overlay the two-line headline from §3–5 in an image editor or directly
in CapCut as a static export. This reuses a real, already-approved,
already-paid-for asset instead of generating a new one, and guarantees
visual continuity with the actual opening shot rather than a
similar-but-different generated alternative.

## 8. Rationale

Every choice above traces to something already established: the
contradiction comes from Hook Pattern 1, the base image comes from
Block A, the restraint comes from the identity's own "no hype energy"
philosophy, the color comes from the existing system's own semantic
rule (and specifically avoids misusing it), the trimmed wording follows
the same excerpting discipline every other typography card already
uses, and the safe-zone logic is the same one just established for
Opening Typography Package, extended from a moving frame to a still one.
Nothing here introduces a new visual idea — it applies the existing one
to a context (pre-play, feed-scale, silent) the identity hadn't been
asked to work in yet.

## 9. Relationship to the Director Package

Referenced, not owned — same relationship as Voice Package, the CapCut
Assembly Package, and the Opening Typography Package already have to
Director Package. `director-package-v*/asset-manifest.md` should cite
the Thumbnail Package by artifact ID as a dependency; it should not
contain the thumbnail's content inline.

## 10. Repository location

**Per-episode instance**, its own top-level folder, sibling to
`script/`, `voice/`, `assembly/`, `opening-typography/`, and
`director-package-v*/`:

```
episodes/<episode-id>/thumbnail/
  thumbnail-package-v1.md
  thumbnail-v1.png   (or the final composited image asset)
```

For Luxury Destruction:
`episodes/luxury-destruction/thumbnail/thumbnail-package-v1.md` — not
created by this document; this is the target path for a future write.

**Specification (this document):** `docs/specifications/`, same
location as every other artifact-type spec, not inside any episode
folder.

**Not recommended:** `canonical/`, or merging into `Visual Identity
System v2` directly. Same standard as the other proposed artifacts —
one episode of evidence earns a review, not automatic canonical status.
