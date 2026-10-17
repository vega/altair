from __future__ import annotations

import json
import re
from datetime import datetime
from typing import TYPE_CHECKING

import narwhals.stable.v1 as nw
import pandas as pd
import pytest

import altair as alt
from altair.utils import sanitize_narwhals_dataframe
from altair.utils.data import to_values
from tests import skip_requires_polars, skip_requires_pyarrow

if TYPE_CHECKING:
    from typing import Any


@pytest.mark.parametrize(
    "backend",
    [
        pytest.param("polars", marks=skip_requires_polars),
        pytest.param("pyarrow", marks=skip_requires_pyarrow()),
    ],
)
@pytest.mark.parametrize("bit_width", [32, 64])
@pytest.mark.parametrize(
    ("values", "expected"),
    [
        pytest.param(
            [None, float("nan"), float("inf"), -float("inf"), -0.0, 1.5],
            [None, None, None, None, -0.0, 1.5],
            id="mixed",
        ),
        pytest.param(
            [float("nan"), float("inf"), -float("inf")],
            [None, None, None],
            id="all-nonfinite",
        ),
        pytest.param([], [], id="empty"),
    ],
)
def test_nonfinite_float_columns(
    backend: str,
    bit_width: int,
    values: list[float | None],
    expected: list[float | None],
) -> None:
    data: Any
    row_ids = list(range(len(values)))
    if backend == "polars":
        import polars as pl

        dtype = pl.Float32 if bit_width == 32 else pl.Float64
        data = pl.DataFrame(
            {"value": values, "row": row_ids},
            schema={"value": dtype, "row": pl.Int64},
        )
    else:
        import pyarrow as pa

        arrow_dtype = pa.float32() if bit_width == 32 else pa.float64()
        data = pa.table(
            {
                "value": pa.array(values, type=arrow_dtype),
                "row": pa.array(row_ids, type=pa.int64()),
            }
        )

    frame = nw.from_native(data, eager_only=True)
    expected_records = [
        {"value": value, "row": row} for row, value in enumerate(expected)
    ]
    assert to_values(frame) == {"values": expected_records}
    assert sanitize_narwhals_dataframe(frame).schema == frame.schema
    json.dumps(to_values(frame), allow_nan=False)
    chart = alt.Chart(data).mark_point().encode(x="value:Q")
    spec = json.loads(chart.to_json(allow_nan=False))
    assert next(iter(spec["datasets"].values())) == expected_records


@skip_requires_pyarrow(requires_tzdata=True)
def test_arrow_timestamp_conversion():
    """Test that arrow timestamp values are converted to ISO-8601 strings."""
    import pyarrow as pa

    data = {
        "date": [datetime(2004, 8, 1), datetime(2004, 9, 1), None],
        "value": [102, 129, 139],
    }
    pa_table = pa.table(data)
    nw_frame = nw.from_native(pa_table)

    values = to_values(nw_frame)
    expected_values = {
        "values": [
            {"date": "2004-08-01T00:00:00.000000", "value": 102},
            {"date": "2004-09-01T00:00:00.000000", "value": 129},
            {"date": None, "value": 139},
        ]
    }
    assert values == expected_values


@skip_requires_pyarrow
def test_duration_raises():
    import pyarrow as pa

    td = pd.timedelta_range(0, periods=3, freq="h")
    df = pd.DataFrame(td).reset_index()
    df.columns = ["id", "timedelta"]
    pa_table = pa.table(df)
    nw_frame = nw.from_native(pa_table)
    with pytest.raises(ValueError) as e:  # noqa: PT011
        to_values(nw_frame)

    # Check that exception mentions the duration[ns] type,
    # which is what the pandas timedelta is converted into

    assert re.match(
        r'^Field "timedelta" has type "Duration.*" which is not supported by Altair',
        e.value.args[0],
    )
