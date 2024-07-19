"""
Bar Chart with Highlighting on Hover and Selection on Click
-----------------------------------------------------------
This example shows a bar chart with highlighting on hover and selecting on click. (Inspired by Tableau's interaction style.)

Based on https://vega.github.io/vega-lite/examples/interactive_bar_select_highlight.html
"""

# category: interactive charts
import altair as alt

source = {
    "values": [
        {"a": "A", "b": 28},
        {"a": "B", "b": 55},
        {"a": "C", "b": 43},
        {"a": "D", "b": 91},
        {"a": "E", "b": 81},
        {"a": "F", "b": 53},
        {"a": "G", "b": 19},
        {"a": "H", "b": 87},
        {"a": "I", "b": 52},
    ]
}

select = alt.selection_point(name="select", on="click")
highlight = alt.selection_point(name="highlight", on="pointerover", empty=False)

stroke_width = (
    alt.when(select).then(alt.value(2, empty=False))
    .when(highlight).then(alt.value(1))
    .otherwise(alt.value(0))
)


alt.Chart(source, height=200).mark_bar(
    fill="#4C78A8", stroke="black", cursor="pointer"
).encode(
    x="a:O",
    y="b:Q",
    fillOpacity=alt.when(select).then(alt.value(1)).otherwise(alt.value(0.3)),
    strokeWidth=stroke_width,
).configure_scale(bandPaddingInner=0.2).add_params(select, highlight)
