"""
Utility routines
"""


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
    type_map = {'ordinal': 'O',
                'nominal': 'N',
                'quantity': 'Q',
                'time': 'T'}
    valid_types = list(type_map.keys()) + list(type_map.values())
    if typ is not None and typ not in valid_types:
        raise ValueError('Invalid type code: "{0}".\n'
                         'Valid values are {1}'.format(typ, valid_types))
    typ = type_map.get(typ, typ)

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
