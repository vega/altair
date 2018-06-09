"""
US Population Over Time
=======================
This chart visualizes the age distribution of the US population over time.
It uses a slider widget that is bound to the year to visualize the age
distribution over time.
"""
# category: case studies
import altair as alt
from altair.expr import datum, if_
from vega_datasets import data

pop = data.population.url

pink_blue = alt.Scale(domain=('Male', 'Female'),
                      range=["steelblue", "salmon"])

slider = alt.binding_range(min=1900, max=2000, step=10)
select_year = alt.selection_single(name="year", fields=['year'], bind=slider)

alt.Chart(pop).mark_bar().encode(
    x=alt.X('sex:N', axis=alt.Axis(title=None)),
    y=alt.Y('people:Q', scale=alt.Scale(domain=(0, 12000000))),
    color=alt.Color('sex:N', scale=pink_blue),
    column='age:O'
).properties(
    width=20
).add_selection(
    select_year
).transform_calculate(
    "sex", if_(datum.sex == 1, "Male", "Female")
).transform_filter(
    select_year
)
