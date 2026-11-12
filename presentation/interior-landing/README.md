# Interior landing presentation

**We Reimagine Learning** — a visual University of Maryland interior page concept.

View online: https://jiayukang0414.github.io/admissions-design/presentation/interior-landing/

Built with UMD Design System 2.1.0 and page-builder 4cadc21. Includes the default small standard hero, breadcrumb, sidebar, section intro, two-column standard and overlay cards, tabs, accordions, a quote, statistics grid and list, promo banner, curated calendar highlights, a live native Maryland Today News Feed, and a YouTube embed.

Content draws on the two supplied Fearlessly Forward reference pages, with source links on the presentation. Calendar highlights are from April 2026; news is fetched dynamically from Maryland Today using the original reference page’s news category. All editorial photographs and logos are included in assets/. UMD components, fonts and YouTube require an internet connection.

This directory is standalone and is published by the repository’s existing GitHub Pages workflow.

The hero now uses the original We Reimagine Learning headline, description and Startup Shell background. Site navigation matches the four source sections. A two-column Do Good Month block uses the original College Park Scholars planting photograph, heading, copy and Learn More destination from the reference page.

News now uses the native `umd-feed-news` component rather than curated article cards: two columns, four initial stories and a native load-more control. It uses the intentionally public read-only feed configuration published on the supplied reference page. GraphQL and GitHub Pages CORS checks passed.

Spacing/link correction: calendar figure and caption retain32px gaps; fragment scrolling uses one header offset; the quote uses native inline spacing; the tab-column gap is32px; sticky sidebar content can scroll on shorter viewports. Editorial/source/navigation links use native UMD text-link styles, while section actions use native secondary CTAs. CSS cascade checks at375/768/1440px and link/asset/component validation passed. Browser rendering remains unverified due to a browser-runtime connection failure.

## Native interior quote

The President Pines quotation is 259 characters and uses the default inline `umd-element-quote`, without `data-visual-size="large"`, custom font overrides, a gray wrapper or added panel padding. It remains in the 800px interior column with the standard 56px mobile / 80px desktop section gap.

Native Design System 2.1.0 values:

| Viewport | Quote font / line height | Attribution | Title |
| --- | --- | --- | --- |
| 375px | Interstate 700, 18px / 25.2px | 16px | 14px italic |
| 768px | Interstate 700, 20.30px / 28.43px | 17.23px | 15.23px italic |
| 1440px | Interstate 700, 22px / 27.5px | 18px | 16px italic |

Quote-to-attribution margin is 16px. Native container layout switches at 500px: 24px left and 32px top padding below the breakpoint; 64px left and no top padding above it. Alignment is left. These are the component’s own styles; the campaign screenshot’s centered composition is a separate treatment.

Verified against the pinned component source, typography and spacing tokens. The font-face bundle includes the Interstate 600–700 face. Browser computed-style verification remains unavailable because the Browser connection fails at initialization.
