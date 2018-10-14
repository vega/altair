"""
Histogram with a Global Mean Overlay
------------------------------------
This example shows a histogram with a global mean overlay.
"""
# category: histograms
import altair as alt
from vega_datasets import data

source = data.movies()

base = alt.Chart(source)

bar = base.mark_bar().encode(
    x=alt.X('IMDB_Rating', bin=True, axis=None),
    y='count()'
)

rule = base.mark_rule(color='red').encode(
    x='mean(IMDB_Rating)',
    size=alt.value(5)
)

bar + rule
