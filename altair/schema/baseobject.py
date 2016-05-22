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

    def to_altair(self, tablevel=0, extra_args=None,
                  extra_kwds=None, ignore=None):
        """Export string of Python code to recreate object"""
        signature = '{0}('.format(self.__class__.__name__)
        if extra_args:
            signature += ', '.join(extra_args) + ', '
        if extra_kwds:
            signature += ', '.join('{0}={1}'.format(k, v)
                                   for k, v in sorted(extra_kwds.items()))
            signature += ', '
        code = [signature.rstrip()]

        if ignore is None:
            ignore = []

        kwarg_count = 0
        for k in sorted(self.traits()):
            if k in self and k not in self.skip and k not in ignore:
                kwarg_count += 1
                v = getattr(self, k)
                if v is None:
                    pass
                elif isinstance(v, BaseObject):
                    vcode = v.to_altair(tablevel + 4)
                    code.append('    {0}={1},'.format(k, vcode))
                else:
                    code.append('    {0}={1},'.format(k, repr(v)))
        if kwarg_count == 0:
            code[-1] = code[-1].rstrip(',') + ')'
        else:
            code.append(')')

        return ('\n' + ' ' * tablevel).join(code)

    @classmethod
    def from_json(cls, jsn):
        """Initialize object from a suitable JSON string"""
        return cls.from_dict(json.loads(jsn))

    @classmethod
    def from_dict(cls, dct):
        """Initialize a Layer from a vegalite JSON dictionary"""
        try:
            obj = cls()
        except TypeError as err:
            # TypeError indicates that an argument is missing
            obj = cls('')

        for prop, val in dct.items():
            if not obj.has_trait(prop):
                raise ValueError("{0} not a valid property in {1}"
                                 "".format(prop, cls))
            else:
                trait = obj.traits()[prop]
                if isinstance(trait, T.Instance):
                    obj.set_trait(prop, trait.klass.from_dict(val))
                else:
                    obj.set_trait(prop, val)
        return obj

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
