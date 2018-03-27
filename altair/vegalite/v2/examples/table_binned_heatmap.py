"""
Table Binned Heatmap
-----------------------
This example shows how to make a heatmap.
"""
# category: basic charts

import altair as alt
from vega_datasets import data

source = data.movies.url

chart = alt.Chart(source).mark_rect().encode(
    alt.X('IMDB_Rating:Q', bin=alt.Bin(maxbins=60)),
    alt.Y('Rotten_Tomatoes_Rating:Q', bin=alt.Bin(maxbins=40)),
    alt.Color('count(IMDB_Rating):Q', scale=alt.Scale(scheme='greenblue'))
)
