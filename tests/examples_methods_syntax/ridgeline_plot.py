"""
Ridgeline plot
--------------
A `Ridgeline plot <https://serialmentor.com/blog/2017/9/15/goodbye-joyplots>`_
lets you visualize distribution of a numeric value for different
subsets of data (what we call "facets" in Altair).

Such a chart can be created in Altair by first transforming the data into a
suitable representation.
"""
# category: distributions
import altair as alt
from vega_datasets import data

source = data.seattle_weather.url

step = 20
overlap = 1

alt.Chart(source, height=step).transform_timeunit(
    Month='month(date)'
).transform_joinaggregate(
    mean_temp='mean(temp_max)', groupby=['Month']
).transform_bin(
    ['bin_max', 'bin_min'], 'temp_max'
).transform_aggregate(
    value='count()', groupby=['Month', 'mean_temp', 'bin_min', 'bin_max']
).transform_impute(
    impute='value', groupby=['Month', 'mean_temp'], key='bin_min', value=0
).mark_area(
    interpolate='monotone',
    fillOpacity=0.8,
    stroke='lightgray',
    strokeWidth=0.5
).encode(
    alt.X('bin_min:Q')
        .bin('binned')
        .title('Maximum Daily Temperature (C)'),
    alt.Y('value:Q')
        .axis(None)
        .scale(range=[step, -step * overlap]),
    alt.Fill('mean_temp:Q')
        .legend(None)
        .scale(domain=[30, 5], scheme='redyellowblue')
).facet(
    row=alt.Row('Month:T')
        .title(None)
        .header(labelAngle=0, labelAlign='left', format='%B')
).properties(
    title='Seattle Weather',
    bounds='flush'
).configure_facet(
    spacing=0
).configure_view(
    stroke=None
).configure_title(
    anchor='end'
)
