import warnings
from . import codegen, SchemaBase, Undefined


def schemaclass(*args, init_func=True, docstring=True, property_map=True):
    """A decorator to add boilerplate to a schema class

    This will read the _json_schema attribute of a SchemaBase class, and add
    one or all of three attributes/methods, based on the schema:

    - An __init__ function
    - a __doc__ docstring

    In all cases, if the attribute/method is explicitly defined in the class
    it will not be overwritten.

    A simple invocation adds all three attributes/methods:

        @schemaclass
        class MySchema(SchemaBase):
            __schema = {...}

    Optionally, you can invoke schemaclass with arguments to turn off
    some of the added behaviors:

        @schemaclass(init_func=True, docstring=False)
        class MySchema(SchemaBase):
            __schema = {...}
    """

    def _decorator(cls, init_func=init_func, docstring=docstring):
        if not (isinstance(cls, type) and issubclass(cls, SchemaBase)):
            warnings.warn("class is not an instance of SchemaBase.")

        name = cls.__name__
        gen = codegen.SchemaGenerator(
            name, schema=cls._schema, rootschema=cls._rootschema
        )

        if init_func and "__init__" not in cls.__dict__:
            init_code = gen.init_code()
            globals_ = {name: cls, "Undefined": Undefined}
            locals_ = {}
            exec(init_code, globals_, locals_)
            setattr(cls, "__init__", locals_["__init__"])

        if docstring and not cls.__doc__:
            setattr(cls, "__doc__", gen.docstring())
        return cls

    if len(args) == 0:
        return _decorator
    elif len(args) == 1:
        return _decorator(args[0])
    else:
        raise ValueError(
            "optional arguments to schemaclass must be " "passed by keyword"
        )
