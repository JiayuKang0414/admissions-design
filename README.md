# Admissions Design

Design work for the UMD Admissions site — multiple pages sharing a common header, footer, and design-system chrome.

## Layout

```
admissions-design/
├── pages/              Page HTML, one directory per site section
├── shared/             Header, footer, head, and end-scripts partials
├── images/
│   ├── logos/          Admissions and UMD logos
│   ├── academics/      Academics page assets (formerly projects/admissions-academics)
│   └── admissions/     Admissions homepage assets (formerly projects/admissions-recreation)
├── briefs/             Page briefs / source notes
├── scripts/            Build scripts (HTML partial inlining, etc.)
├── page-builder/       Submodule → design-system-page-builder
│                       Source for critical.css, registry, RULES.md,
│                       slash commands (.claude/commands/), and shared
│                       /images/large /images/small assets.
└── OVERRIDES.md        Admissions-specific shadow-DOM injections and CSS overrides
```

## Image paths

- **Admissions-specific**: `../images/logos/`, `../images/academics/`, `../images/admissions/`
- **Shared library** (campus, people, events, etc.): `../page-builder/images/large/...`, `../page-builder/images/small/...`

## Working with this repo

The page-builder submodule provides slash commands (`.claude/commands/*.md`) and the canonical `critical.css`. Run Claude Code from the root of this repo; it will read `CLAUDE.md` here and follow the project rules.

To update the page-builder pin:

```bash
cd page-builder && git pull origin main && cd ..
git add page-builder && git commit -m "Bump page-builder submodule"
```

## Pages

- `pages/admissions.html` — Undergraduate Admissions homepage (recreation of admissions.umd.edu)
- `pages/academics/` — Academics landing, All Programs, Colleges & Schools, and the by-interest pages
- `pages/student-life/` — Student Life landing
- `pages/how-to-apply/` — How To Apply landing and Freshman Applicants
- `pages/tuition/` — Tuition & Aid landing

Each section's landing page is its `index.html`, so `/pages/academics/` serves it.
The header, footer, and chrome CSS come from `shared/` and are inlined into every
page by `scripts/build-chrome.py`.
