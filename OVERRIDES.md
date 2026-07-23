# Admissions Overrides

Admissions-specific shadow-DOM injections, class overrides, and utility classes that aren't general enough to live in `page-builder/OVERRIDES.md` or `page-builder/styles/critical.css`.

## Admissions logo width override

`umd-element-navigation-header` shadow CSS hard-codes `.element-header-logo img { max-width: 240px }` at tablet+. The admissions wordmark is wider than the default UMD primary wordmark, so we shadow-inject `max-width: 320px`.

Source: `pages/admissions.html` and `pages/academics.html` end-of-body scripts.

Pages using this: `pages/admissions.html`, `pages/academics.html`, `pages/student-life.html`, `pages/tuition.html`.

## Pathway 1:1 image aspect ratio

`umd-element-pathway` has no CSS variable / `::part` hook for the image container; the design calls for a 1:1 image crop, so we shadow-inject `.pathway-image-container, .image-container, .umd-asset-image-wrapper-scaled { aspect-ratio: 1/1 !important; height: auto !important }` plus an `object-fit: cover` rule on the inner `<img>`.

Pages using this: `pages/academics.html`, `pages/student-life.html`, `pages/tuition.html`.

## Banner-promo stacked actions

`umd-element-banner-promo` reprojects `slot="actions"` into its shadow DOM under `.banner-promo-actions` with no gap when actions stack. Shadow-inject `display:flex; flex-direction:column; align-items:flex-end; gap:8px` so primary + secondary CTAs stack with 8px spacing.

Pages using this: `pages/academics.html`, `pages/student-life.html`, `pages/tuition.html`.

## Study-here / eyebrow + rich-text intro section

Custom `.study-here-section` / `.study-here-content` / `.study-here-chevron` layout — pairs a `umd-element-brand-logo-animation` chevron, anchored full-bleed and offset upward into the hero above, with an HR rule + uppercase eyebrow + rich-text body inside `umd-layout-space-horizontal-small`. Hidden below tablet to avoid single-column crowding. Used as the canonical "intro under the hero" pattern for landing pages in this project.

Pages using this: `pages/academics.html`, `pages/student-life.html`, `pages/tuition.html`.

## Quote + brand chevron overlap

Custom `.quote-with-chevron` / `.chevron-overlap` layout used on the admissions homepage between the dark About UMD section and the overlay-card bank. Not generalizable yet — admissions-only for now.

## Card-overlay horizontal padding (desktop+)

`umd-element-card-overlay` (image variant) renders its content inside a shadow-DOM `.card-overlay-image-container` with hard-coded horizontal padding of `token.spacing.md` (24px) at every breakpoint — the upstream styles only adjust `padding-top` at the medium breakpoint, leaving sides at 24px from mobile through 4K. On wide viewports this crowds the headline/eyebrow/CTA against the card edges.

Shadow-inject step-up horizontal padding aligned to the upstream token breakpoints (`highDef.min` = 1200px, `maximum.min` = 1500px):

```css
.card-overlay-image-container { padding-left: 24px !important; padding-right: 24px !important; }
@media (min-width: 1200px) { .card-overlay-image-container { padding-left: 32px !important; padding-right: 32px !important; } }
@media (min-width: 1500px) { .card-overlay-image-container { padding-left: 48px !important; padding-right: 48px !important; } }
```

**Upstream candidate:** this should fold into `web-elements-library/src/composite/card/overlay/image.ts` as additional `createMediaQuery` entries on the `card-overlay-image-container` style block, mirroring the existing `medium.min` paddingTop step-up. The vertical padding does not need to change.

**Scope caveat:** the step-up should only apply when overlay cards sit inside a horizontally-bounded layout (i.e. within `umd-layout-space-horizontal-*`). When the cards are in a "lock" / full-bleed bank that runs edge-to-edge to the browser viewport, the original 24px sides should be retained — the extra side padding is meant to give breathing room inside a constrained card width, not to inset content within an already-edge-to-edge band. Upstream should gate the wider padding on a layout context check (or expose a CSS variable / opt-in attribute so the page can suppress it for full-bleed banks).

Pages using this: `pages/admissions.html`.

## Deadlines table

`.deadlines-table` — simple two-column rich-text table for the Important Dates section. Admissions-specific.

## Small pathway zig-zag — responsive image + balanced grid

Hand-composed "Small pathway style zig zag" rich-text sections (`umd-layout-space-horizontal-small` → `umd-layout-grid-gap-two` → text column + `figure.umd-layout-alignment-block-stacked` image column, alternating column order for the zig-zag). Modeled on the QA design-team `/components/images-and-media` sections `section-60493` / `section-60498`.

Two gotchas required page-level CSS (the inlined `critical.css` subset has no global responsive-image rule):

```css
/* Let the 1fr tracks shrink; otherwise a wide image's min-content forces
   its grid track to the image's intrinsic width and unbalances the columns. */
.umd-layout-grid-gap-two > * { min-width: 0; }
.umd-layout-grid-gap-two figure.umd-layout-alignment-block-stacked img {
  display: block; width: 100%; height: auto;
}
```

Also: a true large headline (`umd-sans-extralarge-bold`, 32px) must sit **outside** the `umd-text-rich-advanced` wrapper — `.umd-text-rich-advanced > * { font-size: 18px }` flattens every `umd-sans-*` class inside it (weight still applies). Put the `<h2>` as a sibling above the rich-text block with `umd-layout-space-vertical-headline-large` for spacing.

Divider rule under the headline (1px black, as in the source): the inlined critical CSS gives `<hr>` no styling (default UA border is an inset ~2px grey). Add `<hr>` as the **first child** of the rich-text block so its 24px above/below spacing comes from `.umd-text-rich-advanced`, and style it:

```css
.umd-layout-grid-gap-two .umd-text-rich-advanced hr {
  border: 0; border-top: 1px solid #000; height: 0;
}
```

Pages using this: `pages/student-life.html`.

## Real design-system layout styles (`layout.min.css`)

All four pages now load the DS layout stylesheet in `<head>`, **before** the inline critical CSS:

```html
<link rel="stylesheet" href="https://unpkg.com/@universityofmaryland/web-styles-library/css/layout.min.css">
```

`layout.min.css` is self-contained (no `var(--token)` dependencies — literal values), so it loads safely on its own without the other CDN bundles. It's placed before the inline `<style>` so the hand-rolled inline layout rules still **win** wherever they exist — adding the link is therefore non-disruptive (identical rendering; the DS sheet just becomes the base/fallback). This matches the load order the canonical `TEMPLATE.html` uses (CDN links → inline subset → `cdn.js`).

`student-life.html` removed its local `.umd-layout-grid-gap-two` block so the DS owns it — this fixed a mobile bug: the hand-rolled copy only applied `gap` at ≥650px, dropping the 32px gap between stacked columns on mobile; `layout.min.css` correctly applies `@media (max-width:649px){gap:32px}`.

**Not stripped (deliberate):** the other inline layout duplicates (horizontal/vertical spacing, other grid classes) were kept. They already match the DS values exactly (verified: horizontal padding 24→48→64px, landing margins 56→80→120px), some carry page-specific extras the DS lacks (e.g. `.umd-layout-space-horizontal-larger` adds `container-type: inline-size; isolation: isolate`), and they use interwoven shared selectors (`[class^="umd-layout-space-horizontal-"]`). A blanket strip is maintainability-only with real regression risk and no functional gain, so it was deferred to a careful, per-breakpoint-verified pass.

Pages: `pages/academics.html`, `pages/admissions.html`, `pages/student-life.html`, `pages/tuition.html`.
