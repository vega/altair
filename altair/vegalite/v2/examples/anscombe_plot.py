"""
Anscombe's Quartet
------------------

This example shows how to use the column channel to make a trellis plot. Anscombe's Quartet is a famous dataset constructed by Francis Anscombe. Common summary statistics are identical for each subset of the data, despite the subsets having vastly different characteristics.
"""
# category: scatter plots
import altair as alt


anscombe = alt.datasets.anscombe()

alt.Chart(anscombe).mark_circle().encode(
    alt.X('X', scale=alt.Scale(zero=False)),
    alt.Y('Y', scale=alt.Scale(zero=False)),
    column='Series'
).properties(
    width=150,
    height=150
)
