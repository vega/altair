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
    info = SchemaInfo(schema, rootschema)
    doc = ["{0} schema wrapper".format(classname)]
    if info.description:
        doc += ['', info.description]
    if info.properties:
        doc += ['',
                'Attributes',
                '----------']
        for prop, propinfo in info.properties.items():
            doc += ["{0} : {1}".format(prop, propinfo.short_description),
                    "    {0}".format(propinfo.description.replace('\n', ' '))]
    if len(doc) > 1:
        doc += ['']
    return ("\n" + indent * " ").join(doc)


INIT_DEF = """
def __init__({arglist}):
    super({classname}, self).__init__({super_arglist})
""".lstrip()


def init_code(classname, schema, rootschema=None, indent=0):
    """Return code suitablde for the __init__ function of a Schema class"""
    info = SchemaInfo(schema, rootschema=rootschema)

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
