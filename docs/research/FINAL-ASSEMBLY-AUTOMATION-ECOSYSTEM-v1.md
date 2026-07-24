# Final Assembly Automation — Ecosystem Comparison

**Status:** Investigation only. No recommendation made, no pipeline
change proposed. This document exists to compare real candidates side
by side for a future decision, after Episode 1 (Luxury Destruction)
publishes.

**Scope note, stated up front because it shapes the whole comparison:**
the goal is not "automate CapCut" — it's "reduce manual work in final
assembly." Several of the strongest candidates below don't involve
CapCut at all. That's intentional, not a scope drift.

**Inclusion rule applied:** projects with no meaningful activity in the
last 12 months were excluded unless already widely adopted and stable.
Every candidate below has either a recent release/commit or (for
FFmpeg) is stable, ubiquitous infrastructure that doesn't need recent
churn to be trustworthy.

---

## Candidates evaluated

### 1. Direct FFmpeg-based assembly (no CapCut involved)

- **Actively maintained:** Yes — FFmpeg is continuously maintained,
  decades-old, one of the most stable pieces of open-source media
  infrastructure in existence. Notably, CapCut Desktop itself bundles
  its own `ffmpeg.exe` (confirmed directly on this machine during the
  PE-003 investigation) — the ecosystem's own most-adopted tool already
  depends on it.
- **Open source:** Yes, LGPL/GPL depending on build.
- **Works with Claude Code:** Yes — no integration needed, it's a CLI
  tool. Already installed on this machine and already used successfully
  in this project.
- **Can control an existing CapCut project:** No — doesn't touch CapCut
  at all, by design.
- **Can import assets:** Yes — any video, image, or audio file.
- **Can manipulate the timeline:** Yes — full programmatic control via
  `concat`, `overlay`, `drawtext`, `amix` and related filters.
- **Can export video:** Yes — this is its core function.
- **Known limitations:** No native project/draft file — the "timeline"
  is a script, not an editable GUI project, so there's no visual preview
  or scrubbing during construction the way CapCut offers. Mismatched
  input frame rates/SAR need explicit normalization (encountered and
  fixed directly in this project's own pacing-review work). Complex
  multi-layer animated typography requires real filter-graph
  expertise, though this project has already demonstrated it directly
  (the pacing-review preview render).
- **Manual work remaining:** Low, once a reusable script template
  exists. The template itself (per-shot placement, typography build-in
  timing, diagram overlay, audio mix) has already been built once for
  this exact episode — the primary remaining work is generalizing it
  across episodes, not inventing it from scratch.

### 2. JSON2Video (cloud video-assembly API + official MCP server)

- **Actively maintained:** Yes — documentation last updated May 2026;
  actively iterating MCP tooling.
- **Open source:** No — commercial API/service. The MCP client wrapper
  (`@json2video/mcp`) is installable via npx; the rendering backend is
  closed, cloud-hosted.
- **Works with Claude Code:** Yes, directly — an official MCP server
  built specifically for coding agents including Claude Code, exposing
  render/status/validation tools.
- **Can control an existing CapCut project:** No — entirely separate
  from CapCut; you'd stop using CapCut for final assembly.
- **Can import assets:** Yes — designed around a JSON "movie"
  specification referencing media by URL.
- **Can manipulate the timeline:** Yes, in principle — full scene/track
  JSON schema. Not independently verified against this project's exact
  requirements (animated typography build-ins, precise per-second
  overlay timing, the specific color/font system) — the documentation
  available didn't confirm these at the level of detail needed to be
  sure, only that a general schema for it exists.
- **Can export video:** Yes — this is the product's core function,
  server-side rendering, no local app required.
- **Known limitations:** Introduces a new paid, closed, third-party
  cloud dependency for the single most important step in the pipeline.
  Pricing not confirmed in this investigation. Capability fit for this
  show's specific animated-typography design language is plausible but
  unverified — would need a real test render before trusting it.
- **Manual work remaining:** Unknown until tested — likely low if the
  schema covers everything needed, but that's not yet confirmed.

### 3. VectCutAPI / CapCutAPI (sun-guannan and forks)

- **Actively maintained:** Yes — 216 commits, v1.5.0 (Sept 2025),
  1.9k stars / 404 forks. The most established project in the
  CapCut-automation space found in this investigation.
- **Open source:** Yes, Apache-2.0.
- **Works with Claude Code:** Yes — HTTP API and an MCP interface,
  documented integration path for Claude among other agent platforms.
- **Can control an existing CapCut project:** No — creates new draft
  projects; doesn't attach to or modify a project already open in
  CapCut.
- **Can import assets:** Yes, via URL.
- **Can manipulate the timeline:** Yes — multi-track, text, subtitles,
  effects, stickers, keyframes, audio.
- **Can export video:** Claimed yes — "generate and export finished
  videos to cloud," distinct from just producing a CapCut-openable
  draft. **Not independently verified in this investigation** — the
  export/rendering mechanism (whether it needs a real CapCut/Jianying
  account, what it costs, whether it's genuinely server-side) wasn't
  confirmed from available documentation.
- **Known limitations:** No explicit CapCut-version compatibility
  statement found — given this project generates the same family of
  draft file this repository's own `pycapcut` pipeline generates, it
  likely carries some version of the same risk PE-003 already found
  (schema drift against whatever CapCut Desktop version is actually
  installed), unless its cloud-export path avoids opening the file in
  a real CapCut app entirely.
- **Manual work remaining:** Unknown until the export path is tested
  directly — potentially very low if the cloud-export claim holds,
  since that would mean never touching CapCut Desktop's GUI at all.

### 4. Windows-MCP (general Windows desktop GUI automation)

- **Actively maintained:** Yes, very — 6.4k stars, 780 forks, 674
  commits, release as recent as June 2026. The most active, most
  widely adopted project in this entire comparison.
- **Open source:** Yes, MIT.
- **Works with Claude Code:** Yes — general MCP server, agent-agnostic.
- **Can control an existing CapCut project:** Yes, in principle —
  drives the real, running CapCut Desktop application through actual
  UI Automation and input injection, the same way a human would. This
  is the one candidate that sidesteps the draft-file-format
  compatibility problem entirely, since it never touches the file
  format at all.
- **Can import assets:** Yes, but only by scripting the literal
  click-through of CapCut's own import dialogs.
- **Can manipulate the timeline:** Yes, same caveat — every operation
  (placing a clip, adding a text card, setting its color) would need
  to be built as a click/type sequence against CapCut's actual UI.
- **Can export video:** Yes, same caveat — scripting the real Export
  button and dialog.
- **Known limitations:** Not tuned for any creative application
  specifically — general purpose. Fragile to CapCut UI layout changes
  between versions. Text-selection reliability issues noted by the
  project itself. Meaningfully slower than a file-based or API-based
  approach (real click/type latency per action, ~0.2–0.5s each).
- **Manual work remaining:** High up-front build cost (every UI action
  for every asset type needs to be scripted once), low marginal cost
  per episode after that — but the most fragile of the realistic
  candidates to future CapCut updates.

### 5. capcut-mcp-server-extended (MigueDuque)

- **Actively maintained:** Weak signal — 7 commits, 2 stars, 5 forks,
  1 open PR. Thin wrapper around VectCutAPI's backend.
- **Open source:** Yes, MIT.
- **Works with Claude Code:** Yes, MCP.
- **Can control an existing CapCut project:** No.
- **Can import assets:** Yes, via the underlying VectCutAPI service.
- **Can manipulate the timeline:** Yes, same underlying engine as
  candidate 3, narrower exposed surface.
- **Can export video:** No — explicitly limited to saving CapCut
  drafts for manual processing; doesn't expose the parent project's
  own export capability.
- **Known limitations:** Requires the separate VectCutAPI backend
  running locally. Low adoption. Strictly weaker than using VectCutAPI
  directly.
- **Manual work remaining:** Same as candidate 3 at best, worse in
  practice since export isn't exposed — CapCut Desktop still needed
  for the final step, with all of PE-003's findings still applying.

### 6. capcut-mcp (burnshall-ui, Elixir)

- **Actively maintained:** Weak signal — 53 commits, 2 stars, 0 forks,
  small/early project.
- **Open source:** License not confirmed in this investigation.
- **Works with Claude Code:** Yes, MCP.
- **Can control an existing CapCut project:** Partially — reads and
  writes CapCut's local `draft_content.json` directly, same general
  approach as `pycapcut`.
- **Can import assets:** Yes, by reference in the JSON.
- **Can manipulate the timeline:** Yes, same file-editing approach.
- **Can export video:** **No — stated explicitly by the project
  itself:** *"CapCut has no CLI for export; only UI automation could do
  it."* This project doesn't attempt it.
- **Known limitations:** Explicitly tested against CapCut v8.3.0 —
  this machine's installed version is 8.9.1.3802, a real, if smaller,
  version gap than the one PE-003 found for `pycapcut` (targeting
  6.7.0), but the same category of risk. The project's own
  documentation acknowledges "CapCut schema changes may break
  compatibility." Windows-only. Requires Erlang/OTP 28 and Elixir
  1.19+ — a real dependency-installation cost on top of everything
  else.
- **Manual work remaining:** Whatever this tool can't do (which
  includes all of export) still requires the same manual CapCut GUI
  work PE-003 already identified as the blocker.

### 7. CapCut Web + custom Playwright automation

- **Actively maintained:** N/A — no existing maintained project found
  targeting this specifically. This would be a from-scratch build, not
  an adoption of existing work.
- **Open source:** N/A.
- **Works with Claude Code:** Yes in principle — Playwright itself is
  actively maintained (Microsoft) and this project already has working
  browser-automation tooling available.
- **Can control an existing CapCut project:** No — and per the prior
  investigation, CapCut Web has no project/draft import mechanism at
  all, so there's nothing to hand it beyond individual media files.
- **Can import assets:** Only by scripting individual file-upload
  dialogs, one at a time, same as any browser UI automation.
- **Can manipulate the timeline:** Only by scripting CapCut Web's
  actual UI, click by click — no shortcut exists, confirmed by the
  prior investigation's finding that no import format is supported.
- **Can export video:** Yes, by scripting the Export button.
- **Known limitations:** Everything would need to be built from zero —
  no existing project to lean on. Web UI automation is generally more
  brittle than desktop UI automation (more frequent visual changes,
  less accessible automation surface than native Windows UI Automation
  offers Windows-MCP).
- **Manual work remaining:** Highest of any realistic candidate to
  build initially, for no clear advantage over candidate 4 (which gets
  the same "drive the real UI" capability with a far more mature,
  actively maintained general tool).

---

## Comparison table

| # | Candidate | Maintained | Open source | Claude Code fit | Controls existing project | Imports assets | Manipulates timeline | Exports video | Manual work remaining |
|---|---|---|---|---|---|---|---|---|---|
| 1 | FFmpeg direct assembly | Yes (stable/ubiquitous) | Yes | Yes, no integration needed | N/A (bypasses CapCut) | Yes | Yes | Yes | **Low** — already proven in this project |
| 2 | JSON2Video | Yes | No (closed API) | Yes, official MCP | N/A (bypasses CapCut) | Yes | Yes, unverified fit | Yes | Unknown — untested |
| 3 | VectCutAPI/CapCutAPI | Yes | Yes | Yes, MCP | No | Yes | Yes | Claimed, unverified | Unknown — export path untested |
| 4 | Windows-MCP | Yes, very | Yes | Yes, general MCP | **Yes** (real GUI) | Yes (scripted) | Yes (scripted) | Yes (scripted) | High build cost, low marginal cost |
| 5 | capcut-mcp-server-extended | Weak | Yes | Yes, MCP | No | Yes | Yes | **No** | High — CapCut GUI still needed |
| 6 | capcut-mcp (Elixir) | Weak | Unconfirmed | Yes, MCP | Partial (file-level) | Yes | Yes | **No, by its own admission** | High — same blocker as PE-003 |
| 7 | CapCut Web + Playwright | N/A, unbuilt | N/A | Yes, buildable | No | Scripted only | Scripted only | Scripted only | Highest — nothing exists yet |

---

## Ranking, by expected production value (not theoretical capability)

1. **FFmpeg direct assembly** — the only candidate with real,
   first-hand proof of working on this exact episode's actual assets in
   this exact project. Everything else on this list is a claim from
   documentation; this one is a result already sitting on disk.
2. **JSON2Video** — the strongest *unproven* candidate: official
   Claude Code MCP support, active maintenance, cloud rendering removes
   the CapCut-version problem entirely. Ranked below FFmpeg only
   because its fit for this show's specific design language hasn't
   been tested yet, and it adds a paid, closed dependency.
3. **VectCutAPI/CapCutAPI** — most mature project actually built around
   CapCut/Jianying specifically, with a real, if unverified, claim to
   solve the exact problem PE-003 found (exporting without needing
   CapCut Desktop's GUI). Worth a direct test before ranking higher.
4. **Windows-MCP** — the most robust fallback if the above all prove
   insufficient, because it's immune to draft-format version drift by
   construction. Ranked here, not higher, because of its real build
   cost and fragility to UI changes.
5. **CapCut Web + Playwright (custom build)** — technically possible,
   no existing project to build on, no clear advantage over Windows-MCP
   for the same class of "drive the real UI" approach.
6. **capcut-mcp-server-extended** — weaker than the project it wraps
   (candidate 3), low adoption, no export path.
7. **capcut-mcp (Elixir)** — smallest, least active, explicitly cannot
   export, and its documentation names a CapCut version further from
   what's actually installed here.

No recommendation is made per instruction. This ranking is for
comparison; a decision on which path (or combination) to pursue is left
for after Episode 1 publishes.
