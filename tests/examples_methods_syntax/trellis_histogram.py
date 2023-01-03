"""
Trellis Histogram
-----------------
This example shows how to make a basic trellis histogram.
https://vega.github.io/vega-lite/examples/trellis_bar_histogram.html
"""
# category: distributions
import altair as alt
from vega_datasets import data

source = data.cars()

alt.Chart(source).mark_bar().encode(
    alt.X("Horsepower:Q").bin(),
    y='count()',
    row='Origin'
)
