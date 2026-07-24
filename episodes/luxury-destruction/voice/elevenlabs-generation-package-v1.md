# ElevenLabs Generation Package v1 — Luxury Destruction

**Artifact ID:** `elevenlabs-generation-package-luxury-destruction-v1`
**Episode ID:** luxury-destruction
**Status:** Generated — ready for submission except one open field (see
§3)
**Basis:** `voice/voice-package-v1.md` (locked spec). Nothing in this
package changes the narration, pacing, or pronunciation guidance already
established there — this document only converts that spec into the
exact text and parameters a single API/UI submission needs. No wording
was altered, no pause or emphasis instruction was added, removed, or
reworded.

---

## 1. Exact submission text

Copy exactly as-is into the `text` field. One string, no line breaks
inserted, matching `voice-package-v1.md`'s "single continuous take"
instruction — this is the same text already reviewed, character for
character identical to `script-package-v3.md`'s locked Final Script.

```
Burberry burned £28.6 million of its own clothes. Every year: "finished goods physically destroyed." Ninety million pounds, over five years. Burberry wasn't alone. Cartier's parent company, Richemont, spent 481 million euros buying back its own unsold watches — then took them apart. Two different companies. Same decision: zero dollars, on purpose, instead of a discount. Why? Because a marked-down coat isn't one lost sale. It's a public price tag — visible to every full-price customer — for the entire collection. So it's never "destroy it" versus "sell it for something." It's "destroy it" versus "quietly discount everything else, too." Count it that way, and zero is the cheaper number. This is the markdown tax. Burberry stopped in 2018; France banned it in 2022. So the next time a brand protects its scarcity — a waitlist, a restock kept deliberately tiny — there's a different way to read it. It's not exclusivity built for you. It's the markdown tax, paid in a different currency: your attention, your patience, the appeal of being let in. Is that exclusivity? Or is it the markdown tax?
```

177 words. The paragraph breaks used for readability in
`voice-package-v1.md` and `script-package-v3.md` are collapsed to a
single line here only because that's the literal string the `text`
field takes — no words, punctuation, or pauses were changed to do this;
periods, colons, em-dashes, and quotation marks are all preserved
exactly, and it's the punctuation (not the line breaks) that was always
carrying the pacing.

---

## 2. Generation settings

| Parameter | Value | Source |
|---|---|---|
| `model_id` | `eleven_multilingual_v2` | `voice-package-v1.md` recommendation, carried forward unchanged |
| `voice_id` | **Not set — see §3** | Never selected in any prior artifact |
| `stability` | `0.50` | Midpoint of `voice-package-v1.md`'s recommended 0.45–0.55 range — a range isn't a submittable value, so the midpoint is used as the single exact number, not a new creative choice |
| `similarity_boost` | `0.80` | Midpoint of the recommended 0.75–0.85 range, same reasoning |
| `style` | `0.15` | Midpoint of the recommended 0.10–0.20 (low) range, same reasoning |
| `use_speaker_boost` | `true` | Unchanged from recommendation |
| `output_format` | `mp3_44100_128` | Standard quality default; not previously specified — adjust only if the production pipeline needs a different container/bitrate downstream |

**Request word-level timestamps/alignment with this submission** — use
the timestamps-enabled endpoint/response option rather than the plain
synthesis call. This is not optional: every timing figure in
`director-package-v3/shot-list.md` and `assembly/capcut-assembly-package-v1.md`
is a planning estimate that specifically depends on this output to be
re-anchored, per the verification protocol already defined in
`voice-package-v1.md`.

---

## 3. Open field: voice selection

`voice_id` cannot be filled in — no prior artifact ever selected a
narrator voice for this show. This was already flagged as a gap in
`voice-package-v1.md` §"Recommended ElevenLabs settings" and is restated
here because it's the one field that actually blocks submission: every
other parameter in §2 is a real, submittable value, but the API call
cannot be made without a `voice_id`. Selection criteria already on
record (unchanged, not decided here): documentary/analytical register,
"quiet confidence, no hype energy" (`Visual Identity System v2` §1),
capable of both a flat/deadpan hook delivery and a genuine-question
inflection.

---

## 4. Pronunciation — how it's handled in this submission

Per `voice-package-v1.md`, unchanged:

| Term | Pronunciation |
|---|---|
| Burberry | "BUR-ber-ee" |
| Richemont | "REESH-mohn" (silent final "t") |
| Cartier | "kar-tee-AY" |

These are English-approximation respellings for a human reviewer, not
phoneme data — they were never converted to IPA/CMU phonemes in any
prior artifact, and none are invented here. Two honest options, neither
exercised in this package:

- **Do nothing extra:** submit the text in §1 as-is (it's already
  standard spelling — "Burberry," "Richemont," "Cartier" — nothing was
  respelled into it) and check the rendered audio against the table
  above after generation.
- **If mispronounced on the first render:** the correct fix is
  ElevenLabs' Pronunciation Dictionary feature (phoneme-based, applied
  via a separate dictionary parameter at generation time) — not editing
  the submission text. No dictionary entries are prepared here, since
  that requires exact IPA/CMU phonemes this project has never specified
  beyond the rough respellings above, and guessing them would be adding
  new, unverified technical content rather than packaging what's already
  decided.

This package does not modify the text to work around pronunciation risk
— per instruction, pronunciation is exactly as already specified,
carried into a post-generation check rather than a text change.

---

## 5. What this package does not do

Does not select a voice. Does not submit the generation. Does not
change `voice-package-v1.md`, `script-package-v3.md`, or any other
locked artifact. Once a `voice_id` is chosen, §1 and §2 together are the
complete, submittable request — no further editing needed.
