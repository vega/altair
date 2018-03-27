"""
Streamgraph
-----------------
This example shows the streamgraph from vega-lite examples.
"""

import altair as alt
from vega_datasets import data

source = data.unemployment_across_industries.url

chart = alt.Chart(source).mark_area().encode(
    alt.X('date:T',
        timeUnit = 'yearmonth',
        axis=alt.Axis(format='%Y', domain=False, tickSize=0)
    ),
    alt.Y('sum(count):Q', stack='center', axis=None),
    alt.Color('series:N',
        scale=alt.Scale(scheme='category20b')
    )
).interactive()
