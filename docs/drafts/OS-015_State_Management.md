# Open Secret OS --- State Management

**Status:** Draft v0.1

## Purpose

Open Secret OS tracks production state automatically.

The system always knows:

-   Current stage
-   Completed artifacts
-   Invalidated artifacts
-   Next executable actions

------------------------------------------------------------------------

## Episode Status

Idea

Research

Selected

Reveal Ready

Script Ready

Direction Ready

Production Ready

QA Passed

Published

Postmortem Complete

------------------------------------------------------------------------

## Automatic Invalidation

If Script changes:

-   Director Package → Outdated
-   Voice Package → Outdated
-   QA → Outdated

If Reveal changes:

All downstream artifacts become Outdated.

------------------------------------------------------------------------

## Human Gates

Only Eugene may approve:

-   Episode Selection
-   Reveal
-   Script Lock
-   Final QA
-   Publication

Workers prepare decisions.

They do not finalize them.
