# Apply Now — page brief

**Source:** https://admissions.umd.edu/apply-now
**Output:** `pages/apply-now/index.html`

The site's "apply" hub, linked from the header's red CTA. It is a top-level page
on the source site (`/apply-now`), not a child of How To Apply, so it gets its
own section directory. It has no `data-child-ref` group in `shared/header.html`,
so the mobile drawer opens at the top level rather than on a section — the same
correct behaviour as `pages/calendar/` and `pages/personas/`.

## Section map

| # | Section | Component | Notes |
|---|---|---|---|
| 2 | Hero | `umd-element-hero` small / center | Reuses `images/admissions/how-to-apply-hero.jpg` |
| 3 | #BeATerp Resources | rule + uppercase eyebrow + `.umd-text-rich-advanced`, brand chevron | Same lockup as academics §4, how-to-apply §4, transfer-applicants §3 |
| 4 | How to Apply | `umd-element-pathway` image left | Platform links promoted from inline prose to the actions slot |
| 5 | When to Apply | dark band: `umd-element-section-intro` + `umd-element-carousel-thumbnail` | Same treatment as transfer-applicants §6 |
| 6 | What to Submit | `umd-element-pathway` image right | Checklist bullets become secondary CTAs |
| 7 | Resources | light: `section-intro` + 2 × `umd-element-card-icon`, one section / one lock | Gap from `umd-layout-vertical-landing-child` on the intro (32/40/48px) |
| 8 | Stay connected | `umd-element-banner-promo` | The source's footer CTA band |

## Deliberate departures from the source

- **Platform links promoted to CTAs.** The source buries Common App / ApplyWeb as
  inline links inside a paragraph. On a page whose only job is "apply", they
  become the actions row, and the two ApplyWeb routes are named by applicant type
  rather than the source's ambiguous repeated "ApplyWeb".
- **Deadlines as a carousel, not a 3-up grid.** The source shows five dates under
  three applicant-type headings. `transfer-applicants.html` §6 already
  established a thumbnail carousel of transparent text-only cards for
  "Application Deadlines"; this page reuses it so the treatment reads the same
  everywhere in the project. The applicant type moves to the card eyebrow so each
  slide stands alone.
- **No breadcrumb.** The source has one; no landing page in this project renders
  one, and matching the siblings won.
- **Resources arrow graphic dropped.** The icon-link card already carries that
  affordance.
- **Resources runs light, not dark.** Two dark bands back to back (When to Apply
  and Resources) made the lower half of the page heavy, and the section carries
  no imagery to justify the weight. It uses the light two-up icon-card lockup
  from `academics/index.html` §7, which leaves `When to Apply` as the page's
  single dark band. The icon is `icon-link.svg` — byte-identical to
  `icon-link-dark.svg` (both md5 `7877acfc…`, same red glyph), just the name the
  light cards use.
- **Freshman / Transfer checklists link locally** (`../how-to-apply/…`);
  International and Shady Grove stay on admissions.umd.edu — those pages have not
  been built in this project.

## Spacing note

The Resources heading and its cards live in a **single** `<section>` inside a
single lock, with the gap supplied by `umd-layout-vertical-landing-child` on
`umd-element-section-intro` — the DS class documented in
`page-builder/LAYOUT-PATTERNS.md` § "Section-Intro to Content Spacing"
(`margin-bottom: 32px → 40px → 48px`). This was first built as two adjacent
dark sections, which stacked each section's own vertical padding and pushed the
heading ~200px above its cards. The intro and the content it introduces belong
in the same section; only the spacing class should set that gap.

## Chrome change this page caused

The header's red CTA and the drawer's "Apply Now" link previously pointed at
`https://admissions.umd.edu/apply-now`. Both now point at
`{{ROOT}}pages/apply-now/`, so the CTA lands on the prototype. That edit is in
`shared/header.html` and was propagated to all 13 pages by
`scripts/build-chrome.py`.

## Assets

| File | Origin | Treatment |
|---|---|---|
| `images/admissions/how-to-apply-hero.jpg` | already in repo | Byte-identical (md5 `415b41b1…`) to the source's apply-now hero — reused, not duplicated |
| `images/apply-now/students-talk.jpg` | source `rich-text/Students-talk.jpg` | 2953px → 2000px, q82 progressive (269 KB) |
| `images/apply-now/students-studying.jpg` | source `highlights/ESJLTC_Students_09262018_0245-5.jpg` | 4000px → 2400px, q82 progressive (462 KB) |
