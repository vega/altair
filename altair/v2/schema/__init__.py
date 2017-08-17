from ._interface import *
from ._schema import SCHEMA_FILE, load_schema
from ._vegalite_version import vegalite_version, vegalite_schema_url
from . import visitors

from ._interface import (jstraitlets, named_channels,
                         channel_wrappers, channel_collections)
jstraitlets.JSONHasTraits.register_converters(to_dict=visitors.ToDict,
                                              from_dict=visitors.FromDict,
                                              to_python=visitors.ToPython)
