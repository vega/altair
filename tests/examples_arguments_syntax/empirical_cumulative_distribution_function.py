"""
Empirical Cumulative Distribution Function
------------------------------------------
This example shows an empirical cumulative distribution function.
"""
# category: distributions
import altair as alt
from altair.datasets import data

source = data.movies.url

alt.Chart(source).transform_window(
    ecdf="cume_dist()",
    sort=[{"field": "IMDB Rating"}],
).mark_line(
    interpolate="step-after"
).encode(
    x="IMDB Rating:Q",
    y="ecdf:Q"
)
