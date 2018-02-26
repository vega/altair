"""
Streamgraph
-----------------
This example shows the steamgraph from vega-lite examples.
"""

import altair as alt
from vega_datasets import data

source = data.unemployment_across_industries()


chart = alt.Chart(source).mark_area().encode(
    x = alt.X('date:T', timeUnit = 'yearmonth',
              axis=alt.Axis(format='%Y', domain = False, tickSize = 0)),
    y = alt.Y('sum(count)', stack = 'center', axis = None),
    color = alt.Color('series', scale=alt.Scale(scheme='category20b'))
    ).interactive()
