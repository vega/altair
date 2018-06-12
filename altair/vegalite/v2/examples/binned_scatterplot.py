"""
Binned Scatterplot
------------------
This example shows how to make a binned scatterplot.
"""
# category: scatter plots
import altair as alt


source = alt.datasets.movies.url

alt.Chart(source).mark_circle().encode(
    alt.X('IMDB_Rating:Q', bin=True),
    alt.Y('Rotten_Tomatoes_Rating:Q', bin=True),
    size='count()'
)
