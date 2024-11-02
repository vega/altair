"""
Selection Histogram
===================
This chart shows an example of using an interval selection to filter the
contents of an attached histogram, allowing the user to see the proportion
of items in each category within the selection.
"""
# category: interactive charts
import altair as alt
from vega_datasets import data

source = data.cars()

brush = alt.selection_interval()

points = alt.Chart(source).mark_point().encode(
    x='Horsepower:Q',
    y='Miles_per_Gallon:Q',
    color=alt.when(brush).then("Origin:N").otherwise(alt.value("lightgray"))
).add_params(
    brush
)

bars = alt.Chart(source).mark_bar().encode(
    y='Origin:N',
    color='Origin:N',
    x='count(Origin):Q'
).transform_filter(
    brush
)

points & bars
