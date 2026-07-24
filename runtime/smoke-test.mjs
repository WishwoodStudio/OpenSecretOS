// Runtime smoke test — Engine validation only.
//
// Proves the Engine can:
//   1. Locate the Demo Episode workspace.
//   2. Load the fixture Visual Identity.
//   3. Load the fixture Production Playbook.
//   4. Report exactly which artifacts were resolved.
//
// Explicitly does NOT implement Contracts, invoke any Worker, produce a
// Director Package, or implement Manifest. Runtime validation only.

import { existsSync, readFileSync, statSync, writeFileSync } from "node:fs";
import { resolvePath, REPO_ROOT } from "./repository-resolver/resolver.mjs";

function loadArtifact(label, relativePath) {
  const abs = resolvePath(relativePath);
  const found = existsSync(abs);
  const entry = { label, relativePath, resolvedPath: abs, found };
  if (found) {
    const st = statSync(abs);
    entry.kind = st.isDirectory() ? "directory" : "file";
    if (entry.kind === "file") {
      const content = readFileSync(abs, "utf8");
      entry.bytes = content.length;
      entry.firstLine = content.split("\n")[0];
    }
  }
  return entry;
}

const results = [
  loadArtifact("Demo Episode workspace", "episodes/demo-episode"),
  loadArtifact(
    "Visual Identity (fixture)",
    "episodes/demo-episode/fixtures/visual-identity.md",
  ),
  loadArtifact(
    "Production Playbook (fixture)",
    "episodes/demo-episode/fixtures/production-playbook.md",
  ),
];

const allResolved = results.every((r) => r.found);
const timestamp = new Date().toISOString();

const lines = [];
lines.push("# Runtime Smoke Test Report");
lines.push("");
lines.push(`Generated: ${timestamp}`);
lines.push(`Repository root: \`${REPO_ROOT}\``);
lines.push("");
lines.push(
  "Scope: Repository Resolver + basic artifact loading only. Does not " +
    "invoke any Worker, Contract, or Manifest.",
);
lines.push("");
for (const r of results) {
  lines.push(`## ${r.label}`);
  lines.push(`- Status: ${r.found ? "RESOLVED" : "MISSING"}`);
  lines.push(`- Requested path: \`${r.relativePath}\``);
  lines.push(`- Resolved path: \`${r.resolvedPath}\``);
  if (r.found) {
    lines.push(`- Kind: ${r.kind}`);
    if (r.kind === "file") {
      lines.push(`- Size: ${r.bytes} bytes`);
      lines.push(`- First line: \`${r.firstLine}\``);
    }
  }
  lines.push("");
}
lines.push(`## Result: ${allResolved ? "PASS" : "FAIL"}`);
lines.push("");

const reportPath = resolvePath("runtime/smoke-test-report.md");
writeFileSync(reportPath, lines.join("\n") + "\n", "utf8");

console.log(lines.join("\n"));
console.log(`(report written to ${reportPath})`);

process.exit(allResolved ? 0 : 1);
