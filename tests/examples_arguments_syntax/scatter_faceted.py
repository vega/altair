"""
Faceted Scatter Plot
--------------------
A series of scatter plots, one for each country/area of origin.
"""
# category: scatter plots
import altair as alt
from vega_datasets import data

source = data.cars()

alt.Chart(source, width=100, height=100).mark_point().encode(
    x="Horsepower:Q",
    y="Miles_per_Gallon:Q",
    row="Origin:N",
)
