"""
Becker's Barley Faceted Plot
----------------------------
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
from vega_datasets import data

source = data.barley()

alt.Chart(source, title="The Morris Mistake").mark_point().encode(
    alt.X('yield:Q')
        .title("Barley Yield (bushels/acre)")
        .scale(zero=False)
        .axis(grid=False),
    alt.Y('variety:N')
        .title("")
        .sort('-x')
        .axis(grid=True),
    alt.Color('year:N')
        .legend(title="Year"),
    alt.Row('site:N')
        .title("")
        .sort(alt.EncodingSortField(field='yield', op='sum', order='descending'))
).properties(
    height=alt.Step(20)
).configure_view(stroke="transparent")
