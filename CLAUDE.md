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

Do **not** write to `examples/` or `test/` — those exist in the page-builder repo, not here.

## Image paths

- **Admissions-owned** (logos, page-specific photography): `../images/...`
- **Shared library** (large/small/medium campus, people, events, default): `../page-builder/images/large/...` etc.

When `images-index.json` is needed, read `page-builder/images/images-index.json`.

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

## Source of truth hierarchy (admissions)

1. Slash commands in `page-builder/.claude/commands/*.md`
2. `page-builder/RULES.md`
3. `page-builder/registry/`
4. `page-builder/styles/critical.css`
5. `OVERRIDES.md` (this repo) — admissions-specific shadow injections and class overrides
6. `page-builder/OVERRIDES.md` — generic shadow injections (visit-card, banner-promo, etc.)
