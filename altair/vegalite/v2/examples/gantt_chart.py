"""
Gantt Chart
-----------------
This example shows how to make a simple gantt chart.
"""

import altair as alt
from vega_datasets import data

data = [
      {"task": "A","start": 1, "end": 3},
      {"task": "B","start": 3, "end": 8},
      {"task": "C","start": 8, "end": 10}
       ]

source = alt.pd.DataFrame(data)


chart = alt.Chart(source).mark_bar().encode(
    x = 'start',
    x2 = 'end',
    y = 'task',
)  
chart
