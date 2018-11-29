"""
Horizontal Grouped Bar Chart
----------------------------
This example shows a horizontal grouped bar chart achieved by making cosmetic changes to a trellis plot.
"""
# category: bar charts
import altair as alt
from vega_datasets import data

source = data.barley()

alt.Chart(source).mark_bar().encode(
    # The length of the bars
    x=alt.X(
        'yield:Q',
        axis=alt.Axis(grid=False)
    ),
    # The field used to define the subelements of each group
    y=alt.Y(
        'year:N',
        axis=alt.Axis(title="")
    ),
    color='year:N',
    # The field used to group the subelements
    row='variety'
).configure_view(
    stroke='transparent'  # Remove the trellis frames so multiple charts appear as one.
).transform_filter(
    alt.datum.site == 'Morris'
)
