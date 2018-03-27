import os
from os.path import join, dirname, abspath

import pytest

from altair.utils.execeval import eval_block

EXAMPLE_DIR = abspath(join(dirname(__file__), '..'))


def iter_example_filenames():
    for filename in os.listdir(EXAMPLE_DIR):
        if filename.startswith('__'):
            continue
        if not filename.endswith('.py'):
            continue
        yield filename


@pytest.mark.parametrize('filename', iter_example_filenames())
def test_examples(filename):
    with open(join(EXAMPLE_DIR, filename)) as f:
        source = f.read()

    chart = eval_block(source)

    if chart is None:
        raise ValueError("Example file should define chart in its final "
                         "statement.")
    dct = chart.to_dict()
