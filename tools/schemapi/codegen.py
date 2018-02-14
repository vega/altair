"""Code generation utilities"""
from .utils import SchemaInfo, is_valid_identifier


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


def schema_class(classname, schema, schemarepr=None,
                 rootschema=None, basename='SchemaBase'):
    """Generate code for a schema class

    Parameters
    ----------
    classname : string
        The name of the class to generate
    schema : dict
        The dictionary defining the schema class
    basename : string (default: "SchemaBase")
        The name of the base class to use in the class definition
    schemarepr : CodeSnippet or object, optional
        An object whose repr will be used in the place of the explicit schema.
        This can be useful, for example, when the generated code should reference
        a predefined schema object. The user must ensure that the schema within
        the evaluated code is identical to the schema used to generate the code.
    """
    schemarepr = schemarepr if schemarepr is not None else schema
    rootschema = rootschema if rootschema is not None else CodeSnippet('_schema')
    return SCHEMA_CLASS_TEMPLATE.format(
        classname=classname,
        basename=basename,
        schema=schemarepr,
        rootschema=rootschema,
        docstring=docstring(classname, schema, indent=4),
        init_code=init_code(classname, schema, indent=4)
    )


def docstring(classname, schema, indent=4):
    # TODO fill this out
    return "{0} schema wrapper".format(classname)


INIT_DEF = """
def __init__({arglist}):
    super({classname}, self).__init__({super_arglist})
""".lstrip()


def init_code(classname, schema, indent=0):
    """Return code suitable for the __init__ function of a Schema class"""
    info = SchemaInfo(schema)

    args = ['self']
    super_args = []

    if info.is_empty() or info.is_compound():
        args.extend(['*args', '**kwds'])
        super_args.extend(['*args', '**kwds'])
    elif info.is_value():
        args.extend(['*args'])
        super_args.extend(['*args'])
    elif info.is_object():
        required = {p for p in info.required if is_valid_identifier(p)}
        props = {p for p in info.properties if is_valid_identifier(p)}
        props -= required

        args.extend('{0}=Undefined'.format(p)
                    for p in sorted(required) + sorted(props))
        args.append('**kwds')

        super_args.extend('{0}={0}'.format(p)
                          for p in sorted(required) + sorted(props))
        super_args.append('**kwds')
    else:
        raise ValueError("Schema object not understood")

    code = INIT_DEF.format(classname=classname,
                           arglist=', '.join(args),
                           super_arglist=', '.join(super_args))
    if indent:
        code = code.replace('\n', '\n' + indent * ' ')
    return code
