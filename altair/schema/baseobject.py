import pandas as pd

try:
    import traitlets as T
except ImportError:
    from IPython.utils import traitlets as T


class BaseObject(T.HasTraits):

    skip = []

    def __contains__(self, key):
        try:
            value = getattr(self, key)
        except AttributeError:
            return False

        # comparison to None will break, so check DataFrame specifically
        if isinstance(value, pd.DataFrame):
            return True
        elif value is not None:
            if isinstance(value, (int, float, bool)):
                return True
            else:
                return bool(value)
        else:
            return False

    def __dir__(self):
        """Customize tab completed attributes."""
        return list(self.traits())+['to_dict']

    def to_dict(self):
        result = {}
        for k in self.traits():
            if k in self and k not in self.skip:
                v = getattr(self, k)
                if v is not None:
                    result[k] = trait_to_dict(v)
        return result


def trait_to_dict(obj):
    """Recursively convert object to dictionary"""
    if isinstance(obj, BaseObject):
        return obj.to_dict()
    elif isinstance(obj, list):
        return [trait_to_dict(o) for o in obj]
    else:
        return obj
