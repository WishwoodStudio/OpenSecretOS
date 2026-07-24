// Manifest v1 report — Runtime diagnostic tool.
//
// Runs Manifest v1 (engine/manifests/manifest.mjs) against a given episode
// and reports the answers to its four questions. Does not invoke any
// Worker and does not touch Contracts or Production Graph.

import { writeFileSync } from "node:fs";
import { getManifest } from "../engine/manifests/manifest.mjs";
import { resolvePath } from "./repository-resolver/resolver.mjs";

const episodeId = process.argv[2] || "demo-episode";
const m = getManifest(episodeId);

const lines = [];
lines.push("# Manifest v1 Report");
lines.push("");
lines.push(`Generated: ${new Date().toISOString()}`);
lines.push("");
lines.push(`1. Which episode is this?          ${m.episode}`);
lines.push(
  `2. Which production artifacts exist? Script Package: ${
    m.artifacts.scriptPackage ? "yes" : "no"
  }, Director Package: ${m.artifacts.directorPackage ? "yes" : "no"}`,
);
lines.push(`3. Which Worker is currently active? ${m.activeWorker}`);
lines.push(`4. What is the next expected artifact? ${m.nextExpectedArtifact}`);
lines.push("");

const reportPath = resolvePath("runtime/manifest-report.md");
writeFileSync(reportPath, lines.join("\n") + "\n", "utf8");

console.log(lines.join("\n"));
console.log(`(report written to ${reportPath})`);
