import pkgutil

import pytest

from altair.utils.execeval import eval_block
from altair import examples


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
