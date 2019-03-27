"""
Tukey Box Plot (1.5 IQR)
------------------------
This example shows how to make a box plot with 1.5 IQR using US Population data from 2000.
"""
# category: other charts
import altair as alt
from vega_datasets import data

source = data.population.url

alt.Chart(source).mark_boxplot(extent=1.5).encode(
    x='age:O',
    y='people:Q'
)