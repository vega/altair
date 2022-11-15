"""
Mosaic Chart with Labels
------------------------
"""
# category: tables

import altair as alt
from vega_datasets import data

source = data.cars()

base = (
    alt.Chart(source)
    .transform_aggregate(count_="count()", groupby=["Origin", "Cylinders"])
    .transform_stack(
        stack="count_",
        as_=["stack_count_Origin1", "stack_count_Origin2"],
        offset="normalize",
        sort=[alt.SortField("Origin", "ascending")],
        groupby=[],
    )
    .transform_window(
        x="min(stack_count_Origin1)",
        x2="max(stack_count_Origin2)",
        rank_Cylinders="dense_rank()",
        distinct_Cylinders="distinct(Cylinders)",
        groupby=["Origin"],
        frame=[None, None],
        sort=[alt.SortField("Cylinders", "ascending")],
    )
    .transform_window(
        rank_Origin="dense_rank()",
        frame=[None, None],
        sort=[alt.SortField("Origin", "ascending")],
    )
    .transform_stack(
        stack="count_",
        groupby=["Origin"],
        as_=["y", "y2"],
        offset="normalize",
        sort=[alt.SortField("Cylinders", "ascending")],
    )
    .transform_calculate(
        ny="datum.y + (datum.rank_Cylinders - 1) * datum.distinct_Cylinders * 0.01 / 3",
        ny2="datum.y2 + (datum.rank_Cylinders - 1) * datum.distinct_Cylinders * 0.01 / 3",
        nx="datum.x + (datum.rank_Origin - 1) * 0.01",
        nx2="datum.x2 + (datum.rank_Origin - 1) * 0.01",
        xc="(datum.nx+datum.nx2)/2",
        yc="(datum.ny+datum.ny2)/2",
    )
)


rect = base.mark_rect().encode(
    x=alt.X("nx:Q", axis=None),
    x2="nx2",
    y="ny:Q",
    y2="ny2",
    color=alt.Color("Origin:N", legend=None),
    opacity=alt.Opacity("Cylinders:Q", legend=None),
    tooltip=["Origin:N", "Cylinders:Q"],
)


text = base.mark_text(baseline="middle").encode(
    x=alt.X("xc:Q", axis=None), y=alt.Y("yc:Q", title="Cylinders"), text="Cylinders:N"
)


mosaic = rect + text

origin_labels = base.mark_text(baseline="middle", align="center").encode(
    x=alt.X(
        "min(xc):Q",
        axis=alt.Axis(title="Origin", orient="top"),
    ),
    color=alt.Color("Origin", legend=None),
    text="Origin",
)

(
    (origin_labels & mosaic)
    .resolve_scale(x="shared")
    .configure_view(stroke="")
    .configure_concat(spacing=10)
    .configure_axis(domain=False, ticks=False, labels=False, grid=False)
)
