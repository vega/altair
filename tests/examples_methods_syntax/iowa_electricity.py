"""
Iowa's Renewable Energy Boom
----------------------------
This example is a fully developed stacked chart using the sample dataset of Iowa's electricity sources.
"""
# category: case studies
import altair as alt
from vega_datasets import data

source = data.iowa_electricity()

alt.Chart(
    source,
    title=alt.Title(
        "Iowa's green energy boom",
        subtitle="A growing share of the state's energy has come from renewable sources"
    )
).mark_area().encode(
    alt.X("year:T").title("Year"),
    alt.Y("net_generation:Q")
        .title("Share of net generation")
        .stack("normalize")
        .axis(format=".0%"),
    alt.Color("source:N").title("Electricity source")
)
