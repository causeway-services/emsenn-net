# emsenn-net-theatre

The emsenn.net production site, in two acts:

- `backstage/` — Hugo source (content, config, theme)
- `frontstage/` — built HTML, published via GitHub Pages as `emsenn.net`

Edit in `backstage/`; `frontstage/` is CI-published output, not hand-edited.

## Publishing (one command)

`cd backstage && pnpm run publish` (or `node scripts/publish.mjs`). It:

1. refuses on a dirty working tree or a branch other than `main` (it never
   commits content on the Leader's behalf);
2. builds the site locally with Hugo first and refuses to push if that build
   fails, so a broken commit never reaches CI;
3. pushes `main`, which is what actually triggers the real deploy path --
   `.github/workflows/publish-emsenn-net.yml` builds with Hugo (extended,
   pinned to "latest" in CI), indexes with Pagefind, and mirrors the result
   into `emsenn/emsenn-net-frontstage`, which GitHub Pages serves at
   `https://emsenn.net`;
4. watches the resulting Actions run (via `gh run watch`) through to a
   pass/fail result instead of leaving the operator to check by hand.

Local build verification requires a current Hugo **extended** binary (the
theme's `render-link.html` uses the `try` template function, added in Hugo
0.128 -- Ubuntu's packaged `hugo` 0.123.7 is too old and errors). Installed
locally at `/usr/local/bin/hugo` (v0.164.0 extended) on 2026-07-23, which
takes precedence over the apt package on `PATH`.

Verified 2026-07-23: theme submodule initializes over SSH
(`git submodule update --init --recursive`), a full local build with the
pinned-current Hugo produces the same 1063-page route set as the live
`frontstage/` checkout (differences limited to the Pagefind index, which is a
separate CI step, and files `frontstage/` intentionally excludes), SSH push
authenticates against `origin` (`git push --dry-run` succeeded), and `gh run
list --workflow=publish-emsenn-net.yml` reaches the real workflow history.
The end-to-end script itself (commit → push → watched CI run) was not run
live in that verification pass because it refuses to run against its own
uncommitted addition to this repo, and this pass was instructed not to
commit; the Leader's next real content commit is the first live end-to-end
exercise of `publish.mjs`.

## Queued but unpublished content (checked 2026-07-23)

None. No `draft: true` front matter, no untracked or staged files in
`backstage/`, and `backstage`'s local `main` is identical to `origin/main`.
The last real content commit is from 2026-06-03 (`content/blog` itself last
dated 2026-03-29); the only commit since is a 2026-07-17 tag-only commit
touching no content. Nothing is sitting ready to publish.
