"""
Binned Scatterplot
-----------------
This example shows how to make a binned scatterplot.
"""

import altair as alt
from vega_datasets import data

source = data.movies()

chart = alt.Chart(source).mark_circle().encode(
    x = alt.X('IMDB_Rating',  bin = alt.BinParams(maxbins=10)),
    y = alt.Y('Rotten_Tomatoes_Rating',  bin = alt.BinParams(maxbins=10)),
    size = 'count(IMDB_Rating)'
)  
chart
