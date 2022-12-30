"""
Grouped Bar Chart with xOffset
------------------------------
Like :ref:`gallery_grouped_bar_chart`, this example shows a grouped bar chart.  Whereas :ref:`gallery_grouped_bar_chart` used the ``column`` encoding channel, this example uses the ``xOffset`` encoding channel.  This is adapted from a corresponding Vega-Lite Example:
`Grouped Bar Chart <https://vega.github.io/vega-lite/examples/bar_grouped.html>`_.
"""
# category: bar charts
import altair as alt
import pandas as pd

source = pd.DataFrame({"Category":list("AAABBBCCC"),
                     "Group":list("xyzxyzxyz"),
                     "Value":[0.1, 0.6, 0.9, 0.7, 0.2, 1.1, 0.6, 0.1, 0.2]})

alt.Chart(source).mark_bar().encode(
    x="Category:N",
    y="Value:Q",
    xOffset="Group:N",
    color="Group:N"
)
