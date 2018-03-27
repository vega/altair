"""
Layered Plot with Dual-Axis
---------------------------
This example shows how to combine two plots and keep their axes.
"""

import altair as alt
from vega_datasets import data

source = data.seattle_weather()

base = alt.Chart(source).encode(
    alt.X('date:O',
        axis=alt.Axis(format='%b'),
        timeUnit='month',
        scale=alt.Scale(zero=False)
    )
)

bar = base.mark_bar().encode(
    y='mean(precipitation)'
)


line =  base.mark_line(color='red').encode(
    y='mean(temp_max)',
)

chart = (bar + line).resolve_scale(y='independent')
