"""
Layered Plot with Dual-Axis
-----------------------
This example shows how to combine two plots and keep their axes.
"""

import altair as alt
from vega_datasets import data

source = data.seattle_weather()

bar = alt.Chart(source).mark_bar().encode(
    x = alt.X('date:O', axis = alt.Axis(format = '%b'), timeUnit = 'month',
             scale = alt.Scale(zero=False)),
    y = 'mean(precipitation)')


line = alt.Chart(source).mark_line(color = 'red').encode(
    x = alt.X('date:O', axis = alt.Axis(format = '%b'), timeUnit = 'month',
             scale = alt.Scale(zero=False)),
    #y = alt.Y('mean(temp_max)', resolveMode = 'independent'))
    y = 'mean(temp_max)')


chart = line + bar
