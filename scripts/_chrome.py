"""Shared site chrome — single source for every build script in this repo.

The chrome lives in shared/ as four files:

    shared/header.html          header stack (nav-utility + utility-header +
                                navigation-header with the project nav items)
    shared/footer.html          visual footer
    shared/chrome.css           CSS companions the chrome markup depends on
    shared/chrome-scripts.html  chrome-driven shadow injections

`block(key)` wraps one of them in SHARED:<key>:START / :END markers.
scripts/build-chrome.py splices those blocks into hand-authored pages;
scripts/build-programs.py and scripts/build-colleges-schools.py emit the same
blocks when generating their pages. Because both paths render byte-identical
output, running any of the three converges — no ordering dependency.

Markup, CSS, and scripts are deliberately in ONE module. Splitting them is what
caused the original bug: a page took the chrome markup from a sibling and its
<head> from TEMPLATE.html, silently dropping the CSS companions.

Depth
    Pages live at more than one depth under pages/ (pages/admissions.html but
    also pages/academics/programs.html), so the chrome cannot hard-code `../`.
    Every path in shared/header.html and shared/footer.html is written
    repo-root-relative behind a `{{ROOT}}` token, and `payload`/`block` expand
    it to the right number of `../` for the page being written. Pass `depth` as
    the number of directories between the repo root and the page's own
    directory: 1 for pages/admissions.html, 2 for pages/academics/index.html.
    `depth_of(path)` computes it from a page path.
"""
import os

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SHARED = os.path.join(REPO, 'shared')

_START = '  <!-- SHARED:%s:START — generated from shared/%s; do not edit here -->'
_END = '  <!-- SHARED:%s:END -->'

# key -> (source file, wrapper applied to the file's contents)
_REGIONS = {
    'header':         ('header.html',         lambda s: s),
    'footer':         ('footer.html',          lambda s: s),
    'chrome-css':     ('chrome.css',           lambda s: '  <style>\n' + s + '\n  </style>'),
    'chrome-scripts': ('chrome-scripts.html',  lambda s: s),
}


ROOT_TOKEN = '{{ROOT}}'


def depth_of(path):
    """How many `../` a page at `path` needs to reach the repo root."""
    rel = os.path.relpath(os.path.abspath(path), REPO)
    return len(rel.replace(os.sep, '/').split('/')) - 1


def _resolve(text, depth):
    return text.replace(ROOT_TOKEN, '../' * depth)


def _read(name):
    with open(os.path.join(SHARED, name), encoding='utf-8') as fh:
        return fh.read().rstrip('\n')


def source_file(key):
    return _REGIONS[key][0]


def payload(key, depth=1):
    """The region's content, without markers, with {{ROOT}} resolved for `depth`."""
    src, wrap = _REGIONS[key]
    return _resolve(wrap(_read(src)), depth)


def block(key, depth=1):
    """The region's content wrapped in its SHARED:<key> markers."""
    return '\n'.join([_START % (key, source_file(key)), payload(key, depth), _END % key])


def keys():
    return list(_REGIONS)
