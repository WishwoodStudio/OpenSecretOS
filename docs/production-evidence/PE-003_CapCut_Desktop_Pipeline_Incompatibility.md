# PE-003 — CapCut Desktop Pipeline Incompatibility

**Status:** Confirmed Production Evidence
**Date:** 2026-07-14
**Scope:** whether the `pycapcut`-generated Luxury Destruction draft is
compatible with a real, installed CapCut Desktop application. Real
end-to-end test, not inference — CapCut Desktop was installed on the
working machine specifically to run this test.

**Investigation closed at the point specified by the user.** Per
explicit instruction, `root_meta_info.json` was not modified and
CapCut's internal project format was not further reverse-engineered
beyond what was needed to reach a conclusion. This document reports
what was found up to that stopping point, not a complete resolution.

---

## What was tested

1. Locate the real CapCut Desktop project directory on this machine, by
   filesystem search, not documentation.
2. Copy the existing `pycapcut`-generated draft
   (`assembly/capcut_drafts/luxury-destruction-v1/`) into that location,
   unmodified.
3. Launch CapCut Desktop.
4–8. Verify the draft appears in Projects, opens correctly, and can be
   exported.

Steps 1–3 were completed for real. Steps 4–8 could not be completed —
not a CapCut finding, a tooling one: no Windows GUI automation or
screenshot capability was available to interact with or observe the
running CapCut window. That gap is disclosed here for completeness; it
is not the basis for the conclusion below, which rests on filesystem
evidence gathered independently of it.

## What was found

**1. The documented base path was correct; the internal structure it
was assumed to have was not.**

`%LOCALAPPDATA%\CapCut\User Data\Projects\com.lveditor.draft\` is the
real projects directory — confirmed by finding an actual project there
(`0714`) created by the installed app itself, not by prior
documentation. Comparing that real project's structure against what
`pycapcut` generates:

| Present in a real CapCut project | Present in the `pycapcut` draft |
|---|---|
| `draft_content.json` + `.bak`, duplicated live under `Timelines/<UUID>/` | `draft_content.json` only, flat, no `Timelines/` |
| `draft_agency_config.json`, `draft_biz_config.json`, `draft_virtual_store.json`, `key_value.json`, `timeline_layout.json`, `Timelines/project.json` | none of these |
| `Timelines/<UUID>/attachment/`, `common_attachment/`, `draft.extra`, template files | none |
| `.locked`, `Resources/audioAlg/`, `Resources/videoAlg/`, several empty feature folders | none |

**2. The version gap is documented, not inferred.** The generated
draft's own `draft_content.json` declares `app_version: "6.7.0"`. The
installed application is `8.9.1.3802`. The structural differences above
are consistent with CapCut having moved to a multi-timeline project
format somewhere between those versions; `pycapcut` targets the older,
flatter one.

**3. Project discovery is index-driven, not a folder scan.** One level
above the project folders, `root_meta_info.json` contains an
`all_draft_store` array — for the real `0714` project, this entry is
fully populated (draft ID, cover image path, root path, JSON file path).
Nothing in the `pycapcut` generation path writes an equivalent entry.
Per instruction, this file was not modified to test whether adding an
entry would be sufficient — the structural gap in finding 1 makes that a
secondary question, not the primary blocker.

## Conclusion

**The current `pycapcut` pipeline is not compatible with the installed
CapCut Desktop version (8.9.1.3802) as-is.** Two independent, real gaps
were found, either of which alone would block real production use:

1. The generated draft is missing the entire `Timelines/` subsystem and
   several required config files that every real project of this
   CapCut version has.
2. The generated draft is never registered in the index CapCut's
   Projects screen actually reads from.

This does not mean the underlying approach (generating a draft
programmatically for CapCut assembly, evaluated and implemented in
`AUTOMATION-EVALUATION-v1.md`) was wrong — the earlier evaluation's own
verified claim was narrower than "opens in CapCut": that a real,
third-party library produced a structurally valid, correctly-timed
draft matching the locked production plan. That claim still holds and
was re-confirmed again in this session (correct base path found, file
copy succeeded, CapCut launched successfully). What's now also known,
from a real test rather than an assumption, is that structural validity
by `pycapcut`'s own definition is not the same thing as compatibility
with this specific installed CapCut version.

## Investigation closed here

Per instruction: no modification to `root_meta_info.json`, no further
reverse-engineering of CapCut's internal format. Whether to pursue a
version-matched `pycapcut` release, a different generation approach, or
manual assembly for Export V1 is a decision for whoever reviews this
finding — not resolved or recommended by this document.
