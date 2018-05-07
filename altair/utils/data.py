import json
import random
import uuid

import pandas as pd
from toolz.curried import curry, pipe  # noqa
from typing import Callable

from .core import sanitize_dataframe
from .plugin_registry import PluginRegistry


# ==============================================================================
# Data transformer registry
# ==============================================================================
DataTransformerType = Callable

class DataTransformerRegistry(PluginRegistry[DataTransformerType]):
    pass


# ==============================================================================
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
# DataModelType = Union[dict, pd.DataFrame, gpd.GeoDataFrame, geojson interface object]
# DataModelTransformerType = Callable[[DataModelType, KwArgs], DataModelType]
# ==============================================================================


class MaxRowsError(Exception):
    """Raised when a data model has too many rows."""
    pass


@curry
def limit_rows(data, max_rows=5000):
    """Raise MaxRowsError if the data model has more than max_rows.

    If max_rows is None, then do not perform any check.
    """
    check_data_type(data)
    if isinstance(data, pd.DataFrame):
        values = data
    elif isinstance(data, dict):
        if 'values' in data:
            values = data['values']
        else:
            return data
    else:
        return data
    if max_rows is not None and len(values) > max_rows:
        raise MaxRowsError('The number of rows in your dataset is greater '
                           'than the maximum allowed ({0}). '
                           'For information on how to plot larger datasets '
                           'in Altair, see the documentation'.format(max_rows))
    return data


@curry
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


@curry
def to_json(data, prefix='altair-data'):
    """Write the data model to a .json file and return a url based data model."""
    check_data_type(data)
    ext = '.json'
    filename = _compute_filename(prefix=prefix, ext=ext)
    data_format = {'type': 'json'}
    if isinstance(data, pd.DataFrame):
        data = sanitize_dataframe(data)
        if not hasattr(data,'__geo_interface__'):
            data.to_json(filename, orient='records')
        else: #GeoPandas
            with open(filename,'w') as f:
                json.dump(data.__geo_interface__, f)
            data_format['property']='features'

    elif hasattr(data,'__geo_interface__'): # geojson object
        with open(filename,'w') as f:
            json.dump(data.__geo_interface__, f)
        
    elif isinstance(data, dict):
        if 'values' not in data:
            raise KeyError('values expected in data dict, but not present.')
        values = data['values']
        with open(filename,'w') as f:
            json.dump(values, f)
    return {
        'url': filename,
        'format': data_format
    }


@curry
def to_csv(data, prefix='altair-data'):
    """Write the data model to a .csv file and return a url based data model."""
    check_data_type(data)
    ext = '.csv'
    filename = _compute_filename(prefix=prefix, ext=ext)
    if isinstance(data, pd.DataFrame):
        if hasattr(data,'__geo_interface__'):#GeoPandas
                raise NotImplementedError('use to_json or to_values with GeoDataFrame objects.')

        data = sanitize_dataframe(data)
        data.to_csv(filename)
        return {
            'url': filename,
            'format': {'type': 'csv'}
        }
    elif hasattr(data,'__geo_interface__'):#GeoJSON
            raise NotImplementedError('to_csv only works with Pandas DataFrame objects.')
    elif isinstance(data, dict):
        raise NotImplementedError('to_csv only works with Pandas DataFrame objects.')


@curry
def to_values(data):
    """Replace a DataFrame by a data model with values."""
    check_data_type(data)
    if isinstance(data, pd.DataFrame):
        data = sanitize_dataframe(data)
        if hasattr(data,'__geo_interface__'):#GeoPandas
            return {
                    'values':data.__geo_interface__,
                    'format':{'type':'json','property':'features'}
                    }

        return {'values': data.to_dict(orient='records')}
    elif hasattr(data,'__geo_interface__'):#GeoJSON
            return {
                    'values':data.__geo_interface__,
                    'format':{'type':'json'}
                    }
    
    elif isinstance(data, dict):
        if 'values' not in data:
            raise KeyError('values expected in data dict, but not present.')
        return data


def check_data_type(data):
    """Raise if the data is not a dict or DataFrame."""
    if not (isinstance(data, (dict, pd.DataFrame)) or hasattr(data,'__geo_interface__')):
        raise TypeError('Expected dict, DataFrame, GeoDataFrame or geojson inteface object , got: {}'.format(type(data)))


# ==============================================================================
# Private utilities
# ==============================================================================


def _compute_uuid_filename(prefix, ext):
    return prefix + '-' + str(uuid.uuid4()) + ext


def _compute_filename(prefix='altair-data', ext='.csv'):
    filename = _compute_uuid_filename(prefix, ext)
    return filename
