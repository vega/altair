"""
Magic functions for rendering vega/vega-lite specifications
"""
import json

import IPython
from IPython.core import magic, magic_arguments

from altair.utils import sanitize_dataframe
from altair.vegalite.v1 import VegaLite as VegaLiteV1
from altair.vegalite.v2 import VegaLite as VegaLiteV2
from altair.vega.v2 import Vega as VegaV2
from altair.vega.v3 import Vega as VegaV3

RENDERERS = {
  'vega': {
      '2': VegaV2,
      '3': VegaV3
  },
  'vega-lite': {
      '1': VegaLiteV1,
      '2': VegaLiteV2
  }
}


def _to_jsondict(df):
    """Convert a dataframe to a JSON dictionary."""
    return sanitize_dataframe(df).to_dict(orient='records')


def _get_variable(name):
    """Get a variable from the notebook namespace."""
    ip = IPython.get_ipython()
    if name not in ip.user_ns:
        raise NameError("argument '{0}' does not match the "
                        "name of any defined variable".format(name))
    return ip.user_ns[name]


@magic.register_cell_magic
@magic_arguments.magic_arguments()
@magic_arguments.argument(
    'data',
    nargs='*',
    help='local variable name of a pandas DataFrame to be used as the dataset')
@magic_arguments.argument('-v', '--version', dest='version', default='3')
@magic_arguments.argument('-y', '--yaml', dest='yaml', action='store_true')
def vega(line, cell):
    """Cell magic for displaying Vega visualizations in CoLab.

    %%vega [name1:variable1 name2:variable2 ...] [--yaml] [--version='3']

    Visualize the contents of the cell using Vega, optionally specifying
    one or more pandas DataFrame objects to be used as the datasets.

    If --yaml is passed, then input is parsed as yaml rather than json.
    """
    args = magic_arguments.parse_argstring(vega, line)

    version = args.version
    assert version in RENDERERS['vega']
    Vega = RENDERERS['vega'][version]

    def namevar(s):
        s = s.split(':')
        if len(s) == 1:
            return s[0], s[0]
        elif len(s) == 2:
            return s[0], s[1]
        else:
            raise ValueError("invalid identifier: '{0}'".format(s))

    try:
        data = list(map(namevar, args.data))
    except ValueError:
        raise ValueError("Could not parse arguments: '{0}'".format(line))

    if args.yaml:
        import yaml
        spec = yaml.load(cell)
    else:
        spec = json.loads(cell)

    if data:
        spec['data'] = [{
            'name': name,
            'values': _to_jsondict(_get_variable(val))
        } for name, val in data]

    return Vega(spec)


@magic.register_cell_magic
@magic_arguments.magic_arguments()
@magic_arguments.argument(
    'data',
    nargs='?',
    help='local variablename of a pandas DataFrame to be used as the dataset')
@magic_arguments.argument('-v', '--version', dest='version', default='2')
@magic_arguments.argument('-y', '--yaml', dest='yaml', action='store_true')
def vegalite(line, cell):
    """Cell magic for displaying vega-lite visualizations in CoLab.

    %%vegalite [dataframe] [--yaml] [--version=2]

    Visualize the contents of the cell using Vega-Lite, optionally
    specifying a pandas DataFrame object to be used as the dataset.

    if --yaml is passed, then input is parsed as yaml rather than json.
    """
    args = magic_arguments.parse_argstring(vegalite, line)
    version = args.version
    assert version in RENDERERS['vega-lite']
    VegaLite = RENDERERS['vega-lite'][version]

    if args.yaml:
        import yaml
        spec = yaml.load(cell)
    else:
        spec = json.loads(cell)
    if args.data is not None:
        spec['data'] = {'values': _to_jsondict(_get_variable(args.data))}

    return VegaLite(spec)
