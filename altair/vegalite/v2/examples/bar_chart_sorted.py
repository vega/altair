"""
Simple Sorted Bar Chart
============================
This example shows a basic sorted bar chart.
"""
# category: bar charts
import altair as alt

data = alt.pd.DataFrame({
    'a': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
    'b': [28, 55, 43, 91, 81, 53, 19, 87, 52]
})

alt.Chart(data).mark_bar().encode(
    x=alt.X('a', sort=alt.EncodingSortField(field='b', op='sum', order='descending')),
    y='b'
)
