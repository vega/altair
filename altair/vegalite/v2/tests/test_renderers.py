"""Tests of various renderers"""

import pytest

import altair as alt


@pytest.fixture
def chart():
    return alt.Chart('data.csv').mark_point()


def test_colab_renderer_embed_options(chart):
    """Test that embed_options in renderer metadata are correctly manifest in html"""
    with alt.renderers.enable('colab', embed_options=dict(actions=False)):
        bundle = chart._repr_mimebundle_(None, None)
        html = bundle['text/html']
        assert ('embed_opt = {"actions": false, "mode": "vega-lite"}' in html or
                'embed_opt = {"mode": "vega-lite", "actions": false}' in html)

    with alt.renderers.enable('colab', embed_options=dict(actions=True)):
        bundle = chart._repr_mimebundle_(None, None)
        html = bundle['text/html']
        assert ('embed_opt = {"actions": true, "mode": "vega-lite"}' in html or
                'embed_opt = {"mode": "vega-lite", "actions": true}' in html)


# TODO: test notebook renderer here when it supports metadata
@pytest.mark.parametrize('renderer', ['default'])
def test_default_renderer_embed_options(chart, renderer):
    # check that metadata is passed appropriately
    with alt.renderers.enable(renderer, embed_options=dict(actions=False)):
        bundle, metadata = chart._repr_mimebundle_(None, None)
        assert metadata == {'embed_options': {'actions': False}}

    # Sanity check: no metadata specified
    with alt.renderers.enable(renderer):
        bundle, metadata = chart._repr_mimebundle_(None, None)
        assert metadata == {}
