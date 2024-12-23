"""
Error Bars with Confidence Interval
======================================
This example shows how to show error bars using confidence intervals.
The confidence intervals are computed internally in vega by a non-parametric
`bootstrap of the mean <https://github.com/vega/vega-statistics/blob/master/src/bootstrapCI.js>`_.
"""
# category: uncertainties and trends
import altair as alt
from vega_datasets import data

source = data.barley()

error_bars = alt.Chart(source).mark_errorbar(extent='ci').encode(
  alt.X('yield').scale(zero=False),
  alt.Y('variety')
)

points = alt.Chart(source).mark_point(filled=True, color='black').encode(
  x=alt.X('mean(yield)'),
  y=alt.Y('variety'),
)

error_bars + points
