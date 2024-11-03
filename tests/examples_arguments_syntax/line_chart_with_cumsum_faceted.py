"""
Faceted Line Chart with Cumulative Sum
--------------------------------------
This chart creates one facet per natural disaster and shows the cumulative number of deaths for that category.
Note the use of different predicates to filter based on both a list and a range.
"""
# category: advanced calculations
import altair as alt
from vega_datasets import data

source = data.disasters()
columns_sorted = ['Drought', 'Epidemic', 'Earthquake', 'Flood']

alt.Chart(source).transform_filter(
    alt.FieldOneOfPredicate(field='Entity', oneOf=columns_sorted), 
    alt.FieldRangePredicate(field='Year', range=[1900, 2000])
).transform_window(
    cumulative_deaths='sum(Deaths)', groupby=['Entity'] # Calculate cumulative sum of Deaths by Entity
).mark_line().encode( 
    alt.X('Year:Q', title=None, axis=alt.Axis(format='d')),
    alt.Y('cumulative_deaths:Q', title=None),
    alt.Color('Entity:N', legend=None)
).properties(
    width=300,
    height=150
).facet(
    facet=alt.Facet(
        'Entity:N',
        title=None,
        sort=columns_sorted,
        header=alt.Header(labelAnchor='start', labelFontStyle='italic')
    ),
    title=alt.Title(
        text=['Cumulative casualties by type of disaster', 'in the 20th century'],
        anchor='middle'
    ),
    columns=2
).resolve_axis(y='independent', x='independent')