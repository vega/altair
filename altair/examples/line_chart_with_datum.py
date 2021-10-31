"""
Line Chart with XDatum and YDatum
---------------------------------
An example of using ``XDatum`` and ``YDatum`` to highlight certain values, including a ``DateTime`` value.
This is adapted from two corresponding Vega-Lite Examples:
`Highlight a Specific Value <https://vega.github.io/vega-lite/docs/datum.html#highlight-a-specific-data-value>`_.
"""
# category: line charts

import altair as alt
from vega_datasets import data

source = data.stocks()
no_source = alt.InlineData([{}])

lines = alt.Chart(source).mark_line().encode(
    x = alt.X("date"),
    y = alt.Y("price"),
    color = "symbol"
)

xrule = alt.Chart(no_source).mark_rule(color='cyan', strokeWidth=2).encode(
    x=alt.XDatum(alt.DateTime(year=2006, month = "November"))
)

yrule = alt.Chart(no_source).mark_rule(strokeDash=[12,6], size=2).encode(
    y = alt.YDatum(350)
)


lines + yrule + xrule