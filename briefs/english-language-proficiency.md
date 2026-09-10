# English Language Proficiency

- Source: https://admissions.umd.edu/apply/english-language-proficiency
- Retrieved: 2026-09-03
- Output: `pages/how-to-apply/english-language-proficiency.html`
- Parent: `How To Apply > International Applicants`

## Component plan

- The original dark `umd-element-hero-minimal`, using the exact three SVG arrow shapes from the homepage's central UMD brand animation. The original black arrow is recolored white, while the gold-over-red-over-white staggered arrangement sits on the hero's black image area.
- `umd-element-breadcrumb` and a two-level `umd-element-nav-slider` matching the page hierarchy.
- Existing rich-text styles for all editorial copy and waiver requirements.
- Three full-width `umd-element-accordion-item` components for the accepted tests, all initially closed.
- A standalone rich-text section using the standard two-column pattern for the alphabetical English-speaking countries and territories list.
- A two-column rich-text section inside the interior content area for the Maryland English Institute resource, with a taller cropped image on the left and the uppercase Resources eyebrow above the rule, heading, copy and secondary CTA on the right.
- The shared four-page interior `umd-element-banner-promo`, constrained to the 800px content column, with mailing-list and Connect inline links plus one “Join the List” CTA.

## Design check

The three accepted tests contain enough copy that a three-column card grid becomes narrow and vertically stretched, so they use full-width accordions for compact scanning and mobile readability. The country names are a continuous alphabetical list rather than comparative tabular data, so they appear in their own section using the standard responsive two-column rich-text pattern and stack into source order on mobile. The MEI resource also uses the responsive two-column rich-text pattern so it remains within the interior page and stacks in source order on mobile. The hero retains the compact dark minimal treatment and uses the homepage brand animation's original staggered arrow geometry in gold, red and white; the long-form content stays on white for readability.

Visible source copy and links are preserved. Navigation and breadcrumbs are adapted to the prototype's local information architecture.
