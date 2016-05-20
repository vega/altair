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

    def to_dict(self):
        result = {}
        for k in self.traits():
            if k in self and k not in self.skip:
                v = getattr(self, k)
                if v is not None:
                    if isinstance(v, BaseObject):
                        result[k] = v.to_dict()
                    else:
                        result[k] = v
        return result
