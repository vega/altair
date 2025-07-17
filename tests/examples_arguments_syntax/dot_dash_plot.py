"""
Dot Dash Plot
=============
How to make the dot-dash plot presented in Edward Tufte's `Visual Display of Quantitative Information <https://www.edwardtufte.com/tufte/books_vdqi>`_. Based
on a JavaScript implementation by `g3o2 <https://bl.ocks.org/g3o2/bd4362574137061c243a2994ba648fb8>`_.
"""
# category: distributions
import altair as alt
from altair.datasets import data

source = data.cars()

# Configure the options common to all layers
brush = alt.selection_interval()
brush_origin = alt.when(brush).then("Origin")
base = alt.Chart(source).add_params(brush)

# Configure the points
points = base.mark_point().encode(
    x=alt.X('Miles_per_Gallon', title=''),
    y=alt.Y('Horsepower', title=''),
    color=brush_origin.otherwise(alt.value("grey")),
)

# Configure the ticks
tick_axis = alt.Axis(labels=False, domain=False, ticks=False)
tick_color = brush_origin.otherwise(alt.value("lightgrey"))

x_ticks = base.mark_tick().encode(
    alt.X('Miles_per_Gallon', axis=tick_axis),
    alt.Y('Origin', title='', axis=tick_axis),
    color=tick_color
)

y_ticks = base.mark_tick().encode(
    alt.X('Origin', title='', axis=tick_axis),
    alt.Y('Horsepower', axis=tick_axis),
    color=tick_color
)

# Build the chart
y_ticks | (points & x_ticks)
