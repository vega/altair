# flake8: noqa
import sys

__version__ = "4.3.0.dev0"

from .vegalite import *


def load_ipython_extension(ipython):
    from ._magics import vega, vegalite

    ipython.register_magic_function(vega, "cell")
    ipython.register_magic_function(vegalite, "cell")


# Setting __all__ and __dir__ without deprecated attributes tries to hide them
# from code completion suggestions
__all__ = [
    x
    for x in dir(sys.modules[__name__])
    if not getattr(getattr(sys.modules[__name__], x), "_deprecated", False)
]


def __dir__():
    return __all__
