from .. import api, spec, html


def test_render():
    data = dict(x=[1, 2, 3],
                y=[4, 5, 6])
    spec = api.Viz(data)
    s = spec.encode(x='x:Q', y='y:Q').mark_line()
    r = html.render(s)
    assert r is not None