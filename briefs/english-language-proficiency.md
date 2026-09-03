# English Language Proficiency

- Source: https://admissions.umd.edu/apply/english-language-proficiency
- Retrieved: 2026-09-03
- Output: `pages/how-to-apply/english-language-proficiency.html`
- Parent: `How To Apply > International Applicants`

## Component plan

- Dark `umd-element-hero-minimal` for the interior-page title.
- `umd-element-breadcrumb` and a two-level `umd-element-nav-slider` matching the page hierarchy.
- Existing rich-text styles for all editorial copy and waiver requirements.
- Three full-width `umd-element-accordion-item` components for the accepted tests, with the first item initially open.
- The standard two-column rich-text pattern for the alphabetical English-speaking countries and territories list.
- Standard image-left `umd-element-pathway` for the Maryland English Institute resource and its secondary CTA.
- The same `umd-element-banner-promo` used on the other Admissions interior pages.

## Design check

The three accepted tests contain enough copy that a three-column card grid becomes narrow and vertically stretched, so they use full-width accordions for compact scanning and mobile readability. The country names are a continuous alphabetical list rather than comparative tabular data, so they use the standard responsive two-column rich-text pattern and stack into source order on mobile. The single MEI resource uses one standard pathway. Dark styling is limited to the minimal hero; the long-form content stays on white for readability.

Visible source copy and links are preserved. Navigation and breadcrumbs are adapted to the prototype's local information architecture.
