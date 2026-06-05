"""
Histogram with Adjustable Bin Size
----------------------------------
This example shows a 2D histogram heatmap whose bin size can be changed with a
slider. Vega-Lite does not allow a parameter to drive ``maxbins`` directly, so
we draw one layer per available bin count and only show the layer that matches
the slider value.
"""
# category: distributions
import altair as alt
from altair.datasets import data

source = data.movies.url

maxbins_options = [10, 20, 30, 40, 50, 60]

slider = alt.binding_range(
    min=min(maxbins_options),
    max=max(maxbins_options),
    step=10,
    name="Max bins ",
)
maxbins = alt.param(name="maxbins", value=30, bind=slider)

layers = [
    alt.Chart(source)
    .mark_rect()
    .encode(
        alt.X("IMDB Rating:Q")
        .bin(maxbins=n)
        .scale(zero=True)
        .axis(format="d", title="IMDB Rating"),
        alt.Y("Rotten Tomatoes Rating:Q")
        .bin(maxbins=n)
        .axis(format="d", title="Rotten Tomatoes Rating"),
        alt.Color("count():Q").scale(scheme="greenblue"),
    )
    .transform_filter(f"maxbins === {n}")
    for n in maxbins_options
]

alt.layer(*layers).add_params(maxbins).properties(
    width=400,
    height=300,
)
