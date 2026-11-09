# /// script
# requires-python = ">=3.11"
# dependencies = ["altair", "pandas"]
#
# [tool.marimo.display]
# cell_output = "above"
# ///
"""
Linked Zoom
===========
This example shows how to link the x-axes of multiple charts so that
zooming or panning in one chart zooms or pans the other as well.

Calling ``.interactive()`` on each chart would create a separate,
independent selection for each chart. Instead, a single interval
selection bound to the scales is created once and attached to both
charts with ``add_params``. Because the same selection object is
shared, changing it in either chart updates the scales of both charts.

The selection is restricted to the ``x`` encoding, so only the shared
``Horsepower`` axis is linked; each chart keeps its own independent
y-axis. Note that with layered charts the shared selection should be
attached to only one layer in each chart, otherwise Vega-Lite reports
duplicate signal names.
"""
# :new:
# category: interactive charts
import altair as alt
from altair.datasets import data

source = data.cars()

zoom = alt.selection_interval(bind='scales', encodings=['x'])

mpg = alt.Chart(source).mark_point().encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    color='Origin',
).add_params(
    zoom
).properties(
    width=300,
    height=300,
    title='Miles per Gallon vs Horsepower'
)

acceleration = alt.Chart(source).mark_point().encode(
    x='Horsepower',
    y='Acceleration',
    color='Origin',
).add_params(
    zoom
).properties(
    width=300,
    height=300,
    title='Acceleration vs Horsepower'
)

mpg | acceleration
