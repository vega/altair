"""
Becker's Barley Trellis Plot
----------------------------
This example shows how to make a Trellis Plot with the barley dataset.
"""
# category: case studies
import altair as alt


source = alt.datasets.barley()

alt.Chart(source).mark_point().encode(
    alt.X('median(yield)', scale=alt.Scale(zero=False)),
    alt.Y(
        'variety',
        sort=alt.EncodingSortField(field='yield', op='median', order='descending'),
        scale=alt.Scale(rangeStep=20)
    ),
    color='year:N',
    row='site'
)
