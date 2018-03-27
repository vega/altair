import os
from os.path import join, dirname, abspath

import pytest

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
    globals_ = {}
    exec(source, globals_)

    if 'chart' not in globals_:
        raise ValueError("Example file should define a chart variable")
    chart = globals_['chart']
    dct = chart.to_dict()
