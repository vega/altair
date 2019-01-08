"""
Scatter Plots with alternate Y axis scale
---------------------------------
A few examples that make use of alternate Y axis scales.
"""
# category: simple charts

import altair as alt
import numpy as np
import pandas as pd

chart_df = pd.DataFrame(
    {
        'x': list(range(0,20)),
        'y': [2** x for x in range(0,20)],
    }
)
base_chart =  alt.Chart(chart_df).mark_line().encode(
    x=alt.X('x', type='quantitative'),
).properties(
    height=200,
    width=200,
)
chart1 = base_chart.encode(
    y=alt.Y('y', type='quantitative'),
).properties(title='linear')
chart2 = base_chart.encode(
    y=alt.Y('y', type='quantitative', scale=alt.Scale(type='log', base=2)),
).properties(title='log base 2')
chart3 = base_chart.encode(
    y=alt.Y('y', type='quantitative', scale=alt.Scale(type='log', base=np.e)),
).properties(title='log base e')
chart4 = base_chart.encode(
    y=alt.Y('y', type='quantitative', scale=alt.Scale(type='log')),
).properties(title='log base 10')
display(chart1 | chart2 | chart3 | chart4)
