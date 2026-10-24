# HeatSync Labs Wiki

**This repository is the HeatSync Labs wiki.** Read it here:

## 👉 https://github.com/heatsynclabs/gh-wiki/wiki

The `wiki/` folder in this repo is the reviewed source of every wiki page; the GitHub wiki above is published from it
automatically. To search the whole wiki's text, use the search box at the top of this repository (it searches `wiki/`),
or [search the published wiki](https://github.com/search?q=repo%3Aheatsynclabs%2Fgh-wiki&type=wikis). The wiki's own
sidebar has a *Find a page* filter for page titles.

| Folder | What it is |
|---|---|
| `wiki/` | Every wiki page as GitHub-flavored Markdown, plus `wiki/files/` for uploads. Mirrored 1:1 to the GitHub wiki. |
| `tools/` | The converter used for the migration from MediaWiki (pandoc + a Lua filter) and the history replay script. |
| `archive/` | Raw MediaWiki export: every revision of every page as JSON (`mediawiki-history.json.gz`), site info, upload list, and the list of files that were already missing from the old server. |

## How to change the wiki

1. Edit the page under `wiki/` (file name = page title with spaces as `-`; `wiki/Home.md` is the front page).
2. Open a pull request against `main`.
3. Once it is approved and merged, the **Publish wiki** workflow pushes the change to the GitHub wiki within a minute or two.

`main` is protected: no direct pushes, one approving review required, and administrators are not exempt.
That gives every wiki change a reviewed, attributable audit trail (the PR plus the commit).

Editing pages directly in the GitHub wiki UI is discouraged: the workflow re-mirrors `wiki/` onto the wiki after
every merge and once a day, so unreviewed edits do not persist (they remain visible in the wiki repo's own git history).

### Page conventions

- Links between pages are plain relative links: `[Laser Cutters](Laser-Cutters)`.
- Uploads live in `wiki/files/`; reference them as `![alt](files/Name.jpg)` or `[manual](files/Name.pdf)`.
- `wiki/_Sidebar.md` and `wiki/_Footer.md` are the wiki sidebar and footer.
- `Category-*.md` pages end with a generated **Pages in this category** list from the migration; keep it up to date by hand.
- `Files.md` is an index of every upload, including the ones the old server had already lost.

## Migration notes

Migrated from the MediaWiki at `wiki.heatsynclabs.org` (MediaWiki 1.19). Every revision of every page was replayed as a
git commit, authored by the original wiki user name (with a non-deliverable `@wiki.heatsynclabs.invalid` address, since the
old wiki stored no emails) and carrying the original edit summary, revision id and timestamp. Run `git log --follow wiki/<Page>.md`
to see a page's history back to 2009.

To re-run the conversion: `python3 tools/replay.py <export-dir> <out-dir>` produces git fast-import streams; see the docstring.
