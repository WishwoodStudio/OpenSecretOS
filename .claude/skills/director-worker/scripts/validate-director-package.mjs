// validate-director-package.mjs
//
// The mechanically-checkable subset of SPEC-Director-Worker-v1 §11's
// validation rules — the parts that don't require semantic
// understanding. Does not replace the qualitative checks the Skill's
// own procedure is responsible for (e.g. "does this prompt actually
// follow Visual Identity"); only catches the objective ones.

import { existsSync, readFileSync, readdirSync } from "node:fs";
import { resolvePath } from "../../../../runtime/repository-resolver/resolver.mjs";

const REQUIRED_META_FIELDS = [
  "artifactId",
  "episodeId",
  "version",
  "status",
  "ownerWorker",
  "inputDependencies",
  "outputConsumers",
  "lastUpdated",
  "approvalState",
];

function readdirSafe(dir) {
  try {
    return readdirSync(dir);
  } catch {
    return [];
  }
}

/**
 * @param {string} episodeId
 * @param {string} version
 * @param {string} scriptPackageRelativePath
 * @param {string} scriptContentBefore the exact script content read before generation began
 */
export function validateDirectorPackage(
  episodeId,
  version,
  scriptPackageRelativePath,
  scriptContentBefore,
) {
  const base = `episodes/${episodeId}/director-package-${version}`;
  const results = [];

  const scriptPath = resolvePath(scriptPackageRelativePath);
  const scriptContentAfter = existsSync(scriptPath)
    ? readFileSync(scriptPath, "utf8")
    : null;
  results.push({
    rule: "Script Package unmodified (byte-identical before/after)",
    pass: scriptContentAfter === scriptContentBefore,
  });

  const metaPath = resolvePath(`${base}/director-package.meta.json`);
  let meta = null;
  if (existsSync(metaPath)) {
    try {
      meta = JSON.parse(readFileSync(metaPath, "utf8"));
    } catch {
      meta = null;
    }
  }
  results.push({
    rule: "Metadata file exists and is valid JSON",
    pass: meta !== null,
  });
  if (meta) {
    const missing = REQUIRED_META_FIELDS.filter((f) => !(f in meta));
    results.push({
      rule: "Metadata has all required OS-014 fields",
      pass: missing.length === 0,
      detail: missing.length ? `missing: ${missing.join(", ")}` : undefined,
    });
  }

  results.push({
    rule: "shot-list.md exists",
    pass: existsSync(resolvePath(`${base}/shot-list.md`)),
  });
  results.push({
    rule: "asset-manifest.md exists",
    pass: existsSync(resolvePath(`${base}/asset-manifest.md`)),
  });

  const higgsfieldFiles = readdirSafe(
    resolvePath(`${base}/prompts/higgsfield`),
  );
  results.push({
    rule: "At least one video-generation prompt file exists",
    pass: higgsfieldFiles.some((f) => f.endsWith(".md")),
  });

  const allPass = results.every((r) => r.pass);
  return { allPass, results };
}
