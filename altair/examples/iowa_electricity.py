"""
Iowa's renewable energy boom
----------------------------
This example is a fully developed stacked chart using the sample dataset of Iowa's electricity sources.
"""
# category: case studies
import altair as alt
from vega_datasets import data

source = data.iowa_electricity()

alt.Chart(source, title="Iowa's renewable energy boom").mark_area().encode(
    x=alt.X(
        "year:T",
        axis=alt.Axis(title="Year")
    ),
    y=alt.Y(
        "net_generation:Q",
        stack="normalize",
        axis=alt.Axis(title="Share of net generation", format=".0%"),
    ),
    color=alt.Color(
        "source:N",
        legend=alt.Legend(title="Electricity source"),
    )
)
