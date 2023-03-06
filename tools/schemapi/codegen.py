"""Code generation utilities"""
from .utils import SchemaInfo, is_valid_identifier, indent_docstring, indent_arglist

import textwrap
import re


class CodeSnippet:
    """Object whose repr() is a string of code"""

    def __init__(self, code):
        self.code = code

    def __repr__(self):
        return self.code


def _get_args(info):
    """Return the list of args & kwds for building the __init__ function"""
    # TODO: - set additional properties correctly
    #       - handle patternProperties etc.
    required = set()
    kwds = set()
    invalid_kwds = set()

    # TODO: specialize for anyOf/oneOf?

    if info.is_allOf():
        # recursively call function on all children
        arginfo = [_get_args(child) for child in info.allOf]
        nonkeyword = all(args[0] for args in arginfo)
        required = set.union(set(), *(args[1] for args in arginfo))
        kwds = set.union(set(), *(args[2] for args in arginfo))
        kwds -= required
        invalid_kwds = set.union(set(), *(args[3] for args in arginfo))
        additional = all(args[4] for args in arginfo)
    elif info.is_empty() or info.is_compound():
        nonkeyword = True
        additional = True
    elif info.is_value():
        nonkeyword = True
        additional = False
    elif info.is_object():
        invalid_kwds = {p for p in info.required if not is_valid_identifier(p)} | {
            p for p in info.properties if not is_valid_identifier(p)
        }
        required = {p for p in info.required if is_valid_identifier(p)}
        kwds = {p for p in info.properties if is_valid_identifier(p)}
        kwds -= required
        nonkeyword = False
        additional = True
        # additional = info.additionalProperties or info.patternProperties
    else:
        raise ValueError("Schema object not understood")

    return (nonkeyword, required, kwds, invalid_kwds, additional)


class SchemaGenerator:
    """Class that defines methods for generating code from schemas

    Parameters
    ----------
    classname : string
        The name of the class to generate
    schema : dict
        The dictionary defining the schema class
    rootschema : dict (optional)
        The root schema for the class
    basename : string or tuple (default: "SchemaBase")
        The name(s) of the base class(es) to use in the class definition
    schemarepr : CodeSnippet or object, optional
        An object whose repr will be used in the place of the explicit schema.
        This can be useful, for example, when the generated code should reference
        a predefined schema object. The user must ensure that the schema within
        the evaluated code is identical to the schema used to generate the code.
    rootschemarepr : CodeSnippet or object, optional
        An object whose repr will be used in the place of the explicit root
        schema.
    **kwargs : dict
        Additional keywords for derived classes.
    """

    schema_class_template = textwrap.dedent(
        '''
    class {classname}({basename}):
        """{docstring}"""
        _schema = {schema!r}
        _rootschema = {rootschema!r}

        {init_code}
    '''
    )

    init_template = textwrap.dedent(
        """
    def __init__({arglist}):
        super({classname}, self).__init__({super_arglist})
    """
    ).lstrip()

    def _process_description(self, description):
        return description

    def __init__(
        self,
        classname,
        schema,
        rootschema=None,
        basename="SchemaBase",
        schemarepr=None,
        rootschemarepr=None,
        nodefault=(),
        haspropsetters=False,
        **kwargs,
    ):
        self.classname = classname
        self.schema = schema
        self.rootschema = rootschema
        self.basename = basename
        self.schemarepr = schemarepr
        self.rootschemarepr = rootschemarepr
        self.nodefault = nodefault
        self.haspropsetters = haspropsetters
        self.kwargs = kwargs

    def subclasses(self):
        """Return a list of subclass names, if any."""
        info = SchemaInfo(self.schema, self.rootschema)
        return [child.refname for child in info.anyOf if child.is_reference()]

    def schema_class(self):
        """Generate code for a schema class"""
        rootschema = self.rootschema if self.rootschema is not None else self.schema
        schemarepr = self.schemarepr if self.schemarepr is not None else self.schema
        rootschemarepr = self.rootschemarepr
        if rootschemarepr is None:
            if rootschema is self.schema:
                rootschemarepr = CodeSnippet("_schema")
            else:
                rootschemarepr = rootschema
        if isinstance(self.basename, str):
            basename = self.basename
        else:
            basename = ", ".join(self.basename)
        return self.schema_class_template.format(
            classname=self.classname,
            basename=basename,
            schema=schemarepr,
            rootschema=rootschemarepr,
            docstring=self.docstring(indent=4),
            init_code=self.init_code(indent=4),
            method_code=self.method_code(indent=4),
            **self.kwargs,
        )

    def docstring(self, indent=0):
        # TODO: add a general description at the top, derived from the schema.
        #       for example, a non-object definition should list valid type, enum
        #       values, etc.
        # TODO: use _get_args here for more information on allOf objects
        info = SchemaInfo(self.schema, self.rootschema)
        doc = ["{} schema wrapper".format(self.classname), "", info.medium_description]
        if info.description:
            doc += self._process_description(  # remove condition description
                re.sub(r"\n\{\n(\n|.)*\n\}", "", info.description)
            ).splitlines()
        # Remove lines which contain the "raw-html" directive which cannot be processed
        # by Sphinx at this level of the docstring. It works for descriptions
        # of attributes which is why we do not do the same below. The removed
        # lines are anyway non-descriptive for a user.
        doc = [line for line in doc if ":raw-html:" not in line]

        if info.properties:
            nonkeyword, required, kwds, invalid_kwds, additional = _get_args(info)
            doc += ["", "Parameters", "----------", ""]
            for prop in sorted(required) + sorted(kwds) + sorted(invalid_kwds):
                propinfo = info.properties[prop]
                doc += [
                    "{} : {}".format(prop, propinfo.short_description),
                    "    {}".format(
                        self._process_description(propinfo.deep_description)
                    ),
                ]
        if len(doc) > 1:
            doc += [""]
        return indent_docstring(doc, indent_level=indent, width=100, lstrip=True)

    def init_code(self, indent=0):
        """Return code suitable for the __init__ function of a Schema class"""
        info = SchemaInfo(self.schema, rootschema=self.rootschema)
        nonkeyword, required, kwds, invalid_kwds, additional = _get_args(info)

        nodefault = set(self.nodefault)
        required -= nodefault
        kwds -= nodefault

        args = ["self"]
        super_args = []

        self.init_kwds = sorted(kwds)

        if nodefault:
            args.extend(sorted(nodefault))
        elif nonkeyword:
            args.append("*args")
            super_args.append("*args")

        args.extend("{}=Undefined".format(p) for p in sorted(required) + sorted(kwds))
        super_args.extend(
            "{0}={0}".format(p)
            for p in sorted(nodefault) + sorted(required) + sorted(kwds)
        )

        if additional:
            args.append("**kwds")
            super_args.append("**kwds")

        arg_indent_level = 9 + indent
        super_arg_indent_level = 23 + len(self.classname) + indent

        initfunc = self.init_template.format(
            classname=self.classname,
            arglist=indent_arglist(args, indent_level=arg_indent_level),
            super_arglist=indent_arglist(
                super_args, indent_level=super_arg_indent_level
            ),
        )
        if indent:
            initfunc = ("\n" + indent * " ").join(initfunc.splitlines())
        return initfunc

    _equiv_python_types = {
        "string": "str",
        "number": "float",
        "integer": "int",
        "object": "dict",
        "boolean": "bool",
        "array": "list",
        "null": "None",
    }

    def get_args(self, si):
        contents = ["self"]
        props = []
        # TODO: do we need to specialize the anyOf code?
        if si.is_anyOf():
            props = sorted(list({p for si_sub in si.anyOf for p in si_sub.properties}))
        elif si.properties:
            props = si.properties

        if props:
            contents.extend([p + "=Undefined" for p in props])
        elif si.type:
            py_type = self._equiv_python_types[si.type]
            if py_type == "list":
                # Try to get a type hint like "List[str]" which is more specific
                # then just "list"
                item_vl_type = si.items.get("type", None)
                if item_vl_type is not None:
                    item_type = self._equiv_python_types[item_vl_type]
                else:
                    item_si = SchemaInfo(si.items, self.rootschema)
                    assert item_si.is_reference()
                    altair_class_name = item_si.title
                    item_type = f"core.{altair_class_name}"
                py_type = f"List[{item_type}]"
            elif si.is_enum():
                # If it's an enum, we can type hint it as a Literal which tells
                # a type checker that only the values in enum are acceptable
                enum_values = [f'"{v}"' for v in si.enum]
                py_type = f"Literal[{', '.join(enum_values)}]"
            contents.append(f"_: {py_type}")

        contents.append("**kwds")

        return contents

    def get_signature(self, attr, sub_si, indent, has_overload=False):
        lines = []
        if has_overload:
            lines.append("@overload")
        args = ", ".join(self.get_args(sub_si))
        lines.append(f"def {attr}({args}) -> '{self.classname}':")
        lines.append(indent * " " + "...\n")
        return lines

    def setter_hint(self, attr, indent):
        si = SchemaInfo(self.schema, self.rootschema).properties[attr]
        if si.is_anyOf():
            return self._get_signature_any_of(si, attr, indent)
        else:
            return self.get_signature(attr, si, indent)

    def _get_signature_any_of(self, si: SchemaInfo, attr, indent):
        signatures = []
        for sub_si in si.anyOf:
            if sub_si.is_anyOf():
                # Recursively call method again to go a level deeper
                signatures.extend(self._get_signature_any_of(sub_si, attr, indent))
            else:
                signatures.extend(
                    self.get_signature(attr, sub_si, indent, has_overload=True)
                )
        return list(flatten(signatures))

    def method_code(self, indent=0):
        """Return code to assist setter methods"""
        if not self.haspropsetters:
            return None
        args = self.init_kwds
        type_hints = [hint for a in args for hint in self.setter_hint(a, indent)]

        return ("\n" + indent * " ").join(type_hints)


def flatten(container):
    """Flatten arbitrarily flattened list

    From https://stackoverflow.com/a/10824420
    """
    for i in container:
        if isinstance(i, (list, tuple)):
            for j in flatten(i):
                yield j
        else:
            yield i
