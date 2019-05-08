import pytest

import altair as alt
from altair.utils import AltairDeprecationWarning
from altair.utils.deprecation import _deprecated


def test_deprecated_class():
    OldChart = _deprecated(alt.Chart, "OldChart")
    with pytest.warns(AltairDeprecationWarning) as record:
        OldChart()
    assert "alt.OldChart" in record[0].message.args[0]
    assert "alt.Chart" in record[0].message.args[0]