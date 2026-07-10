# Open Secret OS --- Runtime Architecture

**Status:** Draft v0.1

## Runtime Responsibilities

Claude Code is the execution runtime.

It does not own knowledge.

It orchestrates workers, loads context, updates artifacts and records
state.

## Runtime Flow

1.  Receive request.
2.  Resolve current production state.
3.  Ask Context Loader for required documents.
4.  Invoke appropriate Worker(s).
5.  Produce artifacts.
6.  Update Production Graph.
7.  Persist outputs.
8.  Report next available actions.

## Runtime Rules

-   Never infer repository structure.
-   Never bypass Canonical Knowledge.
-   Never edit Canonical documents directly.
-   Every meaningful action creates or updates an artifact.
