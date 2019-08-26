# flake8: noqa
__version__ = '3.3.0dev0'

from .vegalite import *
from . import examples

def load_ipython_extension(ipython):
    from ._magics import vega, vegalite
    ipython.register_magic_function(vega, 'cell')
    ipython.register_magic_function(vegalite, 'cell')


def plot(*args, **kwargs):
    raise NotImplementedError('''To use Altair as an engine for pandas, install altair-pandas package:\n\npip install git+https://github.com/altair-viz/altair_pandas''')  
