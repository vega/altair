import json

import pandas as pd
import traitlets as T

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
            trait = obj.traits()[prop]
            obj.set_trait(prop, trait_from_dict(trait, val))
        return obj

    def update_traits(self, **kwargs):
        for key, val in kwargs.items():
            self.set_trait(key, val)
        return self


def trait_from_dict(trait, dct):
    """
    Construct a trait from a dictionary.
    If dct is not a dictionary or list, pass it through
    """
    if isinstance(trait, T.List):
        return [trait_from_dict(trait._trait, item) for item in dct]
    elif not isinstance(dct, dict):
        return dct
    elif isinstance(trait, T.Instance):
        return trait.klass.from_dict(dct)
    elif isinstance(trait, T.Union):
        for subtrait in trait.trait_types:
            try:
                return trait_from_dict(subtrait, dct)
            except T.TraitError:
                pass

    raise T.TraitError('cannot set {0} to {1}'.format(trait, dct))
