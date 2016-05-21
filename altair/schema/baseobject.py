import pandas as pd

try:
    import traitlets as T
except ImportError:
    from IPython.utils import traitlets as T


_attr_template = "Attribute not found: {0}. Valid keyword arguments for this class: {1}"

class BaseObject(T.HasTraits):

    skip = []

    def __init__(self, **kwargs):
        all_traits = list(self.traits())
        for k in kwargs:
            if k not in all_traits:
                raise KeyError(_attr_template.format(k, all_traits))
        super(BaseObject, self).__init__(**kwargs)

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

    def update_traits(self, **kwargs):
        for key, val in kwargs.items():
            self.set_trait(key, val)
        return self


def trait_to_dict(obj):
    """Recursively convert object to dictionary"""
    if isinstance(obj, BaseObject):
        return obj.to_dict()
    elif isinstance(obj, list):
        return [trait_to_dict(o) for o in obj]
    else:
        return obj


#############################################################################
# Hack to make traitlet arguments tab-complete in IPython

from IPython.core.completer import IPCompleter
from IPython.core.getipython import get_ipython

class TraitletIPCompleter(IPCompleter):
    def _default_arguments(self, obj):
        args = super(TraitletIPCompleter, self)._default_arguments(obj)
        if isinstance(obj, type) and issubclass(obj, BaseObject):
            args.extend(obj.class_trait_names())
        return list(set(args))

def enable_traitlet_completer():
    ip = get_ipython()
    if ip is not None:
        ip.Completer.__class__ = TraitletIPCompleter

enable_traitlet_completer()
