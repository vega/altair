"""Tests of various renderers"""

import altair as alt


def test_colab_renderer_embed_options():
    """Test that embed_options in renderer metadata are correctly manifest in html"""
    chart = alt.Chart('data.csv').mark_point()

    with alt.renderers.enable_context('colab', embed_options=dict(actions=False)):
        bundle = chart._repr_mimebundle_(None, None)
        html = bundle['text/html']
        assert ('embed_opt = {"actions": false, "mode": "vega-lite"}' in html or
                'embed_opt = {"mode": "vega-lite", "actions": false}' in html)

    with alt.renderers.enable_context('colab', embed_options=dict(actions=True)):
        bundle = chart._repr_mimebundle_(None, None)
        html = bundle['text/html']
        assert ('embed_opt = {"actions": true, "mode": "vega-lite"}' in html or
                'embed_opt = {"mode": "vega-lite", "actions": true}' in html)
