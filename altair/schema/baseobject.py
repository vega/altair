import pandas as pd

try:
    import traitlets as T
except ImportError:
    from IPython.utils import traitlets as T


class BaseObject(T.HasTraits):

    skip = []

    def __contains__(self, key):
        value = getattr(self, key)
        if isinstance(value, pd.DataFrame):
            return True
        return ((value is not None)
                and (not (not isinstance(value, bool) and not value)))

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

    def __repr__(self):
        return repr(self.to_dict())
