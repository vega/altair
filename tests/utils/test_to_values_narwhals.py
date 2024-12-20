import re
from datetime import datetime

import narwhals.stable.v1 as nw
import pandas as pd
import pytest

from altair.utils.data import to_values
from tests import skip_requires_pyarrow


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
