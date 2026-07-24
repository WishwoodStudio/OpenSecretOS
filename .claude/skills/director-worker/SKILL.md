---
name: director-worker
description: Transform an approved Production Package into a Director Package (shot list, continuity notes, asset manifest, tool-ready video-generation prompts) for one Open Secret episode. Use when asked to direct, shoot-list, or produce a Director Package for an episode that already has an approved script.
---

# Director Worker

This Skill implements `docs/specifications/SPEC-Director-Worker-v1.md`
against the Engine architecture in `docs/specifications/SPEC-001_Open_Secret_Engine_v1.md`.
It is the automated form of the manual process validated on the Luxury
Destruction episode — `episodes/luxury-destruction/director-package-v2/`
is the reference implementation this Skill must reproduce the shape of.
If anything below conflicts with those two documents, the documents win;
do not improvise around them.

## Mission

Convert an approved Production Package into deterministic production
artifacts: a shot-by-shot plan, camera language, continuity notes, an
asset manifest, and tool-ready prompts. Never modify the script. Never
make editorial decisions. Never invent a visual rule not present in an
actual canonical document.

## What "Production Package" means here

Production evidence (not architecture) settled this: a real Open Secret
Production Package is **one monolithic document** containing the script,
beat sheet, shot package, AI generation blocks, asset lists, and more —
not separate files. This Skill's input is a path to that single document.
`SPEC-Director-Worker-v1` §4's definition (Script Package + Visual
Identity + Production Playbook) still describes what Director Worker
*needs*; this Skill gets the script portion by extracting it from the
monolithic input, per the pattern already used in
`episodes/luxury-destruction/script/script-package.md`.

## Procedure

1. **Locate inputs.** Run `scripts/locate-inputs.mjs`'s `locateInputs(episodeId, productionPackagePath)`. This finds the Production Package and searches `canonical/` for Visual Identity, Production Playbook, Decision Log, Content Constitution, and Mechanism Ladder by filename keyword — `canonical/` has no fixed naming convention (production evidence), so don't hardcode exact filenames anywhere else either.

2. **Check each canonical document found, don't just trust its presence.** Run `scripts/check-canonical-doc.mjs`'s `checkCanonicalDoc(path)` on each. A file existing does not mean it has real content — `Content_Constitution_v4_DRAFT.md.docx` was found to be a one-line stub during manual validation. Treat anything `check-canonical-doc.mjs` flags as unavailable exactly like a missing file for citation purposes: you may not cite it, and you must say so explicitly wherever the source material claims a rule comes from it.

3. **Apply `SPEC-Director-Worker-v1` §12's failure conditions.** If Visual Identity or Production Playbook cannot be resolved (missing, or flagged as a stub), halt — do not produce a Director Package. Content Constitution, Decision Log, and Mechanism Ladder are not required inputs per `SPEC-Director-Worker-v1` §4; their absence does not halt generation, it just means any rule the source material attributes to them is unverifiable and must be marked as such.

4. **Extract the script.** Pull the script/narration section out of the Production Package verbatim — no rewording. If `episodes/<id>/script/script-package.md` doesn't already exist, write it (OS-014 metadata fields, source citation, unedited script text — follow the format already used for Luxury Destruction). Record the script's exact content now; it must be byte-identical when this Skill finishes.

5. **Read every available canonical document in full before writing anything.** Do not skim for keywords — the Luxury Destruction validation only caught a real duration-target contradiction because the actual text was read, not assumed from the source material's own claims about what canonical documents say.

6. **Never trust an upstream artifact's self-reported canonical basis.** If the Production Package claims "Document X says Y," verify Y against the actual text of Document X. If the actual document says something else — or doesn't mention it at all — the actual document is correct. Flag the discrepancy explicitly; do not silently follow whichever one seems more permissive, and do not silently follow whichever seems more restrictive either. State the conflict and its source.

7. **Derive the shot list.** One entry per beat: VO text, duration, shot objective, camera language, visual/block reference, transition, continuity notes. For every camera/motion/color/typography choice that traces to an actual canonical rule, cite the specific document and section — not a vague "per Visual Identity." For every choice that doesn't trace to a canonical rule (it's just part of the source material's own creative content), don't force a citation onto it.

8. **Derive continuity notes** — cross-shot constraints (recurring visual bookends, verb/metaphor consistency between similar evidence beats, color-temperature matching, etc.) as they actually appear in the source material.

9. **Derive the asset manifest** — every asset the shot list references, with the same citation discipline as step 7. Cross-reference `Visual Identity`'s "Real Artifacts First" priority order if that document is available.

10. **Derive one prompt file per video-generation block** under `prompts/higgsfield/` (this repository's existing folder name for the video integration, per `SPEC-001` §17 — do not rename it even if a canonical document names a different literal tool; note the mismatch instead, don't resolve it). Leave `prompts/hyperframes/` explained-but-empty unless the source material actually contains image/keyframe-generation content distinct from video and diagram work — check `episodes/luxury-destruction/director-package-v2/prompts/hyperframes/NOTE.md` for why it was empty there, and don't force content into it just to fill it.

11. **Check runtime against the actual canonical target**, if Visual Identity or Decision Log state one. Do not shorten shot durations or reword the script to force compliance — that would be modifying the script (prohibited) or inventing timing not in the source. If the total runtime conflicts with a real canonical target, say so plainly at the top of `shot-list.md`, the way `episodes/luxury-destruction/director-package-v2/shot-list.md` does.

12. **Write the metadata file** (`director-package.meta.json`) with the OS-014 fields (`artifactId`, `episodeId`, `version`, `status`, `ownerWorker`, `inputDependencies`, `outputConsumers`, `lastUpdated`, `approvalState`) plus a `notes` field summarizing what was verified, what wasn't, and why. Status is `"Generated"`, never `"Reviewed"` or `"Approved"` — this Skill cannot grant either (`SPEC-Director-Worker-v1` §13; those require passing Validation Rules and, ultimately, Final QA).

13. **Write all files** via `scripts/write-director-package.mjs`'s `writeDirectorPackage(episodeId, version, content)`.

14. **Run the mechanical validation** via `scripts/validate-director-package.mjs`'s `validateDirectorPackage(...)`, passing the script content captured in step 4. Report every rule's pass/fail — do not silently drop a failing rule from the report.

15. **Report the result** — what was produced, which canonical documents were actually usable, and every conflict or unverifiable claim found. Do not present a conflict as resolved when it wasn't.

## Explicit non-responsibilities

Same as `SPEC-Director-Worker-v1` §3: no script writing, no research, no
editorial decisions, no direct calls to Higgsfield/HyperFrames (this
Skill produces prompts for a later stage to use, it does not generate
video/image content itself), no finalizing approval, no editing
Canonical documents, no deciding its own context — the inputs this Skill
reads are exactly what step 1 locates, nothing loaded ad hoc mid-run.

## If something doesn't fit this procedure

Per this repository's standing rule: stop, document the specific
obstacle as production evidence (a note in the relevant episode's
`production-log.md`, following the pattern already established for
Luxury Destruction), and do not change this Skill's procedure or any
Engine document to route around it. That decision belongs to whoever
reviews the evidence.
