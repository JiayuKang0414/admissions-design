# UMD Learning Landing Page

A full-width landing presentation titled **We Reimagine Learning**, built with UMD Design System 2.1.0 and page-builder 4cadc21.

View online: https://jiayukang0414.github.io/admissions-design/presentation/interior-landing/

The existing URL is retained for shared links. The page uses landing rules throughout, with no interior sidebar or global 800px content cap.

## Layout

Every section uses native landing spacing: 56px mobile, 80px tablet, 120px desktop. Intro-to-content gaps are 32/40/48px.

| Section | Native layout / width |
| --- | --- |
| Hero | Full-bleed small standard hero, centered title |
| Original hero description | Text-only section intro below hero |
| Do Good Month | Full-bleed native standard dark Pathway; cropped image left, text right |
| Do Good, Now | 1600px gapped four-column Standard Card Group, eight cards |
| Standard cards | 1600px gapped two-column grid |
| Statistics grid | 1600px dark band, three large plain statistics |
| Visual tabs | 992px, centered section intro |
| President Pines quote | 1280px native Feature Quote Light, default size for the 259-character text |
| YouTube | 992px, responsive 16:9 |
| Overlay cards | 1600px no-gap two-column image mosaic |
| Statistics list | 1600px native sticky columns with stacked statistics |
| Accordions | 992px, adjacent native siblings with 8px gaps |
| Site Events with Feature | Dark section, 1600px sticky columns: one Large Feature Event and four dark List events |
| News Feed | 992px native live news list, three initial articles and load more |
| United in Purpose | Full-bleed Image Expand with the complete declaration, white native heading and Do Good sculpture photograph |
| Promo banner | 1600px final gold call to action |

The original two-column standard and overlay grids are retained. A third, four-column Standard Card Group was explicitly requested directly after the Pathway. The separate live news collection still uses a list. The Pines section uses native Feature Quote Light with its light-gray panel and background texture; the long quote keeps the native default text size. Its exact quotation, attribution and title are retained.

## Content and images

The exact hero title/description, four navigation labels, Do Good Month image/copy and President Pines quotation are retained from the supplied references. Site Events with Feature uses a dark section and Do Good Challenge as the Large Feature Event, with Do Good Service Challenge, Terps Earth Day Park Clean Up, Maryland Day and Terps Against Hunger in the dark List. The feature uses the native image-above-text composition, large date sign and Featured Event eyebrow ribbon. All five use the reference page's original photos, text and destination URLs. Calendar cards are labeled April 2026 highlights. Source statistics include snapshot/date context.

- https://fearlesslyforward.umd.edu/we-reimagine-learning
- https://fearlesslyforward.umd.edu/do-good-now
- https://today.umd.edu/umd-names-inaugural-do-good-campus-signature-initiatives

All editorial photographs and logos are local. The new eight-card collection is a fixed editorial snapshot matching the supplied screenshot, with text and images verified from Maryland Today on November 12, 2026. It is separate from the existing live News Feed. The Pathway retains the original photo and crops its display to at most 480px high, with the people kept in focus. The UMD runtime/fonts, live news and YouTube require an internet connection. The intentionally public read-only news configuration matches the original reference page’s category.

The supplied United in Purpose declaration appears in a native Image Expand directly before the Promo Banner. It reuses the original 4000px Do Good sculpture photo from the reference page. The native component controls image expansion, overlay and scrolling; the heading uses white UMD typography. Its content is constrained to 800px, while the component itself remains full bleed. No custom animation or internal CSS override is added.

## Local development

Source: build.py. Run `python3 build.py` from this folder to generate `dist/index.html`; the build uses `../../page-builder/TEMPLATE.html`, `do-good-stories.json`, `site-events.json` and the local `news-feed-config.json`. `asset-sources.json` records photograph provenance. Custom composition notes are in `OVERRIDES.md`.

For local viewing, run `python3 -m http.server 4173 --directory dist`, then open http://localhost:4173.

## Validation

Passed: theme and class-name validators; canonical critical CSS; landing-rule and component inventory audit; correct per-component locks; source copy; local assets and anchors; unique IDs; ISO event dates and stat length limits; published landing spacing rules at 375/768/1440px; stylesheet parsing; native live-news initial and next-three pagination. The eight standard cards retain original images, article links, summaries and dates; native grid rules provide one mobile column, two at 650px and four at 1024px. The latest Site Events change preserves all other sections and validates one native Large Feature Event, four List events, section-wide dark theme coverage, five source photographs, destination URLs, complete date ranges and themed CTAs.

Browser visual/interaction verification remains unavailable: supported Browser initialization fails with “Cannot redefine property: process.” No screenshots or computed-style verification were claimed.
