// Manifest v1 — SPEC-001 §11 (minimal implementation).
//
// Answers exactly four questions for a given episode, scoped to what
// Sprint 1 actually needs (Script Package -> Director Package). Computed
// fresh from the episode workspace's current filesystem state on every
// call — not a static declared file, and not a general dependency graph.
//
// Explicitly does NOT: validate against a Contract schema (no Contracts
// implemented yet), or model the full production pipeline (no Production
// Graph implemented yet). Scoped narrowly to the two artifacts this
// sprint cares about; extending beyond them is future work, not this
// module's job.

import { existsSync, readdirSync } from "node:fs";
import { resolvePath } from "../../runtime/repository-resolver/resolver.mjs";

/**
 * @param {string} episodeId e.g. "demo-episode"
 * @returns {{
 *   episode: string,
 *   artifacts: { scriptPackage: boolean, directorPackage: boolean },
 *   activeWorker: string,
 *   nextExpectedArtifact: string,
 * }}
 */
export function getManifest(episodeId) {
  const episodeDir = resolvePath("episodes", episodeId);
  if (!existsSync(episodeDir)) {
    throw new Error(`No episode workspace found for "${episodeId}"`);
  }

  const scriptPackagePath = resolvePath(
    "episodes",
    episodeId,
    "script",
    "script-package.md",
  );
  const directorPackageDir = resolvePath(
    "episodes",
    episodeId,
    "director-package",
  );

  const hasScriptPackage = existsSync(scriptPackagePath);
  const hasDirectorPackage =
    existsSync(directorPackageDir) &&
    readdirSync(directorPackageDir).length > 0;

  // 3 & 4: which Worker is active, what's expected next — a simple
  // presence check over the two artifacts this sprint cares about, not a
  // general graph traversal.
  let activeWorker;
  let nextExpectedArtifact;

  if (!hasScriptPackage) {
    activeWorker = "Editorial Worker";
    nextExpectedArtifact = "Script Package";
  } else if (!hasDirectorPackage) {
    activeWorker = "Director Worker";
    nextExpectedArtifact = "Director Package";
  } else {
    activeWorker = "none (beyond Sprint 1 scope)";
    nextExpectedArtifact = "none (beyond Sprint 1 scope)";
  }

  return {
    episode: episodeId, // Q1: which episode is this?
    artifacts: {
      // Q2: which production artifacts exist?
      scriptPackage: hasScriptPackage,
      directorPackage: hasDirectorPackage,
    },
    activeWorker, // Q3: which Worker is currently active?
    nextExpectedArtifact, // Q4: what is the next expected artifact?
  };
}
