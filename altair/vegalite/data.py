import functools
import json
import os
import random
import uuid

import pandas as pd
from toolz.curried import curry, pipe

from ..utils.core import sanitize_dataframe


#==============================================================================
# Data model transformers
#
# A data model transformer is a pure function that takes a dict or DataFrame
# and returns a transformed version of a dict or DataFrame. The dict objects
# will be the Data portion of the VegaLite schema. The idea is that user can
# pipe a sequence of these data transformers together to prepare the data before
# it hits the renderer.
#
# In this version of Altair, renderers only deal with the dict form of a
# VegaLite spec, after the Data model has been put into a schema compliant
# form.
#
# A data model transformer has the following type signature:
# DataModelType = Union[dict, pd.DataFrame]
# DataModelTransformerType = Callable[[DataModelType, KwArgs], DataModelType]
#==============================================================================


class MaxRowsError(Exception):
    """Raised when a data model has too many rows."""
    pass


@curry
def limit_rows(data, max_rows=5000):
    """Raise MaxRowsError if the data model has more than max_rows."""
    if not isinstance(data, (list, pd.DataFrame)):
        raise TypeError('Expected dict or DataFrame, got: {}'.format(type(data)))
    if len(data) > max_rows:
        raise MaxRowsError('The number of rows in your dataset is greater than the max of {}'.format(max_rows))
    return data


@curry
def sample(data, n=None, frac=None):
    """Reduce the size of the data model by sampling without replacement."""
    _check_data_type(data)
    if isinstance(data, pd.DataFrame):
        return data.sample(n=n, frac=frac)
    elif isinstance(data, dict):
        if 'values' in data:
            values = data['values']
            n = n if n else int(frac*len(values))
            values = random.sample(values, n)
            return {'values': values}


@curry
def to_json(data, filename=None, prefix='altair-data', base_url='/', nbserver_cwd='~'):
    """Write the data model to a .json file and return a url based data model."""
    _check_data_type(data)
    ext = '.json'
    filename, url = _compute_filename_and_url(filename=filename, prefix=prefix,
                                         base_url=base_url, nbserver_cwd=nbserver_cwd,
                                         ext=ext)
    if isinstance(data, pd.DataFrame):
        data = sanitize_dataframe(data)
        data.to_json(filename, orient='records')
    elif isinstance(data, dict):
        if 'values' not in data:
            raise KeyError('values expected in data dict, but not present.')
        values = data['values']
        with open(filename) as f:
            json.dump(values, f)
    return {
        'url': url,
        'format': {'type': 'json'}
    }


@curry
def to_csv(data, filename=None, prefix='altair-data', base_url='/', nbserver_cwd='~'):
    """Write the data model to a .csv file and return a url based data model."""
    _check_data_type(data)
    ext = '.csv'
    filename, url = _compute_filename_and_url(filename=filename, prefix=prefix,
                                         base_url=base_url, nbserver_cwd=nbserver_cwd,
                                         ext=ext)
    if isinstance(data, pd.DataFrame):
        data = sanitize_dataframe(data)
        data.to_csv(filename)
        return {
            'url': url,
            'format': {'type': 'csv'}
        }
    elif isinstance(data, dict):
        raise NotImplementedError('to_csv only works with Pandas DataFrame objects.')


@curry
def to_values(data):
    """Replace a DataFrame by a data model with values."""
    _check_data_type(data)
    if isinstance(data, pd.DataFrame):
        data = sanitize_dataframe(data)
        return {'values': data.to_dict(orient='records')}
    elif isinstance(data, dict):
        if 'values' not in data:
            raise KeyError('values expected in data dict, but not present.')
        return data


@curry
def default_data_transformer(data):
    return pipe(data, limit_rows, to_values)


#==============================================================================
# Private utilities
#==============================================================================


def _check_data_type(data):
    """Raise if the data is not a dict or DataFrame."""
    if not isinstance(data, (dict, pd.DataFrame)):
        raise TypeError('Expected dict or DataFrame, got: {}'.format(type(data)))


def _url_path_join(*pieces):
    """Join components of url into a relative url
    Use to prevent double slash when joining subpath. This will leave the
    initial and final / in place
    """
    initial = pieces[0].startswith('/')
    final = pieces[-1].endswith('/')
    stripped = [s.strip('/') for s in pieces]
    result = '/'.join(s for s in stripped if s)
    if initial: result = '/' + result
    if final: result = result + '/'
    if result == '//': result = '/'
    return result


def _compute_nbserver_url(filename, base_url='/', nbserver_cwd='~'):
    nbserver_cwd = os.path.expanduser(nbserver_cwd)
    here = os.getcwd()
    rel_path = os.path.relpath(here, nbserver_cwd)
    return _url_path_join(base_url, '/files/', rel_path, filename)


def _compute_uuid_filename(prefix, ext):
    return prefix + '-' + str(uuid.uuid4()) + ext


def _compute_filename_and_url(filename=None, prefix='altair',
                         base_url='/', nbserver_cwd='~',
                         ext='.csv'):

    if filename is None:
        filename = _compute_uuid_filename(prefix, ext)
    else:
        if not filename.endswith(ext):
            filename = filename + ext
    url = _compute_nbserver_url(filename, base_url=base_url, nbserver_cwd=nbserver_cwd)
    return filename, url