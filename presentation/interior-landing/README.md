# Interior landing presentation

**We Reimagine Learning** — a visual University of Maryland interior page concept.

View online: https://jiayukang0414.github.io/admissions-design/presentation/interior-landing/

Built with UMD Design System 2.1.0 and page-builder 4cadc21. Includes the default small standard hero, breadcrumb, sidebar, section intro, two-column standard and overlay cards, tabs, accordions, a quote, statistics grid and list, promo banner, curated calendar highlights, a live native Maryland Today News Feed, and a YouTube embed.

Content draws on the two supplied Fearlessly Forward reference pages, with source links on the presentation. Calendar highlights are from April 2026; news is fetched dynamically from Maryland Today using the original reference page’s news category. All editorial photographs and logos are included in assets/. UMD components, fonts and YouTube require an internet connection.

This directory is standalone and is published by the repository’s existing GitHub Pages workflow.

The hero now uses the original We Reimagine Learning headline, description and Startup Shell background. Site navigation matches the four source sections. A two-column Do Good Month block uses the original College Park Scholars planting photograph, heading, copy and Learn More destination from the reference page.

News now uses the native `umd-feed-news` component rather than curated article cards: two columns, four initial stories and a native load-more control. It uses the intentionally public read-only feed configuration published on the supplied reference page. GraphQL and GitHub Pages CORS checks passed.

Spacing/link correction: calendar figure and caption retain32px gaps; fragment scrolling uses one header offset; quote padding is24px/32px; the tab-column gap is32px; sticky sidebar content can scroll on shorter viewports. Editorial/source/navigation links use native UMD text-link styles, while section actions use native secondary CTAs. CSS cascade checks at375/768/1440px and link/asset/component validation passed. Browser rendering remains unverified due to a browser-runtime connection failure.
