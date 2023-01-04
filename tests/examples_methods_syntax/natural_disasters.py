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
    alt.X('Year:T')
        .title(None)
        .scale(domain=['1899','2018']),
    alt.Y('Entity:N')
        .title(None)
        .sort(field="Deaths", op="sum", order='descending'),
    alt.Size('Deaths:Q')
        .scale(range=[0, 2500])
        .title('Deaths')
        .legend(clipHeight=30, format='s'),
    alt.Color('Entity:N').legend(None),
    tooltip=[
        "Entity:N",
        alt.Tooltip("Year:T", format='%Y'),
        alt.Tooltip("Deaths:Q", format='~s')
    ],
).properties(
    width=450,
    height=320,
    title=alt.TitleParams(
        text="Global Deaths from Natural Disasters (1900-2017)",
        subtitle="The size of the bubble represents the total death count per year, by type of disaster",
        anchor='start'
    )
).configure_axisY(
    domain=False,
    ticks=False,
    offset=10
).configure_axisX(
    grid=False,
).configure_view(
    stroke=None
)
