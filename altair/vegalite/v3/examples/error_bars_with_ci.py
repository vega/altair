"""
Error Bars showing Confidence Interval
======================================
This example shows how to show error bars using confidence intervals.
The confidence intervals are computed internally in vega by
a non-parametric `bootstrap of the mean <https://github.com/vega/vega-statistics/blob/master/src/bootstrapCI.js>`_.
"""
# category: bar charts
import altair as alt
from vega_datasets import data

barley = data.barley()

points = alt.Chart(barley).mark_point(filled=True).encode(
    alt.X(
        'mean(yield)',
        scale=alt.Scale(zero=False),
        axis=alt.Axis(title='Barley Yield')
    ),
    y='variety',
    color=alt.value('black')
)

error_bars = alt.Chart(barley).mark_rule().encode(
    x='ci0(yield)',
    x2='ci1(yield)',
    y='variety'
)

points + error_bars
