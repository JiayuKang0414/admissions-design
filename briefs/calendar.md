# Calendar — brief

**Output:** `pages/calendar/index.html` (generated — run `python3 scripts/build-calendar.py`)
**Data:** `briefs/calendar-data.json`

## What this page is

The admissions events calendar, recreated in the design system. Replaces
<https://admissions.umd.edu/calendar?date=2026-08-20&layout=list>.

Two layouts, toggled: an event **list** and a full **month grid**, matching the
live site's `?layout=list` / `?layout=grid`.

| Piece | Comes from |
|---|---|
| Event rows (list view) | `umd-element-event data-display="list"` (DS event card, list variant) |
| Filter band across the top | the page-builder **Filter Band** pattern (`LAYOUT-PATTERNS.md`) |
| Control bar | the live calendar's `.main-controls` — month cursor, prev/next/Today, List/Calendar toggle |
| Mini calendar in the list rail | the right-rail month grid on <https://calendar.umd.edu> |
| Month grid | original; the live grid's cells hold only a date number |
| Month pager | the `umd-shell-pagination` pattern from <https://today.umd.edu/tags/athletics> |

There is no search field — the live calendar has none, and four selects over 64
events do not need one.

## Content

64 real events harvested 2026-08-20 from the live admissions calendar — the
month list pages (`?date=…&layout=list`) for Aug 2026 through Aug 2027, plus
every event's own detail page for the fields the list view omits (event type,
audience, full description, register link, feature image). Four entries the
live site publishes with an empty detail page were dropped.

Event images are the three the source uses, downloaded to `images/calendar/`
rather than hotlinked from the Craft CDN (its URLs carry a signature tied to
the exact `w`/`h` params, so they can't be resized or reliably deep-linked).

Facet vocabularies match the live filter menu:

| Group | Values |
|---|---|
| Audience | Prospective Students · Admitted/Enrolled Students |
| Location | On Campus · Virtual |
| Event Type | Academic Programs · Important Deadlines · Tours & Information Sessions |
| College or School | the eight colleges that actually tag events |

The live site nests colleges *inside* its Event Type select, so that one
control mixes two dimensions. Here they are their own select — four controls
fit the band's `umd-layout-grid-gap-four` row exactly.

## Behavior

- **Page order is** filter band → active pills → control bar → count → results.
  The band answers "which events"; the control bar answers "when, and shown
  how", so it sits directly above the results it labels.
- **One date cursor, one month per page.** `state.from` defaults to today
  (2026-08-20) and **both views window to its month**. Month nav moves the
  cursor to the 1st of the next/previous month, "Today" returns it to today.
  There is no results-count line — the month is the count's job now.
- **No group heading in the list.** One month per page, and the control bar
  above already names it. The cards sit directly in `#cal-list` with no
  wrapper — that adjacency is what gives them their upstream divider.
- **The pager** under the list is the `umd-shell-pagination` pattern with
  numbered pages: first · … · prev · **current** · next · … · last, clamped to
  the months the data covers. **Page N is the Nth month**, so a page step is a
  month step; the month rides in each button's `aria-label`. Its CSS is **not**
  in the styles package (see OVERRIDES.md) and is restated from the live page.
- **Facets are shared by both views.** They filter the event set; each view then
  applies its own date window, so switching views never changes what matched.
- **One value per facet** (single `<select>`, as on the live site). The
  removable "Filtered by:" pills and the live count sit under the band.
- **The mini calendar rides the same cursor.** It shows the control bar's month,
  underlines days that have matching events, and a day click moves the cursor
  and scrolls to that day's ribbon. It has no month arrows of its own — the
  control bar owns the month. Only a *picked* day gets the red ring; moving
  months clears it, since month nav snaps the cursor to the 1st.
- **The rail is list-view only, on the right** — where calendar.umd.edu puts
  the same month grid. Grid view hides it and renders full bleed; a month
  picker beside a month grid is a duplicate control that also steals the width
  the grid needs. Below 1020px the rail stacks above the list.
- **The month label** is `umd-campaign-small` (Barlow Condensed italic, matching
  the hero) forced to caps in page CSS — the campaign faces have no
  `-uppercase` sibling. Red arrows flank it; `min-width:11ch` stops them
  jittering as the month name changes length.
- **A static "Upcoming Events" block** closes the page under a tailwing heading
  (`umd-text-line-trailing-light`): the next six events from today as bordered,
  image-less event cards, three up. Rendered at build time, independent of the
  filters and the month cursor. `umd-element-event` has no bordered variant —
  the border is a shadow injection (see OVERRIDES.md).
- **Grid cells list their events** — up to three linked titles with times, then
  a "+N more" toggle. Below 768px the Calendar toggle is hidden and the page is
  list-only; a seven-column grid with content in the cells can't be done at
  375px, and the live site's own grid measures 0×0 there.
- List results group by month under the DS **eyebrow ribbon**
  (`umd-text-decoration-eyebrow umd-eyebrow-ribbon` from `element.min.css`) —
  the same gold ribbon `umd-feed-events-grouped` uses for its date headers on
  calendar.umd.edu. Kept as an `<h2>` so the months stay real headings.

## Notes

- `umd-element-event` reads its date from the `<time>` element's **text
  content**, not the `datetime` attribute (`parseDateFromElement`). The slot is
  `start-date-iso`, not `date-start-iso` — the component's own JSDoc is wrong
  here; `Slots.name.DATE_START_ISO` resolves to `start-date-iso`.
- `data-visual-time` is opt-**out**, not opt-in — `Attributes.isVisual.showTime`
  defaults to `true`, so an all-day deadline with the attribute absent renders
  "12:00am". Every card emits it explicitly: `"true"` when timed, `"false"`
  when all-day.
- `end-date-iso` repeats the start stamp. Without it the DS event meta prints
  "Thu. Aug 20 - undefined. undefined undefined". See OVERRIDES.md.
- Consecutive `umd-element-event[data-display="list"]` siblings get their
  24px + top-rule divider from upstream `web-components.min.css`. Don't add it.
- The hero is `umd-element-hero-minimal data-theme="dark"` with **only** a
  headline — matching the live page, which carries a breadcrumb and an `h1` and
  nothing else. An earlier revision used a standard background hero with a
  supporting paragraph and a "Plan Your Visit" CTA; that copy was invented here,
  not taken from the source, and is gone.
