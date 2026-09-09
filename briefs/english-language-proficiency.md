# English Language Proficiency

- Source: https://admissions.umd.edu/apply/english-language-proficiency
- Retrieved: 2026-09-03
- Output: `pages/how-to-apply/english-language-proficiency.html`
- Parent: `How To Apply > International Applicants`

## Component plan

- Dark `umd-element-hero-minimal` for the interior-page title.
- `umd-element-breadcrumb` and a two-level `umd-element-nav-slider` matching the page hierarchy.
- Existing rich-text styles for all editorial copy and waiver requirements.
- Three full-width `umd-element-accordion-item` components for the accepted tests, all initially closed.
- A standalone rich-text section using the standard two-column pattern for the alphabetical English-speaking countries and territories list.
- A two-column rich-text section inside the interior content area for the Maryland English Institute resource, with its image on the left and copy and secondary CTA on the right.
- The same `umd-element-banner-promo` used on the other Admissions interior pages.

## Design check

The three accepted tests contain enough copy that a three-column card grid becomes narrow and vertically stretched, so they use full-width accordions for compact scanning and mobile readability. The country names are a continuous alphabetical list rather than comparative tabular data, so they appear in their own section using the standard responsive two-column rich-text pattern and stack into source order on mobile. The MEI resource also uses the responsive two-column rich-text pattern so it remains within the interior page and stacks in source order on mobile. Dark styling is limited to the minimal hero; the long-form content stays on white for readability.

Visible source copy and links are preserved. Navigation and breadcrumbs are adapted to the prototype's local information architecture.
