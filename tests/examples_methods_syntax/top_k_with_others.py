"""
Top-K Plot with Others
----------------------
This example shows how to use aggregate, window, and calculate transformations
to display the top-k directors by average worldwide gross while grouping the 
remaining directors as 'All Others'.
"""
# category: advanced calculations
import altair as alt
from vega_datasets import data

source = data.movies.url

alt.Chart(source).mark_bar().encode(
    alt.X("aggregate_gross:Q").aggregate("mean").title(None),
    alt.Y("ranked_director:N")
        .sort(op="mean", field="aggregate_gross", order="descending")
        .title(None)
).transform_aggregate(
    aggregate_gross='mean(Worldwide_Gross)',
    groupby=["Director"],
).transform_window(
    rank='row_number()',
    sort=[alt.SortField("aggregate_gross", order="descending")],
).transform_calculate(
    ranked_director="datum.rank < 10 ? datum.Director : 'All Others'"
).properties(
    title="Top Directors by Average Worldwide Gross",
)
