# Open Secret OS --- Artifact Specification

**Status:** Draft v0.1

## Artifact Metadata

Every production artifact must expose:

-   Artifact ID
-   Episode ID
-   Version
-   Status
-   Owner Worker
-   Input Dependencies
-   Output Consumers
-   Last Updated
-   Approval State

------------------------------------------------------------------------

## Artifact States

Draft

↓

Generated

↓

Reviewed

↓

Approved

↓

Archived

Artifacts may also become:

-   Outdated
-   Blocked
-   Deprecated

------------------------------------------------------------------------

## Design Rule

Artifacts are immutable after approval.

A revision creates a new version rather than overwriting history.
