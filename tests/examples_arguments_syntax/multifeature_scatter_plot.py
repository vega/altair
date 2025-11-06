"""
Multifeature Scatter Plot
=========================
This example shows how to make a scatter plot with multiple feature encodings.
"""
# category: scatter plots
import altair as alt
from altair.datasets import data

source = data.penguins()

alt.Chart(source).mark_circle().encode(
    alt.X('Flipper Length (mm)', scale=alt.Scale(zero=False)),
    alt.Y('Body Mass (g)', scale=alt.Scale(zero=False, padding=1)),
    alt.Size('Beak Depth (mm)', scale=alt.Scale(zero=False)),
    color='Species'
)
