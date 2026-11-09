#!/usr/bin/env python3
"""Mind map viewer checks. Run: python3 MINDMAP/tests/test_viewer.py [name-filter]
Needs network: the viewer loads its libraries from CDNs."""
import sys, re, json, pathlib, tempfile, traceback
from playwright.sync_api import sync_playwright

URL = (pathlib.Path(__file__).resolve().parent.parent / 'template.html').as_uri()
VIEWPORTS = {
    'phone':    dict(viewport={'width': 390,  'height': 844},  has_touch=True),
    'tablet':   dict(viewport={'width': 820,  'height': 1180}, has_touch=True),
    'tablet-l': dict(viewport={'width': 1180, 'height': 820},  has_touch=True),
    'desktop':  dict(viewport={'width': 1440, 'height': 900}),
}
TOUCH = ('phone', 'tablet', 'tablet-l')
ALL = TOUCH + ('desktop',)
CHECKS = []


def check(*viewports):  # no args: logic check, run once at desktop size
    def deco(fn):
        CHECKS.append((fn, viewports or ('desktop',)))
        return fn
    return deco


def open_page(browser, vp, url=URL):
    page = browser.new_context(**VIEWPORTS[vp], accept_downloads=True).new_page()
    page.goto(url)
    page.wait_for_function('window.mindmapReady === true', timeout=20000)
    return page


# ---------- Task 1: parser ----------

def parse(page, text, name='map.md'):
    return page.evaluate("""([t, n]) => { const r = parseMap(t, n); if (!r) return null;
        return flatten(r).map(x => ({id: x.id, title: x.title, body: x.body.trim(), depth: x.depth,
            color: x.color, parentId: x.parentId})); }""", [text, name])


@check()
def check_parse_basic(page):
    ns = parse(page, "intro ignored\n# Root\nroot body\n## A\na body\n### A1\n## B\n")
    assert [n['title'] for n in ns] == ['Root', 'A', 'A1', 'B']
    assert [n['depth'] for n in ns] == [0, 1, 2, 1]
    assert ns[0]['body'] == 'root body' and ns[1]['body'] == 'a body'
    assert ns[2]['parentId'] == ns[1]['id'] and ns[3]['parentId'] == ns[0]['id']


@check()
def check_parse_skips_deep_and_fences(page):
    ns = parse(page, "# R\n## A\n#### Skipped\n######## Eight\n```python\n# not a heading\n```\n")
    assert [n['title'] for n in ns] == ['R', 'A', 'Skipped', 'Eight']
    assert ns[2]['parentId'] == ns[1]['id'] and ns[2]['depth'] == 2
    assert ns[3]['depth'] == 3 and '# not a heading' in ns[3]['body']


@check()
def check_parse_synthetic_root(page):
    ns = parse(page, "# One\n# Two\n", 'os-ch3.md')
    assert ns[0]['id'] == 'root' and ns[0]['title'] == 'os-ch3'
    assert [n['depth'] for n in ns] == [0, 1, 1]
    ns = parse(page, "## Starts deep\n## Second\n", 'x.md')
    assert ns[0]['title'] == 'x' and len(ns) == 3


@check()
def check_parse_colors_and_empty(page):
    text = "# R\n" + "".join(f"## B{i}\n### C{i}\n" for i in range(6))
    ns = parse(page, text)
    assert ns[0]['color'] == 'root'
    b = [n for n in ns if n['depth'] == 1]
    assert [n['color'] for n in b] == ['branch-1', 'branch-2', 'branch-3', 'branch-4', 'branch-5', 'branch-1']
    assert all(n['color'] == next(x for x in ns if x['id'] == n['parentId'])['color'] for n in ns if n['depth'] == 2)
    assert parse(page, "no headings here\n") is None


@check()
def check_parse_bom_crlf(page):  # Review Focus 2
    ns = parse(page, "﻿# Root\r\n## A\r\nbody\r\n")
    assert [n['title'] for n in ns] == ['Root', 'A'] and ns[1]['body'] == 'body'


@check()
def check_embedded_sample(page):
    m = page.evaluate("readEmbeddedMap()")
    assert m['exported'] is False
    ns = parse(page, m['text'], m['name'])
    assert ns and max(n['depth'] for n in ns) >= 4


def launch(bt):
    try:
        return bt.launch()
    except Exception:
        # ponytail: Playwright may not ship a Firefox build for this distro; fall back to any cached one
        builds = sorted(pathlib.Path.home().glob(f'.cache/ms-playwright/{bt.name}-*/{bt.name}/{bt.name}'))
        if not builds:
            raise
        return bt.launch(executable_path=str(builds[-1]))


# ---------- Task 2: markdown / math / code ----------

def md(page, s):
    return page.evaluate("s => renderMarkdown(s)", s)


@check()
def check_render_math(page):
    h = md(page, "Inline $a_b$ and display $$\\frac{1}{n}\\sum_i W_i$$ and \\(x^2\\) and \\[y\\]")
    assert h.count('class="katex"') >= 4 and 'katex-display' in h and '<em>' not in h


@check()
def check_render_dollars_literal(page):  # Review Focus 1
    h = md(page, "costs $5 and $10, code `$x$`")
    assert 'katex' not in h and '$5 and $10' in h and '<code>$x$</code>' in h


@check()
def check_render_code(page):
    h = md(page, "```scheme\n(define (sq x) (* x x))\n```")
    assert 'code-card' in h and '>scheme<' in h and 'hljs-' in h
    for lang, src in [('c', 'int main(void) { return 0; }'), ('python', 'def f(x):\n    return x'),
                      ('haskell', 'sq :: Int -> Int\nsq x = x * x'), ('java', 'class A { int x; }')]:
        assert 'hljs-' in md(page, f"```{lang}\n{src}\n```"), lang


@check()
def check_render_lists_and_html(page):
    h = md(page, "- a\n- b\n\n1. one\n2. two\n\n<script>alert(1)</script> <b>x</b>")
    assert '<ul>' in h and '<ol>' in h
    assert '<script' not in h and '&lt;script&gt;' in h and '&lt;b&gt;' in h
    assert page.evaluate("plainTitle('**Big** $O(n)$ `x`')") == 'Big O(n) x'


# ---------- Task 3: zig-zag layout ----------

LAYOUT_JS = """([spec]) => {
  // spec: list of [id, parentId, w, h]; returns boxes + connector drop segments + widths
  const nodes = new Map(spec.map(([id, p, w, h]) => [id, {id, parentId: p, children: [], w, h}]));
  for (const n of nodes.values()) if (n.parentId) nodes.get(n.parentId).children.push(n);
  const root = [...nodes.values()].find(n => !n.parentId);
  const L = layoutTree(root, n => n.children, n => ({w: n.w, h: n.h}));
  const box = n => { const p = L.pos.get(n.id); return {id: n.id, l: p.x - n.w/2, r: p.x + n.w/2, t: p.y, b: p.y + n.h, x: p.x, row: p.row}; };
  const old = n => n.children.length ? Math.max(n.w, n.children.reduce((s, c) => s + old(c), 0) + 96 * (n.children.length - 1)) : n.w;
  // vertical segments the connectors use: low-row child's drop through its high band, high-row parent's drop through its low band
  const segs = [];
  for (const n of nodes.values()) {
    const p = L.pos.get(n.id), d = depthOf(n);
    if (n.parentId && p.row === 1) segs.push({owner: n.id, x: p.x, t: L.levels[d].top, b: p.y});
    if (n.children.length && p.row === 0) segs.push({owner: n.id, x: p.x, t: p.y + n.h, b: L.levels[d].bottom});
  }
  function depthOf(n) { let d = 0; while (n.parentId) { n = nodes.get(n.parentId); d++; } return d; }
  return {boxes: [...nodes.values()].map(box), segs, width: L.width, oldWidth: old(root)};
}"""


def stress_spec():
    spec = [['r', None, 320, 110]]
    for a in range(5):
        spec.append([f'a{a}', 'r', 300, 120])
        for b in range(4):
            spec.append([f'a{a}b{b}', f'a{a}', 300, 90 + 40 * (b % 2)])
            for c in range(3):
                spec.append([f'a{a}b{b}c{c}', f'a{a}b{b}', 300 if c else 420, 100 if c else 220])
    return spec  # 1 + 5 + 20 + 60 = 86 nodes, 4 levels, mixed sizes incl. code-sized cards


def assert_layout_ok(res):
    bx = res['boxes']
    for i, a in enumerate(bx):
        for b in bx[i + 1:]:
            assert a['r'] <= b['l'] or b['r'] <= a['l'] or a['b'] <= b['t'] or b['b'] <= a['t'], (a['id'], b['id'])
    for s in res['segs']:
        for b in bx:
            if b['id'] != s['owner'] and b['l'] < s['x'] < b['r'] and b['t'] < s['b'] and s['t'] < b['b']:
                raise AssertionError(f"line of {s['owner']} crosses {b['id']}")


@check()
def check_layout_small(page):
    res = page.evaluate(LAYOUT_JS, [[['r', None, 300, 100], ['a', 'r', 300, 90], ['b', 'r', 300, 90], ['c', 'r', 300, 90]]])
    assert_layout_ok(res)
    rows = [b['row'] for b in res['boxes']]
    assert rows == [0, 0, 1, 0]
    a, b, c = res['boxes'][1:]
    assert a['r'] > b['l'] and b['r'] > c['l']  # neighbours tuck in (overlap horizontally)


@check()
def check_layout_stress(page):
    res = page.evaluate(LAYOUT_JS, [stress_spec()])
    assert_layout_ok(res)
    assert res['width'] <= 0.7 * res['oldWidth'], (res['width'], res['oldWidth'])


def main():
    flt = sys.argv[1] if len(sys.argv) > 1 else ''
    failed = 0
    with sync_playwright() as p:
        for bt in (p.chromium, p.firefox):
            browser = launch(bt)
            for fn, vps in CHECKS:
                if flt not in fn.__name__:
                    continue
                for vp in vps:
                    page = None
                    try:
                        page = open_page(browser, vp)
                        fn(page)
                        print(f'PASS {bt.name:8} {vp:8} {fn.__name__}')
                    except Exception:
                        failed += 1
                        print(f'FAIL {bt.name:8} {vp:8} {fn.__name__}')
                        traceback.print_exc()
                    finally:
                        if page:
                            page.context.close()
            browser.close()
    print('ALL PASS' if not failed else f'{failed} FAILED')
    sys.exit(1 if failed else 0)


if __name__ == '__main__':
    main()
