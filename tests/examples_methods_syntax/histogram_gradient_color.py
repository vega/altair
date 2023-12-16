"""
Histogram with Gradient Color
-----------------------------
This example shows how to make a histogram with gradient color.
The low-high IMDB rating is represented with the color scheme `pinkyellowgreen`.
"""
# category: distributions
import altair as alt
from vega_datasets import data

source = data.movies.url

alt.Chart(source).mark_bar().encode(
    alt.X("IMDB_Rating:Q").bin(maxbins=20).scale(domain=[1, 10]),
    alt.Y('count()'),
    alt.Color("IMDB_Rating:Q").bin(maxbins=20).scale(scheme='pinkyellowgreen')
)