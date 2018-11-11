"""
Histogram with a Global Mean Overlay
------------------------------------
This example shows a histogram with a global mean overlay.
"""
# category: histograms
import altair as alt
from vega_datasets import data

source = data.movies.url

bar = alt.Chart(source).mark_bar().encode(
    alt.X('IMDB_Rating:Q', bin=True, axis=None),
    alt.Y('count()')
)

rule = alt.Chart(source).mark_rule(color='red').encode(
    x='mean(IMDB_Rating):Q',
    size=alt.value(5)
)

bar + rule
