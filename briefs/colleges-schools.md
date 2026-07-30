# Colleges & Schools

**Output:** `pages/colleges-schools.html`
**Source:** <https://admissions.umd.edu/programs/colleges-schools>
**Data:** `briefs/colleges-schools-data.json` (13 colleges, 203 programs)
**Images:** `images/colleges-schools/` (13 college photos @ 880×440, hero @ 2000×755)

## What changed from the source

The source page is 13 stacked full-width rows — each a large image, the college
description, and a button that expands a long single-column list of majors. With
203 programs across 13 colleges it scrolls a very long way, and the payloads are
wildly uneven (ARHU has 59 programs, Journalism has 1, Letters & Sciences has 0).

This version keeps the accordion behaviour but replaces the vertical list with a
**bordered card grid** (3 across at desktop). Activating a card opens a
**full-width panel below that card's row**, with the majors in 3–4 columns.

Design decisions confirmed with the user:

| Decision | Choice |
|---|---|
| Where majors open | Full-width panel below the row (not inline, not a modal) |
| Card face | Image + college name + abbreviation + description |
| Card styling | Roughly the DS card-standard type scale, plus the accordion toggle |
| Lock | `umd-layout-space-horizontal-larger` (1600px) |
| Panel lead copy | `umd-sans-small` (16px), capped at the DS 960px paragraph measure |
| Majors columns | 1 / 2 / 3 — capped at 3; see OVERRIDES.md for the 3-vs-4 measurements |
| Program-type labels | DS pill geometry + outline, non-clickable, no colour coding |
| College website link | Card headline and panel headline — no CTAs in the panels |
| Intro | Sibling landing pages' rich-text lockup, but **not** all-caps |
| Breadcrumb | None |
| Hero | Same recipe as `pages/programs.html`, CTA in hero, left-aligned |

## Page structure

1. **Chrome** — header stack + footer copied verbatim from `pages/programs.html`.
2. **Hero** — `umd-element-hero data-layout-height="small"`, sundial image,
   headline "Colleges & Schools", source body copy, primary CTA
   "Explore All Programs" → `programs.html`.
3. **Intro** — the sibling landing pages' rich-text lockup (narrow centred
   `-small` lock, rule, lead paragraph, `.umd-text-rich-advanced` body) carrying
   the two source intro paragraphs. No breadcrumb.
4. **College grid** — 13 tiles + 12 expandable panels. See `OVERRIDES.md`
   § `pages/colleges-schools.html` for the mechanics.
5. **Scroll-to-top + footer.**

## Copy fidelity

All visible text is lifted verbatim from the source page: 13 college names, 13
college descriptions, 203 program names and their department URLs, the hero body
copy, and both intro paragraphs. Verified programmatically against the downloaded
source rather than by eye.

## Regenerating

```
python3 scripts/build-colleges-schools.py
```

Rebuilds the page from `briefs/colleges-schools-data.json` plus the
`TEMPLATE.html` head and the `pages/programs.html` chrome. Edit the JSON (or the
generator's `PAGE_CSS` / `PAGE_JS` blocks) and re-run rather than hand-editing the
2,547-line output — it is overwritten wholesale.

## Notes / open items

- The two colleges with thin data are handled specially: **Letters & Sciences**
  (0 programs) gets a direct link to `ltsc.umd.edu` instead of a toggle;
  **Journalism** (1 program) gets a singularized "View 1 program" label. If the
  source ever fills these in, the generator picks it up automatically.
- Program URLs point at ~200 external department sites. They were captured from
  the source page and have not been link-checked.
- The source's own `schools.css` / `schools.js` were downloaded for reference but
  none of it is used — the interaction is rebuilt on DS tokens and typography.
