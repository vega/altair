"""
Facetted Scatterplot with marginal histograms
---------------------------------------------
This example demonstrates how to generate a facetted scatterplot,
with marginal facetted histograms, and how to share their respective
- x,some y-limits.
"""

import altair as alt
from vega_datasets import data

iris = data.iris()

xlim = (4.0, 8.0)
ylim = (1.9, 4.55)
xscale = alt.Scale(domain=xlim)
yscale = alt.Scale(domain=ylim)

area_args = {'opacity': .3, 'interpolate': 'step'}
blank_axis = alt.Axis(title='')

points = alt.Chart(iris).mark_circle().encode(
    alt.X('sepalLength', scale=xscale),
    alt.Y('sepalWidth', scale=yscale),
    color='species',
)

top_hist = alt.Chart(iris).mark_area(**area_args).encode(
    alt.X('sepalLength:Q',
          # when using bins, the axis scale is set through
          # the bin extent, so we do not specify the scale here
          # (which would be ignored anyway)
          bin=alt.Bin(maxbins=20, extent=xlim),
          stack=None,
          axis=blank_axis,
         ),
    alt.Y('count(*):Q', stack=None, axis=blank_axis),
    alt.Color('species:N'),
).properties(height=60)

right_hist = alt.Chart(iris).mark_area(**area_args).encode(
    alt.Y('sepalWidth:Q',
          bin=alt.Bin(maxbins=20, extent=ylim),
          stack=None,
          axis=blank_axis,
         ),
    alt.X('count(*):Q', stack=None, axis=blank_axis),
    alt.Color('species:N'),
).properties(width=60)

top_hist & (points | right_hist)
