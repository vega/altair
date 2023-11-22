"""
Scatter Plot with Faceted Marginal Histograms
---------------------------------------------
This example demonstrates how to generate a scatter plot,
with faceted marginal histograms that share their respective x- and y-limits.
"""
# category: distributions
import altair as alt
from vega_datasets import data

source = data.iris()

base = alt.Chart(source)
base_bar = base.mark_bar(opacity=0.3, binSpacing=0)

xscale = alt.Scale(domain=(4.0, 8.0))
yscale = alt.Scale(domain=(1.9, 4.55))

points = base.mark_circle().encode(
    alt.X("sepalLength", scale=xscale),
    alt.Y("sepalWidth", scale=yscale),
    color="species",
)

top_hist = (
    base_bar
    .encode(
        alt.X(
            "sepalLength:Q",
            # when using bins, the axis scale is set through
            # the bin extent, so we do not specify the scale here
            # (which would be ignored anyway)
            bin=alt.Bin(maxbins=20, extent=xscale.domain),
            stack=None,
            title="",
        ),
        alt.Y("count()", stack=None, title=""),
        alt.Color("species:N"),
    )
    .properties(height=60)
)

right_hist = (
    base_bar
    .encode(
        alt.Y(
            "sepalWidth:Q",
            bin=alt.Bin(maxbins=20, extent=yscale.domain),
            stack=None,
            title="",
        ),
        alt.X("count()", stack=None, title=""),
        alt.Color("species:N"),
    )
    .properties(width=60)
)

top_hist & (points | right_hist)
