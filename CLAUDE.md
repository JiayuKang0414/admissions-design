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

### Reference page for this project

For admissions-design, the canonical reference is **`pages/academics.html`** — it is the established landing-page design for this project. When building a new page in this repo:

1. Open `pages/academics.html` and copy verbatim:
   - The full header stack (`umd-element-navigation-utility` + `umd-element-utility-header` + `umd-element-navigation-header` with the project nav items)
   - The footer block (`umd-element-footer data-display="visual"`)
   - End-of-body shadow-injection scripts (pathway aspect ratio, banner-promo gap, nav-header logo width, etc.)
2. Use the same logo paths, the same nav item set, and the same footer image — do not substitute or reorder.
3. Only the `<main>` content between the header and footer is page-specific.

### Projects that don't yet have a reference page

Not every design project will start with an existing reference page. In that case, the **first page built becomes the reference** — establish header/nav/logo/footer choices intentionally, document them, and treat that page as authoritative for every subsequent page in the project.

### Reference pages are project-scoped

Reference pages live in this repo only — never copy this project's chrome into the `page-builder/` submodule, and never assume a different design project (e.g. a future `engineering-design` repo) will share these specific nav items, logos, or footer image. The submodule provides the components; each design project owns its own chrome composition.

A future task will extract this project's chrome into `shared/header.html` / `shared/footer.html` and add a build script to inline them.

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
