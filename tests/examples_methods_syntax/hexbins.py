"""
Hexbin Chart
------------
This example shows a hexbin chart.
"""
# category: tables
import altair as alt
from vega_datasets import data

source = data.seattle_weather()

# Size of the hexbins
size = 15
# Count of distinct x features
xFeaturesCount = 12
# Count of distinct y features
yFeaturesCount = 7
# Name of the x field
xField = 'date'
# Name of the y field
yField = 'date'

# the shape of a hexagon
hexagon = "M0,-2.3094010768L2,-1.1547005384 2,1.1547005384 0,2.3094010768 -2,1.1547005384 -2,-1.1547005384Z"

alt.Chart(source).mark_point(size=size**2, shape=hexagon).encode(
    alt.X('xFeaturePos:Q')
        .title('Month')
        .axis(grid=False, tickOpacity=0, domainOpacity=0),
    alt.Y('day(' + yField + '):O')
        .title('Weekday')
        .axis(labelPadding=20, tickOpacity=0, domainOpacity=0),
    stroke=alt.value('black'),
    strokeWidth=alt.value(0.2),
    fill=alt.Color('mean(temp_max):Q').scale(scheme='darkblue'),
    tooltip=['month(' + xField + '):O', 'day(' + yField + '):O', 'mean(temp_max):Q']
).transform_calculate(
    # This field is required for the hexagonal X-Offset
    xFeaturePos='(day(datum.' + yField + ') % 2) / 2 + month(datum.' + xField + ')'
).properties(
    # Exact scaling factors to make the hexbins fit
    width=size * xFeaturesCount * 2,
    height=size * yFeaturesCount * 1.7320508076,  # 1.7320508076 is approx. sin(60°)*2
).configure_view(
    strokeWidth=0
)
