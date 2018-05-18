"""
Dot Dash Plot
=============
This example shows how to make a dot-dash plot presented in Edward Tufte's book
Visual Display of Quantitative Information on page 133. This example is based
on https://bl.ocks.org/g3o2/bd4362574137061c243a2994ba648fb8.
"""
# category: scatter plots
import altair as alt
from vega_datasets import data

cars = data.cars()

brush = alt.selection(type='interval')

tick_axis = alt.Axis(labels=False, domain=False, ticks=False)
tick_axis_notitle = alt.Axis(labels=False, domain=False, ticks=False, title='')

points = alt.Chart(cars).mark_point().encode(
    x=alt.X('Miles_per_Gallon', axis=alt.Axis(title='')),
    y=alt.Y('Horsepower', axis=alt.Axis(title='')),
    color=alt.condition(brush, 'Origin', alt.value('grey'))
).add_selection(
    brush
)

x_ticks = alt.Chart(cars).mark_tick().encode(
    alt.X('Miles_per_Gallon', axis=tick_axis),
    alt.Y('Origin', axis=tick_axis_notitle),
    color=alt.condition(brush, 'Origin', alt.value('lightgrey'))
).add_selection(
    brush
)

y_ticks = alt.Chart(cars).mark_tick().encode(
    alt.X('Origin', axis=tick_axis_notitle),
    alt.Y('Horsepower', axis=tick_axis),
    color=alt.condition(brush, 'Origin', alt.value('lightgrey'))
).add_selection(
    brush
)

y_ticks | (points & x_ticks)
