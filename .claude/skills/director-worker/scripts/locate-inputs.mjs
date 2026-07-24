// locate-inputs.mjs
//
// Locates the inputs Director Worker needs for a given episode: the
// Production Package, and whichever canonical documents can be found.
//
// Production evidence from the manual validation exercise: canonical/
// has no established file-naming convention. The real files that
// appeared were named "Decision_Log_v2 (1).md", "Visual_Identity_System_v2
// (1).md", "Content_Constitution_v4_DRAFT.md.docx" — none of which match
// a predictable pattern a hardcoded path could rely on. This module
// discovers documents by matching filename keywords instead of exact
// names. This is a defensive implementation choice, not an Engine
// architecture change — canonical/README.md does not mandate any
// specific naming scheme, so nothing here contradicts it.

import { existsSync, readdirSync } from "node:fs";
import { resolvePath } from "../../../../runtime/repository-resolver/resolver.mjs";

const DOC_PATTERNS = {
  visualIdentity: /visual.?identity/i,
  productionPlaybook: /production.?playbook/i,
  decisionLog: /decision.?log/i,
  contentConstitution: /constitution/i,
  mechanismLadder: /mechanism.?ladder/i,
};

function findCanonicalDoc(pattern) {
  const canonicalDir = resolvePath("canonical");
  if (!existsSync(canonicalDir)) return null;
  const files = readdirSync(canonicalDir).filter(
    (f) => f.toLowerCase() !== "readme.md",
  );
  const match = files.find((f) => pattern.test(f));
  return match ? resolvePath("canonical", match) : null;
}

/**
 * @param {string} episodeId
 * @param {string} productionPackageRelativePath path relative to repo root
 */
export function locateInputs(episodeId, productionPackageRelativePath) {
  const productionPackagePath = resolvePath(productionPackageRelativePath);
  if (!existsSync(productionPackagePath)) {
    throw new Error(
      `Production Package not found at ${productionPackagePath}`,
    );
  }

  const canonical = {};
  for (const [key, pattern] of Object.entries(DOC_PATTERNS)) {
    canonical[key] = findCanonicalDoc(pattern);
  }

  return {
    episodeId,
    productionPackagePath,
    episodeDir: resolvePath("episodes", episodeId),
    canonical,
  };
}
