"""
Global Deaths from Natural Disasters
------------------------------------
This example shows a proportional symbols visualization of deaths from natural disasters by year and type.
"""
# category: case studies
import altair as alt
from vega_datasets import data

source = data.disasters.url

alt.Chart(source).transform_filter(
    alt.datum.Entity != 'All natural disasters'
).mark_circle(
    opacity=0.8,
    stroke='black',
    strokeWidth=1,
    strokeOpacity=0.4
).encode(
    x=alt.X('Year:O', axis=alt.Axis(labelAngle=0), title=None),
    y=alt.Y(
        'Entity:N',
        sort=alt.EncodingSortField(field="Deaths", op="sum", order='descending'),
        title=None
    ),
    size=alt.Size('Deaths:Q',
        scale=alt.Scale(range=[0, 2500]),
        legend=alt.Legend(title='Deaths')
    ),
    color=alt.Color('Entity:N', legend=None),
    tooltip=["Entity:N", "Year:O", "Deaths:Q"]
).properties(
    width=450,
    height=320,
    title=alt.TitleParams(
        text="Global Deaths from Natural Disasters (1900-2017)",
        subtitle="The size of the bubble represents the total death count per year, by type of disaster",
        anchor='start'
    )
).configure_axis(
    domain=False,
    ticks=False,    
).configure_axisX(
    labelOverlap=True,
).configure_view(
    stroke=None
)
