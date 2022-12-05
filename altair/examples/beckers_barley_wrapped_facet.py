"""
Becker's Barley Trellis Plot (Wrapped Facet)
--------------------------------------------
The example demonstrates the trellis charts created by Richard Becker, William Cleveland and others in the 1990s. 
This is the Altair replicate of `the VegaLite version <https://vega.github.io/vega-lite/docs/facet.html#facet-full>`_ 
demonstrating the usage of `columns` argument to create wrapped facet.
"""
# category: advanced calculations
import altair as alt
from vega_datasets import data

source = data.barley.url

alt.Chart(source).mark_point().encode(
    alt.X('median(yield):Q').scale(zero=False),
    y='variety:O',
    color='year:N',
    facet=alt.Facet('site:O', columns=2),
).properties(
    width=200,
    height=100,
)
