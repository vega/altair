"""
Text over a Heatmap
-------------------

An example of a layered chart of text over a heatmap using the cars dataset.
"""
# category: other charts
import altair as alt
from vega_datasets import data

source = data.cars()

# Configure common options
base = alt.Chart(source)
scale = alt.Scale(paddingInner=0)

# Configure heatmap
heatmap = base.mark_rect().encode(
    alt.X('Cylinders:O', scale=scale),
    alt.Y('Origin:O', scale=scale),
    color='count()'
)

# Configure text
text = base.mark_text(baseline='middle').encode(
    x='Cylinders:O',
    y='Origin:O',
    text='count()',
    color=alt.condition(
        alt.datum['count_*'] > 100,
        alt.value('black'),
        alt.value('white')
    )
)

# Draw the chart
heatmap + text
