"""
Facetted Scatterplot with marginal histograms
---------------------------------------------
This example demonstrates how to generate a facetted scatterplot,
with marginal facetted histograms, and how to share their respective
- x,some y-limits.
"""
# category: other charts
import altair as alt
from vega_datasets import data

source = data.iris()

base = alt.Chart(source)

xscale = alt.Scale(domain=(4.0, 8.0))
yscale = alt.Scale(domain=(1.9, 4.55))

area_args = {'opacity': .3, 'interpolate': 'step'}
blank_axis = alt.Axis(title='')

points = base.mark_circle().encode(
    alt.X('sepalLength', scale=xscale),
    alt.Y('sepalWidth', scale=yscale),
    color='species',
)

top_hist = base.mark_area(**area_args).encode(
    alt.X('sepalLength:Q',
          # when using bins, the axis scale is set through
          # the bin extent, so we do not specify the scale here
          # (which would be ignored anyway)
          bin=alt.Bin(maxbins=20, extent=xscale.domain),
          stack=None,
          axis=blank_axis,
         ),
    alt.Y('count()', stack=None, axis=blank_axis),
    alt.Color('species:N'),
).properties(height=60)

right_hist = base.mark_area(**area_args).encode(
    alt.Y('sepalWidth:Q',
          bin=alt.Bin(maxbins=20, extent=yscale.domain),
          stack=None,
          axis=blank_axis,
         ),
    alt.X('count()', stack=None, axis=blank_axis),
    alt.Color('species:N'),
).properties(width=60)

top_hist & (points | right_hist)
