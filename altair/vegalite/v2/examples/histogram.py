"""
Histogram
-----------------
This example shows how to make a basic histogram, based on the vega-lite docs
https://vega.github.io/vega-lite/examples/histogram.html
"""
import altair as alt
from vega_datasets import data

movies = data.movies.url

chart = alt.Chart(movies).mark_bar().encode(
    x=alt.X("IMDB_Rating",
            type='quantitative',
            bin=alt.BinTransform(
                maxbins=10,
            )),
    y='count(*):Q',
)