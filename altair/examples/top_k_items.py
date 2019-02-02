"""
Top K Items
-----------
This example shows how to use the window and transformation filter to display
the Top items of a long list of items in decreasing order.
The sorting of the x-axis is needed for vega-lite and for the example does
not do anything since we already have a unique value.
Here we sort the top 10 highest ranking movies of IMDB.
"""
# category: case studies
import altair as alt
from vega_datasets import data

source = data.movies.url

# Top 10 movies by IMBD rating
alt.Chart(
    source,
).mark_bar().encode(
    x=alt.X(
        'Title:N', 
        sort=alt.EncodingSortField(field="IMDB_Rating", op="mean", order='descending')
    ),
    y=alt.Y('IMDB_Rating:Q'),
    color=alt.Color('IMDB_Rating:Q')
    
).transform_window(
    rank='rank(IMDB_Rating)',
    sort=[alt.SortField('IMDB_Rating', order='descending')]
).transform_filter(
    (alt.datum.rank < 10)
)