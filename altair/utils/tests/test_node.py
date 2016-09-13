import tempfile
from xml.etree import ElementTree

import pytest
import pandas as pd

from altair.utils.node import savechart, savechart_available, NodeExecError
from altair import Chart


def consistent_with_png(filename):
    """Check that the file has a header consistent with PNG"""
    with open(filename, 'rb') as f:
        arr = f.read()
    return arr.startswith(b'\x89PNG\r\n')


def consistent_with_svg(filename):
    """Check that the file has a structure consistent with SVG"""
    try:
        e = ElementTree.parse(filename)
    except ElementTree.ParseError:
        return False
    else:
        keys = e.getroot().keys()
        return set(keys) == {'width', 'version', 'class', 'height'}


@pytest.mark.skipif(not savechart_available(),
                    reason='node tools are not available')
def test_savechart():
    data = pd.DataFrame({'x': range(10),
                         'y': range(10)})
    chart = Chart(data).mark_point().encode(x='x', y='y')
    
    with tempfile.NamedTemporaryFile(suffix='.png') as f:
        try:
            savechart(chart, f.name)
        except NodeExecError:
            pytest.skip('png failed due to improper nodejs setup')
        assert consistent_with_png(f.name)

    with tempfile.NamedTemporaryFile(suffix='.svg') as f:
        try:
            savechart(chart, f.name)
        except NodeExecError:
            pytest.skip('svg failed due to improper nodejs setup')
        assert consistent_with_svg(f.name)
