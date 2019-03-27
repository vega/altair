"""
Box Plot with Min/Max Whiskers
------------------------------
This example shows how to make a basic box plot using US Population data from 2000.
"""
# category: other charts
import altair as alt
from vega_datasets import data

source = data.population.url

alt.Chart(source).mark_boxplot(extent='min-max').encode(
    x='age:O',
    y='people:Q'
)