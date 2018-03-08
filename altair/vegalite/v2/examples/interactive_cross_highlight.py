"""
Interactive Chart with Cross-Highlight
======================================
This example shows an interactive chart where selections in one portion of
the chart affect what is shown in other panels. Click on the bar chart to
see a detail of the distribution in the upper panel.
"""
# category: interactive

import altair as alt
from vega_datasets import data

pts = alt.selection(type="single", encodings=['x'])

rect = alt.Chart(data.movies.url).mark_rect().encode(
    alt.X('IMDB_Rating:Q', bin=True),
    alt.Y('Rotten_Tomatoes_Rating:Q', bin=True),
    alt.Color('count(*):Q',
        scale=alt.Scale(scheme='greenblue'),
        legend=alt.Legend(title='Total Records')
    )
)

circ = rect.mark_point().encode(
    alt.ColorValue('grey'),
    alt.Size('count(*):Q',
        legend=alt.Legend(title='Records in Selection')
    )
).transform_filter(
    pts.ref()
)

bar = alt.Chart(data.movies.url).mark_bar().encode(
    x='Major_Genre:N',
    y='count(*):Q',
    color=alt.condition(pts, alt.ColorValue("steelblue"), alt.ColorValue("grey"))
).properties(
    selection=pts,
    width=550,
    height=200
)

chart = alt.vconcat(
    rect + circ,
    bar
).resolve_legend(
    color="independent",
    size="independent"
)
