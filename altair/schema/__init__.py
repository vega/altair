from ._interface import *
from ._schema import SCHEMA_FILE, load_schema
from ._vegalite_version import vegalite_version
from . import visitors

from ._interface import jstraitlets
jstraitlets.JSONHasTraits.register_converters(to_dict=visitors.ToDict,
                                              from_dict=visitors.FromDict)
