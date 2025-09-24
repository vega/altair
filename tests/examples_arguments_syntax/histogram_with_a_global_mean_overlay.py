"""
Histogram with a Global Mean Overlay
------------------------------------
This example shows a histogram with a global mean overlay.
"""
# category: distributions
import altair as alt
from altair.datasets import data

source = data.movies.url

base = alt.Chart(source)

bar = base.mark_bar().encode(
    x=alt.X('IMDB Rating:Q', bin=True, axis=None),
    y='count()'
)

rule = base.mark_rule(color='red').encode(
    x='mean(IMDB Rating):Q',
    size=alt.value(5)
)

bar + rule
