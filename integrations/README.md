# integrations/

## Purpose
Isolates external services from production logic. Workers never call tools
directly — they submit standardized requests to the Integration Layer, so
any provider can be replaced without changing a Worker.

## Contract
Each integration receives: an input artifact, configuration, and an output
destination. Each integration returns: a generated artifact, metadata, an
execution log, and failure state. No business logic lives inside an
integration.

## Initial providers

| Folder | Responsibility |
|---|---|
| `higgsfield/` | Video generation, camera execution |
| `hyperframes/` | Image generation, keyframe creation |
| `elevenlabs/` | Voice synthesis |

Additional providers are added as sibling folders as they're adopted.

## What must never be stored here
- Editorial or production logic (belongs in `workers/` or `engine/`)
- Canonical rules
- Credentials in plaintext (use the runtime's secret-handling mechanism,
  not files in this repo)

No adapter implementations exist yet.
