import polars as pl

import altair as alt
from vega_datasets import data

common_data = pl.DataFrame(
    [
        {"Index": 1, "Value": 28, "Position": 1, "Category": "A"},
        {"Index": 2, "Value": 55, "Position": 2, "Category": "A"},
        {"Index": 3, "Value": 43, "Position": 3, "Category": "A"},
        {"Index": 4, "Value": 91, "Position": 4, "Category": "A"},
        {"Index": 5, "Value": 81, "Position": 5, "Category": "A"},
        {"Index": 6, "Value": 53, "Position": 6, "Category": "A"},
        {"Index": 7, "Value": 19, "Position": 1, "Category": "B"},
        {"Index": 8, "Value": 87, "Position": 2, "Category": "B"},
        {"Index": 9, "Value": 52, "Position": 3, "Category": "B"},
        {"Index": 10, "Value": 48, "Position": 4, "Category": "B"},
        {"Index": 11, "Value": 24, "Position": 5, "Category": "B"},
        {"Index": 12, "Value": 49, "Position": 6, "Category": "B"},
        {"Index": 13, "Value": 87, "Position": 1, "Category": "C"},
        {"Index": 14, "Value": 66, "Position": 2, "Category": "C"},
        {"Index": 15, "Value": 17, "Position": 3, "Category": "C"},
        {"Index": 16, "Value": 27, "Position": 4, "Category": "C"},
        {"Index": 17, "Value": 68, "Position": 5, "Category": "C"},
        {"Index": 18, "Value": 16, "Position": 6, "Category": "C"},
    ]
)


bar = (
    alt.Chart(common_data, title="Bar", width=480, height=150)
    .mark_bar()
    .encode(x=alt.X("Index:O").axis(offset=1), y=alt.Y("Value:Q"), tooltip="Value:Q")
)

line = (
    alt.Chart(common_data, width=240, height=150, title="Line")
    .mark_line()
    .encode(
        x=alt.X("Position").axis(grid=False),
        y=alt.Y("Value:Q").axis(grid=False),
        color=alt.Color("Category").legend(None),
        tooltip=["Index", "Value", "Position", "Category"],
    )
)

point_shape = (
    alt.Chart(common_data, width=200, height=200, title="Point (Shape)")
    .mark_point()
    .encode(
        x=alt.X("Position:O").axis(grid=False),
        y=alt.Y("Value:Q").axis(grid=False),
        shape=alt.Shape("Category").legend(None),
        color=alt.Color("Category").legend(None),
        tooltip=["Index", "Value", "Position", "Category"],
    )
)

bar_facet = (
    alt.Chart(data.barley(), width=220, title=alt.Title("Bar (Facet)", anchor="middle"))
    .mark_bar(tooltip=True)
    .encode(column="year:O", x="yield", y="variety", color="site")
)

rect_heatmap = (
    alt.Chart(
        data.seattle_weather(),
        title=alt.Title(
            "Rect (Heatmap)", subtitle="Daily Max Temperatures (C) in Seattle, WA"
        ),
        height=200,
    )
    .mark_rect()
    .encode(
        x=alt.X("date(date):O").title("Day").axis(format="%e", labelAngle=0),
        y=alt.Y("month(date):O").title("Month"),
        color=alt.Color("max(temp_max)").title(None),
        tooltip=[
            alt.Tooltip("monthdate(date)", title="Date"),
            alt.Tooltip("max(temp_max)", title="Max Temp"),
        ],
    )
)

geoshape = (
    alt.Chart(
        alt.topo_feature(data.us_10m.url, "counties"),
        title=alt.Title("Geoshape", subtitle="Unemployment rate per county"),
        width=500,
        height=300,
    )
    .mark_geoshape(tooltip=True)
    .encode(color="rate:Q")
    .transform_lookup(
        lookup="id",
        from_=alt.LookupData(data.unemployment.url, "id", ["rate"]),  # pyright: ignore[reportArgumentType]
    )
    .project(type="albersUsa")
)

point = (
    alt.Chart(data.movies.url, height=250, width=250, title="Point")
    .mark_point()
    .transform_filter(alt.datum["IMDB_Rating"] != None)  # noqa: E711
    .transform_filter(
        alt.FieldRangePredicate("Release_Date", [None, 2019], timeUnit="year")
    )
    .transform_joinaggregate(Average_Rating="mean(IMDB_Rating)")
    .transform_calculate(
        Rating_Delta=alt.datum["IMDB_Rating"] - alt.datum.Average_Rating
    )
    .encode(
        x=alt.X("Release_Date:T").title("Release Date"),
        y=alt.Y("Rating_Delta:Q").title("Rating Delta"),
        color=alt.Color("Rating_Delta:Q").title("Rating Delta").scale(domainMid=0),
    )
)

area = (
    alt.Chart(data.iowa_electricity(), title="Area", height=250, width=250)
    .mark_area(tooltip=True)
    .encode(
        alt.X("year:T").title("Year"),
        alt.Y("net_generation:Q")
        .title("Share of net generation")
        .stack("normalize")
        .axis(format=".0%"),
        alt.Color("source:N").title("Electricity source"),
    )
)


alt_theme_test = (
    (bar | line)
    & (point_shape | bar_facet).resolve_scale(color="independent")
    & (point | area)
    & rect_heatmap
    & geoshape
).properties(
    title=alt.Title(
        "Vega-Altair Theme Test",
        fontSize=20,
        subtitle="Adapted from https://vega.github.io/vega-themes/",
        offset=16,
    )
)

alt_theme_test  # noqa: B018
