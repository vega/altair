import pytest

import altair.vegalite.v5 as alt


def test_layer_props():
    """Beginning in Vega-Lite v5, the properties "height" and "width" were no longer allowed in a subchart within a LayerChart.  We check here that these are moved to the top level by Altair."""
    base = alt.Chart().mark_point()

    # Allowed
    base.properties(width=100) + base
    base.properties(width=100) + base.properties(height=200)
    base.properties(width=100) + base.properties(height=200, width=100)

    # Not allowed
    with pytest.raises(ValueError, match="inconsistent"):
        base.properties(width=100) + base.properties(width=200)

    # Check that the resulting LayerChart has the correct properties.
    c = base.properties(width=100) + base.properties(height=200, width=100)
    assert isinstance(c, alt.LayerChart)
    assert c.width == 100
    assert c.height == 200
