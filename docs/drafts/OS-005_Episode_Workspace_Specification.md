# Open Secret OS --- Episode Workspace Specification

**Status:** Draft v0.1

## Principle

The Episode Workspace is the primary production object.

Every episode has exactly one workspace.

Everything related to that episode lives inside it.

------------------------------------------------------------------------

## Required Components

-   Metadata
-   Research
-   Sources
-   Reveal Brief
-   Script
-   Director Package
-   Voice Package
-   Assets
-   QA
-   Output
-   Postmortem

------------------------------------------------------------------------

## State Machine

Idea

↓

Research

↓

Episode Selection

↓

Reveal

↓

Script

↓

Direction

↓

Production

↓

QA

↓

Publish

↓

Postmortem

Every state produces one or more artifacts.

Claude determines the next step from the current state rather than chat
history.

------------------------------------------------------------------------

## Rule

Nothing related to an episode exists outside its workspace except
Canonical documents.
