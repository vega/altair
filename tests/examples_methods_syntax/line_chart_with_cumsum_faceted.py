"""
Faceted Line Chart with Cumulative Sum
------------------------------
This chart creates multiple line subcharts from the cumulative sum of a field, one for each category.
"""
# category: line charts
import altair as alt
from vega_datasets import data

source = data.disasters()
columns_sorted = ['Drought', 'Epidemic', 'Earthquake', 'Flood']

alt.Chart(source).mark_line(
    interpolate='basis' # Use linear interpolation with B-spline method
).encode( 
    alt.X('Year:Q', title=None).axis(format='d'),
    alt.Y('cumulative:Q', title=None),
    alt.Color('Entity:N', legend=None)
).properties(width=300, height=150).facet(
    facet=alt.Facet(
        'Entity:N',
        title=None,
        sort=columns_sorted,
        header=alt.Header(labelAnchor='start', labelFontStyle='italic')
    ),
    title={
        'text': ['Cumulative casualties by type of disaster', 'in the 20th century'],
        'anchor': 'middle'
    },
    columns=2
).resolve_scale(y='independent').transform_filter(
    {'and': [
        alt.FieldOneOfPredicate(field='Entity', oneOf=columns_sorted), # Filter data to show only disasters in columns_sorted
        alt.FieldRangePredicate(field='Year', range=[1900, 2000]) # Filter data to show only 20th century
    ]}
).transform_window(cumulative='sum(Deaths)', groupby=['Entity']) # Calculate cumulative sum of Deaths by Entity and name it cumulative