
from toolz.curried import curry, pipe
from ..utils.core import sanitize_dataframe
from ..utils.data import (
    MaxRowsError, limit_rows, sample, to_csv, to_json, to_values, check_data_type
)


@curry
def default_data_transformer(data):
    return pipe(data, limit_rows, to_values)


__all__ = (
    'MaxRowsError',
    'curry',
    'sanitize_dataframe',
    'default_data_transformer',
    'limit_rows',
    'pipe',
    'sample',
    'to_csv',
    'to_json',
    'to_values',
    'check_data_type'
)
