from datetime import datetime
import pyarrow as pa
from altair.utils.data import to_values


def test_arrow_timestamp_conversion():
    """Test that arrow timestamp values are converted to ISO-8601 strings"""
    data = {"date": [datetime(2004, 8, 1), datetime(2004, 9, 1)], "value": [102, 129]}
    pa_table = pa.table(data)

    values = to_values(pa_table)
    expected_values = {
        "values": [
            {"date": "2004-08-01T00:00:00.000000", "value": 102},
            {"date": "2004-09-01T00:00:00.000000", "value": 129},
        ]
    }
    assert values == expected_values
