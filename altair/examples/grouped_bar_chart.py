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
    # The field used to define the subelements of each group
    x=alt.X(
        'year:N',
        axis=alt.Axis(title="")
    ),
    # The length of the bars
    y=alt.Y(
        'yield:Q',
        axis=alt.Axis(grid=False)
    ),
    color='year:N',
    # The field used to group the subelements
    column='variety'
).configure_view(
    stroke='transparent'  # Remove the trellis frames so multiple charts appear as one.
).transform_filter(
    alt.datum.site == 'Morris'
)
