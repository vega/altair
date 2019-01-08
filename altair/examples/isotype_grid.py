"""
L.A. Riots Deaths by Gender
---------------------------
This example is a fully developed chart with a grid of isotype figures.
"""
# category: case studies
import altair as alt
from vega_datasets import data

source = data.la_riots()

# Sort by the key field
source = source.sort_values("gender")

# Add an incremental id to the data
source['id'] = source.reset_index().index + 1

alt.Chart(
    source,
    title="L.A. Riots Deaths by Gender"
).transform_calculate(
    col="ceil(datum.id/10)"
).transform_calculate(
    row="datum.id - datum.col*10"
).mark_point(filled=True, size=90).encode(
    x=alt.X("col:O", axis=None),
    y=alt.Y("row:O", axis=None),
    shape=alt.ShapeValue("M1.7 -1.7h-0.8c0.3 -0.2 0.6 -0.5 0.6 -0.9c0 -0.6 -0.4 -1 -1 -1c-0.6 0 -1 0.4 -1 1c0 0.4 0.2 0.7 0.6 0.9h-0.8c-0.4 0 -0.7 0.3 -0.7 0.6v1.9c0 0.3 0.3 0.6 0.6 0.6h0.2c0 0 0 0.1 0 0.1v1.9c0 0.3 0.2 0.6 0.3 0.6h1.3c0.2 0 0.3 -0.3 0.3 -0.6v-1.8c0 0 0 -0.1 0 -0.1h0.2c0.3 0 0.6 -0.3 0.6 -0.6v-2c0.2 -0.3 -0.1 -0.6 -0.4 -0.6z"),
    color=alt.Color(
        "gender:N",
        legend=alt.Legend(title="", padding=15)
    )
).properties(width=400, height=400)
