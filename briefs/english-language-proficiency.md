# English Language Proficiency

- Source: https://admissions.umd.edu/apply/english-language-proficiency
- Retrieved: 2026-09-03
- Output: `pages/how-to-apply/english-language-proficiency.html`
- Parent: `How To Apply > International Applicants`

## Component plan

- The original dark `umd-element-hero-minimal`, using the exact three SVG arrow shapes from the homepage's central UMD brand animation. The original black arrow is recolored white, while the enlarged gold-over-red-over-white staggered arrangement fills most of the hero's right image area.
- `umd-element-breadcrumb` matching the page hierarchy; no left navigation.
- Centered `umd-layout-space-horizontal-normal` content container (1280px maximum with responsive side padding), with long-form rich text capped at 800px and aligned left. Headings, accordions, and two-column sections use the full container width. Existing phone gutters, spacing, and stacking are preserved.
- Existing rich-text styles for all editorial copy and waiver requirements.
- Three full-width `umd-element-accordion-item` components for the accepted tests, all initially closed.
- A standalone rich-text section using the standard two-column pattern for the alphabetical English-speaking countries and territories list.
- A Resources section using `umd-layout-grid-gap-two` with one `umd-element-card-icon` for Maryland English Institute, matching the link-icon cards on the Academics page. The linked card heading replaces the separate CTA; both descriptive paragraphs are preserved. One card occupies the left column on desktop, leaving the second column empty, and uses the full width on mobile.
- The shared four-page interior `umd-element-banner-promo`, constrained to the design-system content container, with mailing-list and Connect inline links plus one “Join the List” CTA.

## Design check

The three accepted tests contain enough copy that a three-column card grid becomes narrow and vertically stretched, so they use full-width accordions for compact scanning and mobile readability. The country names are a continuous alphabetical list rather than comparative tabular data, so they appear in their own section using the standard responsive two-column rich-text pattern and stack into source order on mobile. The MEI resource uses the standard two-column icon-card grid and explicitly supports a single card without stretching it across both desktop columns. The decorative link icon and linked heading match the Academics page examples. The hero retains the compact dark minimal treatment and uses the homepage brand animation's original staggered arrow geometry in gold, red and white; the long-form content stays on white for readability.

Visible source copy and links are preserved. Navigation and breadcrumbs are adapted to the prototype's local information architecture.
