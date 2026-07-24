# Voice Package v1 — Luxury Destruction

**Artifact ID:** `voice-package-luxury-destruction-v1`
**Episode ID:** luxury-destruction
**Version:** 1
**Status:** Generated (production-ready for submission — no audio has
been generated yet; this package is the input spec, not a confirmed
render)
**Owner:** Voice (manual — no Voice Worker implemented)
**Input dependency:** `script/script-package-v3.md` — **locked,
immutable.** The narration text below is reproduced verbatim, beat by
beat, with zero wording changes. All pacing, pronunciation, and emphasis
guidance in this package is metadata alongside the text, never inserted
into it — nothing here modifies the script.
**Output consumers:** Production (rendering — needs real word-level
timestamps to finalize `director-package-v3/shot-list.md`'s timing
column), Subtitle Package (not yet produced), QA
**Last updated:** 2026-07-12

---

## Submission text (single continuous take)

Production practice for this episode (per the source Production
Package's own CapCut Assembly Instructions) treats narration as one
continuous take, not eight spliced clips — natural breath and pacing
carry across beat boundaries. **Submit the full text below to ElevenLabs
in one generation call.** The beat segmentation in the next section is a
reference map for syncing the resulting audio, not eight separate
submissions.

> Burberry burned £28.6 million of its own clothes.
>
> Every year: "finished goods physically destroyed." Ninety million
> pounds, over five years.
>
> Burberry wasn't alone. Cartier's parent company, Richemont, spent 481
> million euros buying back its own unsold watches — then took them
> apart.
>
> Two different companies. Same decision: zero dollars, on purpose,
> instead of a discount. Why?
>
> Because a marked-down coat isn't one lost sale. It's a public price tag
> — visible to every full-price customer — for the entire collection.
>
> So it's never "destroy it" versus "sell it for something." It's
> "destroy it" versus "quietly discount everything else, too." Count it
> that way, and zero is the cheaper number. This is the markdown tax.
>
> Burberry stopped in 2018; France banned it in 2022.
>
> So the next time a brand protects its scarcity — a waitlist, a restock
> kept deliberately tiny — there's a different way to read it. It's not
> exclusivity built for you. It's the markdown tax, paid in a different
> currency: your attention, your patience, the appeal of being let in.
>
> Is that exclusivity? Or is it the markdown tax?

This is character-for-character identical to `script-package-v3.md`'s
Final Script. 177 words.

---

## Pronunciation notes

Carried forward unchanged from the source Production Package (§11) —
unaffected by the script compression, since none of these three names
were touched.

| Term | Pronunciation |
|---|---|
| Burberry | "BUR-ber-ee" |
| Richemont | "REESH-mohn" (silent final "t") |
| Cartier | "kar-tee-AY" |

**Numeral/currency check (new, added for this package):** confirm the
model reads "£28.6 million" as "twenty-eight point six million pounds,"
not a literal currency-symbol misread. "481 million euros" and "Ninety
million pounds" are already spelled out in the script text and carry no
similar risk. Flag in QA if the £ figure renders oddly on first
generation — this is a generation-check item, not a script change.

---

## Pause guidance

Two intentional pauses, carried forward from the source Voice Package
(§11), both on lines that are unchanged in the locked script:

1. **After "Burberry burned £28.6 million of its own clothes."** — let
   the hook land on its own; do not rush into Beat 2.
2. **After "This is the markdown tax."** — let the name register before
   moving into Beat 7's consequence.

No other pauses beyond the script's own punctuation (periods, em-dashes,
the colon in "paid in a different currency:"). Overall pacing is fast
and conversational per the source material's own direction — additional
pauses beyond these two would work against the 58–59s target this
package exists to hit.

---

## Emphasis guidance

Adapted from the source Voice Package (§11) to the locked script's actual
wording — three of the original emphasis points reference phrases that
were cut during compression ("same line," "wasn't the only one," and the
old beat 8a/9 labels); each is mapped below to the equivalent surviving
phrase that carries the same direction. Nothing here is a new creative
addition — each note traces to an emphasis instruction that already
existed in the source material.

| Beat | Phrase to emphasize | Direction |
|---|---|---|
| 1 | "burned" | Flat delivery, no defensive inflection |
| 2 | "finished goods physically destroyed" | This is the quoted disclosure line — where the claim earns its proof; give it slightly more weight than surrounding text |
| 3 | "alone" (in "wasn't alone") | Carries the pattern-not-anomaly point (source's original note was on "wasn't the only one" — same word, same function, shorter phrasing after compression) |
| 4 | "Why?" | Genuine question inflection, not rhetorical-flat |
| 5 | "public price tag" | Carries the reframe from "discount" to "signal" |
| 6 | "the markdown tax" | The thesis name — slow down slightly even within the fast register |
| 8 | "a different way to read it" | Personal-stake pivot — deliver as an invitation, not a warning |
| 8 | "Is that exclusivity? Or is it the markdown tax?" | Genuine question inflection — this is the line the source material's own notes flag as most likely to be quoted in comments |

---

## Recommended ElevenLabs settings

No canonical document (Decision Log v2, Visual Identity System v2,
Production Playbook v1, or the source Production Package) specifies
exact API parameters or a named voice — these are production
recommendations based on the established creative direction ("Analytical
... Quiet confidence. No hype energy," Visual Identity System v2 §1; "Fast,
conversational" pacing, source Production Package §11), not a canonical
requirement. Treat as a starting point to audition against, not a locked
setting.

| Parameter | Recommendation | Why |
|---|---|---|
| Voice | **Not yet selected — open decision.** No prior artifact names one. Needs a voice capable of both a flat/deadpan hook delivery and a genuine-question inflection, in a documentary/analytical register. | Nothing in `canonical/` specifies a narrator voice |
| Model | `eleven_multilingual_v2` | Reliable prosody and pacing control for a short, precisely-timed narration; multilingual model handles Richemont/Cartier's French pronunciation cleanly |
| Stability | 0.45–0.55 | Needs to support three distinct deliveries (flat hook, genuine questions, thesis-name slowdown) without sounding unstable |
| Similarity boost | 0.75–0.85 | Voice consistency across the single continuous take |
| Style exaggeration | 0.10–0.20 (low) | Matches "no hype energy" — avoid an overly performative read |
| Speaker boost | On | Standard for clean narration output |
| Output | Request word-level timestamps/alignment data | Required — every downstream timing figure in this package and in `director-package-v3/shot-list.md` is an estimate until real timestamps exist |

---

## Expected timing per beat (planning estimate)

Carried forward directly from `director-package-v3/shot-list.md` — word-
count-pace estimate, not confirmed. Restated here as the specific
prediction this Voice Package's real output will be checked against.

| Beat | Text starts with | Expected start | Expected end | Expected duration |
|---|---|---|---|---|
| 1 | "Burberry burned..." | 0:00 | 0:05 | 5s |
| 2 | "Every year..." | 0:05 | 0:10 | 5s |
| 3 | "Burberry wasn't alone..." | 0:10 | 0:17 | 7s |
| 4 | "Two different companies..." | 0:17 | 0:22 | 5s |
| 5 | "Because a marked-down coat..." | 0:22 | 0:29 | 7s |
| 6 | "So it's never..." | 0:29 | 0:40 | 11s |
| 7 | "Burberry stopped..." | 0:40 | 0:43 | 3s |
| 8 | "So the next time..." | 0:43 | 0:58 | 15s |

**Total expected runtime: 0:58 (58 seconds).**

---

## Timing verification protocol (for when real audio is generated)

This package has not yet been submitted to ElevenLabs. When it is:

1. Pull word-level timestamps from the generation output.
2. Map them onto the 8 beat boundaries above.
3. **If total runtime lands at 58–59s and no single beat drifts
   substantially from its estimate:** update `director-package-v3/shot-list.md`'s
   timing column to the real timestamps. That file is a derived planning
   document, not the locked script — re-anchoring it to real data is
   expected maintenance, not an edit to the script.
4. **If total runtime falls outside 58–59s, or any beat's real timing
   diverges sharply from its estimate (Beat 7's planned 3-second window
   is the most likely candidate, per the production issue already
   flagged in `director-package-v3/shot-list.md`):** do not shorten,
   reword, or otherwise edit `script-package-v3.md` to compensate. Log
   the actual figures as a new dated entry in `production-log.md`,
   exactly as the original 58s-vs-76s conflict was handled — evidence
   first, no silent correction. That entry is what would trigger a future
   editorial decision, not this package.

`script-package-v3.md` remains locked and immutable regardless of what
real generation produces.
