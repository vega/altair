"""
Line Chart with Points
----------------------
This chart shows a simple line chart with points marking each value. Use
``point=True`` for points with default appearance or customize it with
``OverlayMarkDef()``.
"""
# category: line charts
import altair as alt
from vega_datasets import data

source = data.wheat()

alt.Chart(source).mark_line(
    point=alt.OverlayMarkDef(color="red")
).encode(
    x='year:O',
    y='wheat:Q'
).properties(width=600)
