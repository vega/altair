"""
Simple Line Chart with Markers
------------------------------
This chart shows the most basic line chart with markers, made from a dataframe with two
columns.
"""
# category: simple charts
import altair as alt

x = alt.pd.np.arange(100)
data = alt.pd.DataFrame({'x': x, 'sin(x)': alt.pd.np.sin(x / 5)})

alt.Chart(data).mark_line(point=True).encode(
    x='x',
    y='sin(x)'
)
