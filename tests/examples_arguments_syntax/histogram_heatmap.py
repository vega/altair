"""
2D Histogram Heatmap
--------------------
This example shows how to make a heatmap from binned quantitative data.
"""
# category: distributions
import altair as alt
from altair.datasets import data

source = data.movies.url

alt.Chart(source).mark_rect().encode(
    alt.X('IMDB Rating:Q', bin=alt.Bin(maxbins=60)),
    alt.Y('Rotten Tomatoes Rating:Q', bin=alt.Bin(maxbins=40)),
    alt.Color('count():Q', scale=alt.Scale(scheme='greenblue'))
)
