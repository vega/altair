"""
Interactive Chart with Aggregation
==================================
This example shows an interactive chart where the range binder controls a
threshold as rule where the datapoints on the left-side are aggregated and on the
right-side are drawn as is. 
The ability to slide back and fourth may help you understand how the visualization
represents the aggregation. Adapted from an example by @dwootton.
"""
# category: interactive charts
import altair as alt
from altair.datasets import data

source = data.movies.url

slider = alt.binding_range(min=0, max=10, step=0.1)
threshold = alt.param(name="threshold", value=5, bind=slider)

alt.layer(
    alt.Chart(source).mark_circle().encode(
        x=alt.X("IMDB_Rating:Q").title("IMDB Rating"),
        y=alt.Y("Rotten_Tomatoes_Rating:Q").title("Rotten Tomatoes Rating")
    ).transform_filter(
        alt.datum["IMDB_Rating"] >= threshold
    ),

    alt.Chart(source).mark_circle().encode(
        x=alt.X("IMDB_Rating:Q").bin(maxbins=10),
        y=alt.Y("Rotten_Tomatoes_Rating:Q").bin(maxbins=10),
        size=alt.Size("count():Q").scale(domain=[0,160])
    ).transform_filter(
        alt.datum["IMDB_Rating"] < threshold
    ),

    alt.Chart().mark_rule(color="gray").encode(
        strokeWidth=alt.StrokeWidth(value=6),
        x=alt.X(datum=alt.expr(threshold.name), type="quantitative")
    )
).add_params(threshold)