'''
US Population Pyramid Over Time
===============================
A population pyramid shows the distribution of age groups within a population.
It uses a slider widget that is bound to the year to visualize the age
distribution over time.
'''
# category: case studies
import altair as alt
from vega_datasets import data

source = data.population.url

slider = alt.binding_range(min=1850, max=2000, step=10)
select_year = alt.selection_point(name="year", fields=["year"], bind=slider, value=2000)

sex = alt.datum.sex
male = sex == 1
female = sex == 2

x = alt.X("sum(people):Q").title("population")
color = (
    alt.Color("Sex:N")
    .scale(domain=["Male", "Female"], range=["#1f77b4", "#e377c2"])
    .legend(None)
)

base = (
    alt.Chart(source)
    .encode(y=alt.Y("age:O").axis(None))
    .add_params(select_year)
    .transform_filter(select_year)
    .transform_calculate(Sex=alt.expr.if_(male, "Male", "Female"))
    .properties(width=250)
)
bar = base.encode(color=color).mark_bar()

left = (
    bar.transform_filter(female)
    .encode(x=x.sort("descending"))
    .properties(title="Female")
)
middle = base.encode(text=alt.Text("age:Q")).mark_text().properties(width=20)
right = bar.transform_filter(male).encode(x=x).properties(title="Male")

alt.concat(left, middle, right, spacing=5)