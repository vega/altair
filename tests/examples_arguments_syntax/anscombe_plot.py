"""
Anscombe's Quartet
------------------

`Anscombe's Quartet <https://en.wikipedia.org/wiki/Anscombe%27s_quartet>`_
is a famous dataset constructed by Francis Anscombe.
It is made of 4 different subsets of data.
Each subset has very different characteristics, even though common summary
statistics such as mean and variance are identical.

This example shows how to make a faceted plot, with each facet
showing a different subset of the data.
"""
# category: case studies
import altair as alt
from vega_datasets import data

source = data.anscombe()

alt.Chart(source).mark_circle().encode(
    alt.X("X", scale=alt.Scale(zero=False)),
    alt.Y("Y", scale=alt.Scale(zero=False)),
    alt.Facet("Series", columns=2),
).properties(
    width=180,
    height=180,
)
