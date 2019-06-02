"""
Violinplot
----------
This example shows how to make a king of a Violinplot.
"""
# category: other charts
import altair as alt
from altair import datum
from vega_datasets import data

source = data.cars()

alt.Chart(source).transform_filter(
    datum.Miles_per_Gallon > 0
).transform_bin(
    ['bin_max', 'bin_min'], field='Miles_per_Gallon', bin=alt.Bin(maxbins=20)
).transform_calculate(
    binned=(datum.bin_max + datum.bin_min) / 2
).transform_aggregate(
    value_count='count()', groupby=['Origin', 'binned']
).transform_impute(
    impute='value_count', groupby=['Origin'], key='binned', value=0
).mark_area(
    interpolate='monotone',
    orient='horizontal'
).encode(
    x=alt.X(
        'value_count:Q',
        title=None,
        stack='center',
        axis=alt.Axis(labels=False, values=[0],grid=False, ticks=True),
    ),
    y=alt.Y('binned:Q', bin='binned', title='Miles per Gallon'),
    color=alt.Color('Origin:N', legend=None),
    column=alt.Column(
        'Origin:N',
        header=alt.Header(
            titleOrient='bottom',
            labelOrient='bottom',
            labelPadding=0,
        ),
    ),
).properties( 
    width=80 
).configure_facet(
    spacing=0
).configure_view(
    stroke=None
)
