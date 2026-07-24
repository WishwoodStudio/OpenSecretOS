// Repository Resolver — SPEC-001 §8.
//
// Resolves paths against the canonical repository root, never against the
// invoking process's current working directory ("never infer repository
// structure... never trust a shell or session's current working
// directory"). The root is derived from this module's own file location
// (this file always lives at runtime/repository-resolver/resolver.mjs,
// two directories below the root) rather than from process.cwd().

import { fileURLToPath } from "node:url";
import { dirname, join, resolve } from "node:path";

const THIS_DIR = dirname(fileURLToPath(import.meta.url));
export const REPO_ROOT = resolve(THIS_DIR, "..", "..");

/** Resolve a path relative to the canonical repository root. */
export function resolvePath(...relativeParts) {
  return join(REPO_ROOT, ...relativeParts);
}
