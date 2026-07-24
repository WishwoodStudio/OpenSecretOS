# WILT — Scope Compression Plan v1
### Directive: compress from ~2.5 hr / 7 chapters to a 1–2 hr premium release · Solo dev · iOS-first · v1.0

**Status:** Proposal for lock. Supersedes Blueprint Part 2.2 ("7 chapters, ~2–2.5 hr") and Part 4 chapter table if accepted, per the project's precedence rule (more recent locked decisions take priority over earlier canon).

**Consistency note:** This plan preserves all post-Blueprint locked decisions — the Hold gesture, hinge objects, fragment reconciliation, one signature transformation per chapter, the first-sixty-seconds artifact, the Chapter 1 Gate, the Beat-5 erasure-attribution playtest, the un-poisoned valley, the atmospheric-mystery repositioning, and the Visual Direction Specification v1. Nothing below reopens those.

---

## 1. Executive summary

WILT compresses from **7 chapters / ~8 puzzles / 2 inversions / 4 endings** to **5 chapters / 5 puzzles / 1 inversion / 3 endings**, targeting an **85–110 minute** first playthrough. The compression is structural, not subtractive: two chapters are absorbed into neighbors that already carry overlapping emotional beats, the weakest ending is removed, and the highest-risk production element (the inversion set-pieces) is halved.

The core claim: at 1–2 hours, WILT stops competing against its weaknesses (mobile session-length attrition, solo-dev content burden, "walking sim padding" reviews) and starts competing on its strengths (density, the Hold, the signature transformations, a completable emotional arc). The commercial comps that actually succeeded at premium mobile narrative — Florence (~45 min), Gorogoa (~90 min), Only You Are Here — live in exactly this runtime band. The prior 2.5-hour target was closer to a PC walking-sim runtime ported to a platform where completion rates collapse past the 90-minute mark, and completion rate is the single strongest driver of ratings, and ratings drive App Store visibility.

Estimated reduction in remaining production effort: **~40%**. Estimated time to release: **~10–11 months** from now versus 15+ on the prior scope.

---

## 2. What must remain unchanged (the irreducible identity)

1. **The Hold.** Sustained physical effort to see the truth; denial as the world's resting state. This is the product. Everything else is negotiable before this is.
2. **The complicity reframe.** Minute-three "what did I do," Beat-5 erasure attribution, the player as author of the corruption. This is the marketing hook and the thesis.
3. **The reconciliation verb.** Restore a true memory by resolving a contradiction between states. No keys, no codes. Every remaining puzzle is one of these.
4. **The House as hub and interior state.** Returns between chapters, legibly changed each time. Cheapest emotional multiplier in the game (one diorama, many readings).
5. **The Drive.** The night of the wish, reconstructed through objects. The pivot of the entire narrative. Untouchable.
6. **The Willow choice and the hold-and-release ending mechanic.** "Letting Go" as a physical act, not a menu selection.
7. **The song motif** (clean / detuned / resolved). Three stems carrying the whole emotional spine — highest impact-per-asset ratio in the project.
8. **The un-poisoned valley.** One genuine good memory mid-game. Relocated, not removed (see §4).
9. **One signature transformation per chapter**, the two-hinge cap (reduced to one, see §5), the walkthrough test, and the full accessibility suite.
10. **The Non-Negotiables.** The player is never judged; truth is never externally rewarded.

---

## 3. What is removed entirely (not postponed — removed from V1)

| Cut | What it was | Why it goes |
|---|---|---|
| **Chapter 4 — The Bar (the Loop)** | 4-node diorama replayed 3–4× with per-pass diffs; P4 observation puzzle | Its beat — warmth erased piece by piece, the friends draining — duplicates the Music Store's beat ("the draining world"). At 2.5 hr the repetition was pacing; at 1.5 hr it's redundancy. It also carries the game's only loop controller, per-pass diff data system, and retention tracking: a whole one-use subsystem. Highest cost-to-uniqueness ratio in the game. |
| **Inversion 2 — The Plea** | Second become-her set-piece at the Folding threshold | The GDD itself calls the inversions the highest-risk element and justifies having *two* by runtime. At 90 minutes, one gut-punch is a gut-punch; two is a mechanic, and mechanics get compared. Inversion 1 (Surfacing, the mirror) is the stronger of the pair and survives intact. |
| **The fourth ending — "In Every Reality" (ambiguous)** | Partial truth + mixed light → "can't tell what was real" | The weakest of the four: it rewards indecision, requires its own authored ending sequence, and muddies the clean three-way story (honest / horror / hidden-cathartic) that reviews and store copy can actually communicate. Mixed-state players resolve to the honest or horror ending based on the final choice alone. |
| **The second friend** | Two warning-voice characters | One friend carries the same function (the warning ignored, the erasure barometer) at half the VO, fragment, and photo-asset cost, and a single erased person is *more* legible than two. |
| **Per-loop variant override system** | Material/audio swap infrastructure for the Bar | Dies with the Bar. |
| **FMOD** | Middleware option in the locked stack | Built-in AudioMixer + snapshot crossfades covers a 5-chapter dual-bed game. One less integration, one less license, one less thing Claude Code can silently break. (This resolves an "or" already present in the Architecture Handbook, not a stack change.) |
| **Localization in V1** | — | English-only at launch. Localization is a post-launch decision gated on traction, not a launch requirement. |

---

## 4. What is merged

**Merge A — The Bar's beat folds into the Music Store (Chapter 2).**
The Store already owns "the draining world." It absorbs the Bar's single best moment as its signature transformation: solving Out of Tune causes the store to empty in true light *while the music bed loses instruments one by one* — the Bar's "hearing the warmth leave" idea, delivered in one authored transition instead of a loop system. The surviving friend's warning (voicemail) lives here. Nothing about the Bar's *meaning* is lost; only its *duration* is.

**Merge B — The Folding becomes the approach inside the final chapter (Chapter 5).**
The Folding was already built from re-dressed earlier dioramas. It compresses from a full chapter (5–6 nodes, navigation puzzle, Inversion 2) to a 3-node approach corridor inside the Willow chapter: House hallway → Store fragment → threshold, scaled and wrong, junction passable only under the Hold. The "world contains only what the wish values" statement lands in four minutes instead of eighteen, and the true-light-only-passage idea survives as the corridor's single gate rather than a standalone puzzle.

**Merge C — The valley relocates into the Drive (Chapter 3).**
Canon requires one genuine un-poisoned memory after the Store and before the Drive. In a 5-chapter spine there is no "between," so the valley becomes the Drive's opening movement: the first nodes of the car are the *real* drive — the actual good evening, warm in both states, the smallest Wished/True delta in the game exactly as the Visual Direction Spec requires. Then the player reaches the back seat, finds the box, and reconstructs what the night became. The valley and the wish now sit in the same physical space, which is stronger than adjacency: the player watches the best real memory curdle into the crime, in the same car. Ending exhaustion converts to earned tragedy exactly as the canon principle intends.

**Merge D — Her House inherits the Folding's onset.**
Her House ends with the fold *beginning* (her room's geometry failing after Inversion 1) rather than the Folding being its own act. One transition shot instead of a chapter handoff.

---

## 5. What is simplified

1. **Hinges: cap drops from two per chapter to one.** One perfect hinge per chapter beats two adequate ones, and halves the bespoke interaction code.
2. **Fragments: every fragment must feed an ending determinant or the friend-erasure barometer, or it's cut.** Target ~3 required + ~2 optional per chapter, down from open-ended collection. The memory board remains a read-only reflection (already built) — no new board features, and the Bar's retention surface use is deleted.
3. **Signature transformations: four authored, not seven.** Ch1 (Beat-5 erasure), Ch2 (the store emptying with the music), Ch4 (the shrine/mirror), and Ch5's *is* the ending itself. The Drive's "transformation" is the valley curdling — a lighting/audio shift, not a bespoke set-piece.
4. **Characters: silhouette/photo/audio only, already canon — now with one friend, one beloved, one Vendor (voice + silhouette).** Total VO: one friend voicemail set, the Vendor's Willow monologue, her manuscript read-aloud (optional captioned). Nothing else.
5. **Endings production: 3 endings ≈ 2.5 authored sequences.** The hidden ending (I'll Be In Your Band) is a variant arm of the honest ending — same diorama, resolved song arrangement plus the earliest-memory payoff — not a third bespoke build.
6. **Node budget: ~24–27 nodes total** (House 5, Store 5, Drive 4, Her House 4, Willow+approach 6, plus hub-return variants). Dual-light authoring is the project's real labor cost per the Blueprint's own risk register; this is where the ~40% saving physically lives.

---

## 6. What becomes optional (hidden / replay value, never required)

1. **The hidden ending path.** The earliest-memory object stays discoverable, unmarked, and missable — the reason to replay.
2. **Optional fragments (~2 per chapter).** Depth for the exploring 20%; the memory board's silhouette slots advertise their existence without spoiling.
3. **Delta discoveries beyond the required cadence.** Extra authored Wished/True gaps for players who Hold everything. Cheap (texture/prop swaps), pure texture.
4. **The pet.** The returning-pet motif becomes an optional recurring discovery across chapters rather than a required beat — a quiet reward for attention.
5. **Chapter select + endings-discovered indicator.** Stays (post-completion, already cheap), because it services the ending hunt that the optional layer creates.

---

## 7. The ending: should the game end earlier?

**Yes — and it already wants to.** The Willow choice remains the ending; what changes is when it arrives. At ~150 minutes, the player reaches the choice tired *from the game*. At ~90 minutes, they reach it tired *as the character* — which is the design intent of the entire Phase 3 "the fantasy is exhausting to hold" arc. The Hold does the fatigue work physically; the runtime no longer has to do it by attrition.

Concretely: the choice should land at minute ~80–95 of a first playthrough, with credits inside the same session the player started. A premium mobile narrative that most buyers *finish* produces finished-game reviews — which mention the ending, which is WILT's best material. A game most buyers abandon at 60% produces "atmospheric but I drifted off" reviews. The earlier ending is not a concession; it is the single highest-leverage completion-rate decision available.

---

## 8. Revised chapter structure

| Ch | Location | Phase | Core beat | Signature transformation | Puzzle | ~Time |
|---|---|---|---|---|---|---|
| 1 | **The House** | Grounded | The wrongness; the Hold taught; "what did I do" at minute 3; Beat-5 erasure | The erasure (already gated) | P1 — The Set Table | 15–18 |
| 2 | **The Music Store** | Grounded → Unstable | The draining world; one-sidedness; the friend's warning (absorbs the Bar) | The store empties as the music loses instruments | P2 — Out of Tune | 18–22 |
| 3 | **The Drive** | Unstable | Opens as the **valley** (the real good evening) → curdles into the reconstruction of the wish | The valley curdling (lighting/audio, not bespoke) | P3 — The Night of the Wish | 15–20 |
| 4 | **Her House** | Unstable → Dream | The shrine; her trapped self; **Inversion — Surfacing** (the mirror); the fold begins as she's lost | The mirror / geometry onset | P4 — The Shrine → Surfacing | 18–22 |
| 5 | **The Willow** | Dream | 3-node folded approach (re-dressed assets) → the Vendor → the choice, hold-and-release | The ending itself | P5 — The Choice | 15–20 |

**Hub returns:** brief House transitions between chapters 1→2, 2→3, 3→4 (the shrine grows, Wished spreads or recedes). Chapter 4 exits directly into 5 — no return, deliberately: home is no longer available.

**Total: 81–102 min first playthrough** (+10–15 for completionists, ~25–35 for a second-ending run via chapter select).

**Endings:** Let It Wilt (honest) · Everbloom (horror) · I'll Be In Your Band (hidden, honest-variant). Determinants unchanged: understanding counter, light-preference ratio, final choice, earliest-memory flag — thresholds retuned for the shorter fragment population.

---

## 9. Revised feature list

**Ships in V1:**
1. Node navigation + gyro/swipe look (built)
2. The Hold (pending ergonomics spike — unchanged gate)
3. Object inspection + tap-zoom, dual-state comparison
4. Fragment reconciliation + memory board (read-only, built)
5. Five reconciliation-family puzzles (one per chapter; P4 includes the single inversion)
6. One inversion set-piece with assist mode
7. Hinge objects — one per chapter
8. Four authored signature transformations + the ending
9. Three endings; hold-and-release resolution
10. Song motif: clean / detuned / resolved
11. Dual ambient beds ×5 locations, AudioMixer snapshots
12. Full accessibility suite (unchanged — built early)
13. ES3 save/resume, single slot, iCloud KV optional
14. Chapter select + endings indicator post-completion
15. First-sixty-seconds artifact = trailer spine = App Store preview (unchanged)

**Explicitly not in V1:** the Bar/loop system, Inversion 2, the fourth ending, the second friend, FMOD, localization, iPad-bespoke layouts beyond responsive scaling, Steam build (page/wishlist activity proceeds per the existing four-phase plan; the *build* is post-iOS-launch work).

---

## 10. Revised production roadmap (from mid-July 2026)

| Phase | Window | Work | Gate |
|---|---|---|---|
| **0 — Hold spike** | Weeks 1–3 | Hold ergonomics spike on device; Beat-5 grey-box | **Existing gates unchanged:** Hold ergonomics pass + erasure-attribution playtest. Fail both → the designated anomaly-observation fallback, as already agreed. |
| **1 — Chapter 1 to Gate** | Months 1–3.5 | Ch1 full production (art-directed, both states, P1, hinge, signature erasure, song clean stem); first-sixty-seconds artifact; TestFlight cohort | **Chapter 1 Gate** — existing quantitative kill/pivot thresholds + exposure floor. Second panel review (Claude + ChatGPT) here. |
| **2 — Middle spine** | Months 3.5–7.5 | Ch2, Ch3, Ch4 at ~6 weeks each (reusable systems + re-dress strategy; Ch4 gets the extra week for the inversion) | Inversion assist-mode playtest at end of Ch4 |
| **3 — The Willow** | Months 7.5–9 | Ch5 incl. folded approach, Vendor VO, three endings, resolved song arrangement, credits | Full-run internal playtest; retune ending determinants |
| **4 — Polish & launch** | Months 9–10.5 | Performance/thermal pass (A12 floor), accessibility QA, App Store assets from the existing six-deliverable design brief, pricing, submission, press/festival outreach with the first-sixty-seconds artifact | Release ≈ **month 10–11** (~May–June 2027) |

Steam page goes live during Phase 2–3 per the existing four-phase Steam plan (Next Fest eligibility clock starts at page-live; the port itself is post-launch, architecture already provisioned per Handbook Part 12).

**Pricing recommendation:** **$5.99.** At 1.5 hours, $7.99 invites "short for the price" one-stars; $3.99 undercuts the premium positioning. $5.99 with zero IAP and a complete arc is the defensible statement.

---

## 11. Risks introduced by the compression

1. **"Too short" reviews.** Mitigation: price at $5.99, state runtime honestly in store copy ("a complete 90-minute experience"), and let the optional layer + hidden ending pad perceived value. Honesty about length converts a complaint into a feature for this audience.
2. **Chapter 2 overload.** The Store now carries the draining world, the friend, and the absorbed Bar beat. Mitigation: hard cap — one puzzle, one hinge, one transformation, three required fragments. If it doesn't fit, the *Bar material* yields, never the Store's own beat.
3. **The single inversion carries everything.** With no second set-piece, Surfacing must land. Mitigation: it was already the stronger of the two, it keeps its assist mode, and it gets a dedicated playtest gate at the end of Phase 2.
4. **Losing the Bar loses a marketable set-piece.** The recursion clip would have been distinctive footage. Mitigation: the Ch2 signature transformation (store emptying as the music thins) is designed to be *the* marketing clip and is arguably more shareable — one continuous shot, no context needed.
5. **Pacing whiplash.** Five chapters escalate faster; the valley has less room to breathe. Mitigation: the valley opens the Drive rather than interrupting it, and hub returns are retained precisely as decompression beats.
6. **Sunk-cost inversion risk (the meta-risk).** This plan cuts content the multi-AI loop previously validated. Per the project's own principle, that prior validation was of a *different commercial target*; this plan should get one independent ChatGPT review before lock, specifically prompted to argue *against* the compression.

---

## 12. Why this version may actually be a better game

**The theme is contraction.** WILT is about a world shrinking to contain only what one wish values. A tight 90-minute game that ends before you want it to *enacts* its own thesis; a 2.5-hour version explains it. Every merge above makes the game denser, and density is what the interaction-cadence targets were already reaching for.

**The Hold gains, not loses.** Sustained-effort mechanics fatigue in a good way over 90 minutes and in a bad way over 150. The compression puts the ending exactly where the player's thumb — and the character's denial — are both giving out.

**Completion is the marketing.** A finished game gets reviewed as a whole; the ending, the hold-and-release, the three-way resolution are WILT's best word-of-mouth material, and they only exist for players who arrive. The single biggest predictor of a premium narrative game's App Store trajectory is the ratio of buyers who see the credits.

**Solo-dev survivability.** Seven chapters at solo pace is a 15+ month exposure to burnout, drift, and market movement. Five chapters with two whole subsystems deleted (loop controller, second inversion) is a project a single non-programmer founder can actually observe, verify, and finish — which was identified from the start as the fatal-risk axis.

**What I would personally ship:** exactly this spine, with one asymmetry of care — over-invest in Chapter 1 and the Willow beyond their share (they are the review, the trailer, and the memory), build Chapters 2–4 to "excellent but disciplined," and treat every hour saved by this compression as polish budget, not new content budget.

---

*Requires: one independent ChatGPT adversarial review → lock → incorporate into Strategic Context v2 as the canonical scope, superseding Blueprint Parts 2.2, 4, and 10.1.*
