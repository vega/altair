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

# We do not want to specify the exact axis manually,
# and ``alt.Bin`` expects a range, rather than a ``alt.Scale`` instance.
xscale = alt.Scale(padding=1, zero=False)
yscale = alt.Scale(padding=1, zero=False)
xlim = xscale.domain
ylim = yscale.domain

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
