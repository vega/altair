# /// script
# requires-python = ">=3.11"
# dependencies = ["altair", "pandas"]
#
# [tool.marimo.display]
# cell_output = "above"
# ///
"""
Relative Frequency Histogram
----------------------------
This example shows a histogram of car horsepower where the height of each bar is the
share of all cars in that bin, instead of the number of cars. Cars without a horsepower
value are filtered out first, so the bars add up to 100%. The data is then binned and
counted, the total count is added to every row with a joinaggregate transform, and the
relative frequency is each bin's count divided by the total.

Adapted from `Relative Frequency Histogram <https://vega.github.io/vega-lite/examples/histogram_rel_freq.html>`_.
"""
# category: distributions
import altair as alt
from altair.datasets import data

source = data.cars.url

alt.Chart(source).mark_bar(tooltip=True).encode(
    x=alt.X(
        "bin_Horsepower:Q", bin=alt.Bin(binned=True, step=20), title="Horsepower"
    ),
    x2="bin_Horsepower_end:Q",
    y=alt.Y(
        "PercentOfTotal:Q",
        axis=alt.Axis(format=".1~%"),
        title="Relative Frequency",
    ),
).transform_filter(
    "isValid(datum.Horsepower)"
).transform_bin(
    "bin_Horsepower", field="Horsepower", bin=alt.Bin(step=20)
).transform_aggregate(
    Count="count()", groupby=["bin_Horsepower", "bin_Horsepower_end"]
).transform_joinaggregate(
    TotalCount="sum(Count)"
).transform_calculate(
    PercentOfTotal="datum.Count / datum.TotalCount"
)
