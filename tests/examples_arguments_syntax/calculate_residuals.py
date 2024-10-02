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

imdb_rating = alt.datum["IMDB Rating"]

chart = (
    alt.Chart("https://vega.github.io/vega-lite/data/movies.json")
    .mark_point()
    .transform_filter(imdb_rating != None)
    .transform_filter(
        alt.FieldRangePredicate("Release Date", [None, 2019], timeUnit="year")
    )
    .transform_joinaggregate(AverageRating="mean(IMDB Rating)")
    .transform_calculate(RatingDelta=imdb_rating - alt.datum.AverageRating)
    .encode(
        x="Release Date:T",
        y=alt.Y("RatingDelta:Q", title="Rating Delta"),
        color=alt.Color(
            "RatingDelta:Q",
            title="Rating Delta",
            scale=alt.Scale(domainMid=0),
        ),
    )
)
chart