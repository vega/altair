"""
Interactive Crossfilter
=======================
This example shows a multi-panel view of the same data, where you can interactively
select a portion of the data in any of the panels to highlight that portion in any
of the other panels.
"""
# category: interactive charts
import altair as alt
from vega_datasets import data

source = alt.UrlData(
    data.flights_2k.url,
    format={'parse': {'date': 'date'}}
)

brush = alt.selection_interval(encodings=['x'])

# Define the base chart, with the common parts of the
# background and highlights
base = alt.Chart(width=160, height=130).mark_bar().encode(
    x=alt.X(alt.repeat('column')).bin(maxbins=20),
    y='count()'
)

# gray background with selection
background = base.encode(
    color=alt.value('#ddd')
).add_params(brush)

# blue highlights on the transformed data
highlight = base.transform_filter(brush)

# layer the two charts & repeat
alt.layer(
    background,
    highlight,
    data=source
).transform_calculate(
    "time",
    "hours(datum.date)"
).repeat(column=["distance", "delay", "time"])
