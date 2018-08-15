"""
Box Plot with Min/Max Whiskers
------------------------------
This example shows how to make a basic box plot using US Population
data from 2000.

https://vega.github.io/vega-lite/examples/box-plot_minmax_2D_vertical_normalized.html
"""
# category: bar charts
import altair as alt
from vega_datasets import data

population = data.population.url

# Define aggregate fields
lower_box = 'q1(people):Q'
lower_whisker = 'min(people):Q'
upper_box = 'q3(people):Q'
upper_whisker = 'max(people):Q'

# Compose each layer individually
lower_plot = alt.Chart(population).mark_rule().encode(
    y=alt.Y(lower_whisker, axis=alt.Axis(title="population")),
    y2=lower_box,
    x='age:O'
)

middle_plot = alt.Chart(population).mark_bar(size=5.0).encode(
    y=lower_box,
    y2=upper_box,
    x='age:O'
)

upper_plot = alt.Chart(population).mark_rule().encode(
    y=upper_whisker,
    y2=upper_box,
    x='age:O'
)

middle_tick = alt.Chart(population).mark_tick(
    color='white',
    size=5.0
).encode(
    y='median(people):Q',
    x='age:O',
)

lower_plot + middle_plot + upper_plot + middle_tick
