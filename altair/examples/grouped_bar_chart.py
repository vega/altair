"""
Grouped Bar Chart
-----------------
This example shows a grouped bar chart achieved by making cosmetic changes to a trellis plot.
"""
# category: bar charts
import altair as alt
from vega_datasets import data

source = data.barley()

alt.Chart(source).mark_bar().encode(
    x=alt.X(
        'yield:Q',
        axis=alt.Axis(grid=False)
    ),
    y=alt.Y(
        'year:N',
        axis=alt.Axis(title="")
    ),
    color='year:N',
    row='variety:N'
).configure_view(
    stroke='transparent'  # Removes trellis frames so multiple charts appear as one
).transform_filter(
    alt.datum.site == 'Morris'
)
