"""
US Population by Age and Sex
============================
This chart visualizes the age distribution of the US population over time.
It uses a slider widget that is bound to the year to visualize the age
distribution over time.
"""
# category: case studies
import altair as alt
from vega_datasets import data

source = data.population.url

select_year = alt.selection_point(
    name="Year",
    fields=["year"],
    bind=alt.binding_range(min=1900, max=2000, step=10, name="Year"),
    init={"year": 2000},
)

alt.Chart(source).mark_bar().encode(
    x=alt.X("sex:N", axis=alt.Axis(labels=False, title=None, ticks=False)),
    y=alt.Y("people:Q", scale=alt.Scale(domain=(0, 12000000)), title="Population"),
    color=alt.Color(
        "sex:N",
        scale=alt.Scale(domain=("Male", "Female"), range=["steelblue", "salmon"]),
        title="Sex",
    ),
    column=alt.Column("age:O", title="Age"),
).properties(
    width=20,
    title="U.S. Population by Age and Sex"
).add_params(
    select_year
).transform_calculate(
    "sex", alt.expr.if_(alt.datum.sex == 1, "Male", "Female")
).transform_filter(
    select_year
).configure_facet(
    spacing=8
)
