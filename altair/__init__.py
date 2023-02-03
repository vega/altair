# flake8: noqa
__version__ = "4.3.0.dev0"

from .vegalite import *


def load_ipython_extension(ipython):
    from ._magics import vegalite

    ipython.register_magic_function(vegalite, "cell")
