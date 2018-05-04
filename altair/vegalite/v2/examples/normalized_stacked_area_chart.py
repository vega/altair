"""
Normalized Stacked Area Chart
-----------------------------
This example shows how to make a normalized stacked area chart.
"""
# category: simple charts
import altair as alt
from vega_datasets import data

source = data.unemployment_across_industries.url

alt.Chart(source).mark_area().encode(
    x="date:T",
    y=alt.Y("count:Q", stack="normalize"),
    color="series:N"
)
