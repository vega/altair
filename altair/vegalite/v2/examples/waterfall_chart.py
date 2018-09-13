"""
Waterfall Chart
-----------------
This example shows how to make a simple waterfall chart.
"""
# category: bar charts
import altair as alt
import pandas as pd
from altair import datum

data = pd.DataFrame([
    {"Fixed costs": 5,
     "Advertising costs": 3,
     "Other costs": 2},
])

data_waterfall = data.melt()

data_waterfall['start'] = data_waterfall.value.cumsum().shift().fillna(0)
data_waterfall['end'] = data_waterfall.value.cumsum()
data_waterfall.drop(['value'], axis=1, inplace=True)

data_waterfall = data_waterfall.append(
                    {'variable': 'Total costs',
                     'start': 0,
                     'end': max(data_waterfall['end'])
                     }, ignore_index=True)

waterfall_bars = alt.Chart(data_waterfall).mark_bar(size=100).encode(
    y2=alt.Y2('end:Q'),
    y=alt.Y('start:Q', axis=alt.Axis(grid=False)),
    x=alt.X('variable:N')
)

ticks = alt.Chart(data_waterfall).mark_tick(
    color="grey",
    size=150,
    xOffset=100
).encode(
    y='end:Q',
    x='variable:N'
).transform_filter(
    datum.variable != "Total costs"
)

(waterfall_bars+ticks).configure_axisX(
    labelAngle=0
).properties(
    width=500
)
