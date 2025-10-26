"""
Becker's Barley Wrapped Facet Plot
----------------------------------
The example demonstrates the faceted charts created by Richard Becker,
William Cleveland and others in the 1990s. Using the visualization technique
where each row is a different site (i.e. the chart is faceted by site),
they identified an anomaly in a widely used agriculatural dataset,
where the "Morris" site accidentally had the years 1931 and 1932 swapped.
They named this
`"The Morris Mistake." <http://ml.stat.purdue.edu/stat695t/writings/Trellis.User.pdf>`_.
"""
# category: case studies
import altair as alt
from altair.datasets import data

source = data.barley.url

alt.Chart(source).mark_point().encode(
    alt.X("median(yield):Q").scale(zero=False),
    y="variety:O",
    color="year:N",
    facet=alt.Facet("site:O", columns=2),
).properties(
    width=200,
    height=100,
)
