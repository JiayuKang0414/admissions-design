# We Reimagine Learning

Independent landing-page presentation using UMD Design System 2.1.0 and page-builder `4cadc21`.

View: https://jiayukang0414.github.io/admissions-design/presentation/reimagine-learning/

Reference: https://fearlesslyforward.umd.edu/we-reimagine-learning, captured November 14, 2026. The Do Good presentation keeps its separate original URL.

## Page composition

| Original content | Presentation component |
| --- | --- |
| We Reimagine Learning title, full introduction and Startup Shell photo | Small, centered, standard Hero, full bleed |
| Here at UMD, education is edu-action. | Ordinary light Pathway, image left, original body and Learn More destination |
| Latest News | Native News Feed cards in a 1600px lock, three columns and one initial row, with native load-more pagination |
| Three innovation and entrepreneurship statistics | Three native large Stats with red dividers in a 1600px gapped grid |
| Ecosystem heading and xFoundry video | Wide Section Intro, followed by a responsive 16:9 YouTube embed and the original caption in a 992px lock; caption title uses native 18px bold sentence-case text |
| Academy, Arts for All, Do Good Accelerator and Pitch Dingman | Four aligned Standard Cards with original photographs, in a 1600px two-column grid |
| Jennifer King Rice quotation | Feature Quote Light in a 1280px lock, native default text size for the full quotation |
| Apply, Join, Support, Connect, Cheer | Five Image Overlay Cards in the native three-column grid, arranged 3+2 |

There are eight top-level sections: Hero, Pathway, News, Statistics, ecosystem heading with video, program cards, Quote and action cards. The video with its caption and the four program cards are separate sections, giving them the same 120px desktop separation as the other major components. Landing margins use 56px below 768px, 80px at 768–1023px and 120px at 1024px and above. Intro-to-content gaps use 32/40/48px. The source has no carousel or side navigation.

All editorial copy, statistics, link destinations and photographs come from the source snapshot. The statistics are reproduced source content, not independently updated claims. The source news grid displayed nine articles; this presentation uses the user-requested cards layout with three initial articles and access to more through native pagination and the original Read More destination. Action-card descriptions remain in accessible link labels. The xFoundry title and paragraph are supplementary video copy inside its figcaption, not an additional section heading. The caption starts 16px below the video.

The new page reuses the user-approved navigation and visual footer from the Do Good presentation at build time. Desktop labels remain on one line, with the native drawer at narrower widths. Support Maryland retains the approved native utility typography and external-link SVG. Published assets are copied locally, so viewing this page does not require the Do Good page to be present.

Current-navigation state is applied separately on each page: Innovations in Teaching and Learning is selected here, and A Do Good Campus is selected on the Do Good page. Desktop and mobile menus agree. Both entries link to their respective published presentation pages.

## Build and files

From the repository root:

```sh
python3 presentation/reimagine-learning/build.py
```

Build inputs are `content.json`, `news-feed-config.json`, `../../page-builder/TEMPLATE.html` and the approved `../interior-landing/dist/index.html` chrome. The builder only reads that existing page. It never rebuilds or edits it.

`dist/` contains the deployable `index.html` and local assets. `asset-sources.json` records original image URLs and hashes; `source-snapshot.json` records the source capture. `feed-validation.json` records the checked public news responses without the feed token. The source page supplies the public, read-only news configuration; do not print it in logs. `OVERRIDES.md` describes scoped layout and chrome adaptations.

For a local preview:

```sh
python3 -m http.server 4173 --directory presentation/reimagine-learning/dist
```

Open http://localhost:4173. UMD component bundles, fonts, live news and YouTube require an internet connection. The video uses the privacy-enhanced embed URL without the original tracking parameter.

## Verification

Checked theme values, house class names, canonical critical CSS, verbatim source copy, component slots, section order, local image hashes and paths, image descriptions, unique IDs, internal anchors and original card destinations. The news API returned two distinct batches of three articles, including images. Navigation checks verify each page's own selected item and destination in desktop and mobile menus, with main content unchanged by the navigation correction.

Browser visual and interaction verification is incomplete: the supported Browser connection fails with `Cannot redefine property: process`. No screenshot, computed-style, responsive rendering or load-more interaction check is claimed.
