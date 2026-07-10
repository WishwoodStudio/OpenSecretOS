# Open Secret OS --- Repository Structure

**Status:** Draft v0.1

## Proposed Layout

    OpenSecretOS/
    ├── .claude/
    │   ├── CLAUDE.md
    │   ├── skills/
    │   └── workers/
    ├── docs/
    │   ├── canonical/
    │   ├── architecture/
    │   ├── episodes/
    │   ├── postmortems/
    │   ├── research/
    │   └── archive/
    ├── integrations/
    ├── prompts/
    ├── assets/
    ├── output/
    └── tools/

## Principles

-   Canonical documents are immutable except through Knowledge Worker.
-   Episode work happens only inside episode workspaces.
-   Generated outputs never mix with canonical knowledge.
-   External tool adapters live under integrations.
-   Temporary files never enter canonical folders.
