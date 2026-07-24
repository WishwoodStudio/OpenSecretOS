# PRODUCTION-FLOW-v1: Approved Production Package → Published Video

**Status:** Production process documentation. Describes *what Open Secret
produces and in what order*, not how any of it is implemented.
**Scope:** Starts at an Approved Production Package (script already
locked). Ends at a Published video. Everything before this range
(Topic → Research → Reveal Brief → Script, and the Episode Selection,
Reveal, and Script Lock approvals that gate them) is out of scope, as is
everything after publication (Postmortem).
**Explicitly excluded from this document:** Runtime, Manifest, Workers,
Contracts-as-schema, and every other Engine implementation concept. Where
a stage or artifact name below traces back to an existing architecture
document, that's cited for traceability only — it does not mean this
document is describing implementation.

This document answers one question: *if you strip away everything about
how Open Secret Engine executes, what does the production of one video
actually consist of?*

---

## Overview

```
Approved Production Package
        │
        ├───────────────┬────────────────┐
        ▼                ▼                ▼
    Direction           Voice          Subtitles
        │                │                │
  Director Package  Voice Package   Subtitle Package
        │                │                │
        ▼                │                │
    Production            │                │
   (rendering)             │                │
        │                │                │
   Rendered Media          │                │
        └────────┬────────┴────────────────┘
                 ▼
                QA  ←  Final QA (human approval)
                 │
            QA Package
                 ▼
             Publishing  ←  Publication (human approval)
                 │
          Publishing Package
                 ▼
           Published Video
```

Three stages (Direction, Voice, Subtitles) run in parallel off the same
Approved Production Package. Production (rendering) depends on
Direction's output. QA depends on all of the above converging. Publishing
is the final stage.

---

## Stage 1: Direction

- **Input artifact:** Approved Production Package (the locked script,
  plus the visual/production conventions it must follow).
- **Transformation:** the script is broken into a shot-by-shot plan;
  camera language and continuity are worked out per shot; the visual
  assets each shot will need are identified; a tool-ready prompt is
  drafted for each shot.
- **Output artifact:** Director Package (shot list, continuity notes,
  asset manifest, one prompt set for video/camera shots, one prompt set
  for image/keyframe shots).
- **Human approval:** none dedicated to this stage specifically — it sits
  between the Script Lock approval (before it) and the Final QA approval
  (after it, alongside every other stage's output).
- **External service:** none. This stage produces a plan and prompts; it
  does not generate any actual video or image content itself.

*Source: Production Contracts and Director Package definitions (existing
architecture documents); the "no dedicated approval" finding was
confirmed while specifying this stage's implementation in detail.*

## Stage 2: Voice

- **Input artifact:** Approved Production Package (the script's narration
  text).
- **Transformation:** narration is converted into spoken audio.
- **Output artifact:** Voice Package.
- **Human approval:** none named.
- **External service:** voice synthesis (the provider responsible for
  turning text into narration audio).

*Source: existing architecture documents (Voice Package as a named
Contract; voice synthesis as a named integration responsibility).*

## Stage 3: Subtitles

- **Input artifact:** the script's text, aligned against the Voice
  stage's spoken-audio timing.
- **Transformation:** narration text is time-aligned to the actual
  spoken audio.
- **Output artifact:** Subtitle Package.
- **Human approval:** none named.
- **External service:** none specified.

**Gap, flagged not resolved:** Subtitle Package is named as one of the
script's three parallel outputs in the existing production-dependency
documentation, but it is not among the nine Contracts formally listed
elsewhere in the same body of documents. This document uses the graph's
own name for it and does not attempt to reconcile the inconsistency —
that's an architecture decision, not a production-process one.

## Stage 4: Production (rendering)

- **Input artifact:** Director Package's prompt sets (video/camera
  prompts, image/keyframe prompts) and its asset manifest.
- **Transformation:** each prompt is executed by the responsible external
  service, producing actual video clips and images/keyframes rather than
  plans for them.
- **Output artifact:** the rendered media itself — actual video clips and
  images/keyframes.
- **Human approval:** none named.
- **External service:** one provider for video generation and camera
  execution; a second provider for image generation and keyframe
  creation. Each prompt is routed to whichever of the two it was written
  for.

**Gap, flagged not resolved:** the existing production-dependency
documentation moves directly from Director Package (and Voice Package)
to QA Package, with no formally named artifact in between for the
rendered output this stage produces. "Rendered media" here is a
descriptive label, not a defined Contract name. Any future formalization
of this artifact is an architecture decision, not something this
document is deciding.

## Stage 5: QA

- **Input artifact:** as formally declared in existing production-graph
  documentation, Director Package and Voice Package. In practice, a real
  quality review also needs the actual rendered media and the subtitle
  package alongside them — that dependency exists in reality but isn't
  named in the current graph documentation (the same gap noted above, one
  level downstream).
- **Transformation:** the converging outputs of Direction, Voice,
  Subtitles, and Production are reviewed together for correctness and
  consistency against the show's own standards.
- **Output artifact:** QA Package.
- **Human approval:** **Final QA** — one of the show's named approval
  gates. Only the show's editorial authority may pass this gate.
- **External service:** none.

*Source: existing state-management documentation (Final QA as a named
Human Gate) and production-graph documentation (QA Package's declared
inputs).*

## Stage 6: Publishing

- **Input artifact:** QA Package.
- **Transformation:** the approved package is prepared for release and
  distributed.
- **Output artifact:** Publishing Package, then the Published Video
  itself.
- **Human approval:** **Publication** — one of the show's named approval
  gates, the last one in the pipeline.
- **External service:** none specified in current documentation.

**Gap, flagged not resolved:** no distribution platform (e.g., a video
hosting or publishing service) is named anywhere in existing
documentation as an external service for this stage, even though actual
publication clearly requires one. This document notes the absence rather
than inventing one.

*Source: existing state-management documentation (Publication as a named
Human Gate) and production-graph documentation (Publishing Package →
Published Episode).*

---

## End point reached

**Published Video.** Postmortem — which existing documentation describes
as feeding back into the show's canonical knowledge afterward — begins
after this point and is out of scope for this document, per the stated
ending point.

## Summary of gaps this document surfaced

Three places where the existing documentation doesn't fully name
something this process actually needs, none of them resolved here:

1. Subtitle Package is used but not formally listed as a Contract
   (Stage 3).
2. The actual rendered media produced by external generation services
   has no formally named artifact (Stage 4, inherited by Stage 5).
3. No distribution/publishing external service is named anywhere,
   despite Publication being a named approval gate (Stage 6).

These are observations for whoever next works on the underlying
architecture, not decisions made by this document.
