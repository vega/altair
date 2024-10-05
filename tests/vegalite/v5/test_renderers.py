"""Tests of various renderers."""

import json
from importlib.metadata import version as importlib_version

import pytest
from packaging.version import Version

import altair.vegalite.v5 as alt
from tests import skip_requires_vl_convert

try:
    import anywidget

except ImportError:
    anywidget = None  # type: ignore


skip_requires_anywidget = pytest.mark.skipif(
    not anywidget, reason="anywidget not importable"
)
if Version(importlib_version("ipywidgets")) < Version("8.1.4"):
    # See https://github.com/vega/altair/issues/3234#issuecomment-2268515312
    jupyter_marks = skip_requires_anywidget(
        pytest.mark.filterwarnings(
            "ignore:Deprecated in traitlets 4.1.*:DeprecationWarning"
        )
    )
else:
    jupyter_marks = skip_requires_anywidget


@pytest.fixture
def chart():
    return alt.Chart("data.csv").mark_point()


def test_html_renderer_embed_options(chart, renderer="html"):
    """Test that embed_options in renderer metadata are correctly manifest in html."""
    # Short of parsing the javascript, it's difficult to parse out the
    # actions. So we use string matching

    def assert_has_options(chart, **opts):
        html = chart._repr_mimebundle_(None, None)["text/html"]
        for key, val in opts.items():
            assert json.dumps({key: val})[1:-1] in html

    with alt.renderers.enable(renderer):
        assert_has_options(chart, mode="vega-lite")

        with alt.renderers.enable(embed_options={"actions": {"export": True}}):
            assert_has_options(chart, mode="vega-lite", actions={"export": True})

        with alt.renderers.set_embed_options(actions=True):
            assert_has_options(chart, mode="vega-lite", actions=True)


def test_mimetype_renderer_embed_options(chart, renderer="mimetype"):
    # check that metadata is passed appropriately
    mimetype = alt.display.VEGALITE_MIME_TYPE
    spec = chart.to_dict()
    with alt.renderers.enable(renderer):
        # Sanity check: no metadata specified
        bundle, metadata = chart._repr_mimebundle_(None, None)
        assert bundle[mimetype] == spec
        assert metadata == {}
        with alt.renderers.set_embed_options(actions=False):
            bundle, metadata = chart._repr_mimebundle_(None, None)
            assert set(bundle.keys()) == {mimetype, "text/plain"}
            assert bundle[mimetype] == spec
            assert metadata == {mimetype: {"embed_options": {"actions": False}}}


def test_json_renderer_embed_options(chart, renderer="json"):
    """Test that embed_options in renderer metadata are correctly manifest in html."""
    mimetype = "application/json"
    spec = chart.to_dict()
    with alt.renderers.enable(renderer):
        # Sanity check: no options specified
        bundle, metadata = chart._repr_mimebundle_(None, None)
        assert bundle[mimetype] == spec
        assert metadata == {}

        with alt.renderers.enable(option="foo"):
            bundle, metadata = chart._repr_mimebundle_(None, None)
            assert set(bundle.keys()) == {mimetype, "text/plain"}
            assert bundle[mimetype] == spec
            assert metadata == {mimetype: {"option": "foo"}}


@skip_requires_vl_convert
def test_renderer_with_none_embed_options(chart, renderer="mimetype"):
    # Check that setting embed_options to None doesn't crash
    from altair.utils.mimebundle import spec_to_mimebundle

    spec = chart.to_dict()
    with alt.renderers.enable(renderer, embed_options=None):
        bundle = spec_to_mimebundle(
            spec=spec,
            mode="vega-lite",
            format="svg",
            embed_options=None,
        )
        assert bundle["image/svg+xml"].startswith("<svg")


@jupyter_marks
def test_jupyter_renderer_mimetype(chart, renderer="jupyter") -> None:
    """Test that we get the expected widget mimetype when the jupyter renderer is enabled."""
    with alt.renderers.enable(renderer):
        assert (
            "application/vnd.jupyter.widget-view+json"
            in chart._repr_mimebundle_(None, None)[0]
        )
