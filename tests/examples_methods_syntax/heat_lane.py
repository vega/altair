"""
Heat Lane Chart
---------------
This example shows how to make an alternative form of a histogram `designed at Google <https://www.smashingmagazine.com/2022/07/accessibility-first-approach-chart-visual-design/>`_ with the goal of increasing accessibility.
"""
# category: distributions
import altair as alt
from vega_datasets import data

source = data.cars.url

chart = alt.Chart(source, title="Car horsepower", height=100, width=300).encode(
    alt.X("bin_Horsepower_start:Q")
        .title("Horsepower")
        .axis(grid=False),
    alt.X2("bin_Horsepower_end:Q"),
    alt.Y("y:O").axis(None),
    alt.Y2("y2"),
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
    alt.Color("max_bin_count_end:O")
        .title("Number of models")
        .scale(scheme="lighttealblue")
)
layer2 = chart.mark_bar(xOffset=1, x2Offset=-1, yOffset=-3, y2Offset=3).encode(
    alt.Color("bin_count_end:O").title("Number of models")
)

layer1 + layer2
