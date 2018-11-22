"""
Box Plot with Min/Max Whiskers
------------------------------
This example shows how to make a basic box plot using US Population data from 2000.
"""
# category: other charts
import altair as alt
from vega_datasets import data

source = data.population()

base = alt.Chart(source)

# Define aggregate fields
lower_box = 'q1(people):Q'
lower_whisker = 'min(people):Q'
upper_box = 'q3(people):Q'
upper_whisker = 'max(people):Q'

# Compose each layer individually
lower_plot = base.mark_rule().encode(
    y=alt.Y(lower_whisker, axis=alt.Axis(title="population")),
    y2=lower_box,
    x='age:O'
)

middle_plot = base.mark_bar(size=5.0).encode(
    y=lower_box,
    y2=upper_box,
    x='age:O'
)

upper_plot = base.mark_rule().encode(
    y=upper_whisker,
    y2=upper_box,
    x='age:O'
)

middle_tick = base.mark_tick(
    color='white',
    size=5.0
).encode(
    y='median(people):Q',
    x='age:O',
)

lower_plot + middle_plot + upper_plot + middle_tick
