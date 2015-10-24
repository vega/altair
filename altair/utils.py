"""
Utility routines
"""
import warnings

import pandas as pd
import traitlets as T

TYPECODE_MAP = {'ordinal': 'O',
                'nominal': 'N',
                'quantity': 'Q',
                'time': 'T'}


def parse_shorthand(sh):
    """
    Altair accepts a shorthand expression for aggregation, name, and type.

    Parse strings of the form

    - "col_name"
    - "col_name:O"
    - "avg(col_name)"
    - "avg(col_name):O"

    Parameters
    ----------
    sh: str
    """
    # TODO: use an actual parser for this?

    # extract type code
    L = sh.split(':')
    sh0 = L[0].strip()
    if len(L) == 1:
        typ = None
    elif len(L) == 2:
        typ = L[1].strip()
    else:
        raise ValueError('Multiple colons not valid in data specification:'
                         '{0}'.format(sh))

    # find aggregate
    if not sh0.endswith(')'):
        agg, name = None, sh0
    else:
        L = sh0[:-1].split('(')
        if len(L) == 2:
            agg, name = L
        else:
            raise ValueError("Unmatched parentheses")

    # validate & store type code
    valid_types = list(TYPECODE_MAP.keys()) + list(TYPECODE_MAP.values())
    if typ is not None and typ not in valid_types:
        raise ValueError('Invalid type code: "{0}".\n'
                         'Valid values are {1}'.format(typ, valid_types))
    typ = TYPECODE_MAP.get(typ, typ)

    # validate & store aggregate
    valid_aggs = ['avg', 'sum', 'median', 'min', 'max', 'count']
    if agg is not None and agg not in valid_aggs:
        raise ValueError('Invalid aggregate: "{0}()".\n'
                         'Valid values are {1}'.format(agg, valid_aggs))

    # encode and return the results
    result = {}
    if typ:
        result['type'] = typ
    if agg:
        result['aggregate'] = agg
    if name:
        result['name'] = name
    return result


def infer_vegalite_type(data, name=None):
    """
    From an array-like input, infer the correct vega typecode
    ('O', 'N', 'Q', or 'T')

    Parameters
    ----------
    data: Numpy array or Pandas Series
    name: str
    """
    # See if we can read the type from the name
    if name is not None:
        parsed = parse_shorthand(name)
        if parsed.get('type'):
            return parsed['type']

    # Otherwise, infer based on the dtype of the input
    typ = pd.lib.infer_dtype(data)

    # TODO: Once this returns 'O', please update test_select_x and test_select_y in test_api.py

    if typ in ['floating', 'mixed-integer-float', 'integer',
               'mixed-integer', 'complex']:
        typecode = 'quantity'
    elif typ in ['string', 'bytes', 'categorical', 'boolean', 'mixed', 'unicode']:
        typecode = 'nominal'
    elif typ in ['datetime', 'datetime64', 'timedelta',
                 'timedelta64', 'date', 'time', 'period']:
        typecode = 'time'
    else:
        warnings.warn("I don't know how to infer vega type from '{0}'.  "
                      "Defaulting to nominal.".format(typ))
        typecode = 'nominal'

    return TYPECODE_MAP[typecode]


class DataFrameTrait(T.Any):
    """A custom TraitType for pandas.DataFrame or other similar labeled data.
    
    This mainly exists for objects where == doesn't make sense for comparison.
    """
    
    default_value = None
    allow_none = True
    info_text = 'a pandas.DataFrame or similar object'

    def set(self, obj, value):
        new_value = self._validate(obj, value)
        try:
            old_value = obj._trait_values[self.name]
        except KeyError:
            old_value = self.default_value

        obj._trait_values[self.name] = new_value
        try:
            silent = bool(id(old_value) == id(new_value))
        except:
            # if there is an error in comparing, default to notify
            pass
        #     raise
            silent = False
        if silent is not True:
            # we explicitly compare silent to True just in case the equality
            # comparison above returns something other than True/False
            obj._notify_trait(self.name, old_value, new_value)
