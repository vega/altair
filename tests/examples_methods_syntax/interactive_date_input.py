"""
Filter a Time Series with a Date Input
======================================
This example shows how to bind an HTML date input to a parameter and use the
selected date to filter a time-series chart.
"""

# category: interactive charts
import altair as alt
import pandas as pd

source = pd.DataFrame(
    {
        "date": pd.date_range("2024-01-01", periods=14, freq="D"),
        "visitors": [
            120,
            135,
            128,
            142,
            160,
            175,
            168,
            155,
            172,
            184,
            191,
            205,
            198,
            214,
        ],
    }
)

start_date = alt.param(
    name="start_date",
    value="2024-01-05",
    bind=alt.binding(input="date", name="Start date: "),
)

chart = (
    alt.Chart(source)
    .mark_line(point=True)
    .encode(
        alt.X("date:T"),
        alt.Y("visitors:Q"),
        tooltip=[
            alt.Tooltip("date:T", title="Date"),
            alt.Tooltip("visitors:Q", title="Visitors"),
        ],
    )
    .transform_filter(alt.datum.date >= alt.expr.timeParse(start_date, "%Y-%m-%d"))
    .add_params(start_date)
)

chart
