"""
Faceted Histogram
-----------------
This example shows how to make a basic faceted histogram,
with one histogram subplot for different subsets of the data.

Based off the vega-lite example:
https://vega.github.io/vega-lite/examples/trellis_bar_histogram.html
"""
# category: distributions
import altair as alt
from altair.datasets import data

source = data.cars()

alt.Chart(source).mark_bar().encode(
    alt.X("Horsepower:Q", bin=True),
    y="count()",
    row="Origin",
)
