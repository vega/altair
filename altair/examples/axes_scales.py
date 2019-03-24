"""
Controlling Axis Scale
----------------------
A few examples that make use of alternate Y axis scales.
"""
# category: other charts

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
    x=alt.X('x:Q'),
).properties(
    height=200,
    width=200,
)

chart_linear = base_chart.encode(
    y=alt.Y('y:Q'),
).properties(title='linear')

chart_base_2 = base_chart.encode(
    y=alt.Y('y:Q', scale=alt.Scale(type='log', base=2)),
).properties(title='log base 2')

chart_base_e = base_chart.encode(
    y=alt.Y('y:Q', scale=alt.Scale(type='log', base=np.e)),
).properties(title='log base e')

chart_base_10 = base_chart.encode(
    y=alt.Y('y:Q', scale=alt.Scale(type='log')),
).properties(title='log base 10')

(chart_linear | chart_base_2) & (chart_base_e | chart_base_10)
