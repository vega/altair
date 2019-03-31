"""
Becker's Barley Trellis Plot (wrapped facet)
--------------------------------------------
The example demonstrates the trellis charts created by Richard Becker, William Cleveland and others in the 1990s. 
This is the Altair replicate of `the VegaLite version <https://vega.github.io/vega-lite/docs/facet.html#facet-full>`_ 
demonstrating the usage of `columns` argument to create wrapped facet.
"""

import altair as alt
from vega_datasets import data

source = data.barley()

alt.Chart(source, columns=2).mark_point().encode(
    x=alt.X(
        'yield:Q',
        scale=alt.Scale(zero=False),
        aggregate='median'
    ),
    y=alt.Y(
        'variety:O',
        sort=alt.SortByEncoding(encoding='x', order='descending'),
        scale=alt.Scale(rangeStep=12),
    ),
    color=alt.Color('year:N', legend=alt.Legend(title="Year")),
    facet=alt.Facet(
        'site:O',
        sort=alt.EncodingSortField(field='yield', op='median')
    )
)
