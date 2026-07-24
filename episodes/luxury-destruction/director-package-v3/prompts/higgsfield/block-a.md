# Video Generation Prompt — Block A (Boutique interior)

**Used in:** Beat 1 (0:00–0:05)
**Canonical citations:** `Visual Identity System v2` §2 (Documentary
Hybrid rules, AI footage carries no legible text/logos), §6 (motion
principles — slow push-in 2–5%).

- **Scene description:** upscale clothing boutique interior, garment
  racks in soft focus, warm ambient light, no legible signage.
- **Cinematic direction:** documentary-grade stillness, not fashion-ad
  energy — matches canonical visual philosophy ("Analytical... Quiet
  confidence. No hype energy," §1).
- **Camera movement:** slow push-in, 2–3% scale — within the canonical
  "2–5% scale over the shot duration" range (§6).
- **Mood:** quiet, controlled, slightly cold undertone beneath the
  warmth.
- **Lighting:** warm key, cool rim, low contrast.
- **Composition:** racks receding into shallow depth of field, left
  third empty for typography.
- **Negative constraints:** no legible text, no logos, no brand
  check-patterns, no faces, no fast motion, no lens flares — directly
  satisfies §2's "AI footage never carries legible factual information."

**Note on generation tool:** written platform-agnostically; the source
material's canonical AI video stack is Runway/Kling (`Decision Log v2`
§5), not Higgsfield — see `asset-manifest.md` for why this repository's
folder is still named `higgsfield/`.

**Change from v2:** none. Beat 1's VO, duration, and scene requirements
are unchanged in the locked script.

---

## Execution package (Higgsfield MCP `generate_video`)

Prepared for the first real generation attempt of this episode. The
creative content above is unchanged — everything below is reformatting
required to fit the actual connected tool's parameters, not a creative
revision.

**Finding:** the fields above (Scene description / Cinematic direction /
Camera movement / Mood / Lighting / Composition / Negative constraints)
are written as separate labeled sections, but the real Higgsfield
`generate_video` tool takes one flat `prompt` string and has no separate
negative-prompt field. This prompt was not immediately executable as
formatted; the minimum fix is consolidating those fields into one prompt
string and folding the negative constraints into it — no wording was
added or changed, only joined.

**Consolidated prompt (submit exactly as one string):**
> Upscale clothing boutique interior, garment racks in soft focus, warm
> ambient light, no legible signage. Documentary-grade stillness, not
> fashion-ad energy — quiet, controlled mood with a slightly cold
> undertone beneath the warmth. Warm key light, cool rim light, low
> contrast. Racks receding into shallow depth of field, left third of
> frame empty. Slow push-in camera movement, 2-3% scale over the shot.
> No legible text, no logos, no brand patterns, no faces, no fast
> motion, no lens flares.

**Model:** `seedance_2_0_mini` (Seedance 2.0 Mini, Bytedance) — this
project's default video generation model unless explicitly overridden.
Confirmed via the connected Higgsfield MCP (`models_explore`) to be a
real, currently available model, distinct from the full `seedance_2_0`
(which supports up to 4k; Mini is capped at 720p).

**Full parameter set:**

| Parameter | Value | Why set explicitly |
|---|---|---|
| `model` | `seedance_2_0_mini` | Project default (see memory: OpenSecretOS default video model) |
| `prompt` | consolidated text above | No separate negative-prompt field exists |
| `aspect_ratio` | `9:16` | Model default is not vertical; this show's format is 9:16 (matches `asset-manifest.md`) |
| `duration` | `15` | Model default is 5s; asset-manifest calls for a ~15s reference length. Within Mini's supported 4–15s range |
| `resolution` | `720p` | Already this project's stated convention; also the ceiling for Mini (no 1080p/4k on this variant) |
| `generate_audio` | `false` | Model defaults this to `true` (native ambient audio). This is a silent B-roll block — VO and music are layered separately per the source material's own CapCut assembly — so native audio would be an unwanted, unrequested addition |
| `bitrate_mode` | left at default (`standard`) | No stated need for higher bitrate |
| `genre` | left at default (`auto`) | None of the model's genre presets (action/horror/comedy/noir/drama/epic) fit a documentary/analytical piece; forcing one would be an uninstructed creative change |
| `medias` | omitted | Pure text-to-video — no starting image for this block |

**Generated:** 2026-07-12. Success on first attempt, no prompt changes
needed. Output: `https://d8j0ntlcm91z4.cloudfront.net/user_3G7kcYKrXZeRrvSmreaxmPMgNHP/hf_20260712_055053_b9723905-9e24-43b6-bc09-d82d497ce58d.mp4`
(job id `b9723905-9e24-43b6-bc09-d82d497ce58d`, 37.5 credits). Full
production evidence — timing, Seedance-specific quirks observed — logged
in `production-log.md`, 2026-07-12 entry. Not yet downloaded/archived
locally; the hosted URL should be treated as time-limited.
