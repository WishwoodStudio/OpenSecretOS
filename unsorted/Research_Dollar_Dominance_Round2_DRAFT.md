# Research Memo Round 2 — Stress-Testing "Coordination Lock"

**Status:** DRAFT — for 04_Research. Builds on Research_Dollar_Dominance_DRAFT.md (Round 1). Adversarial self-review, not a script. Still pending ChatGPT IC pass and Eugene ratification.
**Objective:** Test whether coordination lock survives contact with the strongest available counter-evidence, before it becomes the episode's spine.

---

## Part 1 — Why hasn't another currency built the same lock?

### EURO

**1. Conditions for network effect that already exist:**
Genuinely strong — second-most-traded currency (28.9% of FX trades), second-largest reserve currency (~20% of reserves), a large, credible central bank (ECB), a trading bloc comparable in economic size to the US, and deep regional trade integration.

**2. Essential condition still missing:**
A single, unified pool of AAA-rated safe assets at Treasury scale. Highly-rated euro sovereign debt is under 50% of GDP, versus over 100% in the US. The market is fragmented across national issuers — Bunds, French OATs, Italian BTPs — with different credit ratings and yields (Bunds under 3%, BTPs above 3%, Polish bonds above 5%). There is no single euro-area bond a reserve manager can buy in Treasury-like volume.

**3. Why can't the network simply move there?**
Because building that missing pool means creating roughly €5 trillion of unified debt — about a third of euro-area GDP — which requires a level of shared fiscal liability the member states have repeatedly declined to accept. It's not that the euro lacks demand; it's that the *supply side* of the loop (a deep, singular safe asset to absorb that demand) doesn't exist and can't exist without fiscal union.

**4. Obstacle type: Structural / Political.**
Not technological, not really about trust — German Bunds and the ECB are trusted. It's a sovereignty problem: no single European treasury exists to issue the asset at scale, and creating one means member states pooling fiscal liability, which is a political decision they have not made.

---

### CHINESE YUAN (RMB)

**1. Conditions for network effect that already exist:**
China is the world's largest trading nation and manufacturing hub — real invoicing potential. China has built its own payments rail (CIPS, an alternative to SWIFT), has bilateral currency swap lines with dozens of countries, runs the world's largest CBDC pilot (e-CNY), and RMB use is growing in Belt and Road, BRICS, and sanctioned-country trade (Russia, Iran).

**2. Essential condition still missing:**
Free convertibility. China maintains a closed capital account — money cannot move freely in and out of RMB assets. A central bank cannot hold a reserve asset it can't reliably convert back to its own currency in a crisis, so the RMB can't function as a reserve asset at scale regardless of how much trade uses it for invoicing.

**3. Why can't the network simply move there?**
Because opening the capital account is not a technical upgrade — it directly threatens the thing Beijing prioritizes over currency internationalization: control of domestic financial stability and the exchange rate. China's 2015–16 capital flight shock is the live memory shaping policy; the leadership has explicitly signaled gradual, controlled opening, not liberalization. The obstacle isn't infrastructure — CIPS and e-CNY are already built — it's that full internationalization requires giving up a form of control the state is not willing to give up.

**4. Obstacle type: Political / Structural — deliberate policy trade-off.**
Beijing has chosen capital control over currency internationalization. This is a regime priority, not a capability gap.

---

### The pattern across both

Neither missing ingredient is technological or about trust in institutions. Both are the **same category of obstacle**: a government would have to surrender a form of sovereignty it currently holds — fiscal sovereignty for the EU, capital-account control for China — and neither is willing to. This sharpens the mechanism considerably: **the lock isn't just "everyone already uses dollars."** It's that the *specific* thing a challenger needs to supply (a deep singular safe asset, or a fully open capital account) requires a political sacrifice that only the US has already made (fiscal union since 1789, post-Bretton-Woods openness) and that its two largest rivals will not make. This is strong material for the escalation section — it's what makes the reveal *provable* rather than asserted.

---

## Part 2 — Competing explanations

| Mechanism | Could it alone explain today's observations? | What it fails to explain | Causes lock / results from lock / independent? |
|---|---|---|---|
| **Treasury market depth / safe assets** | Partially — explains why central banks *hold* dollars, not why a Korean exporter invoices a Brazilian importer in dollars for a transaction neither the US touches | The FX-transaction dominance (89.2%) exceeding the reserve share (56.9%) — if this were purely a reserves/safe-asset story, the two numbers should track more closely | **Both** — this is the crux finding of Part 3. It's not a rival explanation; it's one half of a two-way feedback loop with invoicing choice |
| **Liquidity** | No — liquidity describes the market's depth, not an independent cause of *why* it got deep | Why the loop started and why it self-reinforces | **Results from** the lock — dollar markets are liquid because so many participants already transact in dollars |
| **Trust in institutions** | No — necessary but not differentiating | Why the dollar dominates the euro or Swiss franc by such a wide margin, when institutional trust/rule-of-law scores between the US, EU, and Switzerland are much closer than the usage gap | **Independent precondition**, not the driver of scale — trust gates entry to the game, it doesn't explain who wins it |
| **Reserve currency status** | No — circular | This *is* the outcome being explained, not a cause of itself | **Results from** the lock (reserves follow usage, per Round 1 Step 3) |
| **Switching costs** | No, but it's the closest to being the same thing as coordination lock | Doesn't independently explain why the lock formed, only why it's sticky once formed | Not a rival mechanism — it's the **stabilizing component of the same lock** (the "why nobody moves first" half) |
| **Eurodollar system (offshore dollar creation)** | No — it explains dollar *supply* mechanics (how the world gets dollars without routing through the Fed), presupposing dollar demand already exists | Why the demand exists in the first place | **Results from** the lock, and now also **reinforces** it (easier offshore access lowers the friction of joining) |

**Conclusion of Part 2:** None of these are genuine rivals to coordination lock — they're all either downstream effects of it, preconditions for it, or (in the Treasury-depth case) one literal half of it. The comparison doesn't dethrone coordination lock; it clarifies that "coordination lock" as stated in Round 1 was too vague, and the *real* minimum mechanism is a specific two-way feedback loop, not an abstract "network effect."

---

## Part 3 — Stress-testing the central claim (the actual causal chain)

Round 1's central claim: US trade share falling, dollar transactional dominance flat-to-rising. Here is the mechanism, one step at a time, each step answering "why does the next participant still choose dollars" — no step is allowed to just say "network effects."

1. **An exporter in Country A sells to an importer in Country B. Why price in dollars?** Because competing exporters in the same product category already price in dollars, and matching their pricing currency keeps this exporter's dollar-denominated price — and therefore its competitive position — stable relative to rivals (Gopinath's "strategic complementarity in pricing"). This is a competitive-matching incentive, not habit.

2. **Why did enough exporters already price in dollars for that competitive pressure to exist?** Historical seeding — Bretton Woods (1944) locked the dollar in before the euro existed, oil's default dollar pricing added early mass, and the sheer prior size of the US economy gave it a head start. This only had to happen once to start the loop.

3. **Once a firm earns dollar revenue from dollar-invoiced sales, what does it do next?** It prefers to hold dollar assets and borrow in dollars, to avoid a currency mismatch between what it earns and what it owes.

4. **What does that preference do to the market?** It adds to global demand for dollar-denominated safe assets — which the deep US Treasury market is uniquely positioned to absorb (per Part 1's euro/RMB finding: no rival currency has this capacity).

5. **What does that demand do to the price of dollar credit?** It pushes the cost of borrowing in dollars *down* relative to other currencies (Gopinath–Stein: rising demand for dollar safe assets cheapens dollar financing).

6. **Why does the *next* exporter — in a third country, selling to a fourth — choose dollars?** Not abstract convention: it is now **literally cheaper to borrow in dollars** than in almost any other currency. This is the answer "coordination lock" was missing — the next participant isn't following a crowd, it's following a price signal.

7. **What does that new participant's choice do?** It adds further demand for dollar safe assets, deepening the Treasury market further, which loops back into step 5.

**Where the chain terminates / where another mechanism becomes necessary:** The loop is not self-sufficient in the abstract — it requires, at step 4–5, an actual supplier willing and able to issue a near-unlimited pool of deep, liquid, safe dollar debt. That's not "network effects," that's the US Treasury market specifically. This is exactly the ingredient Part 1 showed the euro and RMB structurally lack. **So the minimum honest mechanism is a coupled pair, not a single abstraction: the invoicing-financing feedback loop, anchored by Treasury depth.** Neither half explains the evidence alone (matches Part 2's finding that Treasury depth alone can't explain invoicing behavior, and that "network effects" alone can't explain why the loop keeps closing).

---

## Part 4 — Searching for the strongest reveal

### Critique of the current reveal
*"The world uses dollars because the world uses dollars."*

This does not survive a single follow-up question. A viewer who is paying attention will immediately think "okay, but *why* does everyone else use it" — and the line has no answer built in. It describes the outcome, not the incentive. Per Constitution's M-dimension ("is there a hidden structure or incentive beneath the surface story"), this line names no incentive at all. It is catchy but empty — a tautology dressed as an insight. It should not survive to the Reveal Brief as written.

### Five alternatives

| # | Reveal statement | Surprising | Honest | One-diagram | <15s | Avoids tautology | Avoids geopolitics |
|---|---|---|---|---|---|---|---|
| **R1** | "Trading in dollars makes borrowing in dollars cheaper — and cheaper dollars pull in the next trade." | Yes | Yes (matches Gopinath–Stein directly) | Yes (loop diagram) | Borderline — trims to ~12 words | Yes — names the actual price incentive | Yes |
| **R2** | "It's not America's size holding up the dollar. It's the cost of being the first country to leave it." | Yes | Yes | Yes (first-mover/switching-cost visual) | Yes | Yes | Yes (economic framing, not sanctions/power) |
| **R3** | "The dollar isn't winning on trust. It's winning on financing cost — and that cost keeps compounding." | Medium | Yes | Yes | Yes | Yes | Yes |
| **R4** | "Every country that prices in dollars makes it cheaper for the next one to do the same." | Medium | Yes | Yes | Yes (shortest) | Yes | Yes |
| **R5** | "The world hasn't chosen the dollar. It's stuck paying the price of switching away from it." | Medium | Borderline — "stuck paying the price" is vague about which price | Yes | Yes | Weakest — closest to restating the tautology | Yes |

### Ranking
1. **R1** — most precise, most evidence-grounded, most diagrammable as the causal loop itself. Best candidate for the spoken reveal line.
2. **R2** — best hook energy; doubles as the natural bridge into the euro/RMB escalation beat ("so why hasn't anyone else done this?").
3. **R4** — tightest, best as an on-screen typography line paired with R1's spoken version.
4. **R3** — solid but slightly abstract ("financing cost" undefined without setup).
5. **R5** — weakest; too close to restating the flawed original.

### Recommendation
Use **R2 as the hook** (it converts the prior belief — American power — directly into tension in one line) and **R1 as the reveal**, spoken at the purple moment with the mechanism name on screen. R4 can serve as the typography anchor under R1 if a shorter on-screen line is needed.

---

## Final Assessment

**1. Is coordination lock still the best mechanism after adversarial analysis?**
Yes, as a category — but the Round 1 phrasing was too vague and tautological to survive script lock. It refines, it doesn't get replaced.

**2. If not, what replaces it?**
N/A (refined, not replaced). Precise name: the two-way feedback loop between **dollar invoicing and cheap dollar financing**, anchored by US Treasury market depth. Recommend the on-screen mechanism name lean toward something like **"the financing loop"** or **"the cheap-dollar loop"** (final ≤3-word naming decision per Visual Identity System §7B is Eugene's).

**3. What is the single sentence that changes the viewer's mental model the most?**
R1: *"Trading in dollars makes borrowing in dollars cheaper — and cheaper dollars pull in the next trade."*

**4. After this second pass, should this topic still become an Open Secret episode?**
**Yes — and it's now a stronger episode than Round 1 produced.** The adversarial pass did what it's supposed to do: it forced the mechanism from a catchy-but-empty description into a diagrammable causal loop with a real price mechanism (dollar financing cost) at its center, and it surfaced free escalation material (why the euro and RMB structurally can't replicate it) that makes the claim provable on screen rather than asserted. Recommend folding a compressed version of the euro/RMB comparison into the escalation beat — it's what pre-empts the smart viewer's obvious objection ("well why not the euro then?") within the Rolling Payoff window, rather than leaving it unanswered.

---

*Round 2 stress-test — DRAFT. Awaiting ChatGPT IC adversarial pass and Eugene's Selection Gate ratification before this feeds a Reveal Brief.*
