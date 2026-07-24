# PE-001 --- Missing Fact Audit

**Status:** Confirmed Production Evidence

**Date:** 2026-07-11

**Episode:** The Giant Is The Hostage

------------------------------------------------------------------------

# Summary

During production of the episode **The Giant Is The Hostage**, the
Director Skill was unable to validate the episode's central quantitative
claim.

The workflow stopped correctly instead of inventing an explanation.

This is recorded as production evidence.

------------------------------------------------------------------------

# Trigger

While expanding the episode from the approved **00:00--00:15** opening
into the **Mechanism Reveal (00:15--00:30)**, the Director Skill
attempted to explain the statement:

> "45% of Microsoft's future cloud revenue depends on OpenAI."

The Editorial Board package contained the quantitative claim, the
editorial recommendation, and the mechanism framing, but it did not
contain a primary-source explanation demonstrating why the figure is
approximately 45%.

------------------------------------------------------------------------

# Investigation

Director Skill searched for supporting citations, primary sources,
referenced research artifacts, and fact-audit documentation.

No supporting evidence was found.

The Editorial Board document explicitly states that it is an editorial
comparison exercise rather than a research artifact.

A footnote references a separate **primary-source-only fact audit**.

No such artifact exists inside the current repository.

------------------------------------------------------------------------

# System Behavior

The system behaved correctly.

-   It did not invent an explanation.
-   It did not weaken the claim arbitrarily.
-   It did not rewrite the episode around unsupported assumptions.
-   It reported the missing evidence as a production blocker.

This behavior is consistent with the Open Secret principle that
mechanisms must be supported by research rather than generated during
script writing.

------------------------------------------------------------------------

# Root Cause

The production pipeline currently assumes that Editorial Board decisions
are sufficiently supported by upstream research.

This assumption was false for this episode.

An intermediate evidence-verification step was missing.

------------------------------------------------------------------------

# Impact

Editorial work paused until the quantitative claim can be verified.

No incorrect information entered the script.

Trust was preserved.

------------------------------------------------------------------------

# Architectural Decision

None.

This document records evidence only.

No new Worker, Runtime component, Contract, ADR, or Engine change is
proposed.

Additional production evidence is required before changing the
architecture.

------------------------------------------------------------------------

# Follow-up

Future episodes should continue recording similar findings.

If this evidence repeats across multiple productions, the project may
justify introducing a dedicated upstream verification stage.

Until repeated evidence exists, this remains an observed production
finding rather than an architectural requirement.
