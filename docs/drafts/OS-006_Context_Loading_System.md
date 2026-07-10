# Open Secret OS --- Context Loading System

**Status:** Draft v0.1

## Purpose

Claude should load only the minimum knowledge required for the current
task.

Reading the full repository by default is prohibited.

------------------------------------------------------------------------

## Loading Strategy

### S9 Review

Load:

-   Constitution (Section 9)
-   Mechanism Ladder
-   S9 Scorecard

### Reveal Development

Load:

-   Constitution (Section 10)
-   Mechanism Ladder
-   Decision Log (editorial decisions)

### Script Production

Load:

-   Constitution
-   Reveal Brief
-   Production Playbook
-   Production Postmortem

### Director Package

Load:

-   Visual Identity
-   Production Playbook
-   Current Script
-   Current Workspace

### Voice

Load:

-   Voice Package
-   Script
-   Production Playbook

### QA

Load only documents relevant to validation.

------------------------------------------------------------------------

## Dynamic Assembly

The Context Loader assembles task-specific context before any Worker
begins execution.

Workers never decide what to load.

The Context Loader owns that responsibility.

------------------------------------------------------------------------

## Future Direction

The Context Loader will evolve into an automatic dependency resolver
capable of determining required documents from the requested task.
