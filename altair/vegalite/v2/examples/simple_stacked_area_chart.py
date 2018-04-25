"""
Simple Stacked Area Chart
-------------------------
This example shows how to make a simple stacked area chart.
"""
# category: basic charts

import altair as alt
from vega_datasets import data

source = data.unemployment_across_industries.url

alt.Chart(source).mark_area().encode(
    x="date:T",
    y="count:Q",
    color="series:N"
)
