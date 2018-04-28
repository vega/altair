"""
Slope Graph
-----------------------
This example shows how to make Slope Graph.
"""
# category: line charts
import altair as alt
from vega_datasets import data

source = data.barley()

# The year here is stored by pandas as an integer. When treating columns as dates,
# it is best to use either a string representation or a datetime representation.
source.year = source.year.astype(str)

alt.Chart(source).mark_line().encode(
    x='year',
    y='median(yield)',
    color='site'
)
