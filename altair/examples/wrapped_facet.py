"""
Wrapped Facet Example
---------------------
This shows an example of a wrapped facet plot, where faceted data are limited
to a specified number of columns.
"""
# category: other charts

import altair as alt
from vega_datasets import data

source = data.barley.url

alt.Chart(source).mark_point().encode(
    alt.X('median(yield):Q', scale=alt.Scale(zero=False)),
    y='variety:O',
    color='year:N',
    facet='site:O',
).properties(
    columns=2,
    width=200,
    height=100,
)
