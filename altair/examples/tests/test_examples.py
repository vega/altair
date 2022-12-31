import io
from itertools import chain
import pkgutil

import pytest

from altair.utils.execeval import eval_block
from altair import examples
from altair.examples import attribute_syntax

try:
    import altair_saver  # noqa: F401
except ImportError:
    altair_saver = None

try:
    import vl_convert as vlc  # noqa: F401
except ImportError:
    vlc = None


def iter_example_filenames():
    for importer, modname, ispkg in pkgutil.iter_modules(examples.__path__):
        if ispkg or modname.startswith("_"):
            continue
        yield modname + ".py"


def iter_attribute_syntax_filenames():
    for importer, modname, ispkg in pkgutil.iter_modules(attribute_syntax.__path__):
        if ispkg or modname.startswith("_"):
            continue
        yield modname + ".py"


@pytest.mark.parametrize(
    "filename", chain(iter_example_filenames(), iter_attribute_syntax_filenames())
)
def test_examples(filename: str):
    source = pkgutil.get_data(examples.__name__, filename)
    chart = eval_block(source)

    if chart is None:
        raise ValueError("Example file should define chart in its final " "statement.")
    chart.to_dict()


@pytest.mark.parametrize("engine", ["vl-convert", "altair_saver"])
@pytest.mark.parametrize(
    "filename", chain(iter_example_filenames(), iter_attribute_syntax_filenames())
)
def test_render_examples_to_png(engine, filename):
    if engine == "vl-convert" and vlc is None:
        pytest.skip("vl_convert not importable; cannot run mimebundle tests")
    elif engine == "altair_saver":
        if altair_saver is None:
            pytest.skip("altair_saver not importable; cannot run png tests")
        if "png" not in altair_saver.available_formats("vega-lite"):
            pytest.skip("altair_saver not configured to save to png")

    source = pkgutil.get_data(examples.__name__, filename)
    chart = eval_block(source)
    out = io.BytesIO()
    chart.save(out, format="png", engine=engine)
    assert out.getvalue().startswith(b"\x89PNG")
