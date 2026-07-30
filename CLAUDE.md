# Claude Code — Admissions Design

This is the **Admissions design project**. It builds on the design-system page builder (vendored as a submodule at `page-builder/`).

## Where to find things

| What | Location |
|---|---|
| Slash commands | `page-builder/.claude/commands/*.md` |
| Layout/spacing/component rules | `page-builder/RULES.md` |
| Component slots & attributes | `page-builder/registry/` |
| Critical CSS (canonical) | `page-builder/styles/critical.css` |
| Skeleton + inlined CSS | `page-builder/TEMPLATE.html` |
| Layout HTML patterns | `page-builder/LAYOUT-PATTERNS.md` |
| Generic page-builder overrides | `page-builder/OVERRIDES.md` |
| **Admissions-specific overrides** | `OVERRIDES.md` (this repo) |

The page-builder's own `CLAUDE.md` (`page-builder/CLAUDE.md`) defines the canonical rules — read it. This file layers admissions-specific guidance on top.

## Output paths

- New admissions pages → `pages/<page-name>.html`
- New admissions images → `images/academics/`, `images/admissions/`, or a new `images/<page>/` folder per page
- Briefs / source notes → `briefs/<page-name>.md`

Do **not** write to `examples/` or `test/` — test/qa fixtures live in the page-builder repo, and demo/example pages live in the separate `page-builder-examples` repo, not here.

## Image paths

- **Admissions-owned** (logos, page-specific photography): `../images/...`
- **Shared library** (large/small/medium campus, people, events, default): `../page-builder/images/large/...` etc.

When `images-index.json` is needed, read `page-builder/images/images-index.json`.

### Image optimization scope

When shrinking oversized images (the `/optimize-images` skill or ad-hoc), only touch **static** JPG/PNG/WebP. **GIFs, animated WebPs, and video files are out of scope** — don't resave or report on them (resampling breaks animation, and they need dedicated tooling). Exclude `.gif` and video extensions from scans, and check `n_frames > 1` on any WebP before touching it. This rule is also baked into `~/.claude/commands/optimize-images.md`.

## Shared chrome and reference pages

Every page within a single design project must use the **same site header, navigation, logo, and footer**. Pages in this project should look like a coherent site — they should not invent their own chrome, nav items, or logo treatment.

### The chrome lives in `shared/` — never copy it between pages

| File | What it holds |
|---|---|
| `shared/header.html` | Header stack: `umd-element-navigation-utility` + `umd-element-utility-header` + `umd-element-navigation-header` with the project nav items and logo |
| `shared/footer.html` | `umd-element-footer data-display="visual"` |
| `shared/chrome.css` | CSS companions the chrome markup depends on (see below) |
| `shared/chrome-scripts.html` | Chrome-driven shadow injections (nav-header logo width) |

**Edit `shared/`, then run the inliner:**

```bash
python3 scripts/build-chrome.py          # splices shared/ into every page in pages/
python3 scripts/build-chrome.py --check  # exits non-zero if any page is stale (CI-friendly)
```

Each region sits between `SHARED:<key>:START` / `:END` markers in the page. **Do not hand-edit anything between those markers** — the next run overwrites it. On a page that has no markers yet, the script finds the existing chrome by content and wraps it, so adding a new page needs no special setup.

The two generated pages (`scripts/build-programs.py`, `scripts/build-colleges-schools.py`) emit the *same* blocks via `scripts/_chrome.py`, so running any of the three converges on identical bytes — there is no ordering dependency between them.

Only the content between the header and footer is page-specific.

### ⚠️ Why the CSS and scripts live with the markup

**`page-builder/TEMPLATE.html` does not contain every rule the chrome needs.** Before the extraction these rules sat in a page-specific `<style>` block while the markup was copied from a sibling page — so building a `<head>` from TEMPLATE while copying markup from a page silently dropped them. No console error, no layout break, just unstyled chrome. That happened twice.

| Rule | Why TEMPLATE isn't enough |
|---|---|
| `umd-element-navigation-header div[slot="utility-navigation"] a` | `critical.css` §11's BASE layer styles `.umd-shell-utility-item a`, which never matches this project's plain `<a>` children — they render browser-default blue and underlined without it. Must load **after** the critical block to win at equal specificity. |
| `umd-element-scroll-top[data-layout-fixed="true"]` | Pins to `right:24px; bottom:24px`; the DS default is `right:40px; bottom:10vh`. Opt-in per page, but styled from `shared/` wherever used. |

**Chrome vs. page-level shadow injections.** Only injections driven by the *chrome* belong in `shared/chrome-scripts.html` — currently just the nav-header logo width. The pathway aspect-ratio, banner-promo stacked-actions, call-to-action and card-overlay injections are driven by **page content** and stay in the page that uses them. Don't move them to `shared/`; a page with no `umd-element-pathway` should not carry the pathway injection.

**When verifying:** assert utility-nav `gap: 24px` **at ≥1024px** — the DS hides the utility slot below desktop, so it measures 0×0 at tablet width and a narrow viewport masks the bug entirely. Also check `umd-element-scroll-top` computes `right/bottom: 24px` and that the nav logo's shadow `max-width` is `320px`.

### Projects that don't yet have a reference page

Not every design project will start with an existing `shared/` chrome. In that case, the **first page built establishes it** — make the header/nav/logo/footer choices intentionally, extract them into `shared/` straight away, and treat that as authoritative for every subsequent page in the project.

### The chrome is project-scoped

`shared/` lives in this repo only — never copy this project's chrome into the `page-builder/` submodule, and never assume a different design project (e.g. a future `engineering-design` repo) will share these specific nav items, logos, or footer image. The submodule provides the components; each design project owns its own chrome composition.

That scoping is why `shared/chrome.css` is not upstreamed: the flat-`<a>` utility-nav treatment is *this project's* composition choice, not a design-system default. The one genuinely generic bug it exposed — `critical.css` §11 zeroing the slot gap unconditionally — was fixed upstream instead (`design-system-page-builder` `be3ea6c`).

## Logos

| Slot | Path |
|---|---|
| Header (`umd-element-navigation-header` `slot="logo"`) | `../images/logos/admissions-logo.svg` |
| Footer (`umd-element-footer` `slot="logo"`) | `../images/logos/footer-logo.svg` |
| Fallback (header onerror) | `../images/logos/primary-logo-dark.svg` |

Always include the `onerror` runtime fallback for hotlink-protected URLs (see page-builder/CLAUDE.md).

## Verifying pages in the preview pane

When checking admissions pages in the in-app Browser pane (`mcp__Claude_Browser__*`) against the `admissions-static` dev server, watch for these known quirks:

- **Viewport desync.** A *fresh* tab reports the correct `window.innerWidth` on first measure, but after `location.reload()` or re-`navigate` on the same tab it often sticks at `0` (or a stale width like `375`). When `innerWidth` is `0`, all media queries fail and computed styles read as base/mobile values — this is **not** a CSS bug. Fix: open a fresh tab (and close old ones — there's an ~8-tab cap).
- **Blank screenshots.** `computer{action:screenshot}` frequently returns a blank light-gray image even when the DOM/CSS engine is healthy. Rely on DOM/computed-style assertions via `javascript_tool` for verification, not screenshots.
- **Stale cache.** Navigating to a just-edited page can serve a cached copy. Confirm with `curl` that the dev server serves the change, then navigate with a cache-buster query (`?v=2`) to force a fresh load.

Practical verification recipe: assert on computed styles (9 CSS bundles loaded, `customElements.get(...)` registered, utility-nav gap `24px`, no horizontal overflow) via `javascript_tool` in a fresh tab, rather than trusting screenshots or a reused tab.

## Source of truth hierarchy (admissions)

1. Slash commands in `page-builder/.claude/commands/*.md`
2. `page-builder/RULES.md`
3. `page-builder/registry/`
4. `page-builder/styles/critical.css`
5. `OVERRIDES.md` (this repo) — admissions-specific shadow injections and class overrides
6. `page-builder/OVERRIDES.md` — generic shadow injections (visit-card, banner-promo, etc.)
