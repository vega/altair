"""
Empirical Cumulative Distribution Function
------------------------------------------
This example shows an empirical cumulative distribution function.
"""
# category: line charts
import altair as alt
from vega_datasets import data

source = data.movies.url

alt.Chart(source).transform_window(
    ecdf="cume_dist()",
    sort=[{"field": "IMDB_Rating"}],
).mark_line(
    interpolate="step-after"
).encode(
    x="IMDB_Rating:Q",
    y="ecdf:Q"
)
