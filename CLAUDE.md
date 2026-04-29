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

## Shared chrome

All admissions pages should render the same header stack and footer. The chrome lives inline in each page for now (see `pages/admissions.html` lines ~445–515 and ~975–982 for the canonical header/footer). When adding a new page, copy the chrome blocks from an existing page rather than reinventing them.

A future task will extract the chrome into `shared/header.html` / `shared/footer.html` and add a build script to inline them.

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
