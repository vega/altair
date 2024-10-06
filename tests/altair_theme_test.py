# ruff: noqa: E711
from __future__ import annotations

import json
from typing import TYPE_CHECKING

import jinja2

if TYPE_CHECKING:
    from altair.typing import ChartType


def alt_theme_test() -> ChartType:
    import altair as alt
    from vega_datasets import data

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

    bar = (
        alt.Chart(common_data, title="Bar", width=480, height=150)
        .mark_bar()
        .encode(
            x=alt.X("Index:O").axis(offset=1), y=alt.Y("Value:Q"), tooltip="Value:Q"
        )
    )

    line = (
        alt.Chart(common_data, width=240, height=150, title="Line")
        .mark_line()
        .encode(
            x=alt.X("Position:O").axis(grid=False),
            y=alt.Y("Value:Q").axis(grid=False),
            color=alt.Color("Category:N").legend(None),
            tooltip=["Index:O", "Value:Q", "Position:O", "Category:N"],
        )
    )

    point_shape = (
        alt.Chart(common_data, width=200, height=200, title="Point (Shape)")
        .mark_point()
        .encode(
            x=alt.X("Position:O").axis(grid=False),
            y=alt.Y("Value:Q").axis(grid=False),
            shape=alt.Shape("Category:N").legend(None),
            color=alt.Color("Category:N").legend(None),
            tooltip=["Index:O", "Value:Q", "Position:O", "Category:N"],
        )
    )

    bar_facet = (
        alt.Chart(
            data.barley(), width=220, title=alt.Title("Bar (Facet)", anchor="middle")
        )
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
            "id", alt.LookupData(alt.UrlData(data.unemployment.url), "id", ["rate"])
        )
        .project(type="albersUsa")
    )

    point = (
        alt.Chart(data.movies.url, height=250, width=250, title="Point")
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
    compound_chart = (
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
    return compound_chart


THEME_TEST_TEMPLATE = jinja2.Template(
    """\
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <style>
    #header {
        padding: 10px 0 20px;
        height: 20px;
    }
    #{{ output_div }}.vega-embed {
      width: 100%;
      display: flex;
    }
    #{{ output_div }}.vega-embed details,
    #{{ output_div }}.vega-embed details summary {
      position: relative;
    }
  </style>
  <script type="text/javascript" src="{{ base_url }}/vega@{{ vega_version }}"></script>
  <script type="text/javascript" src="{{ base_url }}/vega-lite@{{ vegalite_version }}"></script>
  <script type="text/javascript" src="{{ base_url }}/vega-embed@{{ vegaembed_version }}"></script>
</head>
<body>
  <div id="header">
    Theme:
    <select id="themes">
      <option value="default">default</option>
      <option value="excel">excel</option>
      <option value="ggplot2">ggplot2</option>
      <option value="quartz">quartz</option>
      <option value="vox">vox</option>
      <option value="dark">dark</option>
      <option value="fivethirtyeight">fivethirtyeight</option>
      <option value="latimes">latimes</option>
      <option value="urbaninstitute">urbaninstitute</option>
      <option value="googlecharts">googlecharts</option>
      <option value="powerbi">powerbi</option>
      <optgroup label="Carbon">
        <option value="carbonwhite">carbonwhite</option>
        <option value="carbong10">carbong10</option>
        <option value="carbong90">carbong90</option>
        <option value="carbong100">carbong100</option>
      </optgroup>
    </select>
    <br />
  </div>
  <div id="{{ output_div }}"></div>
  <script>
    // Vega Theme Test - But single view, no renderer option
    var spec = {{ spec }};
    var container = document.querySelector("#{{ output_div }}");
    var themes = document.querySelector("#themes");
    var currentLocation = window.location;
    var url = new URL(currentLocation);

    themes.addEventListener("change", function () {
      theme = themes.options[themes.selectedIndex].value;
      url.searchParams.set("theme", `${themes.options[themes.selectedIndex].value}`);
      window.history.replaceState(null, null, url);
      refresh();
    });

    function refresh() {
      const themeName = themes.options[themes.selectedIndex].value;
      container.innerHTML = "";
      var el = document.createElement("div");
      el.setAttribute("class", "view");
      container.appendChild(el);
      vegaEmbed(el, spec, {
          theme: themeName,
          defaultStyle: true,
          mode: "vega-lite"
      });
    }

    // Mostly the standard template
    // - Need to adapt these two ideas into one
    (function(vegaEmbed) {
      var embedOpt = { mode: "vega-lite" };

      function showError(el, error){
          el.innerHTML = ('<div style="color:red;">'
                          + '<p>JavaScript Error: ' + error.message + '</p>'
                          + "<p>This usually means there's a typo in your chart specification. "
                          + "See the javascript console for the full traceback.</p>"
                          + '</div>');
          throw error;
      }
      const el = document.getElementById('{{ output_div }}');
      vegaEmbed("#{{ output_div }}", spec, embedOpt)
        .catch(error => showError(el, error));
    })(vegaEmbed);

  </script>
</body>
</html>
"""
)


def render_theme_test() -> str:
    import altair as alt

    return THEME_TEST_TEMPLATE.render(
        spec=json.dumps(alt_theme_test().to_dict(context={"pre_transform": False})),
        vegalite_version=alt.VEGALITE_VERSION,
        vegaembed_version=alt.VEGAEMBED_VERSION,
        vega_version=alt.VEGA_VERSION,
        base_url="https://cdn.jsdelivr.net/npm",
        output_div="vis",
    )
