"""
Box Plot with Min/Max Whiskers
------------------------------
This example shows how to make a basic box plot using US Population data from 2000.  
Note that the default value of the `extent` property is 1.5, which can be used to 
produce in the standard modified boxplot.
"""
# category: other charts
import altair as alt
from vega_datasets import data

source = data.population.url

alt.Chart(source).mark_boxplot().encode(
    x='age:O',
    y='people:Q'
)
