"""
Strip Plot with Jitter
---------
This example shows how to make a strip plot with jitter.
"""
# category: distributions
import altair as alt
from vega_datasets import data

source = data.movies.url

alt.Chart(source).mark_circle(size=8).encode(
    y="Major_Genre:N",
    x="IMDB_Rating:Q",
    yOffset="jitter:Q",
    color=alt.Color('Major_Genre:N', legend=None)
).transform_calculate(
    # Generate Gaussian jitter with a Box-Muller transform
    jitter="sqrt(-2*log(random()))*cos(2*PI*random())"
)
