"""Code generation utilities."""

from __future__ import annotations

import re
import textwrap
from dataclasses import dataclass
from itertools import chain
from typing import Final, Iterator

from .utils import (
    SchemaInfo,
    flatten,
    indent_docstring,
    is_valid_identifier,
    jsonschema_to_python_types,
    spell_literal,
)


class CodeSnippet:
    """Object whose repr() is a string of code."""

    def __init__(self, code: str):
        self.code = code

    def __repr__(self) -> str:
        return self.code


@dataclass
class ArgInfo:
    nonkeyword: bool
    required: set[str]
    kwds: set[str]
    invalid_kwds: set[str]
    additional: bool


def get_args(info: SchemaInfo) -> ArgInfo:
    """Return the list of args & kwds for building the __init__ function."""
    # TODO: - set additional properties correctly
    #       - handle patternProperties etc.
    required: set[str] = set()
    kwds: set[str] = set()
    invalid_kwds: set[str] = set()

    # TODO: specialize for anyOf/oneOf?

    if info.is_allOf():
        # recursively call function on all children
        arginfo: list[ArgInfo] = [get_args(child) for child in info.allOf]
        nonkeyword = all(args.nonkeyword for args in arginfo)
        required = {args.required for args in arginfo}
        kwds = {args.kwds for args in arginfo}
        kwds -= required
        invalid_kwds = {args.invalid_kwds for args in arginfo}
        additional = all(args.additional for args in arginfo)
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
        msg = "Schema object not understood"
        raise ValueError(msg)

    return ArgInfo(
        nonkeyword=nonkeyword,
        required=required,
        kwds=kwds,
        invalid_kwds=invalid_kwds,
        additional=additional,
    )


class SchemaGenerator:
    """
    Class that defines methods for generating code from schemas.

    Parameters
    ----------
    classname : string
        The name of the class to generate
    schema : dict
        The dictionary defining the schema class
    rootschema : dict (optional)
        The root schema for the class
    basename : string or list of strings (default: "SchemaBase")
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

    init_template: Final = textwrap.dedent(
        """
    def __init__({arglist}):
        super({classname}, self).__init__({super_arglist})
    """
    ).lstrip()

    def _process_description(self, description: str):
        return description

    def __init__(
        self,
        classname: str,
        schema: dict,
        rootschema: dict | None = None,
        basename: str | list[str] = "SchemaBase",
        schemarepr: object | None = None,
        rootschemarepr: object | None = None,
        nodefault: list[str] | None = None,
        haspropsetters: bool = False,
        **kwargs,
    ) -> None:
        self.classname = classname
        self.schema = schema
        self.rootschema = rootschema
        self.basename = basename
        self.schemarepr = schemarepr
        self.rootschemarepr = rootschemarepr
        self.nodefault = nodefault or ()
        self.haspropsetters = haspropsetters
        self.kwargs = kwargs

    def subclasses(self) -> Iterator[str]:
        """Return an Iterator over subclass names, if any."""
        for child in SchemaInfo(self.schema, self.rootschema).anyOf:
            if child.is_reference():
                yield child.refname

    def schema_class(self) -> str:
        """Generate code for a schema class."""
        rootschema: dict = self.rootschema or self.schema
        schemarepr: object = self.schemarepr or self.schema
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

    @property
    def info(self) -> SchemaInfo:
        return SchemaInfo(self.schema, self.rootschema)

    @property
    def arg_info(self) -> ArgInfo:
        return get_args(self.info)

    def docstring(self, indent: int = 0) -> str:
        info = self.info
        # https://numpydoc.readthedocs.io/en/latest/format.html#short-summary
        doc = [f"{self.classname} schema wrapper"]
        if info.description:
            # https://numpydoc.readthedocs.io/en/latest/format.html#extended-summary
            # Remove condition from description
            desc: str = re.sub(r"\n\{\n(\n|.)*\n\}", "", info.description)
            ext_summary: list[str] = self._process_description(desc).splitlines()
            # Remove lines which contain the "raw-html" directive which cannot be processed
            # by Sphinx at this level of the docstring. It works for descriptions
            # of attributes which is why we do not do the same below. The removed
            # lines are anyway non-descriptive for a user.
            ext_summary = [line for line in ext_summary if ":raw-html:" not in line]
            # Only add an extended summary if the above did not result in an empty list.
            if ext_summary:
                doc.append("")
                doc.extend(ext_summary)

        if info.properties:
            arg_info = self.arg_info
            doc += ["", "Parameters", "----------", ""]
            for prop in (
                sorted(arg_info.required)
                + sorted(arg_info.kwds)
                + sorted(arg_info.invalid_kwds)
            ):
                propinfo = info.properties[prop]
                doc += [
                    f"{prop} : {propinfo.get_python_type_representation()}",
                    f"    {self._process_description(propinfo.deep_description)}",
                ]
        return indent_docstring(doc, indent_level=indent, width=100, lstrip=True)

    def init_code(self, indent: int = 0) -> str:
        """Return code suitable for the __init__ function of a Schema class."""
        args, super_args = self.init_args()

        initfunc = self.init_template.format(
            classname=self.classname,
            arglist=", ".join(args),
            super_arglist=", ".join(super_args),
        )
        if indent:
            initfunc = ("\n" + indent * " ").join(initfunc.splitlines())
        return initfunc

    def init_args(self) -> tuple[list[str], list[str]]:
        info = self.info
        arg_info = self.arg_info

        nodefault = set(self.nodefault)
        arg_info.required -= nodefault
        arg_info.kwds -= nodefault

        args: list[str] = ["self"]
        super_args: list[str] = []

        self.init_kwds: list[str] = sorted(arg_info.kwds)
        init_required: list[str] = sorted(arg_info.required)
        _nodefault: list[str] = sorted(nodefault)

        if nodefault:
            args.extend(_nodefault)
        elif arg_info.nonkeyword:
            args.append("*args")
            super_args.append("*args")

        it = (
            f"{p}: {info.properties[p].get_python_type_representation(target='annotation', use_undefined=True)} = Undefined"
            for p in chain(init_required, self.init_kwds)
        )
        args.extend(it)
        super_args.extend(
            f"{p}={p}" for p in chain(_nodefault, init_required, self.init_kwds)
        )

        if arg_info.additional:
            args.append("**kwds")
            super_args.append("**kwds")
        return args, super_args

    def get_args(self, si: SchemaInfo) -> list[str]:
        contents = ["self"]
        prop_infos: dict[str, SchemaInfo] = {}
        if si.is_anyOf():
            prop_infos = {}
            for si_sub in si.anyOf:
                prop_infos.update(si_sub.properties)
        elif si.properties:
            prop_infos = dict(si.properties.items())

        if prop_infos:
            contents.extend(
                f"{p}: {info.get_python_type_representation(target='annotation', use_undefined=True)} = Undefined"
                for p, info in prop_infos.items()
            )
        elif si.type:
            py_type = jsonschema_to_python_types[si.type]
            if py_type == "list":
                # Try to get a type hint like "List[str]" which is more specific
                # then just "list"
                item_vl_type = si.items.get("type", None)
                if item_vl_type is not None:
                    item_type = jsonschema_to_python_types[item_vl_type]
                else:
                    item_si = SchemaInfo(si.items, self.rootschema)
                    assert item_si.is_reference()
                    altair_class_name = item_si.title
                    item_type = f"core.{altair_class_name}"
                py_type = f"List[{item_type}]"
            elif si.is_enum():
                # If it's an enum, we can type hint it as a Literal which tells
                # a type checker that only the values in enum are acceptable
                py_type = spell_literal(si.enum)
            contents.append(f"_: {py_type}")

        contents.append("**kwds")

        return contents

    def get_signature(
        self, attr: str, sub_si: SchemaInfo, indent: int, has_overload: bool = False
    ) -> list[str]:
        lines = []
        if has_overload:
            lines.append("@overload")
        args = ", ".join(self.get_args(sub_si))
        lines.extend(
            (f"def {attr}({args}) -> '{self.classname}':", indent * " " + "...\n")
        )
        return lines

    def setter_hint(self, attr: str, indent: int) -> list[str]:
        si = SchemaInfo(self.schema, self.rootschema).properties[attr]
        if si.is_anyOf():
            return self._get_signature_any_of(si, attr, indent)
        else:
            return self.get_signature(attr, si, indent, has_overload=True)

    def _get_signature_any_of(
        self, si: SchemaInfo, attr: str, indent: int
    ) -> list[str]:
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

    def method_code(self, indent: int = 0) -> str | None:
        """Return code to assist setter methods."""
        if not self.haspropsetters:
            return None
        args = self.init_kwds
        type_hints = (hint for a in args for hint in self.setter_hint(a, indent))

        return ("\n" + indent * " ").join(type_hints)
