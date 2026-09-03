# English Language Proficiency

- Source: https://admissions.umd.edu/apply/english-language-proficiency
- Retrieved: 2026-09-03
- Output: `pages/how-to-apply/english-language-proficiency.html`
- Parent: `How To Apply > International Applicants`

## Component plan

- Dark `umd-element-hero-minimal` for the interior-page title.
- `umd-element-breadcrumb` and a two-level `umd-element-nav-slider` matching the page hierarchy.
- Existing rich-text styles for all editorial copy and waiver requirements.
- One three-card grid of bordered `umd-element-card` components for the accepted tests.
- The project-owned reusable rich-text table function for English-speaking countries and territories.
- Secondary `umd-element-call-to-action` for the Maryland English Institute resource.
- The same `umd-element-banner-promo` used on the other Admissions interior pages.

## Design check

The page has one true repeated-content family (the three accepted tests), so it uses one card grid. The country list remains a semantic table because its column structure is meaningful and the design system has no table component. The MEI resource stays in normal rich text with a CTA rather than introducing a second card treatment. Dark styling is limited to the minimal hero; the long-form content stays on white for readability.

Visible source copy and links are preserved. Navigation and breadcrumbs are adapted to the prototype's local information architecture.
