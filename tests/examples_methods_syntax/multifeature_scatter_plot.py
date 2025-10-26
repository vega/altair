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
    alt.X('Flipper Length (mm)').scale(zero=False),
    alt.Y('Body Mass (g)').scale(zero=False, padding=1),
    alt.Size('Beak Depth (mm)').scale(zero=False),
    color='Species'
)
