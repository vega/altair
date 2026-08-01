"""
Filter a Scatter Plot with a Number Input
=========================================
This example shows how to bind an HTML number input to a parameter and use the
entered value to filter a scatter plot.
"""

# category: interactive charts
import altair as alt
from altair.datasets import data

source = data.cars.url

minimum_horsepower = alt.param(
    name="minimum_horsepower",
    value=100,
    bind=alt.binding(input="number", name="Minimum horsepower: "),
)

chart = (
    alt.Chart(source)
    .mark_circle(size=60)
    .encode(
        alt.X("Horsepower:Q"),
        alt.Y("Miles_per_Gallon:Q"),
        alt.Color("Origin:N"),
        tooltip=[
            alt.Tooltip("Name:N"),
            alt.Tooltip("Horsepower:Q"),
            alt.Tooltip("Miles_per_Gallon:Q"),
        ],
    )
    .transform_filter(alt.datum.Horsepower >= minimum_horsepower)
    .add_params(minimum_horsepower)
)

chart
