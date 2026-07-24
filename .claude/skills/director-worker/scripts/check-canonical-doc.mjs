// check-canonical-doc.mjs
//
// Detects whether a canonical document found by locate-inputs.mjs is
// real content or an empty placeholder. Production evidence: during
// manual validation, "Content_Constitution_v4_DRAFT.md.docx" turned out
// to contain a single sentence — "See content in downloaded file —
// Content_Constitution_v4_DRAFT.md" — pointing at a file that doesn't
// exist. That was caught by a human reading it. This check exists so a
// future run doesn't quietly cite a stub as if it were real guidance.
//
// No pandoc or Python is available in this environment (confirmed during
// manual validation — see episodes/luxury-destruction/director-package-comparison.md).
// .docx text is extracted the same way it was extracted by hand: unzip
// word/document.xml and strip tags.

import { readFileSync } from "node:fs";
import { execFileSync } from "node:child_process";

const STUB_PATTERNS = [/see content in/i, /placeholder/i, /^\s*$/];
const MIN_REAL_CONTENT_CHARS = 200;

function extractDocxText(path) {
  const xml = execFileSync("unzip", ["-p", path, "word/document.xml"], {
    encoding: "utf8",
  });
  const matches = [...xml.matchAll(/<w:t[^>]*>([^<]*)<\/w:t>/g)];
  return matches.map((m) => m[1]).join(" ");
}

/** @param {string|null} path */
export function checkCanonicalDoc(path) {
  if (!path) {
    return { available: false, reason: "not found in canonical/" };
  }

  let text;
  try {
    text = path.toLowerCase().endsWith(".docx")
      ? extractDocxText(path)
      : readFileSync(path, "utf8");
  } catch (e) {
    return { available: false, reason: `could not read: ${e.message}` };
  }

  const trimmed = text.trim();
  const looksLikeStub =
    trimmed.length < MIN_REAL_CONTENT_CHARS ||
    STUB_PATTERNS.some((p) => p.test(trimmed));

  if (looksLikeStub) {
    return {
      available: false,
      reason:
        "present but appears to be a stub/placeholder, not real content",
      extractedText: trimmed,
    };
  }

  return { available: true, path, text: trimmed, charCount: trimmed.length };
}
