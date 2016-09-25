import tempfile

import pytest
import pandas as pd

from altair.utils.node import savechart, vl_cmd_available, consistent_with_png, consistent_with_svg
from altair import Chart


def make_chart():
    data = pd.DataFrame({'x': range(10),
                         'y': range(10)})
    return Chart(data).mark_point().encode(x='x', y='y')


@pytest.mark.skipif(not vl_cmd_available('vl2png'),
                    reason='command-line tool vl2png is not available')
def test_savechart_png():
    chart = make_chart()

    with tempfile.NamedTemporaryFile(suffix='.png') as f:
        savechart(chart, f.name)
        assert consistent_with_png(f.name)


@pytest.mark.skipif(not vl_cmd_available('vl2svg'),
                    reason='command-line tool vl2svg is not available')
def test_savechart_svg():
    chart = make_chart()

    with tempfile.NamedTemporaryFile(suffix='.svg') as f:
        savechart(chart, f.name)
        assert consistent_with_svg(f.name)
