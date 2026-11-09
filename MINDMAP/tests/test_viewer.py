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


# ---------- Task 4: page, rendering, themes, toolbar ----------

@check(*ALL)
def check_sample_renders(page):
    assert page.locator('#mindMap .katex').count() > 0
    assert page.locator('#mindMap .katex-display').count() > 0
    for lang in ('c', 'python', 'scheme', 'haskell'):
        assert page.locator(f'#mindMap code.language-{lang} [class^="hljs-"]').count() > 0, lang
    assert page.locator('#mindMap .note ul').count() > 0 and page.locator('#mindMap .note ol').count() > 0
    assert page.locator('[contenteditable]').count() == 0


@check(*ALL)
def check_dom_no_overlap_no_hscroll(page):
    rects = page.evaluate("[...document.querySelectorAll('#mindMap .node')].map(e => {const r = e.getBoundingClientRect(); return [r.left, r.right, r.top, r.bottom]})")
    assert len(rects) > 5
    for i, a in enumerate(rects):
        for b in rects[i+1:]:
            assert a[1] <= b[0] + 0.5 or b[1] <= a[0] + 0.5 or a[3] <= b[2] + 0.5 or b[3] <= a[2] + 0.5
    assert page.evaluate("document.documentElement.scrollWidth <= innerWidth")


@check(*TOUCH)
def check_toolbar_touch_targets(page):
    w = page.viewport_size['width']
    for el in page.locator('#toolbar button, #toolbar input').all():
        b = el.bounding_box()
        assert b and b['height'] >= 44 and b['width'] >= 44 and b['x'] >= 0 and b['x'] + b['width'] <= w
    t = page.locator('#mindMap .toggle').first.bounding_box()  # at the initial scale of 1
    assert t['width'] >= 32 and t['height'] >= 32


@check(*ALL)
def check_initial_view(page):
    assert page.evaluate("view.scale") == 1
    root = page.locator('#mindMap .node').first.bounding_box()
    wr = page.locator('#mapWrapper').bounding_box()
    assert wr['y'] <= root['y'] <= wr['y'] + wr['height'] / 3
    assert abs((root['x'] + root['width'] / 2) - (wr['x'] + wr['width'] / 2)) < 2


@check()
def check_theme(page):
    page.emulate_media(color_scheme='light'); page.reload(); page.wait_for_function('window.mindmapReady')
    assert page.evaluate("document.documentElement.dataset.theme") == 'dark'
    page.click('#themeBtn')
    assert page.evaluate("document.documentElement.dataset.theme") == 'light'
    page.reload(); page.wait_for_function('window.mindmapReady')
    assert page.evaluate("document.documentElement.dataset.theme") == 'light'


@check()
def check_depth_expand_collapse(page):
    total = page.locator('#mindMap .node').count()
    page.fill('#depthInput', '0'); assert page.locator('#mindMap .node').count() == 1
    page.fill('#depthInput', ''); assert page.locator('#mindMap .node').count() == total
    page.click('#collapseBtn')
    assert page.locator('#mindMap .node').count() == 1 + page.evaluate("mapRoot.children.length")
    page.click('#expandBtn'); assert page.locator('#mindMap .node').count() == total


@check()
def check_works_without_libs(page):
    ctx = page.context.browser.new_context(**VIEWPORTS['desktop'])
    ctx.route(re.compile(r'cdn\.jsdelivr\.net|cdnjs\.cloudflare\.com'), lambda r: r.abort())
    p2 = ctx.new_page(); p2.goto(URL); p2.wait_for_function('window.mindmapReady === true')
    assert p2.locator('#mindMap .node').count() > 5 and '$' in p2.inner_text('#mindMap')
    ctx.close()


@check('phone')
def check_long_content_fits(page):  # Review Focus 3
    page.evaluate("""setMap(parseMap('# R\\n## Long\\nhttps://example.com/' + 'a'.repeat(120) + ' ' + 'x'.repeat(80) +
        '\\n\\n$$\\\\begin{bmatrix}1&2&3&4&5&6&7&8&9&10&11&12&13&14&15\\\\end{bmatrix}$$\\n', 'l.md'))""")
    for el in page.locator('#mindMap .node').all():
        assert el.evaluate("e => e.scrollWidth <= e.clientWidth + 1")


# ---------- Task 5: gestures, selection, path bar ----------

PTR = """([type, sel, x, y, id, idx = 0]) => { const el = document.querySelectorAll(sel)[idx];
  el.dispatchEvent(new PointerEvent(type, {pointerId: id, pointerType: 'touch', isPrimary: id === 1,
    clientX: x, clientY: y, button: 0, buttons: type === 'pointerup' ? 0 : 1, bubbles: true, cancelable: true})); }"""


def center(page, sel, idx=0):
    b = page.locator(sel).nth(idx).bounding_box(); return b['x'] + b['width'] / 2, b['y'] + b['height'] / 2


def tap(page, sel, idx=0):  # dispatches on the element itself, so it works even when it is off-screen
    x, y = center(page, sel, idx)
    page.evaluate(PTR, ['pointerdown', sel, x, y, 1, idx]); page.evaluate(PTR, ['pointerup', sel, x, y, 1, idx])


@check(*TOUCH)
def check_drag_on_node_pans(page):
    x, y = center(page, '#mindMap .node .title')
    before = page.evaluate("({...view})")
    page.evaluate(PTR, ['pointerdown', '#mindMap .node .title', x, y, 1])
    page.evaluate(PTR, ['pointermove', '#mapWrapper', x - 60, y + 40, 1])
    page.evaluate(PTR, ['pointerup', '#mapWrapper', x - 60, y + 40, 1])
    after = page.evaluate("({...view})")
    assert round(after['x'] - before['x']) == -60 and round(after['y'] - before['y']) == 40
    assert page.evaluate("selectedId") in (None, page.evaluate("mapRoot.id"))  # a drag is not a tap-select


@check('desktop')
def check_mouse_drag_pans(page):
    x, y = center(page, '#mindMap .node .title')
    vx = page.evaluate("view.x")
    page.mouse.move(x, y); page.mouse.down(); page.mouse.move(x + 50, y, steps=5); page.mouse.up()
    assert round(page.evaluate("view.x") - vx) == 50


@check(*TOUCH)
def check_pinch_zoom_and_release_over_toggle(page):  # Review Focus 4
    n = page.locator('#mindMap .node').count()
    tx, ty = center(page, '#mindMap .toggle')
    s0 = page.evaluate("view.scale")
    page.evaluate(PTR, ['pointerdown', '#mindMap .toggle', tx, ty, 1])       # finger 1 rests on a toggle
    page.evaluate(PTR, ['pointerdown', '#mapWrapper', tx + 60, ty + 60, 2])
    page.evaluate(PTR, ['pointermove', '#mapWrapper', tx + 160, ty + 160, 2])
    assert page.evaluate("view.scale") > s0
    page.evaluate(PTR, ['pointerup', '#mapWrapper', tx + 160, ty + 160, 2])
    page.evaluate(PTR, ['pointerup', '#mindMap .toggle', tx, ty, 1])         # finger 1 never moved
    assert page.locator('#mindMap .node').count() == n


@check(*ALL)
def check_tap_toggle_select_and_crumbs(page):
    n = page.locator('#mindMap .node').count()
    tap(page, '#mindMap .toggle', 1); assert page.locator('#mindMap .node').count() < n
    tap(page, '#mindMap .toggle', 1); assert page.locator('#mindMap .node').count() == n
    deepest = page.evaluate("[...nodesById.values()].reduce((a, b) => b.depth > a.depth ? b : a).id")
    tap(page, f'#node-{deepest} .title')
    crumbs = page.locator('#pathBar .crumb')
    assert crumbs.count() == page.evaluate(f"nodesById.get('{deepest}').depth") + 1
    assert page.locator(f'#node-{deepest}.selected').count() == 1
    page.locator('#pathBar .crumb').nth(1).click()
    sid = page.evaluate("selectedId"); assert sid == crumbs.nth(1).get_attribute('data-id')
    page.wait_for_timeout(400)
    b, wr = page.locator(f'#node-{sid}').bounding_box(), page.locator('#mapWrapper').bounding_box()
    assert wr['x'] <= b['x'] + b['width'] / 2 <= wr['x'] + wr['width'] and wr['y'] <= b['y'] <= wr['y'] + wr['height']
    assert page.evaluate("document.documentElement.scrollWidth <= innerWidth")


@check()
def check_selection_falls_back_when_hidden(page):
    deepest = page.evaluate("[...nodesById.values()].reduce((a, b) => b.depth > a.depth ? b : a).id")
    tap(page, f'#node-{deepest} .title')
    page.fill('#depthInput', '1')
    sid = page.evaluate("selectedId")
    assert page.evaluate(f"nodesById.get('{sid}').depth") == 1 and page.locator(f'#node-{sid}.selected').count() == 1


@check()
def check_link_tap_opens_tab(page):  # Review Focus 5
    page.evaluate("setMap(parseMap('# R\\n## L\\nsee [docs](https://example.com/)\\n', 'l.md'))")
    x, y = center(page, '#mindMap .note a')
    with page.context.expect_page() as popup:  # real mouse click: synthetic events would trip popup blocking
        page.mouse.click(x, y)
    assert popup.value.url.startswith('https://example.com')


# ---------- Task 6: open, remember, save ----------

MAP_A = "# Alpha Map\n## One\n$x^2$\n```c\nint a;\n```\n"
MAP_B = "# Beta Map\n## Two\n"


def write_tmp(name, text):
    p = pathlib.Path(tempfile.mkdtemp()) / name; p.write_text(text); return str(p)


def root_title(page): return page.locator('#mindMap .node .title').first.inner_text()


@check(*ALL)
def check_open_and_remember(page):
    page.set_input_files('#fileInput', write_tmp('alpha.md', MAP_A))
    page.wait_for_function("document.querySelector('#mindMap .node .title').textContent.includes('Alpha')")
    page.reload(); page.wait_for_function('window.mindmapReady')
    assert root_title(page) == 'Alpha Map'


@check()
def check_open_bad_file(page):
    page.set_input_files('#fileInput', write_tmp('alpha.md', MAP_A))
    page.wait_for_function("document.querySelector('#mindMap .node .title').textContent.includes('Alpha')")
    page.set_input_files('#fileInput', write_tmp('bad.md', "no headings at all\n"))
    page.wait_for_selector('#toast', state='visible')
    assert 'No headings' in page.inner_text('#toast') and root_title(page) == 'Alpha Map'


@check('phone', 'desktop')
def check_save_single_file(page):
    page.set_input_files('#fileInput', write_tmp('alpha.md', MAP_A + "\n</script> stays text\n"))
    page.wait_for_function("document.querySelector('#mindMap .node .title').textContent.includes('Alpha')")
    with page.expect_download() as dl:
        page.click('#saveBtn')
    assert dl.value.suggested_filename == 'alpha.html'
    out = write_tmp('alpha.html', ''); dl.value.save_as(out)
    fresh = page.context.browser.new_context(**VIEWPORTS['desktop'])  # empty storage
    p2 = fresh.new_page(); p2.goto(pathlib.Path(out).as_uri()); p2.wait_for_function('window.mindmapReady')
    assert root_title(p2) == 'Alpha Map' and p2.locator('#mindMap .katex').count() > 0
    assert p2.locator('#mindMap code [class^="hljs-"]').count() > 0
    p2.set_input_files('#fileInput', write_tmp('beta.md', MAP_B))
    p2.wait_for_function("document.querySelector('#mindMap .node .title').textContent.includes('Beta')")
    fresh.close()


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
