// write-director-package.mjs
//
// Writes a Director Package to disk in the structure defined by
// SPEC-Director-Worker-v1 §5. Takes already-composed content — this
// script performs no extraction or interpretation itself; that happens
// in the Skill's own procedure (SKILL.md), following exactly the steps
// used during manual validation.

import { mkdirSync, writeFileSync } from "node:fs";
import { dirname } from "node:path";
import { resolvePath } from "../../../../runtime/repository-resolver/resolver.mjs";

function writeFile(relativePath, content) {
  const abs = resolvePath(relativePath);
  mkdirSync(dirname(abs), { recursive: true });
  writeFileSync(abs, content, "utf8");
  return abs;
}

/**
 * @param {string} episodeId
 * @param {string} version e.g. "v1", "v2", "v3"
 * @param {{
 *   metaJson: object,
 *   shotListMarkdown: string,
 *   assetManifestMarkdown: string,
 *   higgsfieldPrompts: { filename: string, content: string }[],
 *   hyperframesNote: string,
 * }} content
 */
export function writeDirectorPackage(episodeId, version, content) {
  const base = `episodes/${episodeId}/director-package-${version}`;
  const written = [];

  written.push(
    writeFile(
      `${base}/director-package.meta.json`,
      JSON.stringify(content.metaJson, null, 2) + "\n",
    ),
  );
  written.push(writeFile(`${base}/shot-list.md`, content.shotListMarkdown));
  written.push(
    writeFile(`${base}/asset-manifest.md`, content.assetManifestMarkdown),
  );
  for (const p of content.higgsfieldPrompts) {
    written.push(
      writeFile(`${base}/prompts/higgsfield/${p.filename}`, p.content),
    );
  }
  written.push(
    writeFile(`${base}/prompts/hyperframes/NOTE.md`, content.hyperframesNote),
  );

  return { base: resolvePath(base), files: written };
}
