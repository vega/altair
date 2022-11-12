"""
Text over a Heatmap
-------------------

An example of a layered chart of text over a heatmap using the cars dataset.
"""
# category: tables
import altair as alt
from vega_datasets import data

source = data.cars()

# Configure common options. We specify the aggregation
# as a transform here so we can reuse it in both layers.
base = alt.Chart(source).transform_aggregate(
    mean_horsepower='mean(Horsepower)',
    groupby=['Origin', 'Cylinders']
).encode(
    alt.X('Cylinders:O'),
    alt.Y('Origin:O'),
)

# Configure heatmap
heatmap = base.mark_rect().encode(
    color=alt.Color('mean_horsepower:Q',
        scale=alt.Scale(scheme='viridis'),
        legend=alt.Legend(title="Mean of Horsepower"),
    )
)

# Configure text
text = base.mark_text(baseline='middle').encode(
    text=alt.Text('mean_horsepower:Q', format=".0f"),
    color=alt.condition(
        alt.datum.mean_horsepower > 150,
        alt.value('black'),
        alt.value('white')
    )
)

# Draw the chart
heatmap + text
