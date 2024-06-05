import io
import pkgutil

import pytest

import altair as alt
from altair.utils.execeval import eval_block
from tests import examples_arguments_syntax
from tests import examples_methods_syntax


try:
    import vl_convert as vlc
except ImportError:
    vlc = None


def iter_examples_filenames(syntax_module):
    for _importer, modname, ispkg in pkgutil.iter_modules(syntax_module.__path__):
        if (
            ispkg
            or modname.startswith("_")
            # Temporarily skip this test until https://github.com/vega/altair/issues/3418
            # is fixed
            or modname == "interval_selection_map_quakes"
        ):
            continue
        yield modname + ".py"


@pytest.mark.parametrize(
    "syntax_module", [examples_arguments_syntax, examples_methods_syntax]
)
def test_render_examples_to_chart(syntax_module):
    for filename in iter_examples_filenames(syntax_module):
        source = pkgutil.get_data(syntax_module.__name__, filename)
        chart = eval_block(source)

        if chart is None:
            msg = (
                f"Example file {filename} should define chart in its final "
                "statement."
            )
            raise ValueError(msg)

        try:
            assert isinstance(chart.to_dict(), dict)
        except Exception as err:
            msg = (
                f"Example file {filename} raised an exception when "
                f"converting to a dict: {err}"
            )
            raise AssertionError(msg) from err


@pytest.mark.parametrize(
    "syntax_module", [examples_arguments_syntax, examples_methods_syntax]
)
def test_from_and_to_json_roundtrip(syntax_module):
    """Tests if the to_json and from_json (and by extension to_dict and from_dict)
    work for all examples in the Example Gallery.
    """
    for filename in iter_examples_filenames(syntax_module):
        source = pkgutil.get_data(syntax_module.__name__, filename)
        chart = eval_block(source)

        if chart is None:
            msg = (
                f"Example file {filename} should define chart in its final "
                "statement."
            )
            raise ValueError(msg)

        try:
            first_json = chart.to_json()
            reconstructed_chart = alt.Chart.from_json(first_json)
            # As the chart objects are not
            # necessarily the same - they could use different objects to encode the same
            # information - we do not test for equality of the chart objects, but rather
            # for equality of the json strings.
            second_json = reconstructed_chart.to_json()
            assert first_json == second_json
        except Exception as err:
            msg = (
                f"Example file {filename} raised an exception when "
                f"doing a json conversion roundtrip: {err}"
            )
            raise AssertionError(msg) from err


@pytest.mark.parametrize("engine", ["vl-convert"])
@pytest.mark.parametrize(
    "syntax_module", [examples_arguments_syntax, examples_methods_syntax]
)
def test_render_examples_to_png(engine, syntax_module):
    for filename in iter_examples_filenames(syntax_module):
        if engine == "vl-convert" and vlc is None:
            pytest.skip("vl_convert not importable; cannot run mimebundle tests")

        source = pkgutil.get_data(syntax_module.__name__, filename)
        chart = eval_block(source)
        out = io.BytesIO()
        chart.save(out, format="png", engine=engine)
        assert out.getvalue().startswith(b"\x89PNG")
