"""Code generation utilities"""
import textwrap

from .utils import SchemaInfo, is_valid_identifier, indent_docstring, indent_arglist


class CodeSnippet(object):
    """Object whose repr() is a string of code"""
    def __init__(self, code):
        self.code = code

    def __repr__(self):
        return self.code


SCHEMA_CLASS_TEMPLATE = '''
class {classname}({basename}):
    """{docstring}"""
    _schema = {schema!r}
    _rootschema = {rootschema!r}

    {init_code}
'''


def schema_class(classname, schema, rootschema=None, basename='SchemaBase',
                 schemarepr=None, rootschemarepr=None):
    """Generate code for a schema class

    Parameters
    ----------
    classname : string
        The name of the class to generate
    schema : dict
        The dictionary defining the schema class
    rootschema : dict (optional)
        The root schema for the class
    basename : string (default: "SchemaBase")
        The name of the base class to use in the class definition
    schemarepr : CodeSnippet or object, optional
        An object whose repr will be used in the place of the explicit schema.
        This can be useful, for example, when the generated code should reference
        a predefined schema object. The user must ensure that the schema within
        the evaluated code is identical to the schema used to generate the code.
    rootschemarepr : CodeSnippet or object, optional
        An object whose repr will be used in the place of the explicit root
        schema.
    """
    rootschema = rootschema if rootschema is not None else schema
    schemarepr = schemarepr if schemarepr is not None else schema
    if rootschemarepr is None:
        if rootschema is schema:
            rootschemarepr = CodeSnippet('_schema')
        else:
            rootschemarepr = rootschema
    return SCHEMA_CLASS_TEMPLATE.format(
        classname=classname,
        basename=basename,
        schema=schemarepr,
        rootschema=rootschemarepr,
        docstring=docstring(classname=classname, schema=schema,
                            rootschema=rootschema, indent=4),
        init_code=init_code(classname=classname, schema=schema,
                            rootschema=rootschema, indent=4)
    )


def docstring(classname, schema, rootschema=None, indent=4):
    # TODO: add a general description at the top, derived from the schema.
    #       for example, a non-object definition should list valid type, enum
    #       values, etc.
    # TODO: use _get_args here for more information on allOf objects
    info = SchemaInfo(schema, rootschema)
    doc = ["{0} schema wrapper".format(classname)]

    if info.description:
        doc += info.description.splitlines()
    if info.properties:
        doc += ['',
                'Attributes',
                '----------']
        for prop, propinfo in info.properties.items():
            doc += ["{0} : {1}".format(prop, propinfo.short_description),
                    "    {0}".format(propinfo.description)]
    if len(doc) > 1:
        doc += ['']
    return indent_docstring(doc, indent_level=indent, width=80, lstrip=True)


def _get_args(info):
    """Return the list of args & kwds for building the __init__ function"""
    # TODO: - set additional properties correctly
    #       - handle patternProperties etc.
    required = set()
    kwds = set()

    # TODO: specialize for anyOf/oneOf?

    if info.is_allOf():
        # recursively call function on all children
        arginfo = [_get_args(child) for child in info.allOf]
        nonkeyword = all(args[0] for args in arginfo)
        required = set.union(set(), *(args[1] for args in arginfo))
        kwds = set.union(set(), *(args[2] for args in arginfo))
        additional = all(args[3] for args in arginfo)
    elif info.is_empty() or info.is_compound():
        nonkeyword = True
        additional = True
    elif info.is_value():
        nonkeyword = True
        additional=False
    elif info.is_object():
        required = {p for p in info.required if is_valid_identifier(p)}
        kwds = {p for p in info.properties if is_valid_identifier(p)}
        kwds -= required
        nonkeyword = False
        additional = True
    else:
        raise ValueError("Schema object not understood")

    return (nonkeyword, required, kwds, additional)


INIT_DEF = """
def __init__({arglist}):
    super({classname}, self).__init__({super_arglist})
""".lstrip()


def init_code(classname, schema, rootschema=None, indent=0, nodefault=()):
    """Return code suitablde for the __init__ function of a Schema class"""
    info = SchemaInfo(schema, rootschema=rootschema)
    nonkeyword, required, kwds, additional =_get_args(info)

    nodefault=set(nodefault)
    required -= nodefault
    kwds -= nodefault

    args = ['self']
    super_args = []

    if nodefault:
        args.extend(sorted(nodefault))
    elif nonkeyword:
        args.append('*args')
        super_args.append('*args')

    args.extend('{0}=Undefined'.format(p)
                for p in sorted(required) + sorted(kwds))
    super_args.extend('{0}={0}'.format(p)
                      for p in sorted(nodefault) + sorted(required) + sorted(kwds))

    if additional:
        args.append('**kwds')
        super_args.append('**kwds')

    arg_indent_level = 9 + indent
    super_arg_indent_level = 23 + len(classname) + indent

    initfunc = INIT_DEF.format(classname=classname,
                               arglist=indent_arglist(args, indent_level=arg_indent_level),
                               super_arglist=indent_arglist(super_args, indent_level=super_arg_indent_level))
    if indent:
        initfunc = ('\n' + indent * ' ').join(initfunc.splitlines())
    return initfunc
