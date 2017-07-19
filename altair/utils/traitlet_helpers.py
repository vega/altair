"""
Helpers for working with traitlet-based classes.

In particular, these helpers help with instantiation of HasTraits object
hierarchies from dictionaries and lists of trait names.
"""
import six
import traitlets as T


def infer_keywords(cls, *args, **kwargs):
    """Utility to initialize a HasTraits object from args and kwargs

    Arguments are converted to keyword arguments by inferring the keyword
    from their type.
    Keyword arguments are converted to the correct Instance class
    if required.
    """
    # TODO: can we make this more efficient & less fragile?
    def is_simple_union(trait):
        """Return True if trait is, e.g. Union(Class, List(Class))"""
        return (isinstance(trait, T.Union) and
                len(trait.trait_types) == 2 and
                isinstance(trait.trait_types[0], T.Instance) and
                isinstance(trait.trait_types[1], T.List) and
                trait.trait_types[0].klass == trait.trait_types[1]._trait.klass)

    # TODO: make this less brittle
    def get_class(trait):
        if isinstance(trait, T.Instance):
            return trait.klass
        elif is_simple_union(trait):
            return trait.trait_types[0].klass
        else:
            return None

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


def update_traits(obj, **kwargs):
    """Convenience routine to call set_trait() with a dictionary of values"""
    for key, val in kwargs.items():
        obj.set_trait(key, val)
    return obj


def update_inferred_traits(obj, *args, **kwargs):
    """Infer types from positional arguments and update traits of obj"""
    kwargs = infer_keywords(obj, *args, **kwargs)
    return update_traits(obj, **kwargs)


def update_subtraits(obj, attrs, *args, **kwargs):
    """Recursively update sub-traits without overwriting other traits"""
    if not (args or kwargs):
        return obj
    if isinstance(attrs, six.string_types):
        attrs = (attrs,)
    if len(attrs) == 0:
        update_inferred_traits(obj, *args, **kwargs)
    else:
        attr = attrs[0]
        trait = getattr(obj, attr)  # error here if attr is not present
        if trait is None:
            trait = obj.traits()[attr].klass()
        setattr(obj, attr, update_subtraits(trait, attrs[1:], *args, **kwargs))
    return obj
