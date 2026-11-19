"""
Scatter Plot with Null Values in Grey
-------------------------------------
By default, points with a missing (null) value in one of the position fields are left
out of a scatter plot. This example keeps them with ``invalid="show"`` on the mark, which
draws a missing value at the start of its axis, and colors these points grey so they are
easy to tell apart from movies that have both ratings.

Adapted from `Scatterplot with Null Values in Grey <https://vega.github.io/vega-lite/examples/point_invalid_color.html>`_.
"""
# category: scatter plots
import altair as alt
from altair.datasets import data

source = data.movies.url

missing_rating = (
    "datum['IMDB Rating'] === null || datum['Rotten Tomatoes Rating'] === null"
)

alt.Chart(source).mark_point(invalid="show").encode(
    alt.X("IMDB Rating:Q"),
    alt.Y("Rotten Tomatoes Rating:Q"),
    color=alt.when(missing_rating).then(alt.value("#aaa")),
)
