import io
import pkgutil

import pytest

from altair.utils.execeval import eval_block
from altair import examples


def require_altair_saver(func):
    try:
        import altair_saver  # noqa: F401
    except ImportError:
        return pytest.mark.skip("altair_saver not importable; cannot run saver tests")(
            func
        )
    else:   
        return func


def iter_example_filenames():
    for importer, modname, ispkg in pkgutil.iter_modules(examples.__path__):
        if ispkg or modname.startswith('_'):
            continue
        yield modname + '.py'


@pytest.mark.parametrize('filename', iter_example_filenames())
def test_examples(filename):
    source = pkgutil.get_data(examples.__name__, filename)
    chart = eval_block(source)

    if chart is None:
        raise ValueError("Example file should define chart in its final "
                         "statement.")
    chart.to_dict()


@require_altair_saver
@pytest.mark.parametrize('filename', iter_example_filenames())
def test_render_examples_to_png(filename):
    source = pkgutil.get_data(examples.__name__, filename)
    chart = eval_block(source)
    out = io.BytesIO()
    chart.save(out, format="png")
    assert out.getvalue().startswith(b'\x89PNG')
