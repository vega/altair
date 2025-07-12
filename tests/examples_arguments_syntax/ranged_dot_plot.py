"""
Ranged Dot Plot
---------------
This example shows a ranged dot plot to convey changing life expectancy for the five most populous countries (between 1955 and 2000).
"""
# category: advanced calculations
import altair as alt
from vega_datasets import data

source = data.countries.url

chart = (
    alt.Chart(source)
    .encode(x="life_expect:Q", y="country:N")
    .transform_filter(
        alt.FieldOneOfPredicate(
            field="country",
            oneOf=["China", "India", "United States", "Indonesia", "Brazil"],
        )
    )
    .transform_filter(alt.FieldOneOfPredicate(field="year", oneOf=[1955, 2000]))
)

line = chart.mark_line(color="#db646f").encode(detail="country:N")

# Add points for life expectancy in 1955 & 2000
color = alt.Color(
    "year:O", scale=alt.Scale(domain=[1955, 2000], range=["#e6959c", "#911a24"])
)
points = (
    chart.mark_point(
        size=100,
        opacity=1,
        filled=True,
    )
    .encode(color=color)
    .interactive()
)

(line + points)
