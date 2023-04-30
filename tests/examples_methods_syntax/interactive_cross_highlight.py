"""
Interactive Chart with Cross-Highlight
======================================
This example shows an interactive chart where selections in one portion of
the chart affect what is shown in other panels. Click on the bar chart to
see a detail of the distribution in the upper panel.
"""
# category: interactive charts
import altair as alt
from vega_datasets import data

source = data.movies.url

pts = alt.selection_point(encodings=['x'])

rect = alt.Chart(data.movies.url).mark_rect().encode(
    alt.X('IMDB_Rating:Q').bin(),
    alt.Y('Rotten_Tomatoes_Rating:Q').bin(),
    alt.Color('count()').scale(scheme='greenblue').title('Total Records')
)

circ = rect.mark_point().encode(
    alt.ColorValue('grey'),
    alt.Size('count()').title('Records in Selection')
).transform_filter(
    pts
)

bar = alt.Chart(source, width=550, height=200).mark_bar().encode(
    x='Major_Genre:N',
    y='count()',
    color=alt.condition(pts, alt.ColorValue("steelblue"), alt.ColorValue("grey"))
).add_params(pts)

alt.vconcat(
    rect + circ,
    bar
).resolve_legend(
    color="independent",
    size="independent"
)
