import io
import json

import narwhals.stable.v1 as nw
import numpy as np
import pandas as pd
import pytest

from altair.utils import (
    infer_vegalite_type_for_pandas,
    sanitize_narwhals_dataframe,
    sanitize_pandas_dataframe,
)
from tests import skip_requires_polars, skip_requires_pyarrow


def test_infer_vegalite_type():
    def _check(arr, typ):
        assert infer_vegalite_type_for_pandas(arr) == typ

    _check(np.arange(5, dtype=float), "quantitative")
    _check(np.arange(5, dtype=int), "quantitative")
    _check(np.zeros(5, dtype=bool), "nominal")
    _check(pd.date_range("2012", "2013"), "temporal")
    _check(pd.timedelta_range(365, periods=12), "temporal")

    rng = np.random.default_rng()
    nulled = pd.Series(rng.integers(10, size=10))
    nulled[0] = None
    _check(nulled, "quantitative")
    _check(["a", "b", "c"], "nominal")

    with pytest.warns(UserWarning, match=r"infer vegalite type"):
        _check([], "nominal")


def test_sanitize_dataframe():
    # create a dataframe with various types
    df = pd.DataFrame(
        {
            "s": list("abcde"),
            "f": np.arange(5, dtype=float),
            "i": np.arange(5, dtype=int),
            "b": np.array([True, False, True, True, False]),
            "d": pd.date_range("2012-01-01", periods=5, freq="h"),
            "c": pd.Series(list("ababc"), dtype="category"),
            "c2": pd.Series([1, "A", 2.5, "B", None], dtype="category"),
            "o": pd.Series([np.array(i) for i in range(5)]),
            "p": pd.date_range("2012-01-01", periods=5, freq="h").tz_localize("UTC"),
        }
    )

    # add some nulls
    df.iloc[0, df.columns.get_loc("s")] = None
    df.iloc[0, df.columns.get_loc("f")] = np.nan
    df.iloc[0, df.columns.get_loc("d")] = pd.NaT
    df.iloc[0, df.columns.get_loc("o")] = np.array(np.nan)

    # JSON serialize. This will fail on non-sanitized dataframes
    print(df[["s", "c2"]])
    df_clean = sanitize_pandas_dataframe(df)
    print(df_clean[["s", "c2"]])
    print(df_clean[["s", "c2"]].to_dict())
    s = json.dumps(df_clean.to_dict(orient="records"))
    print(s)

    # Re-construct pandas dataframe
    df2 = pd.read_json(io.StringIO(s))

    # Re-order the columns to match df
    df2 = df2[df.columns]

    # pandas doesn't properly recognize np.array(np.nan); use float64 so df matches read_json
    df.iloc[0, df.columns.get_loc("o")] = np.nan
    df["o"] = df["o"].astype(np.float64)

    # Re-apply original types
    for col in df:
        if str(df[col].dtype).startswith("datetime"):
            # astype(datetime) introduces time-zone issues:
            # to_datetime() does not.
            utc = isinstance(df[col].dtype, pd.DatetimeTZDtype)
            df2[col] = pd.to_datetime(df2[col], utc=utc)
        else:
            df2[col] = df2[col].astype(df[col].dtype)

    assert df.equals(df2)


@pytest.mark.filterwarnings("ignore:'H' is deprecated.*:FutureWarning")
@skip_requires_pyarrow
def test_sanitize_dataframe_arrow_columns():
    import pyarrow as pa

    # create a dataframe with various types
    df = pd.DataFrame(
        {
            "s": list("abcde"),
            "f": np.arange(5, dtype=float),
            "i": np.arange(5, dtype=int),
            "b": np.array([True, False, True, True, False]),
            "d": pd.date_range("2012-01-01", periods=5, freq="h"),
            "c": pd.Series(list("ababc"), dtype="category"),
            "p": pd.date_range("2012-01-01", periods=5, freq="h").tz_localize("UTC"),
        }
    )
    df_arrow = pa.Table.from_pandas(df).to_pandas(types_mapper=pd.ArrowDtype)
    df_clean = sanitize_pandas_dataframe(df_arrow)
    records = df_clean.to_dict(orient="records")
    assert records[0] == {
        "s": "a",
        "f": 0.0,
        "i": 0,
        "b": True,
        "d": "2012-01-01T00:00:00",
        "c": "a",
        "p": "2012-01-01T00:00:00+00:00",
    }

    # Make sure we can serialize to JSON without error
    json.dumps(records)


@skip_requires_pyarrow(requires_tzdata=True)
def test_sanitize_pyarrow_table_columns() -> None:
    import pyarrow as pa

    # create a dataframe with various types
    df = pd.DataFrame(
        {
            "s": list("abcde"),
            "f": np.arange(5, dtype=float),
            "i": np.arange(5, dtype=int),
            "b": np.array([True, False, True, True, False]),
            "d": pd.date_range("2012-01-01", periods=5, freq="h"),
            "c": pd.Series(list("ababc"), dtype="category"),
            "p": pd.date_range("2012-01-01", periods=5, freq="h").tz_localize("UTC"),
        }
    )

    # Create pyarrow table with explicit schema so that date32 type is preserved
    pa_table = pa.Table.from_pandas(
        df,
        pa.schema(
            (
                pa.field("s", pa.string()),
                pa.field("f", pa.float64()),
                pa.field("i", pa.int64()),
                pa.field("b", pa.bool_()),
                pa.field("d", pa.date32()),
                pa.field("c", pa.dictionary(pa.int8(), pa.string())),
                pa.field("p", pa.timestamp("ns", tz="UTC")),
            )
        ),
    )
    sanitized = sanitize_narwhals_dataframe(nw.from_native(pa_table, eager_only=True))
    values = sanitized.rows(named=True)

    assert values[0] == {
        "s": "a",
        "f": 0.0,
        "i": 0,
        "b": True,
        "d": "2012-01-01T00:00:00",
        "c": "a",
        "p": "2012-01-01T00:00:00.000000000",
    }

    # Make sure we can serialize to JSON without error
    json.dumps(values)


@skip_requires_polars
def test_sanitize_polars_datetime_timezone_preserved() -> None:
    import polars as pl

    start = pl.datetime(2023, 11, 5, time_zone="US/Mountain")
    df = pl.DataFrame(
        {
            "datetime": pl.datetime_range(
                start, start.dt.offset_by("3h"), "1h", closed="both", eager=True
            ),
            "value": [10, 20, 30, 40],
        }
    )

    sanitized = sanitize_narwhals_dataframe(nw.from_native(df, eager_only=True))

    assert sanitized.rows(named=True) == [
        {"datetime": "2023-11-05T00:00:00-0600", "value": 10},
        {"datetime": "2023-11-05T01:00:00-0600", "value": 20},
        {"datetime": "2023-11-05T01:00:00-0700", "value": 30},
        {"datetime": "2023-11-05T02:00:00-0700", "value": 40},
    ]


def test_sanitize_dataframe_colnames():
    df = pd.DataFrame(np.arange(12).reshape(4, 3))

    # Test that RangeIndex is converted to strings
    df = sanitize_pandas_dataframe(df)
    assert [isinstance(col, str) for col in df.columns]

    # Test that non-string columns result in an error
    df.columns = [4, "foo", "bar"]
    with pytest.raises(ValueError, match=r"Dataframe contains invalid column name: 4."):
        sanitize_pandas_dataframe(df)


def test_sanitize_dataframe_timedelta():
    df = pd.DataFrame({"r": pd.timedelta_range(start="1 day", periods=4)})
    with pytest.raises(ValueError, match='Field "r" has type "timedelta'):
        sanitize_pandas_dataframe(df)


def test_sanitize_dataframe_infs():
    df = pd.DataFrame({"x": [0, 1, 2, np.inf, -np.inf, np.nan]})
    df_clean = sanitize_pandas_dataframe(df)
    assert list(df_clean.dtypes) == [object]
    assert list(df_clean["x"]) == [0, 1, 2, None, None, None]


@pytest.mark.skipif(
    not hasattr(pd, "Int64Dtype"),
    reason=f"Nullable integers not supported in pandas v{pd.__version__}",
)
def test_sanitize_nullable_integers():
    df = pd.DataFrame(
        {
            "int_np": [1, 2, 3, 4, 5],
            "int64": pd.Series([1, 2, 3, None, 5], dtype="UInt8"),
            "int64_nan": pd.Series([1, 2, 3, float("nan"), 5], dtype="Int64"),
            "float": [1.0, 2.0, 3.0, 4, 5.0],
            "float_null": [1, 2, None, 4, 5],
            "float_inf": [1, 2, None, 4, (float("inf"))],
        }
    )

    df_clean = sanitize_pandas_dataframe(df)
    assert {col.dtype.name for _, col in df_clean.items()} == {"object"}

    result_python = {col_name: list(col) for col_name, col in df_clean.items()}
    assert result_python == {
        "int_np": [1, 2, 3, 4, 5],
        "int64": [1, 2, 3, None, 5],
        "int64_nan": [1, 2, 3, None, 5],
        "float": [1.0, 2.0, 3.0, 4.0, 5.0],
        "float_null": [1.0, 2.0, None, 4.0, 5.0],
        "float_inf": [1.0, 2.0, None, 4.0, None],
    }


@pytest.mark.skipif(
    not hasattr(pd, "StringDtype"),
    reason=f"dedicated String dtype not supported in pandas v{pd.__version__}",
)
def test_sanitize_string_dtype():
    df = pd.DataFrame(
        {
            "string_object": ["a", "b", "c", "d"],
            "string_string": pd.array(["a", "b", "c", "d"], dtype="string"),
            "string_object_null": ["a", "b", None, "d"],
            "string_string_null": pd.array(["a", "b", None, "d"], dtype="string"),
        }
    )

    df_clean = sanitize_pandas_dataframe(df)
    # pandas 3+ with pyarrow may leave .dtype.name as "str" in some cases
    assert {col.dtype.name for _, col in df_clean.items()} <= {"object", "str"}

    result_python = {col_name: list(col) for col_name, col in df_clean.items()}
    assert result_python == {
        "string_object": ["a", "b", "c", "d"],
        "string_string": ["a", "b", "c", "d"],
        "string_object_null": ["a", "b", None, "d"],
        "string_string_null": ["a", "b", None, "d"],
    }


@pytest.mark.skipif(
    not hasattr(pd, "BooleanDtype"),
    reason=f"Nullable boolean dtype not supported in pandas v{pd.__version__}",
)
def test_sanitize_boolean_dtype():
    df = pd.DataFrame(
        {
            "bool_none": pd.array([True, False, None], dtype="boolean"),
            "none": pd.array([None, None, None], dtype="boolean"),
            "bool": pd.array([True, False, True], dtype="boolean"),
        }
    )

    df_clean = sanitize_pandas_dataframe(df)
    assert {col.dtype.name for _, col in df_clean.items()} == {"object"}

    result_python = {col_name: list(col) for col_name, col in df_clean.items()}
    assert result_python == {
        "bool_none": [True, False, None],
        "none": [None, None, None],
        "bool": [True, False, True],
    }
