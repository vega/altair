"""
Violin Plot
-----------
This example shows how to make a Violin Plot using Altair's density transform.
"""
# category: distributions
import altair as alt
from vega_datasets import data

alt.Chart(data.cars(), width=100).transform_density(
    'Miles_per_Gallon',
    as_=['Miles_per_Gallon', 'density'],
    extent=[5, 50],
    groupby=['Origin']
).mark_area(orient='horizontal').encode(
    alt.X('density:Q')
        .stack('center')
        .impute(None)
        .title(None)
        .axis(labels=False, values=[0], grid=False, ticks=True),
    alt.Y('Miles_per_Gallon:Q'),
    alt.Color('Origin:N'),
    alt.Column('Origin:N')
        .spacing(0)
        .header(titleOrient='bottom', labelOrient='bottom', labelPadding=0)
).configure_view(
    stroke=None
)
