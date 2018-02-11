import json
import random
import functools

import pandas as pd

from ..utils.core import sanitize_dataframe

#==============================================================================
# Utilities
#==============================================================================

# From https://github.com/JulienPalard/Pipe/blob/master/pipe.py
# MIT license
class pipe(object):
    """A pipe decorator for data model transformers."""
    def __init__(self, function):
        self.function = function
        functools.update_wrapper(self, function)

    def __ror__(self, other):
        return self.function(other)

    def __call__(self, *args, **kwargs):
        return pipe(lambda x: self.function(x, *args, **kwargs))


class MaxRowsError(Exception):
    """Raised when a data model has too many rows."""
    pass


def check_data_type(data):
    """Raise if the data is not a dict or DataFrame."""
    if not isinstance(data, (dict, pd.DataFrame)):
        raise TypeError('Expected dict or DataFrame, got: {}'.format(type(data)))


#==============================================================================
# Data model transformers
#
# A data model transformer has the following type signature:
# DataModelType = Union[dict, pd.DataFrame]
# DataModelTransformerType = Callable[[DataModelType, KwArgs], DataModelType]
#==============================================================================


def from_url(url, format=None):
    """Build a data model from a url."""
    data = {'url': url}
    if format is not None:
        assert format in ['json', 'csv', 'tsv']
        data['format'] = {'type': format}
    return data


@pipe
def limit_rows(data, max_rows=5000):
    """Raise MaxRowsError if the data model has more than max_rows."""
    if not isinstance(data, (list, pd.DataFrame)):
        raise TypeError('Expected dict or DataFrame, got: {}'.format(type(data)))
    if len(data) > max_rows:
        raise MaxRowsError('The number of rows in your dataset is greater than the max of {}'.format(max_rows))
    return data


@pipe
def sample(data, n=None, frac=None):
    """Reduce the size of the data model by sampling without replacement."""
    check_data_type(data)
    if isinstance(data, pd.DataFrame):
        return data.sample(n=n, frac=frac)
    elif isinstance(data, dict):
        if 'values' in data:
            values = data['values']
            n = n if n else int(frac*len(values))
            values = random.sample(values, n)
            return {'values': values}


@pipe
def to_json(data, filename=None):
    """Write the data model to a .json file and return a url based data model."""
    check_data_type(data)
    if not filename.endswith('.json'):
        filename = filename + '.json'
    if isinstance(data, pd.DataFrame):
        data = sanitize_dataframe(data)
        data.to_json(filename, orient='records')
    elif isinstance(data, dict):
        if 'values' not in data:
            raise KeyError('values expected in data dict, but not present.')
        values = data['values']
        with open(filename) as f:
            json.dump(values, f)
    return {'url': filename, 'format': {'type': 'json'}}


@pipe
def to_csv(data, filename=None):
    """Write the data model to a .csv file and return a url based data model."""
    check_data_type(data)
    if not filename.endswith('.csv'):
        filename = filename + '.csv'
    if isinstance(data, pd.DataFrame):
        data = sanitize_dataframe(data)
        data.to_csv(filename)
        return {'url': filename, 'format': {'type': 'csv'}}
    elif isinstance(data, dict):
        raise NotImplementedError('to_csv only works with Pandas DataFrame objects.')


@pipe
def to_values(data):
    """Replace a DataFrame by a data model with values."""
    check_data_type(data)
    if isinstance(data, pd.DataFrame):
        data = sanitize_dataframe(data)
        return {'values': data.to_dict(orient='records')}
    elif isinstance(data, dict):
        if 'values' not in data:
            raise KeyError('values expected in data dict, but not present.')
        return data

