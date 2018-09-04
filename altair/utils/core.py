"""
Utility routines
"""
import collections
from copy import deepcopy
import itertools
import re
import sys
import traceback
import warnings

import six
import pandas as pd
import numpy as np

try:
    from pandas.api.types import infer_dtype
except ImportError: # Pandas before 0.20.0
    from pandas.lib import infer_dtype

from .schemapi import SchemaBase, Undefined


TYPECODE_MAP = {'ordinal': 'O',
                'nominal': 'N',
                'quantitative': 'Q',
                'temporal': 'T'}

INV_TYPECODE_MAP = {v: k for k, v in TYPECODE_MAP.items()}


# aggregates from vega-lite version 2.4.3
AGGREGATES = ['argmax', 'argmin', 'average', 'count', 'distinct', 'max',
              'mean', 'median', 'min', 'missing', 'q1', 'q3', 'ci0', 'ci1',
              'stderr', 'stdev', 'stdevp', 'sum', 'valid', 'values',
              'variance', 'variancep']

# window aggregates from vega-lite version 2.5.2
WINDOW_AGGREGATES = ["row_number", "rank", "dense_rank", "percent_rank",
                     "cume_dist", "ntile", "lag", "lead", "first_value",
                     "last_value", "nth_value"]

# timeUnits from vega-lite version 2.4.3
TIMEUNITS = ["utcyear", "utcquarter", "utcmonth", "utcday", "utcdate",
             "utchours", "utcminutes", "utcseconds", "utcmilliseconds",
             "utcyearquarter", "utcyearquartermonth", "utcyearmonth",
             "utcyearmonthdate", "utcyearmonthdatehours",
             "utcyearmonthdatehoursminutes",
             "utcyearmonthdatehoursminutesseconds",
             "utcquartermonth", "utcmonthdate", "utchoursminutes",
             "utchoursminutesseconds", "utcminutesseconds",
             "utcsecondsmilliseconds",
             "year", "quarter", "month", "day", "date", "hours", "minutes",
             "seconds", "milliseconds", "yearquarter", "yearquartermonth",
             "yearmonth", "yearmonthdate", "yearmonthdatehours",
             "yearmonthdatehoursminutes",
             "yearmonthdatehoursminutesseconds", "quartermonth", "monthdate",
             "hoursminutes", "hoursminutesseconds", "minutesseconds",
             "secondsmilliseconds"]


def infer_vegalite_type(data):
    """
    From an array-like input, infer the correct vega typecode
    ('ordinal', 'nominal', 'quantitative', or 'temporal')

    Parameters
    ----------
    data: Numpy array or Pandas Series
    """
    # Otherwise, infer based on the dtype of the input
    typ = infer_dtype(data)

    # TODO: Once this returns 'O', please update test_select_x and test_select_y in test_api.py

    if typ in ['floating', 'mixed-integer-float', 'integer',
               'mixed-integer', 'complex']:
        return 'quantitative'
    elif typ in ['string', 'bytes', 'categorical', 'boolean', 'mixed', 'unicode']:
        return 'nominal'
    elif typ in ['datetime', 'datetime64', 'timedelta',
                 'timedelta64', 'date', 'time', 'period']:
        return 'temporal'
    else:
        warnings.warn("I don't know how to infer vegalite type from '{}'.  "
                      "Defaulting to nominal.".format(typ))
        return 'nominal'


def sanitize_dataframe(df):
    """Sanitize a DataFrame to prepare it for serialization.

    * Make a copy
    * Convert RangeIndex columns to strings
    * Raise ValueError if column names are not strings
    * Raise ValueError if it has a hierarchical index.
    * Convert categoricals to strings.
    * Convert np.bool_ dtypes to Python bool objects
    * Convert np.int dtypes to Python int objects
    * Convert floats to objects and replace NaNs/infs with None.
    * Convert DateTime dtypes into appropriate string representations
    * Raise a ValueError for TimeDelta dtypes
    """
    df = df.copy()

    if isinstance(df.columns, pd.RangeIndex):
        df.columns = df.columns.astype(str)

    for col in df.columns:
        if not isinstance(col, six.string_types):
            raise ValueError('Dataframe contains invalid column name: {0!r}. '
                             'Column names must be strings'.format(col))

    if isinstance(df.index, pd.MultiIndex):
        raise ValueError('Hierarchical indices not supported')
    if isinstance(df.columns, pd.MultiIndex):
        raise ValueError('Hierarchical indices not supported')

    def to_list_if_array(val):
        if isinstance(val, np.ndarray):
            return val.tolist()
        else:
            return val

    for col_name, dtype in df.dtypes.iteritems():
        if str(dtype) == 'category':
            # XXXX: work around bug in to_json for categorical types
            # https://github.com/pydata/pandas/issues/10778
            col = df[col_name].astype(object)
            df[col_name] = col.where(col.notnull(), None)
        elif str(dtype) == 'bool':
            # convert numpy bools to objects; np.bool is not JSON serializable
            df[col_name] = df[col_name].astype(object)
        elif str(dtype).startswith('datetime'):
            # Convert datetimes to strings. This needs to be a full ISO string
            # with time, which is why we cannot use ``col.astype(str)``.
            # This is because Javascript parses date-only times in UTC, but
            # parses full ISO-8601 dates as local time, and dates in Vega and
            # Vega-Lite are displayed in local time by default.
            # (see https://github.com/altair-viz/altair/issues/1027)
            df[col_name] = df[col_name].apply(lambda x: x.isoformat()).replace('NaT', '')
        elif str(dtype).startswith('timedelta'):
            raise ValueError('Field "{col_name}" has type "{dtype}" which is '
                             'not supported by Altair. Please convert to '
                             'either a timestamp or a numerical value.'
                             ''.format(col_name=col_name, dtype=dtype))
        elif np.issubdtype(dtype, np.integer):
            # convert integers to objects; np.int is not JSON serializable
            df[col_name] = df[col_name].astype(object)
        elif np.issubdtype(dtype, np.floating):
            # For floats, convert to Python float: np.float is not JSON serializable
            # Also convert NaN/inf values to null, as they are not JSON serializable
            col = df[col_name]
            bad_values = col.isnull() | np.isinf(col)
            df[col_name] = col.astype(object).where(~bad_values, None)
        elif dtype == object:
            # Convert numpy arrays saved as objects to lists
            # Arrays are not JSON serializable
            col = df[col_name].apply(to_list_if_array, convert_dtype=False)
            df[col_name] = col.where(col.notnull(), None)
    return df


def parse_shorthand(shorthand, data=None, parse_aggregates=True,
                    parse_window_ops=False,
                    parse_timeunits=True, parse_types=True):
    """General tool to parse shorthand values

    These are of the form:

    - "col_name"
    - "col_name:O"
    - "average(col_name)"
    - "average(col_name):O"

    Optionally, a dataframe may be supplied, from which the type
    will be inferred if not specified in the shorthand.

    Parameters
    ----------
    shorthand : dict or string
        The shorthand representation to be parsed
    data : DataFrame, optional
        If specified and of type DataFrame, then use these values to infer the
        column type if not provided by the shorthand.
    parse_aggregates : boolean
        If True (default), then parse aggregate functions within the shorthand.
    parse_window_ops : boolean
        If True then parse window operations within the shorthand (default:False)
    parse_timeunits : boolean
        If True (default), then parse timeUnits from within the shorthand
    parse_types : boolean
        If True (default), then parse typecodes within the shorthand

    Returns
    -------
    attrs : dict
        a dictionary of attributes extracted from the shorthand

    Examples
    --------
    >>> data = pd.DataFrame({'foo': ['A', 'B', 'A', 'B'],
    ...                      'bar': [1, 2, 3, 4]})

    >>> parse_shorthand('name') == {'field': 'name'}
    True

    >> parse_shorthand('name:Q') == {'field': 'name', 'type': 'quantitative'}
    True

    >>> parse_shorthand('average(col)') == {'aggregate': 'average', 'field': 'col'}
    True

    >>> parse_shorthand('foo:O') == {'field': 'foo', 'type': 'ordinal'}
    True

    >>> parse_shorthand('min(foo):Q') == {'aggregate': 'min', 'field': 'foo', 'type': 'quantitative'}
    True

    >>> parse_shorthand('month(col)') == {'field': 'col', 'timeUnit': 'month', 'type': 'temporal'}
    True

    >>> parse_shorthand('year(col):O') == {'field': 'col', 'timeUnit': 'year', 'type': 'ordinal'}
    True

    >>> parse_shorthand('foo', data) == {'field': 'foo', 'type': 'nominal'}
    True

    >>> parse_shorthand('bar', data) == {'field': 'bar', 'type': 'quantitative'}
    True

    >>> parse_shorthand('bar:O', data) == {'field': 'bar', 'type': 'ordinal'}
    True

    >>> parse_shorthand('sum(bar)', data) == {'aggregate': 'sum', 'field': 'bar', 'type': 'quantitative'}
    True

    >>> parse_shorthand('count()', data) == {'aggregate': 'count', 'type': 'quantitative'}
    True
    """
    if not shorthand:
        return {}

    valid_typecodes = list(TYPECODE_MAP) + list(INV_TYPECODE_MAP)

    units = dict(field='(?P<field>.*)',
                 type='(?P<type>{})'.format('|'.join(valid_typecodes)),
                 count='(?P<aggregate>count)',
                 aggregate='(?P<aggregate>{})'.format('|'.join(AGGREGATES)),
                 window_op='(?P<op>{})'.format('|'.join(AGGREGATES + WINDOW_AGGREGATES)),
                 timeUnit='(?P<timeUnit>{})'.format('|'.join(TIMEUNITS)))

    patterns = []

    if parse_aggregates or parse_window_ops:
        patterns.extend([r'{count}\(\)'])
    if parse_aggregates:
        patterns.extend([r'{aggregate}\({field}\)'])
    if parse_window_ops:
        patterns.extend([r'{window_op}\({field}\)'])
    if parse_timeunits:
        patterns.extend([r'{timeUnit}\({field}\)'])

    patterns.extend([r'{field}'])

    if parse_types:
        patterns = list(itertools.chain(*((p + ':{type}', p) for p in patterns)))

    regexps = (re.compile('\A' + p.format(**units) + '\Z', re.DOTALL)
               for p in patterns)

    # find matches depending on valid fields passed
    if isinstance(shorthand, dict):
        attrs = shorthand
    else:
        attrs = next(exp.match(shorthand).groupdict() for exp in regexps
                     if exp.match(shorthand))

    # Handle short form of the type expression
    if 'type' in attrs:
        attrs['type'] = INV_TYPECODE_MAP.get(attrs['type'], attrs['type'])

    # counts are quantitative by default
    if attrs == {'aggregate': 'count'}:
        attrs['type'] = 'quantitative'

    # times are temporal by default
    if 'timeUnit' in attrs and 'type' not in attrs:
        attrs['type'] = 'temporal'

    # if data is specified and type is not, infer type from data
    if isinstance(data, pd.DataFrame) and 'type' not in attrs:
        if 'field' in attrs and attrs['field'] in data.columns:
            attrs['type'] = infer_vegalite_type(data[attrs['field']])
    return attrs


def use_signature(Obj):
    """Apply call signature and documentation of Obj to the decorated method"""
    def decorate(f):
        # call-signature of f is exposed via __wrapped__.
        # we want it to mimic Obj.__init__
        f.__wrapped__ = Obj.__init__
        f._uses_signature = Obj

        # Supplement the docstring of f with information from Obj
        doclines = Obj.__doc__.splitlines()
        if f.__doc__:
            doc = f.__doc__ + '\n'.join(doclines[1:])
        else:
            doc = '\n'.join(doclines)
        try:
            f.__doc__ = doc
        except AttributeError:
            # __doc__ is not modifiable for classes in Python < 3.3
            pass
        return f
    return decorate


def update_subtraits(obj, attrs, **kwargs):
    """Recursively update sub-traits without overwriting other traits"""
    # TODO: infer keywords from args
    if not kwargs:
        return obj

    # obj can be a SchemaBase object or a dict
    if obj is Undefined:
        obj = dct = {}
    elif isinstance(obj, SchemaBase):
        dct = obj._kwds
    else:
        dct = obj

    if isinstance(attrs, six.string_types):
        attrs = (attrs,)

    if len(attrs) == 0:
        dct.update(kwargs)
    else:
        attr = attrs[0]
        trait = dct.get(attr, Undefined)
        if trait is Undefined:
            trait = dct[attr] = {}
        dct[attr] = update_subtraits(trait, attrs[1:], **kwargs)
    return obj


def update_nested(original, update, copy=False):
    """Update nested dictionaries

    Parameters
    ----------
    original : dict
        the original (nested) dictionary, which will be updated in-place
    update : dict
        the nested dictionary of updates
    copy : bool, default False
        if True, then copy the original dictionary rather than modifying it

    Returns
    -------
    original : dict
        a reference to the (modified) original dict

    Examples
    --------
    >>> original = {'x': {'b': 2, 'c': 4}}
    >>> update = {'x': {'b': 5, 'd': 6}, 'y': 40}
    >>> update_nested(original, update)  # doctest: +SKIP
    {'x': {'b': 5, 'c': 4, 'd': 6}, 'y': 40}
    >>> original  # doctest: +SKIP
    {'x': {'b': 5, 'c': 4, 'd': 6}, 'y': 40}
    """
    if copy:
        original = deepcopy(original)
    for key, val in update.items():
        if isinstance(val, collections.Mapping):
            orig_val = original.get(key, {})
            if isinstance(orig_val, collections.Mapping):
                original[key] = update_nested(orig_val, val)
            else:
                original[key] = val
        else:
            original[key] = val
    return original


def display_traceback(in_ipython=True):
    exc_info = sys.exc_info()

    if in_ipython:
        from IPython.core.getipython import get_ipython
        ip = get_ipython()
    else:
        ip = None

    if ip is not None:
        ip.showtraceback(exc_info)
    else:
        traceback.print_exception(*exc_info)
