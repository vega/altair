# ruff: noqa: E711
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from altair.typing import ChartType


def alt_theme_test() -> ChartType:
    import altair as alt
    from altair.datasets import data

    us_10m = data.us_10m.url
    unemployment = data.unemployment.url
    movies = data.movies.url
    barley = data.barley.url
    iowa_electricity = data.iowa_electricity.url
    common_data = alt.InlineData(
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

    HEIGHT_SMALL = 140
    STANDARD = 180
    WIDTH_GEO = int(STANDARD * 1.667)

    bar = (
        alt.Chart(common_data, height=HEIGHT_SMALL, width=STANDARD, title="Bar")
        .mark_bar()
        .encode(
            x=alt.X("Index:O").axis(offset=1), y=alt.Y("Value:Q"), tooltip="Value:Q"
        )
        .transform_filter(alt.datum["Index"] <= 9)
    )
    line = (
        alt.Chart(common_data, height=HEIGHT_SMALL, width=STANDARD, title="Line")
        .mark_line()
        .encode(
            x=alt.X("Position:O").axis(grid=False),
            y=alt.Y("Value:Q").axis(grid=False),
            color=alt.Color("Category:N").legend(None),
            tooltip=["Index:O", "Value:Q", "Position:O", "Category:N"],
        )
    )
    point_shape = (
        alt.Chart(
            common_data, height=HEIGHT_SMALL, width=STANDARD, title="Point (Shape)"
        )
        .mark_point()
        .encode(
            x=alt.X("Position:O").axis(grid=False),
            y=alt.Y("Value:Q").axis(grid=False),
            shape=alt.Shape("Category:N").legend(None),
            color=alt.Color("Category:N").legend(None),
            tooltip=["Index:O", "Value:Q", "Position:O", "Category:N"],
        )
    )
    point = (
        alt.Chart(movies, height=STANDARD, width=STANDARD, title="Point")
        .mark_point(tooltip=True)
        .transform_filter(alt.datum["IMDB_Rating"] != None)
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
    bar_stack = (
        alt.Chart(barley, height=STANDARD, width=STANDARD, title="Bar (Stacked)")
        .mark_bar(tooltip=True)
        .encode(
            x="sum(yield):Q",
            y=alt.Y("variety:N"),
            color=alt.Color("site:N").legend(orient="bottom", columns=2),
        )
    )
    area = (
        alt.Chart(iowa_electricity, height=STANDARD, width=STANDARD, title="Area")
        .mark_area(tooltip=True)
        .encode(
            x=alt.X("year:T").title("Year"),
            y=alt.Y("net_generation:Q")
            .title("Share of net generation")
            .stack("normalize")
            .axis(format=".0%"),
            color=alt.Color("source:N")
            .title("Electricity source")
            .legend(orient="bottom", columns=2),
        )
    )
    geoshape = (
        alt.Chart(
            alt.topo_feature(us_10m, "counties"),
            height=STANDARD,
            width=WIDTH_GEO,
            title=alt.Title("Geoshape", subtitle="Unemployment rate per county"),
        )
        .mark_geoshape(tooltip=True)
        .encode(color="rate:Q")
        .transform_lookup(
            "id", alt.LookupData(alt.UrlData(unemployment), "id", ["rate"])
        )
        .project(type="albersUsa")
    )

    compound_chart = (
        (bar | line | point_shape) & (point | bar_stack) & (area | geoshape)
    ).properties(
        title=alt.Title(
            "Vega-Altair Theme Test",
            fontSize=20,
            subtitle="Adapted from https://vega.github.io/vega-themes/",
        )
    )
    return compound_chart
