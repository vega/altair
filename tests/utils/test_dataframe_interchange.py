from datetime import datetime
import pyarrow as pa
import pandas as pd
import pytest

from altair.utils.data import to_values


def test_arrow_timestamp_conversion():
    """Test that arrow timestamp values are converted to ISO-8601 strings"""
    data = {
        "date": [datetime(2004, 8, 1), datetime(2004, 9, 1), None],
        "value": [102, 129, 139],
    }
    pa_table = pa.table(data)

    values = to_values(pa_table)
    expected_values = {
        "values": [
            {"date": "2004-08-01T00:00:00.000000", "value": 102},
            {"date": "2004-09-01T00:00:00.000000", "value": 129},
            {"date": None, "value": 139},
        ]
    }
    assert values == expected_values


def test_duration_raises():
    td = pd.timedelta_range(0, periods=3, freq="h")
    df = pd.DataFrame(td).reset_index()
    df.columns = ["id", "timedelta"]
    pa_table = pa.table(df)
    with pytest.raises(ValueError) as e:
        to_values(pa_table)

    # Check that exception mentions the duration[ns] type,
    # which is what the pandas timedelta is converted into
    assert "duration[ns]" in e.value.args[0]
