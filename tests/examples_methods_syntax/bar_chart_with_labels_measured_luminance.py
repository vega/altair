"""
Bar Chart with Labels based on Measured Luminance
=================================================
This example shows a basic horizontal bar chart with labels where the measured luminance to decides if the text overlay is be colored ``black`` or ``white``.
"""
# category: bar charts
import altair as alt
from vega_datasets import data

source = data.barley()

base = alt.Chart(source).encode(
    x=alt.X('sum(yield):Q').stack('zero'),
    y=alt.Y('site:O').sort('-x'),
    text=alt.Text('sum(yield):Q', format='.0f')
)

bars = base.mark_bar(
    tooltip=alt.expr("luminance(scale('color', datum.sum_yield))")
).encode(
    color='sum(yield):Q'
)

text = base.mark_text(
    align='right',
    dx=-3,
    color=alt.expr("luminance(scale('color', datum.sum_yield)) > 0.5 ? 'black' : 'white'")
)

bars + text
