import json
import os
from .core import ConstExpression


def _populate_namespace():
    all_ = []
    with open(os.path.join(os.path.dirname(__file__), 'const_listing.json')) as f:
        const_listing = json.load(f)
    for name, doc in const_listing.items():
        globals()[name] = ConstExpression(name, doc)
        all_.append(name)
    return all_

__all__ = _populate_namespace()
