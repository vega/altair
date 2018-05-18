"""
Simple Interactive Colored Scatterplot
--------------------------------------
This example shows how to make an interactive scatterplot.
"""
# category: interactive charts
import altair as alt


source = alt.datasets.cars()

alt.Chart(source).mark_circle().encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    color='Origin'
).interactive()
