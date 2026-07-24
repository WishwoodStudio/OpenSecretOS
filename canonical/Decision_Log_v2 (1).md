# Open Secret — Decision Log v2

**Status:** Canonical
**Folder:** 00_Canonical
**Updated:** July 2026 — post-Norway, post-knowledge-base-audit
**Replaces:** Decision_Log.md (v1)

---

## Governance Rules

- Every strategic decision is logged here with status.
- Status: ACTIVE | SUPERSEDED | PROVISIONAL | CLOSED
- SUPERSEDED decisions are kept for historical reference — never deleted.
- Review Triggers are logged here when fired.

---

## SECTION 1 — Project Foundation

### Channel Name
**Decision:** Open Secret
**Status:** ACTIVE — CANONICAL
**Notes:** Handle `opensecret.official` registered across YouTube, TikTok, Instagram.

### Channel Mission
**Decision:** Reveal hidden mechanisms behind taken-for-granted business outcomes. Transformation over education.
**Status:** ACTIVE — CANONICAL

### AI Workflow
**Decision:**
- Claude = Head of Content and Production (execution)
- ChatGPT = Investment Committee (strategic review, architectural decisions)
**Status:** ACTIVE — CANONICAL (Claude Instructions V3, July 2026)

---

## SECTION 2 — Production System

### Primary Production Approach
**Decision (original):** Canva Pro as primary visual tool. Infographic-first production.
**Status:** SUPERSEDED
**Superseded by:** Documentary Hybrid (validated Norway, July 2026)

**Decision (current):** Documentary Hybrid. AI creates atmosphere. Real artifacts carry information. CapCut for assembly.
**Status:** ACTIVE — VALIDATED (2 production cycles)

### Validated Production Pipeline
**Decision:** 9-stage pipeline (Idea → Research → Hook+Script → Shot List → AI Video → Voice → Assembly → QA → Publish)
**Status:** ACTIVE — VALIDATED
**Evidence:** OS-S-0002 (IKEA), OS-S-0003 (Norway)

### Publishing Target
**Decision:** 1080×1920, 58–59 seconds, no Content ID
**Status:** ACTIVE — CANONICAL
**Evidence:** Norway — first export >60s uploaded as standard video, not Short. Content ID triggered by CapCut music.

### Hook Rule
**Decision:** First surprise must arrive within 3 seconds of video start
**Status:** ACTIVE — CANONICAL
**Evidence:** IKEA — 8-second recognition-only opening. Norway — contradiction in first sentence. Two-cycle validation.

---

## SECTION 3 — Editorial Philosophy

### Hook Philosophy
**Decision (original):** Accurate from first sentence.
**Status:** SUPERSEDED

**Decision (current):** Curiosity-first. A hook may simplify reality provided the complete episode makes the statement factually true in context.
**Reference example:** "Norway turned gambling losses into Olympic funding."
**Status:** ACTIVE — CANONICAL
**Evidence:** Norway production cycle (OS-S-0003)

### Script Voice
**Decision:** Conversational, intelligent, fast. Not BBC. Not movie trailer. Like an intelligent person explaining something unbelievable.
**Status:** ACTIVE — CANONICAL

---

## SECTION 4 — Visual Identity

### Color System
**Decision:** Dark background #0D1117, purple #A855F7 once per episode at reveal beat, amber #E8A838 for money flow only.
**Status:** ACTIVE — CANONICAL

### Purple Rule
**Decision:** Purple appears at most once per episode, at the single reveal moment. Never in the opening. Never repeated.
**Status:** ACTIVE — CANONICAL

### Typography
**Decision:** Space Grotesk ExtraBold for numbers/headlines, Inter Medium for labels/body.
**Status:** ACTIVE — CANONICAL

---

## SECTION 5 — Technology Stack

### AI Video Generation
**Decision:** Runway / Kling for AI cinematic footage. Shot-by-shot prompting in ~15-second blocks.
**Status:** ACTIVE — VALIDATED (Norway)

### Voice
**Decision:** ElevenLabs, conversational tone, fast pacing, post-visual-planning generation.
**Status:** ACTIVE — VALIDATED

### Assembly
**Decision:** CapCut. Hard cuts as default. Minimal transitions.
**Status:** ACTIVE — VALIDATED

### Music
**Decision (original):** Epidemic Sound.
**Status:** UNDER REVIEW — Content ID risk identified (Norway)

**Decision (interim):** YouTube Audio Library or commercially licensed music with no Content ID risk. Do not use CapCut built-in music.
**Status:** ACTIVE

### Scheduling
**Decision:** Metricool (optional). Direct platform upload acceptable.
**Status:** PROVISIONAL — not actively used

---

## SECTION 6 — Architecture Decisions

### Agent Architecture
**Decision (original):** 15-agent orchestrated system (AI Production Architecture v1).
**Status:** SUPERSEDED — never implemented
**Superseded by:** Claude Instructions V3 + Production Playbook v1

### Knowledge Base Structure
**Decision (July 2026):** 6-folder structure (00_Canonical, 01_Episodes, 02_Postmortems, 03_Prompts, 04_Research, 05_Archive). ≤10 files in 00_Canonical.
**Status:** ACTIVE

### Pilot Episode Set
**Decision (original):** Costco → Airports → Billionaires.
**Status:** SUPERSEDED — pilot set was redesigned before any of these were produced

**Decision (actual):** First two published episodes are IKEA (OS-S-0002) and Norway (OS-S-0003).
**Status:** CLOSED (both published)

---

## SECTION 7 — Review Triggers

### Review Trigger 1 — After first produced video
**Status:** FIRED (post-IKEA). Key findings: production time ~2x planned; Documentary Hybrid validated as superior approach; Canva-first workflow superseded.

### Review Trigger 2 — After 10 published videos
**Status:** PENDING (2/10 episodes published)
**Questions to resolve at Trigger 2:**
- Retention shape: does it peak at the reveal beat?
- Which hook patterns perform best by platform?
- Does the 60/40 core/wing split hold?
- Does Documentary Hybrid outperform infographic competitors in data?
- Is 58–59s the right target runtime?

### Review Trigger 3 — After 25–30 published videos
**Status:** PENDING
**Action:** Full strategic audit, recommended on Opus max-reasoning model.

---

## SECTION 8 — Open Decisions / Signal Log

*This section tracks analytics signals and open questions that may trigger future decisions.*

| Date | Signal | Status |
|---|---|---|
| July 2026 | IKEA + Norway low retention in first 10 seconds — hook structure identified as primary cause | Being addressed via hook rule |
| July 2026 | CapCut music Content ID risk identified | Interim rule active — YouTube Audio Library |
| July 2026 | Knowledge base volume (65 docs / 2 episodes) identified as inverted — migration executed | Migration plan in progress |

---

*Decision Log v2 — Canonical. Promote to 00_Canonical.*
*Replaces: Decision_Log.md (v1)*
