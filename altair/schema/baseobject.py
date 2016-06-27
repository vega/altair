import pandas as pd
import traitlets as T

from ..utils._py3k_compat import string_types

_attr_template = "Attribute not found: {0}. Valid keyword arguments for this class: {1}"


class BaseObject(T.HasTraits):

    skip = []

    def __init__(self, **kwargs):
        all_traits = list(self.traits())
        for k in kwargs:
            if k not in all_traits:
                raise KeyError(_attr_template.format(k, all_traits))
        super(BaseObject, self).__init__(**kwargs)

    @classmethod
    def infer_keywords(cls, *args, **kwargs):
        """Utility to initialize object from args and kwargs

        Arguments are converted to keyword arguments by inferring the keyword
        from their type.
        Keyword arguments are converted to the correct Instance class
        if required.
        """
        def get_class(trait):
            # TODO: what do do with lists?
            if isinstance(trait, T.Union):
                for klass in map(get_class, trait.trait_types):
                    if klass:
                        return klass
            elif isinstance(trait, T.Instance):
                return trait.klass

        traits = cls.class_traits()
        classes = {n: get_class(t) for n, t in traits.items()}

        # Turn all keyword arguments to the appropriate class
        for name, arg in kwargs.items():
            Trait = classes.get(name, None)
            if Trait is not None and not isinstance(arg, Trait):
                try:
                    kwargs[name] = Trait(arg)
                except (TypeError, T.TraitError):
                    pass  # errors will handled by traitlets below

        # find forward/backward mapping among unique classes
        name_to_trait = {}
        while classes:
            name, trait = classes.popitem()
            if trait is None:
                continue
            if trait not in set.union(set(classes.values()),
                                      set(name_to_trait.values())):
                name_to_trait[name] = trait
        trait_to_name = {t: n for n, t in name_to_trait.items()}

        # Update all arguments
        for arg in args:
            name = trait_to_name.get(type(arg), None)
            if name is None:
                raise ValueError("{0}: Unable to infer argument name for {1}".format(cls, arg))
            elif name in kwargs:
                raise ValueError("{0}: {1} specified both by arg and kwarg".format(cls, name))
            else:
                kwargs[name] = arg
        return kwargs

    def update_traits(self, **kwargs):
        for key, val in kwargs.items():
            self.set_trait(key, val)
        return self

    def update_inferred_traits(self, *args, **kwargs):
        kwargs = self.infer_keywords(*args, **kwargs)
        return self.update_traits(**kwargs)

    def update_subtraits(self, attrs, *args, **kwargs):
        """Update sub-traits without overwriting other traits"""
        if not (args or kwargs):
            return self
        if isinstance(attrs, string_types):
            attrs = (attrs,)
        if len(attrs) == 0:
            self.update_inferred_traits(*args, **kwargs)
        else:
            attr = attrs[0]
            if attr not in self.traits():
                raise ValueError('{0} has no trait {1}'.format(self, attr))
            trait = getattr(self, attr)
            if trait is None:
                trait = self.traits()[attr].klass()
            setattr(self, attr, trait.update_subtraits(attrs[1:], *args, **kwargs))
        return self

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
        return list(self.traits())

    @classmethod
    def from_dict(cls, dct):
        """Instantiate the object from a valid JSON dictionary"""
        from ..utils.visitors import FromDict
        return FromDict().clsvisit(cls, dct)

    def to_dict(self, data=True):
        """Emit the JSON representation for this object as as dict."""
        from ..utils.visitors import ToDict
        self._finalize()
        return ToDict().visit(self, data)

    def _finalize(self, **kwargs):
        """Finalize the object, and all contained objects, for export."""
        def finalize_obj(obj):
            if isinstance(obj, BaseObject):
                obj._finalize(**kwargs)
            elif isinstance(obj, list):
                for item in obj:
                    finalize_obj(item)

        for name in self.traits():
            value = getattr(self, name)
            finalize_obj(value)
