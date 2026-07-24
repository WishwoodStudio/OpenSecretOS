# Open Secret — Visual Storytelling Framework v1

**Status:** DRAFT — pending Investment Committee review before promotion to `00_Canonical`
**Folder (on ratification):** `00_Canonical`
**Authority:** Operates within Content Constitution v4, Section 8 (Visual & Storytelling Principles), as its governing decision layer. On any conflict, the Constitution wins.
**Relationship:** Defines *which* visual medium a beat should use. Visual Identity System v2 defines how that medium looks and behaves once chosen. Neither document restates the other's content.
**Updated:** July 2026

---

## Section 1 — Purpose

This document governs one decision, repeated for every beat of every episode:

**Given what this beat needs to accomplish, what visual medium delivers it with the least cognitive load?**

This is not a style guide. Color, typography, hook visual patterns, and publishing specifications live in the Visual Identity System. This is not a production workflow. Sequencing, tooling, and generation mechanics live in the Production Playbook. This document sits above both: it is the reasoning layer that decides which medium a beat needs before either of those documents is consulted.

---

## Section 2 — Core Principle

Visuals do not decorate narration. Visuals reduce the effort required to understand it.

Every visual decision is judged against one question:

> **What visual representation allows the viewer to understand this idea fastest?**

Never:

> "What would look coolest?"

Never:

> "What AI video should accompany this sentence?"

Premium aesthetic quality remains a requirement of the channel — but it is satisfied through restraint, color discipline, and documentary authenticity (Visual Identity System v2), never by defaulting to cinematic footage in place of an explanation.

---

## Section 3 — The Three Communication Goals

Every beat serves one or more of three goals. Identify the **primary** goal before choosing a medium.

### 3.1 Understand

The viewer needs to grasp a structure: a mechanism, process, system, incentive, flow, comparison, cause-and-effect relationship, or sequence.

**Preferred visual language:** diagrams, motion graphics, icon animation, maps, timelines, charts, explanatory graphics.

**Test:** Could this beat's claim be drawn as an arrow, a bar, a node, or a line — and would that drawing *be* the explanation, not just illustrate it?

### 3.2 Believe

The viewer needs confidence that a claim is real: a historical event, a real company, a piece of evidence, a quote, a document, a regulation, a statistic, a screenshot, an interface, a physical object.

**Preferred visual language:** documentary footage, archival material, screenshots, photographs, official documents — shown at their actual scale, undecorated.

**Test:** Does this beat's credibility depend on the audience seeing that the source is real, not reconstructed?

### 3.3 Feel

The viewer needs to register scale, atmosphere, tension, surprise, human stakes, or place.

**Preferred visual language:** cinematic AI footage, real documentary footage, environmental shots, human presence, dramatic pacing.

**Test:** Would removing this beat's atmosphere lose something the narration and typography can't carry alone?

### 3.4 Beats Frequently Need More Than One Goal

A REVEAL beat, for example, often needs the audience to *understand* the mechanism and *feel* the weight of it landing at the same moment. This is resolved through layering (Section 6), not by choosing a single medium for the whole beat. When goals genuinely compete for the same screen space and layering isn't enough, the priority order is:

**Understand > Believe > Feel.**

A viewer who fails to understand the mechanism has lost the episode. A viewer who misses an atmospheric beat has lost polish, not comprehension. Feel is never sacrificed by omission — layer it underneath — but it never wins a direct conflict for the primary visual.

---

## Section 4 — The Visual Decision Tree

Apply this at storyboard stage, per beat, before any shot is planned or any AI generation is requested.

1. **What must the audience understand at this beat?** If a relationship, process, comparison, or structure — this is the primary goal. Go to Section 5, Understand rows.
2. **What must the audience believe at this beat?** If the beat's job is proving a claim is real — this is the primary goal. Go to Section 5, Believe rows.
3. **What must the audience feel at this beat?** If neither understanding nor belief is at stake — if the beat's job is place, mood, scale, or stakes — this is the primary goal. Go to Section 5, Feel rows.
4. **Does more than one goal apply?** If so, apply the Hybrid Principle (Section 6): the primary goal from Steps 1–3 takes the dominant/foreground layer; the secondary goal takes the background layer.
5. **Select the medium** from Section 5's default rules. Only deviate with a stated reason — never by defaulting to whatever medium the previous beat used.

---

## Section 5 — Default Rules

| Editorial situation | Primary goal | Default medium |
|---|---|---|
| Mechanism / hidden structure | Understand | Animated diagram |
| Money flow | Understand | Animated flow graphic (amber, per Visual Identity System) |
| Comparison / contrast | Understand | Chart or side-by-side split |
| Ownership / control structure | Understand | Node-and-line diagram (blue, per Visual Identity System) |
| Chronology / sequence | Understand | Timeline animation |
| Geography | Understand | Map |
| Scale / magnitude | Understand | Animated counter or proportion bar |
| Identity reframe ("X is actually Y") | Understand | Label-swap animation |
| Historical event, regulation, filing | Believe | Real document / archival footage |
| Company, product, interface | Believe | Real screenshot or photograph, actual scale |
| Quote, statistic source | Believe | Real artifact, undecorated |
| Emotional weight, surprise, tension | Feel | Cinematic AI or real documentary footage |
| Scale of a place, human impact | Feel | Environmental / human-presence footage |
| Human story | Feel | Real people, real footage |

These are defaults, not requirements. A beat may deviate when a stated reason overrides it — but the default is the starting assumption, not cinematic footage.

---

## Section 6 — The Hybrid Principle

Most beats can carry two goals simultaneously through layering rather than forcing a single-medium choice.

**Structure:**

- **Foreground / dominant layer** — carries the beat's primary goal, per Section 4. This layer is what the viewer's attention and the narration timing are built around.
- **Background layer** — carries a secondary goal, most often Feel. It supports without competing.

**Examples:**

| Foreground (carries information) | Background (carries atmosphere) |
|---|---|
| Animated diagram explaining the mechanism | Slow cinematic city footage, held static or gently pushing in |
| Animated money-flow graphic | Factory or logistics footage |
| Real document, at scale | Softly blurred office environment |

**Rule:** The background layer never carries information the foreground doesn't already state. If the background footage seems to be doing explanatory work, the beat has been misclassified — return to Section 4.

Execution detail for how each layer should look (color, typography, motion behavior, transition style) remains governed entirely by Visual Identity System v2 — this framework decides the layering *structure*, not its rendering.

---

## Section 7 — Anti-Patterns

- **Beautiful footage that explains nothing.** If a beat's primary goal is Understand and the visual carries no structure, the beat has failed regardless of production quality.
- **Cinematic footage substituting for a diagram.** If a relationship could be drawn and would communicate faster than a scene, the scene is the wrong choice — no matter how well-produced.
- **Location standing in for mechanism.** Showing a place is not the same as showing why something happens there.
- **Motion without a statable reason.** Camera movement or animation added for polish rather than to show sequence, causality, or attention direction increases cognitive load rather than reducing it.
- **Decorating instead of explaining.** Any visual whose primary function is "this looks premium" rather than "this is faster to understand" has inverted the framework's core principle.
- **Collapsing three goals into two mediums.** Treating "Documentary Hybrid" as only AI-cinematic-plus-real-artifact, with no explanatory layer, is the specific failure this framework exists to correct. A beat with an Understand goal always gets an explanatory-graphics option on the table.
- **Reconstructing what a real artifact already shows better.** Building a synthetic version of a document, interface, or object that could simply be shown at its real scale wastes production effort and reduces credibility.
- **Choosing medium after generation, to justify it.** Medium is selected at Section 4, before any shot is generated — never selected retroactively to rationalize a clip that already exists.

---

## Section 8 — Relationship to Other Canonical Documents

| Document | Owns | This framework's relationship to it |
|---|---|---|
| Content Constitution v4 | Mission, editorial philosophy, reveal framework, topic selection | This framework operationalizes Constitution §8 (Visual & Storytelling Principles). On conflict, the Constitution wins. |
| Visual Identity System v2 | Color semantics, typography, hook visual patterns, motion rules, publishing technical specs | This framework decides *which* medium a beat uses; Visual Identity System decides how that medium looks and behaves once chosen. Neither restates the other. |
| Visual Medium Decision Framework v1 (draft) | Per-beat operational checklist, Beat Sheet integration, document-by-document edit instructions | The Medium Decision Framework is this document's operational implementation inside the Production Package Generator template. This document carries the principle and hierarchy; the Medium Decision Framework carries the applied checklist. |
| Production Playbook v1 | Workflow sequencing, tooling, generation mechanics | This framework determines what decision gets made; the Playbook determines when in the pipeline it gets made and with what tools. |
| Editorial Handbook v1 | Editorial mindset, belief transformation, mechanisms-over-stories philosophy | This framework applies that philosophy specifically to the choice of visual medium. |

---

## Section 9 — Production Use

At Beat Sheet stage, for every beat:

1. Run the Visual Decision Tree (Section 4).
2. Record the selected medium and, if a hybrid, both layers.
3. Apply the Default Rules (Section 5) unless a stated reason justifies a deviation.
4. Check the beat against the Anti-Patterns (Section 7) before the shot list is finalized.
5. Only beats resolved to Feel as their primary, undominated goal proceed directly to AI cinematic generation without a diagram brief.

---

## Section 10 — Success Criteria

This framework is working when:

- Explanations become measurably easier to follow without added narration.
- Storyboards become more consistent across editors and episodes.
- Medium selection becomes faster because the decision is procedural, not aesthetic judgment each time.
- Unnecessary AI cinematic shots decrease because fewer beats default to them — not because of an enforced quota.
- Motion graphics are used because they communicate better, not to hit a screen-time target.
- Open Secret retains its premium documentary identity while becoming substantially stronger at explaining its subject matter.

---

*Visual Storytelling Framework v1 — DRAFT pending Investment Committee review. Folder on ratification: `00_Canonical`.*
