"""
Scatter Plot with Minimap
-------------------------
This example shows how to create a miniature version of a plot
such that creating a selection in the miniature version
adjusts the axis limits in another, more detailed view.
"""
# category: scatter plots

import altair as alt
from vega_datasets import data

source = data.seattle_weather()

zoom = alt.selection_interval(encodings=["x", "y"])

minimap = (
    alt.Chart(source)
    .mark_point()
    .add_params(zoom)
    .encode(
        x="date:T",
        y="temp_max:Q",
        color=alt.condition(zoom, "weather", alt.value("lightgray")),
    )
    .properties(
        width=200,
        height=200,
        title="Minimap -- click and drag to zoom in the detail view",
    )
)

detail = (
    alt.Chart(source)
    .mark_point()
    .encode(
        alt.X("date:T").scale(domain={"param": zoom.name, "encoding": "x"}),
        alt.Y("temp_max:Q").scale(domain={"param": zoom.name, "encoding": "y"}),
        color="weather",
    )
    .properties(width=600, height=400, title="Seattle weather -- detail view")
)

detail | minimap
