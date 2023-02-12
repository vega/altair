"""
Heat Lane Chart
---------------
This example shows how to make an alternative form of a histogram designed at Google with accessibility in mind.
"""
# category: distributions
import altair as alt
from vega_datasets import data

source = data.cars.url

chart = alt.Chart(source, title="Car horsepower", height=100, width=300).encode(
    x=alt.X(
        "bin_Horsepower_start:Q",
        title="Horsepower",
        axis=alt.Axis(grid=False)
    ),
    x2="bin_Horsepower_end:Q",
    y=alt.Y("y:O", axis=None),
    y2="y2",
).transform_bin(
    ["bin_Horsepower_start", "bin_Horsepower_end"],
    field='Horsepower'
).transform_aggregate(
    count='count()',
    groupby=["bin_Horsepower_start", "bin_Horsepower_end"]
).transform_bin(
    ["bin_count_start", "bin_count_end"],
    field='count'
).transform_calculate(
    y="datum.bin_count_end/2",
    y2="-datum.bin_count_end/2",
).transform_joinaggregate(
    max_bin_count_end="max(bin_count_end)",
)

layer1 = chart.mark_bar(xOffset=1, x2Offset=-1, cornerRadius=3).encode(
    color=alt.Color("max_bin_count_end:O", scale=alt.Scale(scheme="lighttealblue"), title="Number of models")
)
layer2 = chart.mark_bar(xOffset=1, x2Offset=-1, yOffset=-3, y2Offset=3).encode(
    color=alt.Color("bin_count_end:O", title="Number of models")
)

layer1 + layer2
