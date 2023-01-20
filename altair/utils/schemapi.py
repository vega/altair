# The contents of this file are automatically written by
# tools/generate_schema_wrapper.py. Do not modify directly.
import collections
import contextlib
import inspect
import json
import textwrap
from typing import Any, Sequence, List

import jsonschema
import jsonschema.exceptions
import jsonschema.validators
import numpy as np
import pandas as pd

from altair import vegalite

# If DEBUG_MODE is True, then schema objects are converted to dict and
# validated at creation time. This slows things down, particularly for
# larger specs, but leads to much more useful tracebacks for the user.
# Individual schema classes can override this by setting the
# class-level _class_is_valid_at_instantiation attribute to False
DEBUG_MODE = True


def enable_debug_mode():
    global DEBUG_MODE
    DEBUG_MODE = True


def disable_debug_mode():
    global DEBUG_MODE
    DEBUG_MODE = True


@contextlib.contextmanager
def debug_mode(arg):
    global DEBUG_MODE
    original = DEBUG_MODE
    DEBUG_MODE = arg
    try:
        yield
    finally:
        DEBUG_MODE = original


def validate_jsonschema(spec, schema, rootschema=None):
    # We don't use jsonschema.validate as this would validate the schema itself.
    # Instead, we pass the schema directly to the validator class. This is done for
    # two reasons: The schema comes from Vega-Lite and is not based on the user
    # input, therefore there is no need to validate it in the first place. Furthermore,
    # the "uri-reference" format checker fails for some of the references as URIs in
    # "$ref" are not encoded,
    # e.g. '#/definitions/ValueDefWithCondition<MarkPropFieldOrDatumDef,
    # (Gradient|string|null)>' would be a valid $ref in a Vega-Lite schema but
    # it is not a valid URI reference due to the characters such as '<'.
    if rootschema is not None:
        validator_cls = jsonschema.validators.validator_for(rootschema)
        resolver = jsonschema.RefResolver.from_schema(rootschema)
    else:
        validator_cls = jsonschema.validators.validator_for(schema)
        # No resolver is necessary if the schema is already the full schema
        resolver = None

    validator_kwargs = {"resolver": resolver}
    if hasattr(validator_cls, "FORMAT_CHECKER"):
        validator_kwargs["format_checker"] = validator_cls.FORMAT_CHECKER
    validator = validator_cls(schema, **validator_kwargs)
    errors = list(validator.iter_errors(spec))
    if errors:
        errors = _get_most_relevant_errors(errors)
        main_error = errors[0]
        # They can be used to craft more helpful error messages when this error
        # is being converted to a SchemaValidationError
        main_error._additional_errors = errors[1:]
        raise main_error


def _get_most_relevant_errors(
    errors: Sequence[jsonschema.exceptions.ValidationError],
) -> List[jsonschema.exceptions.ValidationError]:
    if len(errors) == 0:
        return []

    # Go to lowest level in schema where an error happened as these give
    # the most relevant error messages
    lowest_level = errors[0]
    while lowest_level.context:
        lowest_level = lowest_level.context[0]

    most_relevant_errors = []
    if lowest_level.validator == "additionalProperties":
        # For these errors, the message is already informative enough and the other
        # errors on the lowest level are not helpful for a user but instead contain
        # the same information in a more verbose way
        most_relevant_errors = [lowest_level]
    else:
        parent = lowest_level.parent
        if parent is None:
            # In this case we are still at the top level and can return all errors
            most_relevant_errors = errors
        else:
            # Return all errors of the lowest level out of which
            # we can construct more informative error messages
            most_relevant_errors = lowest_level.parent.context

    # This should never happen but might still be good to test for it as else
    # the original error would just slip through without being raised
    if len(most_relevant_errors) == 0:
        raise Exception("Could not determine the most relevant errors") from errors[0]

    return most_relevant_errors


def _subclasses(cls):
    """Breadth-first sequence of all classes which inherit from cls."""
    seen = set()
    current_set = {cls}
    while current_set:
        seen |= current_set
        current_set = set.union(*(set(cls.__subclasses__()) for cls in current_set))
        for cls in current_set - seen:
            yield cls


def _todict(obj, validate, context):
    """Convert an object to a dict representation."""
    if isinstance(obj, SchemaBase):
        return obj.to_dict(validate=validate, context=context)
    elif isinstance(obj, (list, tuple, np.ndarray)):
        return [_todict(v, validate, context) for v in obj]
    elif isinstance(obj, dict):
        return {
            k: _todict(v, validate, context)
            for k, v in obj.items()
            if v is not Undefined
        }
    elif hasattr(obj, "to_dict"):
        return obj.to_dict()
    elif isinstance(obj, np.number):
        return float(obj)
    elif isinstance(obj, (pd.Timestamp, np.datetime64)):
        return pd.Timestamp(obj).isoformat()
    else:
        return obj


def _resolve_references(schema, root=None):
    """Resolve schema references."""
    resolver = jsonschema.RefResolver.from_schema(root or schema)
    while "$ref" in schema:
        with resolver.resolving(schema["$ref"]) as resolved:
            schema = resolved
    return schema


class SchemaValidationError(jsonschema.ValidationError):
    """A wrapper for jsonschema.ValidationError with friendlier traceback"""

    def __init__(self, obj, err):
        super(SchemaValidationError, self).__init__(**err._contents())
        self.obj = obj
        self._additional_errors = getattr(err, "_additional_errors", [])

    def __str__(self):
        cls = self.obj.__class__
        schema_path = ["{}.{}".format(cls.__module__, cls.__name__)]
        schema_path.extend(self.schema_path)
        schema_path = "->".join(
            str(val)
            for val in schema_path[:-1]
            if val not in ("properties", "additionalProperties", "patternProperties")
        )
        message = self.message
        if self._additional_errors:
            message += "\n        " + "\n        ".join(
                [e.message for e in self._additional_errors]
            )
        return """Invalid specification

        {}, validating {!r}

        {}
        """.format(
            schema_path, self.validator, message
        )


class UndefinedType(object):
    """A singleton object for marking undefined attributes"""

    __instance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls.__instance, cls):
            cls.__instance = object.__new__(cls, *args, **kwargs)
        return cls.__instance

    def __repr__(self):
        return "Undefined"


# In the future Altair may implement a more complete set of type hints.
# But for now, we'll add an annotation to indicate that the type checker
# should permit any value passed to a function argument whose default
# value is Undefined.
Undefined: Any = UndefinedType()


class SchemaBase(object):
    """Base class for schema wrappers.

    Each derived class should set the _schema class attribute (and optionally
    the _rootschema class attribute) which is used for validation.
    """

    _schema = None
    _rootschema = None
    _class_is_valid_at_instantiation = True

    def __init__(self, *args, **kwds):
        # Two valid options for initialization, which should be handled by
        # derived classes:
        # - a single arg with no kwds, for, e.g. {'type': 'string'}
        # - zero args with zero or more kwds for {'type': 'object'}
        if self._schema is None:
            raise ValueError(
                "Cannot instantiate object of type {}: "
                "_schema class attribute is not defined."
                "".format(self.__class__)
            )

        if kwds:
            assert len(args) == 0
        else:
            assert len(args) in [0, 1]

        # use object.__setattr__ because we override setattr below.
        object.__setattr__(self, "_args", args)
        object.__setattr__(self, "_kwds", kwds)

        if DEBUG_MODE and self._class_is_valid_at_instantiation:
            self.to_dict(validate=True)

    def copy(self, deep=True, ignore=()):
        """Return a copy of the object

        Parameters
        ----------
        deep : boolean or list, optional
            If True (default) then return a deep copy of all dict, list, and
            SchemaBase objects within the object structure.
            If False, then only copy the top object.
            If a list or iterable, then only copy the listed attributes.
        ignore : list, optional
            A list of keys for which the contents should not be copied, but
            only stored by reference.
        """

        def _shallow_copy(obj):
            if isinstance(obj, SchemaBase):
                return obj.copy(deep=False)
            elif isinstance(obj, list):
                return obj[:]
            elif isinstance(obj, dict):
                return obj.copy()
            else:
                return obj

        def _deep_copy(obj, ignore=()):
            if isinstance(obj, SchemaBase):
                args = tuple(_deep_copy(arg) for arg in obj._args)
                kwds = {
                    k: (_deep_copy(v, ignore=ignore) if k not in ignore else v)
                    for k, v in obj._kwds.items()
                }
                with debug_mode(False):
                    return obj.__class__(*args, **kwds)
            elif isinstance(obj, list):
                return [_deep_copy(v, ignore=ignore) for v in obj]
            elif isinstance(obj, dict):
                return {
                    k: (_deep_copy(v, ignore=ignore) if k not in ignore else v)
                    for k, v in obj.items()
                }
            else:
                return obj

        try:
            deep = list(deep)
        except TypeError:
            deep_is_list = False
        else:
            deep_is_list = True

        if deep and not deep_is_list:
            return _deep_copy(self, ignore=ignore)

        with debug_mode(False):
            copy = self.__class__(*self._args, **self._kwds)
        if deep_is_list:
            for attr in deep:
                copy[attr] = _shallow_copy(copy._get(attr))
        return copy

    def _get(self, attr, default=Undefined):
        """Get an attribute, returning default if not present."""
        attr = self._kwds.get(attr, Undefined)
        if attr is Undefined:
            attr = default
        return attr

    def __getattr__(self, attr):
        # reminder: getattr is called after the normal lookups
        if attr == "_kwds":
            raise AttributeError()
        if attr in self._kwds:
            return self._kwds[attr]
        else:
            try:
                _getattr = super(SchemaBase, self).__getattr__
            except AttributeError:
                _getattr = super(SchemaBase, self).__getattribute__
            return _getattr(attr)

    def __setattr__(self, item, val):
        self._kwds[item] = val

    def __getitem__(self, item):
        return self._kwds[item]

    def __setitem__(self, item, val):
        self._kwds[item] = val

    def __repr__(self):
        if self._kwds:
            args = (
                "{}: {!r}".format(key, val)
                for key, val in sorted(self._kwds.items())
                if val is not Undefined
            )
            args = "\n" + ",\n".join(args)
            return "{0}({{{1}\n}})".format(
                self.__class__.__name__, args.replace("\n", "\n  ")
            )
        else:
            return "{}({!r})".format(self.__class__.__name__, self._args[0])

    def __eq__(self, other):
        return (
            type(self) is type(other)
            and self._args == other._args
            and self._kwds == other._kwds
        )

    def to_dict(self, validate=True, ignore=None, context=None):
        """Return a dictionary representation of the object

        Parameters
        ----------
        validate : boolean or string
            If True (default), then validate the output dictionary
            against the schema. If "deep" then recursively validate
            all objects in the spec. This takes much more time, but
            it results in friendlier tracebacks for large objects.
        ignore : list
            A list of keys to ignore. This will *not* passed to child to_dict
            function calls.
        context : dict (optional)
            A context dictionary that will be passed to all child to_dict
            function calls

        Returns
        -------
        dct : dictionary
            The dictionary representation of this object

        Raises
        ------
        jsonschema.ValidationError :
            if validate=True and the dict does not conform to the schema
        """
        if context is None:
            context = {}
        if ignore is None:
            ignore = []
        sub_validate = "deep" if validate == "deep" else False

        if self._args and not self._kwds:
            result = _todict(self._args[0], validate=sub_validate, context=context)
        elif not self._args:
            kwds = self._kwds.copy()
            # parsed_shorthand is added by FieldChannelMixin.
            # It's used below to replace shorthand with its long form equivalent
            # parsed_shorthand is removed from context if it exists so that it is
            # not passed to child to_dict function calls
            parsed_shorthand = context.pop("parsed_shorthand", {})
            kwds.update(
                {
                    k: v
                    for k, v in parsed_shorthand.items()
                    if kwds.get(k, Undefined) is Undefined
                }
            )
            kwds = {
                k: v for k, v in kwds.items() if k not in list(ignore) + ["shorthand"]
            }
            result = _todict(
                kwds,
                validate=sub_validate,
                context=context,
            )
        else:
            raise ValueError(
                "{} instance has both a value and properties : "
                "cannot serialize to dict".format(self.__class__)
            )
        if validate:
            try:
                self.validate(result)
            except jsonschema.ValidationError as err:
                raise SchemaValidationError(self, err)
        return result

    def to_json(
        self, validate=True, ignore=[], context={}, indent=2, sort_keys=True, **kwargs
    ):
        """Emit the JSON representation for this object as a string.

        Parameters
        ----------
        validate : boolean or string
            If True (default), then validate the output dictionary
            against the schema. If "deep" then recursively validate
            all objects in the spec. This takes much more time, but
            it results in friendlier tracebacks for large objects.
        ignore : list
            A list of keys to ignore. This will *not* passed to child to_dict
            function calls.
        context : dict (optional)
            A context dictionary that will be passed to all child to_dict
            function calls
        indent : integer, default 2
            the number of spaces of indentation to use
        sort_keys : boolean, default True
            if True, sort keys in the output
        **kwargs
            Additional keyword arguments are passed to ``json.dumps()``

        Returns
        -------
        spec : string
            The JSON specification of the chart object.
        """
        dct = self.to_dict(validate=validate, ignore=ignore, context=context)
        return json.dumps(dct, indent=indent, sort_keys=sort_keys, **kwargs)

    @classmethod
    def _default_wrapper_classes(cls):
        """Return the set of classes used within cls.from_dict()"""
        return _subclasses(SchemaBase)

    @classmethod
    def from_dict(cls, dct, validate=True, _wrapper_classes=None):
        """Construct class from a dictionary representation

        Parameters
        ----------
        dct : dictionary
            The dict from which to construct the class
        validate : boolean
            If True (default), then validate the input against the schema.
        _wrapper_classes : list (optional)
            The set of SchemaBase classes to use when constructing wrappers
            of the dict inputs. If not specified, the result of
            cls._default_wrapper_classes will be used.

        Returns
        -------
        obj : Schema object
            The wrapped schema

        Raises
        ------
        jsonschema.ValidationError :
            if validate=True and dct does not conform to the schema
        """
        if validate:
            cls.validate(dct)
        if _wrapper_classes is None:
            _wrapper_classes = cls._default_wrapper_classes()
        converter = _FromDict(_wrapper_classes)
        return converter.from_dict(dct, cls)

    @classmethod
    def from_json(cls, json_string, validate=True, **kwargs):
        """Instantiate the object from a valid JSON string

        Parameters
        ----------
        json_string : string
            The string containing a valid JSON chart specification.
        validate : boolean
            If True (default), then validate the input against the schema.
        **kwargs :
            Additional keyword arguments are passed to json.loads

        Returns
        -------
        chart : Chart object
            The altair Chart object built from the specification.
        """
        dct = json.loads(json_string, **kwargs)
        return cls.from_dict(dct, validate=validate)

    @classmethod
    def validate(cls, instance, schema=None):
        """
        Validate the instance against the class schema in the context of the
        rootschema.
        """
        if schema is None:
            schema = cls._schema
        return validate_jsonschema(
            instance, schema, rootschema=cls._rootschema or cls._schema
        )

    @classmethod
    def resolve_references(cls, schema=None):
        """Resolve references in the context of this object's schema or root schema."""
        return _resolve_references(
            schema=(schema or cls._schema),
            root=(cls._rootschema or cls._schema or schema),
        )

    @classmethod
    def validate_property(cls, name, value, schema=None):
        """
        Validate a property against property schema in the context of the
        rootschema
        """
        value = _todict(value, validate=False, context={})
        props = cls.resolve_references(schema or cls._schema).get("properties", {})
        return validate_jsonschema(
            value, props.get(name, {}), rootschema=cls._rootschema or cls._schema
        )

    def __dir__(self):
        return sorted(super().__dir__() + list(self._kwds.keys()))


def _passthrough(*args, **kwds):
    return args[0] if args else kwds


class _FromDict(object):
    """Class used to construct SchemaBase class hierarchies from a dict

    The primary purpose of using this class is to be able to build a hash table
    that maps schemas to their wrapper classes. The candidate classes are
    specified in the ``class_list`` argument to the constructor.
    """

    _hash_exclude_keys = ("definitions", "title", "description", "$schema", "id")

    def __init__(self, class_list):
        # Create a mapping of a schema hash to a list of matching classes
        # This lets us quickly determine the correct class to construct
        self.class_dict = collections.defaultdict(list)
        for cls in class_list:
            if cls._schema is not None:
                self.class_dict[self.hash_schema(cls._schema)].append(cls)

    @classmethod
    def hash_schema(cls, schema, use_json=True):
        """
        Compute a python hash for a nested dictionary which
        properly handles dicts, lists, sets, and tuples.

        At the top level, the function excludes from the hashed schema all keys
        listed in `exclude_keys`.

        This implements two methods: one based on conversion to JSON, and one based
        on recursive conversions of unhashable to hashable types; the former seems
        to be slightly faster in several benchmarks.
        """
        if cls._hash_exclude_keys and isinstance(schema, dict):
            schema = {
                key: val
                for key, val in schema.items()
                if key not in cls._hash_exclude_keys
            }
        if use_json:
            s = json.dumps(schema, sort_keys=True)
            return hash(s)
        else:

            def _freeze(val):
                if isinstance(val, dict):
                    return frozenset((k, _freeze(v)) for k, v in val.items())
                elif isinstance(val, set):
                    return frozenset(map(_freeze, val))
                elif isinstance(val, list) or isinstance(val, tuple):
                    return tuple(map(_freeze, val))
                else:
                    return val

            return hash(_freeze(schema))

    def from_dict(
        self, dct, cls=None, schema=None, rootschema=None, default_class=_passthrough
    ):
        """Construct an object from a dict representation"""
        if (schema is None) == (cls is None):
            raise ValueError("Must provide either cls or schema, but not both.")
        if schema is None:
            schema = schema or cls._schema
            rootschema = rootschema or cls._rootschema
        rootschema = rootschema or schema

        if isinstance(dct, SchemaBase):
            return dct

        if cls is None:
            # If there are multiple matches, we use the first one in the dict.
            # Our class dict is constructed breadth-first from top to bottom,
            # so the first class that matches is the most general match.
            matches = self.class_dict[self.hash_schema(schema)]
            if matches:
                cls = matches[0]
            else:
                cls = default_class
        schema = _resolve_references(schema, rootschema)

        if "anyOf" in schema or "oneOf" in schema:
            schemas = schema.get("anyOf", []) + schema.get("oneOf", [])
            for possible_schema in schemas:
                try:
                    validate_jsonschema(dct, possible_schema, rootschema=rootschema)
                except jsonschema.ValidationError:
                    continue
                else:
                    return self.from_dict(
                        dct,
                        schema=possible_schema,
                        rootschema=rootschema,
                        default_class=cls,
                    )

        if isinstance(dct, dict):
            # TODO: handle schemas for additionalProperties/patternProperties
            props = schema.get("properties", {})
            kwds = {}
            for key, val in dct.items():
                if key in props:
                    val = self.from_dict(val, schema=props[key], rootschema=rootschema)
                kwds[key] = val
            return cls(**kwds)

        elif isinstance(dct, list):
            item_schema = schema.get("items", {})
            dct = [
                self.from_dict(val, schema=item_schema, rootschema=rootschema)
                for val in dct
            ]
            return cls(dct)
        else:
            return cls(dct)


class _PropertySetter(object):
    def __init__(self, prop, schema):
        self.prop = prop
        self.schema = schema

    def __get__(self, obj, cls):
        self.obj = obj
        self.cls = cls
        # The docs from the encoding class parameter (e.g. `bin` in X, Color,
        # etc); this provides a general description of the parameter.
        self.__doc__ = self.schema["description"].replace("__", "**")
        property_name = f"{self.prop}"[0].upper() + f"{self.prop}"[1:]
        if hasattr(vegalite, property_name):
            altair_prop = getattr(vegalite, property_name)
            # Add the docstring from the helper class (e.g. `BinParams`) so
            # that all the parameter names of the helper class are included in
            # the final docstring
            attribute_index = altair_prop.__doc__.find("Attributes\n")
            if attribute_index > -1:
                self.__doc__ = (
                    altair_prop.__doc__[:attribute_index].replace("    ", "")
                    + self.__doc__
                    + textwrap.dedent(
                        f"\n\n    {altair_prop.__doc__[attribute_index:]}"
                    )
                )
            # For short docstrings such as Aggregate, Stack, et
            else:
                self.__doc__ = (
                    altair_prop.__doc__.replace("    ", "") + "\n" + self.__doc__
                )
            # Add signatures and tab completion for the method and parameter names
            self.__signature__ = inspect.signature(altair_prop)
            self.__wrapped__ = inspect.getfullargspec(altair_prop)
            self.__name__ = altair_prop.__name__
        else:
            # It seems like bandPosition is the only parameter that doesn't
            # have a helper class.
            pass
        return self

    def __call__(self, *args, **kwargs):
        obj = self.obj.copy()
        # TODO: use schema to validate
        obj[self.prop] = args[0] if args else kwargs
        return obj


def with_property_setters(cls):
    """
    Decorator to add property setters to a Schema class.
    """
    schema = cls.resolve_references()
    for prop, propschema in schema.get("properties", {}).items():
        setattr(cls, prop, _PropertySetter(prop, propschema))
    return cls
