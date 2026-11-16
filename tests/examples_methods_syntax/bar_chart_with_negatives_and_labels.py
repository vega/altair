"""
Horizontal Bar Chart with Negative Values and Labels
----------------------------------------------------
This example shows a horizontal bar chart with positive and negative values,
where each text label is placed to the left of the bar for negative values
and to the right of the bar for positive values.
"""
# category: bar charts
import altair as alt
import pandas as pd

source = pd.DataFrame({
    "a": ["A", "B", "C", "D", "E", "F", "G", "H", "I"],
    "b": [-28, 55, -33, 91, 81, 53, -19, 87, 52],
})

bars = alt.Chart(source).mark_bar().encode(
    alt.Y("a:N"),
    alt.X("b:Q").scale(padding=20),
    color=alt.when(alt.datum.b > 0)
    .then(alt.value("#003865"))
    .otherwise(alt.value("#5E8AB4")),
)

text = alt.Chart(source).mark_text(
    align=alt.expr(alt.expr.if_(alt.datum.b < 0, "right", "left")),
    dx=alt.expr(alt.expr.if_(alt.datum.b < 0, -2, 2)),
).encode(
    alt.Y("a:N"),
    alt.X("b:Q"),
    text="b:Q",
)

bars + text