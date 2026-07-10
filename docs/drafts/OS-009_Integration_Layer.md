# Open Secret OS --- Integration Layer

**Status:** Draft v0.1

## Goal

External services are isolated from production logic.

## Principle

Workers never call tools directly.

They submit standardized requests to the Integration Layer.

## Initial Integrations

### Higgsfield

Responsibilities: - Video generation - Camera execution

### HyperFrames

Responsibilities: - Image generation - Keyframe creation

### ElevenLabs

Responsibilities: - Voice synthesis

### Future

Additional providers should be replaceable without changing Workers.

## Integration Contract

Each integration receives:

-   Input artifact
-   Configuration
-   Output destination

Each integration returns:

-   Generated artifact
-   Metadata
-   Execution log
-   Failure state

No business logic lives inside integrations.
