import json
import os
from .core import ConstExpression


# This maps vega expression constant names to the Python name
NAME_MAP = {}


def _populate_namespace():
    all_ = []
    with open(os.path.join(os.path.dirname(__file__), 'const_listing.json')) as f:
        const_listing = json.load(f)
    for name, doc in const_listing.items():
        globals()[NAME_MAP.get(name, name)] = ConstExpression(name, doc)
        all_.append(NAME_MAP.get(name, name))
    return all_

__all__ = _populate_namespace()
