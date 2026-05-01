# Shared path remappings for admissions wrapper commands

Every slash command in this repo wraps a recipe from `page-builder/.claude/commands/`. The source recipes assume the page-builder repo is the working directory. Apply these remappings before executing the source recipe.

## Reads — page-builder resources

| In source recipe | Read here |
|---|---|
| `TEMPLATE.html` | `page-builder/TEMPLATE.html` |
| `RULES.md` | `page-builder/RULES.md` |
| `LAYOUT-PATTERNS.md` | `page-builder/LAYOUT-PATTERNS.md` |
| `REQUIRED-CSS.md` | `page-builder/REQUIRED-CSS.md` |
| `registry/...` | `page-builder/registry/...` |
| `styles/critical.css` | `page-builder/styles/critical.css` |
| `images/images-index.json` | `page-builder/images/images-index.json` |
| `OVERRIDES.md` (generic shadow injections) | `page-builder/OVERRIDES.md` — also read this repo's local `OVERRIDES.md`; the local one wins on conflict |

## Writes — admissions repo

| In source recipe | Write here |
|---|---|
| `examples/{slug}.html` (landing) | `pages/{slug}.html` |
| `test/{slug}.html` (sample) | `pages/{slug}.html` |
| Hardcoded `/Users/zjocson/repos/design-system-page-builder/examples/{slug}.html` | `pages/{slug}.html` |
| OVERRIDES harvest step | Update this repo's `OVERRIDES.md`, NOT the submodule's |

The page-builder is a submodule — never write inside `page-builder/` from this repo.

## Image refs in generated HTML

| Asset type | Path in generated HTML |
|---|---|
| Shared library: `large/`, `small/`, `medium/` (campus, people, events, default) | `../page-builder/images/large/...`, `../page-builder/images/small/...`, `../page-builder/images/medium/...` |
| Shared icons | `../page-builder/images/icons/...` |
| Admissions logos | `../images/logos/admissions-logo.svg` (header), `../images/logos/footer-logo.svg` (footer), `../images/logos/primary-logo-dark.svg` (onerror fallback) |
| Page-specific photography | `../images/{page-slug}/...` (create the folder if needed) |

## Header & footer chrome

Every admissions page renders the same chrome. Copy verbatim from `pages/admissions.html`:

- Header stack (`umd-element-navigation-utility` + `umd-element-utility-header` + `umd-element-navigation-header` with the Academics / Student Life / How To Apply / Tuition & Aid nav)
- Footer (`umd-element-footer data-display="visual"` with local footer logo + campus image)
- End-of-body shadow-injection scripts (pathway aspect ratio, banner-promo gap, nav-header logo width)

Do not invent new chrome. The shared chrome lives inline in each page until it is extracted to `shared/` partials in a future task.
