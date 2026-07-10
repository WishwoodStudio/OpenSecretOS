# Open Secret OS --- Production Graph

**Status:** Draft v0.1

## Purpose

Production is modeled as a dependency graph rather than a linear
checklist.

Each artifact declares its inputs and outputs.

## Core Rule

When an upstream artifact changes, every dependent artifact becomes
**Outdated** until regenerated.

## Initial Graph

Topic → Research → Reveal Brief → Script

Script produces:

-   Director Package
-   Voice Package
-   Subtitle Package

Director Package produces:

-   Higgsfield Prompts
-   HyperFrames Prompts
-   Asset Manifest

Director + Voice produce:

-   QA Package

QA produces:

-   Publishing Package

Publishing produces:

-   Published Episode

Postmortem feeds back into Canonical Knowledge through Knowledge Worker
only.

## Benefits

-   Automatic invalidation
-   Automatic task planning
-   Safe incremental production
-   No hidden dependencies
