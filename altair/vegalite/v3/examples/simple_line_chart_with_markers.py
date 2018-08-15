"""
Simple Line Chart with Markers
------------------------------
This chart shows the most basic line chart with markers, made from a dataframe with two
columns.
"""
# category: simple charts

import altair as alt
import numpy as np
import pandas as pd

x = np.arange(100)
data = pd.DataFrame({'x': x,
                     'sin(x)': np.sin(x / 5)})

alt.Chart(data).mark_line(point=True).encode(
    x='x',
    y='sin(x)'
)
