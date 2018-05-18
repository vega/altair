"""
Trellis Histogram
-----------------
This example shows how to make a basic trellis histogram.
https://vega.github.io/vega-lite/examples/trellis_bar_histogram.html
"""
# category: histograms
import altair as alt


source = alt.datasets.cars()

alt.Chart(source).mark_bar().encode(
    alt.X("Horsepower:Q", bin=True),
    y='count()',
    row='Origin'
)
