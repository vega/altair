"""
Correlation matrix
--------------
This example shows how to create a correlation matrix and a heatmap from the iris dataset.
"""
# category: other charts
# Load packages

import altair as alt
from vega_datasets import data

# Load the data
df_iris = data.iris()

# Create a correlation matrix
corrMatrix_line = df_iris.corr().round(2).reset_index().rename(columns = {'index':'Var1'}).melt(id_vars = ['Var1'],
                                                                                                value_name = 'Correlation',
                                                                                                var_name = 'Var2')
# Create the heatmap first
heatmap = alt.Chart(corrMatrix_line).encode(
    alt.Y('Var1:N', title = ''),
    alt.X('Var2:N', title = '', axis=alt.Axis(labelAngle=20))
).mark_rect().encode(
     alt.Color('Correlation:Q',
                scale=alt.Scale(scheme='viridis'))
)

# Add the correlation values as a text mark
text = heatmap.mark_text(baseline='middle', fontSize=20).encode(
    text=alt.Text('Correlation:Q', format='.2'),
    color=alt.condition(
        alt.datum.Correlation >= 0.95,
        alt.value('black'),
        alt.value('white')
    )
)

# Set the height, width, title and other properties
corrMatrix_chart = (heatmap + text).properties(
    width = 400,
    height = 400,
    title = "Iris variables correlation matrix",
)
corrMatrix_chart.configure_axis(
    labelFontSize=18,
    titleFontSize=24,
).configure_title(
    fontSize=24,
    anchor='start',
).configure_legend(
    labelFontSize=20,
    titleFontSize=20)
