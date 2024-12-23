"""
Comet Chart
-----------
Inspired by `Zan Armstrong's comet chart <https://www.zanarmstrong.com/infovisresearch>`_
this plot uses ``mark_trail`` to visualize change of grouped data over time.
A more elaborate example and explanation of creating comet charts in Altair
is shown in `this blogpost <https://medium.com/de-dataverbinders/comet-charts-in-python-visualizing-statistical-mix-effects-and-simpsons-paradox-with-altair-6cd51fb58b7c>`_.
"""
# category: advanced calculations

import altair as alt
import vega_datasets

alt.Chart(
    vega_datasets.data.barley.url,
    title='Barley Yield comparison between 1932 and 1931'
).mark_trail().encode(
    alt.X('year:O').title(None),
    alt.Y('variety:N').title('Variety'),
    alt.Size('yield:Q')
        .scale(range=[0, 12])
        .legend(values=[20, 60])
        .title('Barley Yield (bushels/acre)'),
    alt.Color('delta:Q')
        .scale(domainMid=0)
        .title('Yield Delta (%)'),
    alt.Tooltip(['year:O', 'yield:Q']),
    alt.Column('site:N').title('Site')
).transform_pivot(
    "year",
    value="yield",
    groupby=["variety", "site"]
).transform_fold(
    ["1931", "1932"],
    as_=["year", "yield"]
).transform_calculate(
    calculate="datum['1932'] - datum['1931']",
    as_="delta"
).configure_legend(
    orient='bottom',
    direction='horizontal'
).configure_view(
    stroke=None
)
