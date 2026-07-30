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


def _read(name):
    with open(os.path.join(SHARED, name), encoding='utf-8') as fh:
        return fh.read().rstrip('\n')


def source_file(key):
    return _REGIONS[key][0]


def payload(key):
    """The region's content, without markers."""
    src, wrap = _REGIONS[key]
    return wrap(_read(src))


def block(key):
    """The region's content wrapped in its SHARED:<key> markers."""
    return '\n'.join([_START % (key, source_file(key)), payload(key), _END % key])


def keys():
    return list(_REGIONS)
