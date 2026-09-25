#!/usr/bin/env node
// One-command publish for emsenn.net.
//
// The site's actual deploy mechanism is GitHub Actions
// (.github/workflows/publish.yml): a push to `main` builds with Hugo
// (extended, "latest"), indexes with Pagefind, and mirrors the result into
// the public emsenn/emsenn-net-frontstage repo that GitHub Pages serves at
// emsenn.net. That plumbing already exists and needs no new deploy path --
// what was missing was one local command that (a) fails fast on a broken
// build *before* pushing, so a bad commit never reaches Actions, and (b)
// watches the resulting Actions run through to a pass/fail result instead of
// leaving the operator to go check by hand.
//
// This script never invents content and never force-pushes; it refuses on a
// dirty working tree rather than auto-committing this personal site's prose
// on the Leader's behalf.
//
// Usage: node scripts/publish.mjs [--skip-build-check] [--no-watch]

import { spawnSync } from "node:child_process";
import { mkdtempSync, rmSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";

const args = new Set(process.argv.slice(2));
const skipBuildCheck = args.has("--skip-build-check");
const noWatch = args.has("--no-watch");

function run(cmd, cmdArgs, options = {}) {
  const result = spawnSync(cmd, cmdArgs, { encoding: "utf8", ...options });
  return { status: result.status, stdout: (result.stdout ?? "").trim(), stderr: (result.stderr ?? "").trim() };
}

function must(cmd, cmdArgs, options = {}) {
  const result = run(cmd, cmdArgs, options);
  if (result.status !== 0) {
    process.stderr.write(`${result.stderr || result.stdout}\n`);
    throw new Error(`${cmd} ${cmdArgs.join(" ")} exited ${result.status}`);
  }
  return result;
}

console.log("[1/4] Checking working tree is clean...");
const status = must("git", ["status", "--porcelain"]);
if (status.stdout.length > 0) {
  console.error("Working tree has uncommitted changes. Commit your content first:");
  console.error(status.stdout);
  process.exit(1);
}

const branch = must("git", ["rev-parse", "--abbrev-ref", "HEAD"]).stdout;
if (branch !== "main") {
  console.error(`On branch '${branch}', not 'main'. Publish only runs from main.`);
  process.exit(1);
}

if (!skipBuildCheck) {
  console.log("[2/4] Verifying the Hugo build succeeds before pushing...");
  const hugoVersion = run("hugo", ["version"]);
  if (hugoVersion.status !== 0) {
    console.error("hugo not found on PATH. Install a current extended Hugo release (the theme requires Hugo >= 0.128 for the `try` template function; Ubuntu's apt hugo 0.123 is too old).");
    process.exit(1);
  }
  const tmp = mkdtempSync(join(tmpdir(), "emsenn-net-publish-check-"));
  try {
    const build = run("hugo", ["--gc", "--minify", "--destination", tmp]);
    if (build.status !== 0) {
      console.error("Local Hugo build failed -- refusing to push a broken commit:");
      console.error(build.stderr || build.stdout);
      process.exit(1);
    }
    console.log(build.stdout.split("\n").filter((line) => line.includes("Pages") || line.includes("Total")).join("\n"));
  } finally {
    rmSync(tmp, { recursive: true, force: true });
  }
} else {
  console.log("[2/4] Skipping local build check (--skip-build-check).");
}

console.log("[3/4] Pushing main to origin (triggers the Publish emsenn.net workflow)...");
const beforeSha = must("git", ["rev-parse", "HEAD"]).stdout;
must("git", ["push", "origin", "main"]);

if (noWatch) {
  console.log("Pushed. Not watching the run (--no-watch). Check with: gh run list --workflow=publish-emsenn-net.yml");
  process.exit(0);
}

console.log("[4/4] Watching the GitHub Actions run through to completion...");
const gh = run("gh", ["--version"]);
if (gh.status !== 0) {
  console.log("gh CLI not available -- cannot watch the run automatically. Check https://github.com/emsenn/emsenn-net-backstage/actions");
  process.exit(0);
}

// Give Actions a moment to register the new push before we start watching.
await new Promise((resolvePromise) => setTimeout(resolvePromise, 8000));

let runId;
for (let attempt = 0; attempt < 6 && runId === undefined; attempt += 1) {
  const list = run("gh", ["run", "list", "--workflow=publish-emsenn-net.yml", "--json", "databaseId,headSha,status", "--limit", "5"]);
  if (list.status === 0) {
    const runs = JSON.parse(list.stdout || "[]");
    const match = runs.find((candidate) => candidate.headSha === beforeSha);
    if (match !== undefined) runId = match.databaseId;
  }
  if (runId === undefined) await new Promise((resolvePromise) => setTimeout(resolvePromise, 5000));
}

if (runId === undefined) {
  console.log("Could not locate the triggered run yet. Check: gh run list --workflow=publish-emsenn-net.yml");
  process.exit(0);
}

const watch = run("gh", ["run", "watch", String(runId), "--exit-status"]);
console.log(watch.stdout);
if (watch.status !== 0) {
  console.error(`Publish workflow run ${runId} did not succeed.`);
  console.error(watch.stderr);
  process.exit(1);
}
console.log(`Publish workflow run ${runId} succeeded. emsenn.net is updated.`);
