"""
Horizontal Stacked Bar Chart
============================
This is an example of a horizontal stacked bar chart using data which contains crop yields over different regions and different years in the 1930s.

The segments in each bar are ordered by the :class:`Order` configuration submitted to the encoder as an override to the default settings.
"""
# category: basic charts

import altair as alt
from vega_datasets import data

barley = data.barley()

alt.Chart(barley).mark_bar().encode(
    x='sum(yield)',
    y='variety',
    color='site',
    order=alt.Order('site', sort='ascending')
)
