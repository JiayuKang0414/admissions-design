# We Reimagine Learning

Independent landing-page presentation using UMD Design System 2.1.0 and page-builder `4cadc21`.

View: https://jiayukang0414.github.io/admissions-design/presentation/reimagine-learning/

Reference: https://fearlesslyforward.umd.edu/we-reimagine-learning, captured November 14, 2026. The existing Do Good presentation remains at its original URL and is unchanged.

## Page composition

| Original content | Presentation component |
| --- | --- |
| We Reimagine Learning title, full introduction and Startup Shell photo | Small, centered, standard Hero, full bleed |
| Here at UMD, education is edu-action. | Ordinary light Pathway, image left, original body and Learn More destination |
| Latest News | Native News List in a 992px lock, three initial articles and native load-more pagination |
| Three innovation and entrepreneurship statistics | Three native large Stats with red dividers in a 1600px gapped grid |
| Ecosystem heading and xFoundry video | Wide Section Intro, followed by a responsive 16:9 YouTube embed and the original caption in a 992px lock |
| Academy, Arts for All, Do Good Accelerator and Pitch Dingman | Four aligned Standard Cards with original photographs, in a 1600px two-column grid |
| Jennifer King Rice quotation | Feature Quote Light in a 1280px lock, native default text size for the full quotation |
| Apply, Join, Support, Connect, Cheer | Five Image Overlay Cards in the native three-column grid, arranged 3+2 |

There are seven top-level sections: the ecosystem heading, video and four program cards belong to one section. Landing margins use 56/80/120px; child gaps use 32/40/48px. The source has no carousel or side navigation.

All editorial copy, statistics, link destinations and photographs come from the source snapshot. The statistics are reproduced source content, not independently updated claims. The source news grid displayed nine articles; this presentation uses a compact list with three initial articles and access to more through native pagination and the original Read More destination. Action-card descriptions remain in accessible link labels.

The new page reuses the user-approved navigation and visual footer from the Do Good presentation at build time. Desktop labels remain on one line, with the native drawer at narrower widths. Support Maryland retains the approved native utility typography and external-link SVG. Published assets are copied locally, so viewing this page does not require the Do Good page to be present.

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

Checked theme values, house class names, canonical critical CSS, verbatim source copy, component slots, section order, local image hashes and paths, image descriptions, unique IDs, internal anchors and original card destinations. The news API returned two distinct batches of three articles, including images. Hash checks confirm that the Do Good builder, HTML, documentation and Pathway helper remain unchanged.

Browser visual and interaction verification is incomplete: the supported Browser connection fails with `Cannot redefine property: process`. No screenshot, computed-style, responsive rendering or load-more interaction check is claimed.
