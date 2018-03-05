"""
Histogram with a Global Mean Overlay
------------------------------------
This example shows a histogram with a global mean overlay.
"""

import altair as alt
from vega_datasets import data

source = data.movies.url

bar = alt.Chart(source).mark_bar().encode(
    x = alt.X('IMDB_Rating:Q', bin = True, axis = None),
    y = alt.Y('count(*):Q'))

rule = alt.Chart(source).mark_rule(color = 'red').encode(
    x = 'mean(IMDB_Rating):Q',
    size = alt.SizeValue(5))
chart = bar + rule
