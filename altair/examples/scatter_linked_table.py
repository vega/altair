"""
Brushing Scatter Plot to Show Data on a Table
---------------------------------------------
A scatter plot of the cars dataset, with data tables for horsepower, MPG, and origin.
The tables update to reflect the selection on the scatter plot.
"""
# category: scatter plots

import altair as alt
from vega_datasets import data

source = data.cars()

# Brush for selection
brush = alt.selection_interval()

# Scatter Plot
points = alt.Chart(source).mark_point().encode(
    x='Horsepower:Q',
    y='Miles_per_Gallon:Q',
    color=alt.condition(brush, alt.value('steelblue'), alt.value('grey'))
).add_params(brush)

# Base chart for data tables
ranked_text = alt.Chart(source).mark_text(align='right').encode(
    y=alt.Y('row_number:O').axis(None)
).transform_filter(
    brush
).transform_window(
    row_number='row_number()'
).transform_filter(
    'datum.row_number < 15'
)

# Data Tables
horsepower = ranked_text.encode(text='Horsepower:N').properties(
    title=alt.TitleParams(text='Horsepower', align='right')
)
mpg = ranked_text.encode(text='Miles_per_Gallon:N').properties(
    title=alt.TitleParams(text='MPG', align='right')
)
origin = ranked_text.encode(text='Origin:N').properties(
    title=alt.TitleParams(text='Origin', align='right')
)
text = alt.hconcat(horsepower, mpg, origin) # Combine data tables

# Build chart
alt.hconcat(
    points,
    text
).resolve_legend(
    color="independent"
).configure_view(
    stroke=None
)
