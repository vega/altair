"""
Utility routines
"""
import numpy as np
import pandas as pd

TYPECODE_MAP = {'ordinal': 'O',
                'nominal': 'N',
                'quantity': 'Q',
                'time': 'T'}


def parse_shorthand(sh):
    """
    Parse strings of the form

    - "col_name"
    - "col_name:O"
    - "avg(col_name)"
    - "avg(col_name):O"

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
    result = {'type': typ}
    if agg:
        result['aggregate']=agg
    if name:
        result['name']=name
    return result


def infer_type(data, name=None):
    # See if we can read the type from the name
    if name is not None:
        parsed = parse_shorthand(name)
        if result.get('type'):
            return result['type']

    # Otherwise, infer based on the dtype of the input
    data = np.asarray(data)
    typ = pd.lib.infer_dtype(data)

    if typ in ['floating', 'mixed-integer-float', 'complex']:
        typecode = 'quantity'
    elif typ in ['integer', 'mixed-integer']:
        if len(np.unique(data)) > 10:
            typecode = 'quantity'
        else:
            typecode = 'ordinal'
    elif typ in ['string', 'bytes', 'categorical', 'boolean', 'mixed']:
        typecode = 'nominal'
    elif typ in ['datetime', 'datetime64', 'timedelta',
                 'timedelta64', 'date', 'time', 'period']:
        typecode = 'time'
    else:
        warnings.warn("I don't know how to infer vega type from {0}.  "
                      "Defaulting to nominal.".format(typ))
        typecode = 'nominal'

    return TYPECODE_MAP[typecode]
