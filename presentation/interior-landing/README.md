# UMD Do Good Landing Page

A full-width landing presentation titled **Building a Do Good Campus**, built with UMD Design System 2.1.0 and page-builder 4cadc21.

View online: https://jiayukang0414.github.io/admissions-design/presentation/interior-landing/

The existing URL is retained for shared links. This is a landing page with seven sections, followed by the site footer.

## Layout

| Section | Native layout / width |
| --- | --- |
| Hero | Full-bleed small centered hero with the Do Good Campus title, complete introduction and original sculpture photo |
| Do Good Month | Full-bleed standard dark Pathway; cropped image left, text right |
| Do Good, Now | 1600px gapped four-column Standard Card Group, eight cards |
| President Pines quote | 1280px Feature Quote Light, native default text size |
| Site Events with Feature | Dark section, 1600px sticky columns: one Large Feature Event and four List events |
| United in Purpose | Full-bleed Image Expand with a short heading and supporting body text |
| Connect with Maryland | 1600px native three-column Image Overlay Card grid; five links in 3+2 |

The user requested removal of the complete Find a different way forward, Small sparks. Extraordinary possibilities., A classroom without walls, See an idea take shape, Where your interests meet your impact, Learning with a purpose., Your next step starts here, News Feed and Promo Banner sections. Those sections remain removed. A separately approved five-link navigation group now follows the six retained sections, whose content and settings remain unchanged.

Native landing spacing remains 56px mobile, 80px tablet and 120px desktop; intro-to-content gaps are 32/40/48px.

## Content and images

The hero uses the supplied Building a Do Good Campus title and complete introduction, with the original Do Good sculpture photo at focal position 71.21% 45.81%. The Pathway retains its original photo and copy, with image display height capped at 480px. The four-column group is a fixed snapshot of eight Maryland Today articles matching the supplied screenshot, including original summaries, dates, links and local photos.

The Pines quotation and attribution are preserved. Site Events retains the five original source photographs and activity descriptions, including the full April 1–30 service challenge range. Events are labelled as April 2026 highlights.

Image Expand retains the heading “We are united in purpose to do good” and body “Another way the University of Maryland is leading Fearlessly Forward.” Its content matches the [UMD homepage](https://umd.edu/): a right-aligned 480px column with a native red vertical divider. It reuses the original 4000px Do Good sculpture photo and appears before the final navigation group.

All editorial photos and logos are local. The UMD runtime and fonts require an internet connection. There is no live news feed or YouTube embed in the current page.

The final group contains Apply, Join, Support, Connect and Cheer, using the five original photographs and destination URLs from the reference page. Native Image Overlay Cards use uppercase labels and arrow links, in the native three-column grid inside a 1600px lock. Desktop produces 3+2 with equal card widths; narrower screens use the native single-column layout. Cards retain their default size and original new-tab link behavior.

## Local development

Run `python3 build.py` from this folder to generate `dist/index.html`. Build inputs are `../../page-builder/TEMPLATE.html`, `do-good-stories.json`, `site-events.json` and `action-links.json`. The removed feed configuration is no longer a build dependency. `asset-sources.json` records image provenance; `OVERRIDES.md` records composition details.

For local viewing, run `python3 -m http.server 4173 --directory dist`, then open http://localhost:4173.

## Validation

Theme and class-name validators, canonical critical CSS, seven-section order, removal of the nine requested sections, unchanged retained sections, unique IDs, local assets and internal links are checked before publication. The native four-column grid provides one mobile column, two at 650px and four at 1024px.

Browser visual/interaction verification has not been completed: supported Browser initialization fails with “Cannot redefine property: process.” No screenshots or computed-style verification are claimed.
