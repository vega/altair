"""
Dot Dash Plot
=============
This example shows how to make a dot-dash plot presented in Edward Tufte's book Visual Display of Quantitative Information on page 133. This example is based on g3o2’s Block bd4362574137061c243a2994ba648fb8
"""

import altair as alt
from vega_datasets import data

cars = data.cars()

points = alt.Chart(cars).mark_point().encode(
    x=alt.X('Miles_per_Gallon',axis=alt.Axis(title='')), 
    y=alt.Y('Horsepower',axis=alt.Axis(title='')), 
    color='Origin'
)

x_ticks = alt.Chart(cars).mark_tick().encode(
    x=alt.X('Miles_per_Gallon',axis=alt.Axis(labels=False, 
                                             domain=False, 
                                             ticks=False)), 
    y=alt.Y('Origin',axis=alt.Axis(labels=False, 
                                   domain=False, 
                                   ticks=False,
                                   title='')), 
    color='Origin'
)

y_ticks = alt.Chart(cars).mark_tick().encode(
    y=alt.Y('Horsepower',axis=alt.Axis(labels=False, 
                                       domain=False,
                                       ticks=False)), 
    x=alt.X('Origin',axis=alt.Axis(labels=False, 
                                   domain=False, 
                                   ticks=False,
                                   title='')), 
    color='Origin'
)

chart = alt.hconcat(y_ticks, alt.vconcat(points, x_ticks))