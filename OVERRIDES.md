# Admissions Overrides

Admissions-specific shadow-DOM injections, class overrides, and utility classes that aren't general enough to live in `page-builder/OVERRIDES.md` or `page-builder/styles/critical.css`.

## Admissions logo width override

`umd-element-navigation-header` shadow CSS hard-codes `.element-header-logo img { max-width: 240px }` at tablet+. The admissions wordmark is wider than the default UMD primary wordmark, so we shadow-inject `max-width: 320px`.

Source: **`shared/chrome-scripts.html`** — this is the one shadow injection driven by the chrome rather than by page content, so it ships with the header. Inlined into every page by `scripts/build-chrome.py`; do not copy it into a page.

Pages using this: all seven (verified rendering at `max-width: 320px`).

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

## `pages/programs.html` — A–Z program explorer (experts-style filter)

New page recreating <https://admissions.umd.edu/programs> in the DS. Chrome (header/nav/footer/end-of-body scripts + inlined `critical.css`) copied verbatim from the `pages/academics.html` reference. Only `<main>` is page-specific: a small hero + a two-column **filter rail + A–Z directory**, modeled on the client-side filter UX of <https://umdrightnow.umd.edu/experts> (which has no alphabet nav of its own — that piece is original).

- **Data is embedded, not fetched.** All 203 programs (name, dept link, type labels, colleges, interests, **plain-text description**) are inlined as a JS array in an end-of-body `<script>` (harvested once from the admissions Craft GraphQL endpoint; descriptions stripped of HTML). Filtering is 100% client-side over that in-memory array — no runtime API/token dependency. Regenerate via `python3 scripts/build-programs.py` (reads `briefs/programs-data.json`, takes the `<head>` from `page-builder/TEMPLATE.html` and the header stack from `pages/academics.html`). The generated HTML is overwritten wholesale — edit the JSON or the generator's literal blocks, not the page.
  - **The description transform is order-sensitive:** strip tags → unescape entities → collapse whitespace. Any other order changes the bytes (a stray double space where a tag was removed, or `&amp;` surviving literally). The array is serialised with `separators=(',', ':')`, which keeps it at ~129KB instead of ~132KB.
  - **The generator's literal blocks are RAW strings** (`r'''…'''`). They contain CSS/JS backslash escapes (`\2212`, `“`); as normal triple-quoted strings Python reinterprets those and the output is silently corrupted.
  - Grid-entry animations stay **inlined** on this page rather than using `<script src="../page-builder/scripts/grid-animations.js">`. The inlined copy (77 lines) predates and differs from the canonical script (114 lines), so switching is a behavioural change, not a refactor — do it deliberately, not as a side effect of regenerating.
- **Filter model** mirrors experts: free-text search + three accordion checkbox groups (Program Types / Colleges & Schools / Interests). **AND across groups, OR within a group.** Removable "Filtered by:" pills + Clear all; Reset; mobile Filter toggle. Page-built control classes are `pf-*`. The rail's **REFINE** heading uses the DS **`.umd-tailwing-right-headline`** (from `element.min.css`) — a 14px uppercase label with a thin rule trailing to the right; it requires a `<span>` child (masks the line behind the text via inherited white bg) and auto-adds `margin-top:40px` to the following element.
- **Search bar** sits in the results column under the A–Z nav (its own `#pf-search-bar` form, not in the rail), styled after the experts search. The input needs *no* custom box CSS — the DS global `base.min.css` rule `input{}` already supplies the experts look (white bg, `1px solid #E6E6E6`, `12px 16px` padding, full width). The form itself wears the DS **`.umd-layout-background-highlight-light`** class (from `layout.min.css`): gray `#F1F1F1` panel + `border-left:2px solid #E21833` + responsive padding (24→32→56px) — the experts "highlight card". The only page-built piece is the 48px square Maryland-red submit button (`.pf-search-submit`, `#e21833`, hover `#a90007`) holding the experts search-glyph SVG, in a `flex; gap:8px` row.
- **Option labels use the DS `.umd-field-checkbox-wrapper` class** — the DS-native fix for the global `base.min.css` rule `label{font-weight:700}` (that element rule is why bare `<label>` choice text renders bold). `.umd-field-checkbox-wrapper` ships `font-weight:400`, so only the group **header** button stays bold. No page-level weight override, no upstream change needed. Per-option result counts (`(104)`) use `.umd-sans-smaller` (14px grey) rather than a pill, to keep the checkbox/text baseline aligned.
- **Program rows use `umd-element-card data-display="list"`** (no image slot): `headline` = program name (linked to dept page), **`text` = the program description**, and the **`date` slot carries the type labels** (`Major | Limited Enrollment Program`) — the DS list card has no dedicated badge slot, so the bottom date slot is repurposed per design direction. `<p slot="date">`, not `<time>`, renders fine.
- **Active-filter pills** ("Filtered by: …") use the DS **`.umd-pill-list`** child treatment (`#FAFAFA` 12px squared chip, hover yellow `#FFD200`) — the pill buttons are wrapped in a `<span class="umd-pill-list pf-pill-cluster">` (the wrapper's DS `margin-top:-8px` hack is neutralized in favor of flex gap; button hover-yellow added in page CSS since the DS rule targets `a`). Each pill's text + × sit in an inner `<span>` (DS `> span{display:flex;gap:4px}`). The **results count** (`.pf-count-line`) and the **Clear all** link use `.umd-sans-smaller` (14px).
- **Hero** is left-aligned (omit `data-layout-text` — `center` is its only alignment value, left is the default), height `small`, with a primary CTA in `slot="actions"` linking to the colleges-schools page. Image `images/academics/students-walking.jpg` (converted from the sibling `.webp` via `sips`; 2880×1088, ~460KB).
- **`.az-letter`** in-list letter headings: `margin-bottom` 8px mobile, **24px at ≥1024px**.
- **Scroll-to-top** (`umd-element-scroll-top`) is placed once at the end of `<main>`, before the footer. Gotcha: the DS fixed-position rule (`web-components.min.css`) keys on `[data-layout-fixed="true"]` (explicit value) or a bare `[fixed]` attribute — a boolean `data-layout-fixed=""` does **not** match and the button stays `position:static` in flow. Use `data-layout-fixed="true"`. DS default is `right:40px; bottom:10vh`; page CSS overrides to `right:24px; bottom:24px` (fixed to the viewport bottom-right). Component is 52×52 at `z-index:9999`; smooth-scrolls to top on click.
- **"Reset filters" is an outline CTA** (`umd-element-call-to-action data-display="outline"` wrapping a `<button type="button">`). The CTA clones its child into shadow DOM, so a native `type="reset"` can't reach the light-DOM form; the reset is wired by listening for `click` on the light-DOM `.pf-actions` wrapper (the composed click on the shadow-cloned button retargets to the CTA host and bubbles there) → `clearAll()` unchecks all boxes, clears the search, re-renders. Same `clearAll()` backs the "Clear all" pill.
- **A–Z typography:** letter quick-nav uses `.umd-campaign-extrasmall` (32px) and in-list letter headings use `.umd-campaign-small` (44px desktop), both recolored to Maryland red `#e21833`. Nav letters with no matches render as dimmed grey `.az-off` spans; active letters smooth-scroll to their section (`scroll-margin-top:120px` clears the sticky nav). Active letters recompute on every filter change.

No shadow injections introduced. Page-specific CSS lives in its own `<style>` block before `</head>`; data + filter logic in a `<script>` before `</body>`.

## `pages/colleges-schools.html` — expandable college card grid

New page recreating <https://admissions.umd.edu/programs/colleges-schools> in the DS. Chrome (header/nav/footer + inlined `critical.css`) copied verbatim from the `pages/programs.html` sibling; only the hero, intro, and the college grid are page-specific. Regenerate via `python3 scripts/build-colleges-schools.py` (reads `briefs/colleges-schools-data.json`, splices into the `TEMPLATE.html` head + programs chrome). The generated HTML is overwritten wholesale — edit the JSON or the generator's `PAGE_CSS`/`PAGE_JS` blocks, not the page.

- **Hero is identical to `pages/programs.html`** — `umd-element-hero data-layout-height="small"`, no `data-layout-text` (left is the default; `center` is its only alternative), CTA in `slot="actions"`. Verified pixel-identical to the sibling: 400px host height, `h1.umd-campaign-extralarge` at 80px, headline and CTA both at `left: 64px` inside the shadow `umd-layout-space-horizontal-larger umd-lock`.
- **Lock is `umd-layout-space-horizontal-larger` (1600px)**, matching the other card grids in this project. (`umd-layout-space-horizontal-large` / 1400px was tried first; it is a real class — see the lock table in `page-builder/RULES.md` § "Available classes", which lists all six including `-large`.)
- **Intro mirrors the sibling landing pages' rich-text lockup** (`pages/academics.html` "Study Here"): narrow centred `umd-layout-space-horizontal-small` (992px) column, 1px black `<hr>`, lead paragraph, then `.umd-text-rich-advanced` body. Unlike the sibling, the lead is **not** `text-transform: uppercase`, per design direction. There is no breadcrumb — the source page has one, but no other page in this project uses it.
- **Replaces the source's 13 stacked full-width rows with a bordered card grid** (1 / 2 / 3 cols at 650 / 1024px, `gap: 40px 32px` at desktop). Page-built classes are `cs-*`. Cards carry image + red uppercase abbreviation eyebrow + college name + description; description is `-webkit-line-clamp: 4` on the card and repeated in full inside the panel, so no copy is unreachable. Flex `margin-top:auto` on `.cs-tile-foot` pins the toggle to the bottom so tiles in a row equalize (478px at 1440px).
- **Card type scale is copied from the DS card-standard, measured off a live `umd-element-card` rather than read from source**: eyebrow 12px/700, headline 18px/700, body 16px/400 `#454545`. The card's `.umd-element-eyebrow` lives in its shadow styles and ships in **no** CDN bundle, so the eyebrow is restated in page CSS. The real `umd-element-card` is deliberately **not** used: it clones slotted content into shadow DOM, so a slotted toggle button's later `aria-expanded` / chevron-state mutations would never reach the rendered clone.
- **Measure the type classes, don't read them.** A locally downloaded `typography.min.css` disagrees with what the live bundle serves. Live, at 1280px: `smaller` 14 / `small` 16 / `medium` 18 / `large` 18-bold / `larger` 22 / `largest` **44**-bold (they scale fluidly below ~1200px). Reading the file instead cost a round trip here — `umd-sans-largest` was picked for the panel heading expecting 22px and rendered 44px.
- **Expansion is an "expander row", not a per-card accordion.** All 12 panels are children of the same grid, `grid-column: 1 / -1`, parked at the **end** of the grid where `display:none` removes them from grid flow. On open, JS moves the panel to sit immediately after the **last tile in the clicked tile's row** — `rowEnd = min(ceil((idx+1)/cols)*cols - 1, tiles.length-1)`, with `cols` read from `getComputedStyle(grid).gridTemplateColumns`. Without this the panel would break its row part-way and shunt its row-mates down. Single-open, like an accordion group. At 1 column this degrades to a plain accordion (panel lands directly after its own tile) for free.
- **Re-anchoring on viewport change is driven by `matchMedia` change events plus a 150ms-debounced `resize` fallback — deliberately NOT `requestAnimationFrame`.** rAF never fires while `document.hidden` is true, which is permanently the case in the in-app Browser pane (it renders offscreen); an rAF-based re-anchor silently no-ops there and would also stall in any backgrounded tab. Note the preview pane changes the viewport via a CDP metrics override that re-evaluates media queries but dispatches **no** `resize` or `change` event, so this path cannot be exercised by `resize_window` alone — verify by dispatching `new Event('resize')` after resizing.
- **Panel chrome borrows the DS accordion** without using the component (which has no multi-column body or grid-row placement): `border-top: 4px solid #e21833` over a `--umd-color-gray-lightest` body. Majors list is 1 / 2 / 3 / 4 columns at 650 / 1024 / 1280px; program names are `umd-sans-small` (16px). The heading is `umd-sans-larger` (22px) and the lead paragraph `umd-sans-medium` (18px).
- **The panel's lead paragraph is capped at `max-width: 960px`** — the DS paragraph measure, lifted from `element.min.css`: `:is(.umd-text-rich-advanced,.umd-rich-text) p,ul,ol,pre,blockquote { max-width: 960px }`. The value is **restated** rather than inherited by wrapping the paragraph in `.umd-rich-text`, because that class also forces `font-size: 18px` on its children and this paragraph is `.umd-sans-small` (16px). The majors grid below it still uses the panel's full width.
- **Program-type labels use the DS pill geometry with an outline, and are not clickable.** `.cs-types` wears `umd-pill-list` (12px, `padding: 8px 12px`, `#FAFAFA`) and `.cs-type` adds a 1px `--umd-color-gray-light` border. Children are `<span>`, not `<a>` — the DS hover-yellow rule is scoped to `a:hover`/`a:focus`, so spans stay inert and read as labels. **No per-type colour coding:** `Major` / `Minor` / `Certificate` / `Limited Enrollment Program` are peers, and an earlier revision that gave `Major` a black rule and LEP a red one implied a hierarchy that doesn't exist.
- **Pills sit on their own line below the program name**, which is `display: block` (`.cs-major-name`). `.cs-types` is `display: flex; flex-wrap: wrap; gap: 8px; margin-top: 8px`, so the 8px separation is identical horizontally, vertically between wrapped pill rows, and between the name and the pills. The DS pill rhythm (`.umd-pill-list` wrapper `margin-top: -8px` + child `margin-top: 8px`) is **neutralised** via `.cs-types > .cs-type { margin-top: 0 }` — left in place it double-counts against the flex gap and knocks rows out of alignment. Note `.cs-types > .cs-type` (0,2,0) is needed to beat the DS `:is(.umd-text-cluster-pill,.umd-pill-list) > *` (0,1,0).
- **Majors grid caps at 3 columns (1 / 2 / 3 at 650 / 1024px) — don't add a 4th.** The constraint is `Limited Enrollment Program`, the widest pill at 183px: a Major+Minor+LEP trio needs ~323px on one line. Measured at 1440px on CMNS (31 programs): **4 cols** (274px) → the trio wraps, row heights 91/131/135, spread 44px, 2 pill groups wrapping; **3 cols** (378px) → trio fits on one line, heights 91/113, spread 22px, **0** wrapping; **2 cols** (588px) → uniform 91px. 3 is the sweet spot — it buys row-height evenness for +16% panel height (1067 → 1238px), where 2 costs +56% for little further gain. Verified the same at 59 programs (ARHU: spread 22px, 0 wrapping). If the LEP label is ever shortened, a 4th column becomes viable again.
- **No CTAs inside the panels.** The college website is reachable from two places that already exist: the **card headline** and the **panel headline**, both linked to the college domain (`target="_blank" rel="noopener"`). An earlier revision also put a "Visit …" outline CTA at the foot of every panel — redundant, and 12 of them added noise.
- **Letters & Sciences has zero majors** (it's the undeclared-advising home), so its tile renders a direct `.cs-tile-link` to `ltsc.umd.edu` instead of a toggle, and no panel is generated. Journalism has exactly one program, so the toggle label is singularized ("View 1 program").
- **A11y:** each toggle carries `aria-expanded` + `aria-controls`; each panel is `role="region"` with `aria-labelledby` pointing at its `tabindex="-1"` heading, which receives focus on open. `Escape` closes and returns focus to the toggle; the Close button does the same. Deep links (`#agnr`) open the matching college on load and on `hashchange`.
- **Grid entry animations are opted out** (`data-animation="off"` on `.cs-grid`) — the stagger fights the expand/collapse motion.

- **Chrome CSS is harvested from the reference page, not hand-copied** (§24 "PROJECT CHROME COMPANIONS" in the generated page). Two chrome rules live in `pages/programs.html`'s *page-specific* `<style>` block rather than `TEMPLATE.html`: the `div[slot="utility-navigation"]` flat-link restore (critical.css §11 targets the DS `.umd-shell-utility-item` pattern and scopes `gap: 0`, which jams this chrome's plain `<a>` children together unstyled) and the `umd-element-scroll-top[data-layout-fixed]` 24px/24px pin (DS default is `right:40px; bottom:10vh`). Building the head from TEMPLATE alone shipped the chrome markup without either, and **both regressions were silent** — no console error, correct-looking DOM, just wrong rendering. The generator now extracts any rule whose selector matches `CHROME_CSS_SELECTORS` from the reference page's page-specific CSS and **asserts at build time** that the markup and its CSS are both present, so the two cannot drift apart. Verified pixel-identical to `programs.html` at 1440px: slot 141×18 at top 68, links at x 1220/1307, gap 24px, scroll-top fixed 24/24. See `CLAUDE.md` § "Chrome markup alone is not enough".
- **Verify the utility nav at ≥1024px.** The DS hides the utility slot below desktop, so it measures 0×0 at tablet width — a narrow viewport masks this bug entirely. (An earlier check in this session recorded `utilityNavGap: "0px"` and it was mistaken for normal.)

No shadow injections introduced. The page references the canonical `../page-builder/scripts/grid-animations.js` by `src` rather than inlining it (per `page-builder/CLAUDE.md`); the older sibling pages still inline that block.

## Shared chrome (`shared/` + `scripts/build-chrome.py`)

The site chrome — header stack, footer, its CSS companions, and its shadow injection — was copy-pasted into all seven pages, with the CSS living in a different place from the markup. That split caused two silent regressions while building `pages/colleges-schools.html` (unstyled utility nav; scroll-top falling back to the DS `right:40px; bottom:10vh`), so it is now extracted.

- **Source of truth is `shared/`**: `header.html`, `footer.html`, `chrome.css`, `chrome-scripts.html`. `scripts/_chrome.py` wraps each in `SHARED:<key>:START` / `:END` markers; `scripts/build-chrome.py` splices them into every page in `pages/`. The two page generators emit the identical blocks via the same module, so running any of the three converges — no ordering dependency. `--check` exits non-zero if a page is stale.
- **Migration is content-located, not marker-dependent.** On a page with no markers the script finds the existing chrome by content and wraps it, so a new page needs no setup. A zero-width insertion slot (chrome CSS before `</head>`, chrome scripts before `</body>`) must emit its own trailing newline — without it the block runs straight into the following tag (`<!-- SHARED:chrome-css:END --></head>`).
- **Only chrome-driven injections are shared.** `shared/chrome-scripts.html` holds just the nav-header logo width. The pathway aspect-ratio, banner-promo stacked-actions, call-to-action and card-overlay injections are driven by page **content** and stay with the page — verified by usage: `student-life.html` has zero `umd-element-pathway` and correctly carries no pathway injection.
- **Two drifts were normalised**, both confirmed with the user rather than assumed: the footer logo now points at `admissions.html` on all seven pages (it was `https://admissions.umd.edu/` on six and `/` on one, so clicking it left the prototype for production, while the header logo was already relative), and `admissions.html` gained the `line-height: 1.25` on utility links that the other six already had.
- **Scroll-to-top stays opt-in** (only the two long directory pages use the element), but its pin lives in `shared/chrome.css` so it is styled consistently wherever it appears.

### Known remaining drift — the inlined `critical.css` block

`build-chrome.py` deliberately does **not** touch the inlined critical block. Against the current `page-builder/TEMPLATE.html`: `programs.html` is in sync; `colleges-schools.html` differs only by its own appended page CSS; the four other hand-authored pages differ only by the §11 `:has()` gate; and **`admissions.html` carries two intentional page-specific edits inside that block** — an extra `.umd-layout-background-full-dark-no-bottom` utility, and a `:not(.quote-with-chevron)` exclusion on the dark→light transition selector.

Those two are why a blanket refresh from TEMPLATE would be wrong — it would silently clobber them. Rendering is unaffected by the §11 lag either way, because `shared/chrome.css` sets the flat-link `gap: 24px` explicitly on every page. Refreshing critical blocks is a separate task that has to preserve the `admissions.html` edits.

### Pre-existing, not introduced

`pages/admissions.html` has ~64px of horizontal overflow at 1440px. Measured on the pre-migration file as well (64px before, 63px after), with no light-DOM offenders, so it originates in a shadow root or a decorative absolutely-positioned element. Unrelated to the chrome extraction.
