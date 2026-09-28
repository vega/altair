"""Tests of various renderers."""

import json
import logging
from importlib.metadata import version as importlib_version
from types import SimpleNamespace
from unittest.mock import Mock

import pytest
from packaging.version import Version

import altair.vegalite.v6 as alt
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


def test_html_renderer_embed_options(chart):
    """Test that embed_options in renderer metadata are correctly manifest in html."""
    # Short of parsing the javascript, it's difficult to parse out the
    # actions. So we use string matching

    def assert_has_options(chart, **opts):
        html = chart._repr_mimebundle_(None, None)["text/html"]
        for key, val in opts.items():
            assert json.dumps({key: val})[1:-1] in html

    with alt.renderers.enable("html"):
        assert_has_options(chart, mode="vega-lite")

        with alt.renderers.enable(embed_options={"actions": {"export": True}}):
            assert_has_options(chart, mode="vega-lite", actions={"export": True})

        with alt.renderers.set_embed_options(actions=True):
            assert_has_options(chart, mode="vega-lite", actions=True)


@pytest.mark.parametrize(
    ("vl_convert_version", "expected_kwargs"),
    [
        ("1.9.0", {"vl_version": "v6_4", "show_warnings": True}),
        ("2.0.0-rc7", {"vl_version": "v6_4"}),
    ],
)
def test_html_renderer_compiles_for_warnings(
    chart, monkeypatch, vl_convert_version, expected_kwargs
):
    from altair.vegalite.v6 import display

    compile_ = Mock(return_value={})
    vlc = SimpleNamespace(__version__=vl_convert_version, vegalite_to_vega=compile_)
    monkeypatch.setattr(display, "import_vl_convert", lambda: vlc)

    with alt.renderers.enable("html"):
        chart._repr_mimebundle_(None, None)

    compile_.assert_called_once_with(chart.to_dict(), **expected_kwargs)


def test_html_renderer_can_disable_warning_compilation(chart, monkeypatch):
    from altair.vegalite.v6 import display

    import_vl_convert = Mock()
    monkeypatch.setattr(display, "import_vl_convert", import_vl_convert)

    with alt.renderers.enable("html", show_warnings=False):
        chart._repr_mimebundle_(None, None)

    import_vl_convert.assert_not_called()


def test_html_renderer_uses_vegafusion_compilation_for_warnings(chart, monkeypatch):
    from altair.utils import display as display_utils
    from altair.vegalite.v6 import display

    import_vl_convert = Mock()
    compile_with_vegafusion = Mock(return_value={})
    monkeypatch.setattr(display, "import_vl_convert", import_vl_convert)
    monkeypatch.setattr(
        display_utils, "compile_with_vegafusion", compile_with_vegafusion
    )

    with alt.data_transformers.enable("vegafusion"), alt.renderers.enable("html"):
        chart._repr_mimebundle_(None, None)

    import_vl_convert.assert_not_called()
    compile_with_vegafusion.assert_called_once_with(chart.to_dict())


def test_html_renderer_can_disable_vegafusion_warnings(chart, monkeypatch, caplog):
    from altair.utils import display as display_utils

    logger = logging.getLogger("vl_convert")
    logger_disabled = logger.disabled

    def compile_with_warning(spec):
        logger.warning("compile warning")
        return {}

    monkeypatch.setattr(display_utils, "compile_with_vegafusion", compile_with_warning)

    with (
        caplog.at_level(logging.WARNING, logger="vl_convert"),
        alt.data_transformers.enable("vegafusion"),
        alt.renderers.enable("html", show_warnings=False),
    ):
        chart._repr_mimebundle_(None, None)

    assert "compile warning" not in caplog.messages
    assert logger.disabled is logger_disabled


@pytest.mark.parametrize("error", [ImportError, RuntimeError])
def test_html_renderer_without_usable_vl_convert(chart, monkeypatch, error):
    from altair.vegalite.v6 import display

    def raise_error():
        msg = "vl-convert is unavailable"
        raise error(msg)

    monkeypatch.setattr(display, "import_vl_convert", raise_error)

    with alt.renderers.enable("html"):
        assert "text/html" in chart._repr_mimebundle_(None, None)


def test_mimetype_renderer_embed_options(chart):
    # check that metadata is passed appropriately
    from altair.vegalite.v6.display import VEGALITE_MIME_TYPE

    mimetype = VEGALITE_MIME_TYPE
    spec = chart.to_dict()
    with alt.renderers.enable("mimetype"):
        # Sanity check: no metadata specified
        bundle, metadata = chart._repr_mimebundle_(None, None)
        assert bundle[mimetype] == spec
        assert metadata == {}
        with alt.renderers.set_embed_options(actions=False):
            bundle, metadata = chart._repr_mimebundle_(None, None)
            assert set(bundle.keys()) == {mimetype, "text/plain"}
            assert bundle[mimetype] == spec
            assert metadata == {mimetype: {"embed_options": {"actions": False}}}


def test_json_renderer_embed_options(chart):
    """Test that embed_options in renderer metadata are correctly manifest in html."""
    mimetype = "application/json"
    spec = chart.to_dict()
    with alt.renderers.enable("json"):
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
def test_renderer_with_none_embed_options(chart):
    # Check that setting embed_options to None doesn't crash
    from altair.utils.mimebundle import spec_to_mimebundle

    spec = chart.to_dict()
    with alt.renderers.enable("mimetype", embed_options=None):
        bundle = spec_to_mimebundle(
            spec=spec,
            mode="vega-lite",
            format="svg",
            embed_options=None,
        )
        assert bundle["image/svg+xml"].startswith("<svg")


@jupyter_marks
def test_jupyter_renderer_mimetype(chart) -> None:
    """Test that we get the expected widget mimetype when the jupyter renderer is enabled."""
    with alt.renderers.enable("jupyter"):
        assert (
            "application/vnd.jupyter.widget-view+json"
            in chart._repr_mimebundle_(None, None)[0]
        )
