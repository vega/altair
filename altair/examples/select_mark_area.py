"""
Using Selection Interval with mark_area
=========================================

Because area is considered one object, just using the plain 
selector will select the entire area instead of just one part of it.

This example shows how to use two areas, one on top of the other, and a
`transform_filter` to fake out this effect.

"""
# category: interactive charts
import altair as alt
from vega_datasets import data

unemp = data.unemployment_across_industries.url

brush = alt.selection_interval(encodings=['x'],empty='all')

base = alt.Chart(unemp).mark_area(color='goldenrod',opacity=.3).encode(
    x=alt.X('date:T', timeUnit='yearmonth'),
    y=alt.Y('sum(count):Q')
)

selected = base.transform_filter(brush).mark_area(color='goldenrod')
alt.layer(base.add_selection(brush), selected)
