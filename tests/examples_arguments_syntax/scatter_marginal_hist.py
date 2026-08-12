"""
Scatter Plot with Faceted Marginal Histograms
---------------------------------------------
This example demonstrates how to generate a scatter plot,
with faceted marginal histograms that share their respective x- and y-limits.
"""
# category: distributions
import altair as alt
from altair.datasets import data

source = data.penguins()

base = alt.Chart(source)
base_bar = base.mark_bar(opacity=0.3, binSpacing=0)

xscale = alt.Scale(domain=(170, 235))
yscale = alt.Scale(domain=(2500, 6500))

points = base.mark_circle().encode(
    alt.X("Flipper Length (mm)", scale=xscale),
    alt.Y("Body Mass (g)", scale=yscale),
    color="Species",
)

top_hist = (
    base_bar
    .encode(
        alt.X(
            "Flipper Length (mm):Q",
            # when using bins, the axis scale is set through
            # the bin extent, so we do not specify the scale here
            # (which would be ignored anyway)
            bin=alt.Bin(maxbins=20, extent=xscale.domain),
            stack=None,
            title="",
        ),
        alt.Y("count()", stack=None, title=""),
        alt.Color("Species:N"),
    )
    .properties(height=60)
)

right_hist = (
    base_bar
    .encode(
        alt.Y(
            "Body Mass (g):Q",
            bin=alt.Bin(maxbins=20, extent=yscale.domain),
            stack=None,
            title="",
        ),
        alt.X("count()", stack=None, title=""),
        alt.Color("Species:N"),
    )
    .properties(width=60)
)

top_hist & (points | right_hist)
