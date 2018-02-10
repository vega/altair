"""Tools for generating transformation expressions with a dataframe syntax"""

from .core import DataFrame, Expression
from .funcs import *
from .consts import *

# This object provides lazily-evaluated dataframe-like operations
# useful for any data source.
df = DataFrame('anonymous', cols=None, read_only=True)
