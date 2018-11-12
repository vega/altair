"""
Dot Dash Plot
=============
How to make the dot-dash plot presented in Edward Tufte's `Visual Display of Quantitative Information <https://www.edwardtufte.com/tufte/books_vdqi>`_. Based
on a JavaScript implementation by `g3o2 <https://bl.ocks.org/g3o2/bd4362574137061c243a2994ba648fb8>`_.
"""
# category: scatter plots
import altair as alt
from vega_datasets import data

source = data.cars()

# Configure the options common to all layers
brush = alt.selection(type='interval')
base = alt.Chart(source).add_selection(brush)

# Configure the points
points = base.mark_point().encode(
    x=alt.X('Miles_per_Gallon', axis=alt.Axis(title='')),
    y=alt.Y('Horsepower', axis=alt.Axis(title='')),
    color=alt.condition(brush, 'Origin', alt.value('grey'))
)

# Configure the ticks
tick_options = dict(labels=False, domain=False, ticks=False)
tick_axis = alt.Axis(**tick_options)
tick_axis_notitle = alt.Axis(title='', **tick_options)

x_ticks = base.mark_tick().encode(
    alt.X('Miles_per_Gallon', axis=tick_axis),
    alt.Y('Origin', axis=tick_axis_notitle),
    color=alt.condition(brush, 'Origin', alt.value('lightgrey'))
)

y_ticks = base.mark_tick().encode(
    alt.X('Origin', axis=tick_axis_notitle),
    alt.Y('Horsepower', axis=tick_axis),
    color=alt.condition(brush, 'Origin', alt.value('lightgrey'))
)

# Build the chart
y_ticks | (points & x_ticks)
