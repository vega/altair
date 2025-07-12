"""
Line Chart with Stroked Point Markers
-------------------------------------
This example shows a simple line chart with points in a different color.
"""
# category: line charts
import altair as alt
from vega_datasets import data

source = data.stocks()

alt.Chart(source).mark_line(
    point=alt.OverlayMarkDef(filled=False, fill="white")
).encode(
    x='date:T',
    y='price:Q',
    color='symbol:N'
)
