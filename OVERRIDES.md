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

**`.study-here-chevron` must give the wrapper an explicit height and NOT clip.** A DS bump changed `umd-element-brand-logo-animation` so its host no longer contributes height to the wrapper; the earlier `top:-180px` + `overflow:hidden` (no `bottom`) rule then collapsed to a 0-height box and clipped the animation to nothing. Correct rule mirrors the working `.chevron-overlap` (admissions homepage): wrapper `position:absolute; top:-180px; left:0; right:0; bottom:-80px; overflow:visible;` and the animation itself `position:absolute; top:0; left:0; right:0;`. The inset `bottom` gives real height; `overflow:visible` prevents clipping.

Pages using this: `pages/academics.html`, `pages/student-life.html`, `pages/tuition.html`, `pages/how-to-apply.html`.

## Quote + brand chevron overlap

Custom `.quote-with-chevron` / `.chevron-overlap` layout used on the admissions homepage between the dark About UMD section and the overlay-card bank. Not generalizable yet — admissions-only for now.

## When-to-Apply gold band (`.wta-gold`)

Custom Maryland-gold (`#FFD200`) band housing the bespoke deadline-finder widget (there is no DS component for a dropdown filter). The gold background sits on an inner `.wta-gold` div **inside** the `umd-layout-space-horizontal-larger` lock (not the `<section>`), so the band width matches the pathway content lock at every breakpoint (they coincide at ≥1200px; below that the pathway uses component-internal padding, the same minor offset every section-intro on these pages already has). Padding is `80px 48px` (48/24 on mobile). All text is forced black; the widget uses DS typography classes where possible (`umd-sans-smaller` labels, `umd-sans-small` rows/hint, `umd-sans-larger-bold` result title). The result panel uses `background: rgba(0,0,0,0.05)` with a red (`#e21833`) left accent and black row rules. Reset is a `umd-element-call-to-action data-display="secondary"` shown only after a full query executes; its click is delegated on `.wta__foot` so it survives the CTA reprojecting its slotted `<button>`. Text links use `umd-text-link-red` (black text, red underline on hover — the DS default link).

Pages using this: `pages/how-to-apply.html`.

## When-to-Apply left chevron (`.wta-chevron`)

Reuses `umd-element-brand-logo-animation` (same element as the study-here chevron) as a decorative right-pointing chevron entering from the **screen's left edge** and tucking **under** the gold band. Kept **unmirrored** (mirroring reverses the arrows) and shifted a full viewport left. Because the component anchors its cluster to the right of a 100vw internal box, pure-CSS viewport math drifts it off-screen on wide monitors — so a small script anchors it to the gold band's **left edge** (`bandLeft + 70`, recomputed on resize and on scroll-in) instead. It slides in from off-screen-left via an `IntersectionObserver` toggling `.wta-chevron.is-in` + a CSS transition (the DS `umd-animation-transition-slide-right` view-timeline did **not** scrub reliably here — it snapped to its end state). Sits at `z-index:0` under the lock (`z-index:1`).

**Three separate clips must be removed for the full 3-chevron stack to show:** `overflow` on `.wta-section` and `.wta-chevron` (both dropped — the stack only overflows off-screen-left, which never creates horizontal scroll), **and** the DS rule `umd-element-brand-logo-animation:defined { overflow: clip }` (a 25vw box), overridden to `overflow: visible` scoped to `.wta-chevron > umd-element-brand-logo-animation` so the study-here chevron is unaffected. Hidden below 1024px.

Pages using this: `pages/how-to-apply.html`.

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

Two-column image + text (zig-zag) rich-text sections — **now generalized in `page-builder/LAYOUT-PATTERNS.md`** ("Light background — two-column image + text (zig-zag)"), including the responsive-image / balanced-grid and `<hr>` border CSS; the headline-flattening gotcha (a true 32px headline must sit outside the `umd-text-rich-advanced` wrapper) lives in `page-builder/RULES.md §18`. Modeled on the QA design-team `/components/images-and-media` sections `section-60493` / `section-60498`.

Pages using this: `pages/student-life.html`.

## CDN-bundle architecture (migrated from self-contained inline CSS)

All four pages were migrated from the old **self-contained** model (a hand-rolled ~1.18.2-era critical.css inlined in full, no CDN CSS) to the canonical **`TEMPLATE.html` model**: the 9 DS CSS bundles loaded from unpkg, then the current Local-Only `critical.css` inlined, then `cdn.js`.

```html
<link ... css/font-faces.min.css>  <link ... css/tokens.min.css>       <link ... css/base.min.css>
<link ... css/typography.min.css>  <link ... css/element.min.css>      <link ... css/web-components.min.css>
<link ... css/layout.min.css>      <link ... css/animation.min.css>    <link ... css/accessibility.min.css>
<style> …verbatim styles/critical.css (header stripped)… </style>
<script src="…web-components-library@1.18.12/dist/cdn.js"></script>
```

Load order (CDN links → inline critical → `cdn.js`) matters: browsers block on stylesheet fetches before the script, so all CSS applies before elements upgrade. `cdn.js` was bumped `1.18.2 → 1.18.12` to align the component JS with the CSS bundles. This retired the hand-rolled carousel FOUC guards — `web-components.min.css` now ships the carousel host rules (`display`/`container-type`) + placeholder sizing; do **not** re-add a local `content-visibility: hidden` (it loads after the CDN link at equal specificity and reintroduces layout shift).

### Page-specific CSS preserved outside `critical.css`

The old inline block mixed critical CSS with project-specific rules. Those NOT in the CDN bundles or `critical.css` were moved to each page's second `<style>` block:

- **Utility-navigation flat links (all four pages).** These pages use plain `<a>` links in `div[slot="utility-navigation"]` (Visit UMD / Connect), **not** the DS `umd-shell-utility-item` pattern that `critical.css` §11 now targets. §11 scopes `umd-element-navigation-header div[slot="utility-navigation"] { gap: 0 }`, which jams flat links together. Fix: re-declare the flat-link `display:flex; gap:24px` + link styling at the **same** scoped specificity (`umd-element-navigation-header div[slot="utility-navigation"]`) in the page's second `<style>` so it wins by source order. (Future option: migrate the markup to the shell-utility-item pattern instead.)
- **`admissions.html` extras:** `.quote-with-chevron` / `.chevron-overlap`, `.deadlines-table`, `umd-element-hero-grid` height guard, `.banner-promo-actions`, rich-text heading specificity overrides, and `.umd-layout-grid-cards-no-gap` (used only on admissions; absent from CDN + critical.css) — preserved in a second `<style>` block appended after `cdn.js`.

`.umd-layout-grid-tuition-two` and `.umd-action-outline-block` live in `critical.css` (kept upstream), so they were not re-added except where already bundled in the admissions preserve block.

Pages: `pages/academics.html`, `pages/admissions.html`, `pages/student-life.html`, `pages/tuition.html`.

## Post-migration regression fixes

Two things regressed when the pages moved to the CDN-bundle architecture (the DS bundles differ from the old self-contained CSS):

**Rich-text eyebrow/header color.** The `umd-sans-*` typography classes set no color; `base.min.css` defaults paragraph text to the DS gray `#454545`, so section eyebrows ("Study Here", "Make UMD Yours", "College Is a Major Investment") rendered muddy gray instead of black. Fix: add `text-black` to the eyebrow `<p>` (light bg) — `.text-black` ships in `critical.css` and beats the base `p` color. Documented as a reusable pattern in `page-builder/RULES.md §18` and the `evaluate-design` component-risk list.

**"Information For" outline buttons (admissions).** Previously plain `<a class="umd-action-outline-block">` in a no-gap `umd-layout-grid-columns-four` (no spacing). Now the DS component: `umd-element-call-to-action[data-display="outline" data-theme="dark"]` in `umd-layout-grid-gap-four` (32px gap, 1→2→4 cols). The component's inner anchor is `inline-block` with a shadow-DOM `max-width:380px`, so it won't fill the cell — a shadow injection (see end-of-body script, keyed off `.information-for-actions`) forces the inner `[class*="umd-action-outline"]` to `width:100%; max-width:none; display:block; text-align:center`. Host filled via light-DOM `.information-for-actions umd-element-call-to-action { display:block; width:100% }`.
