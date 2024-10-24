"""
Reorder stacked bar segments
============================
This example uses a calculate transform
to check the values of the "site" column
vs the clicked values in the legend,
and assigns a lower order (0)
if there is a match.
The use of "indexOf" checks for equality in an array,
which here allows for multiple segments to be reordered
by holding down the shift key while clicking the legend.
"""
# category: interactive charts
import altair as alt
from vega_datasets import data

selection = alt.selection_point(fields=['site'], bind='legend')

source = data.barley.url

alt.Chart(source).mark_bar().transform_calculate(
    site_order=f"if({selection.name}.site && indexof({selection.name}.site, datum.site) !== -1, 0, 1)"
).encode(
    x='sum(yield):Q',
    y='variety:N',
    color='site:N',
    order='site_order:N',
    opacity=alt.when(selection).then(alt.value(0.9)).otherwise(alt.value(0.2))
).add_params(
    selection
)
