"""
Calculate Residuals
-------------------
A dot plot showing each movie in the database, and the difference from the average movie rating.
The display is sorted by year to visualize everything in sequential order. 
The graph is for all Movies before 2019.

Adapted from `Calculate Residuals <https://vega.github.io/vega-lite/examples/joinaggregate_residual_graph.html>`_.
"""
# category: advanced calculations
import altair as alt
from altair.datasets import data

imdb_rating = alt.datum["IMDB Rating"]
source = data.movies.url

chart = (
    alt.Chart(source)
    .mark_point()
    .transform_filter(imdb_rating != None)
    .transform_filter(
        alt.FieldRangePredicate("Release Date", [None, 2019], timeUnit="year")
    )
    .transform_joinaggregate(Average_Rating="mean(IMDB Rating)")
    .transform_calculate(Rating_Delta=imdb_rating - alt.datum.Average_Rating)
    .encode(
        x=alt.X("Release Date:T", title="Release Date"),
        y=alt.Y("Rating_Delta:Q", title="Rating Delta"),
        color=alt.Color(
            "Rating_Delta:Q",
            title="Rating Delta",
            scale=alt.Scale(domainMid=0),
        ),
    )
)
chart