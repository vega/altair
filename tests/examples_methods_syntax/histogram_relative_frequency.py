"""
Relative Frequency Histogram
----------------------------
This example shows a histogram of car horsepower where the height of each bar is the
share of all cars in that bin, instead of the number of cars. Each car gets a weight of
1 divided by the total number of cars (added to every row with a joinaggregate
transform), and each bar is the sum of the weights in its bin. Cars without a horsepower
value are filtered out first, so the bars add up to 100%.

Adapted from `Relative Frequency Histogram <https://vega.github.io/vega-lite/examples/histogram_rel_freq.html>`_.
"""
# category: distributions
import altair as alt
from altair.datasets import data

source = data.cars.url

alt.Chart(source).mark_bar().encode(
    alt.X("Horsepower:Q").bin(),
    alt.Y("sum(weight):Q").axis(format=".0%").title("Relative Frequency"),
).transform_filter(
    "isValid(datum.Horsepower)"
).transform_joinaggregate(
    total="count()"
).transform_calculate(
    weight="1 / datum.total"
)
