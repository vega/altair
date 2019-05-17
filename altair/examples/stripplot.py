"""
Stripplot
-----------------
This example shows how to make a Stripplot.
"""
# category: scatter plots
import altair as alt
from vega_datasets import data

source = data.movies()

stripplot = (
    alt.Chart(source, width=40)
    .mark_circle(size=8)
    .encode(
        alt.X(
            shorthand="jitter:Q",
            title=None,
            axis=alt.Axis(values=[0], ticks=True, grid=False, labels=False),
            scale=alt.Scale(),
        ),
        alt.Y("IMDB_Rating"),
        alt.Color("Major_Genre", legend=None),
        alt.Column(
            "Major_Genre",
            header=alt.Header(
                labelAngle=-90,
                titleOrient="top",
                labelOrient="bottom",
                labelAlign="right",
                labelPadding=3,
            ),
        ),
    )
    .transform_calculate(jitter="pow(random()-0.5,3)")
    .configure_facet(spacing=0)
    .configure_view(stroke=None)
)
stripplot
