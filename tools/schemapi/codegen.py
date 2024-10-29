"""Code generation utilities."""

from __future__ import annotations

import re
import sys
import textwrap
from collections.abc import Iterable, Iterator
from dataclasses import dataclass
from itertools import chain, starmap
from operator import attrgetter
from typing import Any, Callable, ClassVar, Final, Literal, TypeVar, Union

from .utils import (
    Grouped,
    SchemaInfo,
    indent_docstring,
    is_valid_identifier,
    process_description,
)

if sys.version_info >= (3, 12):
    from typing import TypeAliasType
else:
    from typing_extensions import TypeAliasType


T1 = TypeVar("T1")
T2 = TypeVar("T2")
AttrGetter = TypeAliasType(
    "AttrGetter", Callable[[T1], Union[T2, "tuple[T2, ...]"]], type_params=(T1, T2)
)
"""
Intended to model the signature of ``operator.attrgetter``.

Spelled more generically to support future extension.
"""

ANON: Literal["_"] = "_"
DOUBLESTAR_ARGS: Literal["**kwds"] = "**kwds"
POS_ONLY: Literal["/"] = "/"
KWD_ONLY: Literal["*"] = "*"


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
    schema_info: SchemaInfo

    def iter_args(
        self,
        group: Iterable[str] | AttrGetter[ArgInfo, set[str]],
        *more_groups: Iterable[str] | AttrGetter[ArgInfo, set[str]],
        exclude: str | Iterable[str] | None = None,
    ) -> Iterator[tuple[str, SchemaInfo]]:
        r"""
        Yields (property_name, property_info).

        Useful for signatures and docstrings.

        Parameters
        ----------
        group, \*more_groups
            Each group will independently sorted, and chained.
        exclude
            Property name(s) to omit if they appear during iteration.
        """
        props = self.schema_info.properties
        it = chain.from_iterable(
            sorted(g) for g in self._normalize_groups(group, *more_groups)
        )
        if exclude is not None:
            exclude = {exclude} if isinstance(exclude, str) else set(exclude)
            for p in it:
                if p not in exclude:
                    yield p, props[p]
        else:
            for p in it:
                yield p, props[p]

    def _normalize_groups(
        self, *groups: Iterable[str] | AttrGetter[ArgInfo, set[str]]
    ) -> Iterator[set[str]]:
        for group in groups:
            if isinstance(group, set):
                yield group
            elif isinstance(group, Iterable):
                yield set(group)
            elif callable(group):
                result = group(self)
                if isinstance(result, set):
                    yield result
                else:
                    yield from result
            else:
                msg = (
                    f"Expected all cases to be reducible to a `set[str]`,"
                    f" but got {type(group).__name__!r}"
                )
                raise TypeError(msg)


arg_required_kwds: AttrGetter[ArgInfo, set[str]] = attrgetter("required", "kwds")
arg_invalid_kwds: AttrGetter[ArgInfo, set[str]] = attrgetter("invalid_kwds")
arg_kwds: AttrGetter[ArgInfo, set[str]] = attrgetter("kwds")


def get_args(info: SchemaInfo) -> ArgInfo:
    """Return the list of args & kwds for building the __init__ function."""
    # TODO: - set additional properties correctly
    #       - handle patternProperties etc.
    required: set[str] = set()
    kwds: set[str] = set()
    invalid_kwds: set[str] = set()

    # TODO: specialize for anyOf/oneOf?
    if info.is_empty() or info.is_anyOf():
        nonkeyword = True
        additional = True
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
        nonkeyword = True
        additional = False
        if info.is_allOf():
            # recursively call function on all children
            msg = f"Branch is reachable with:\n{info.raw_schema!r}"
            raise NotImplementedError(msg)
            arginfo: list[ArgInfo] = [get_args(child) for child in info.allOf]
            nonkeyword = all(args.nonkeyword for args in arginfo)
            required = {args.required for args in arginfo}
            kwds = {args.kwds for args in arginfo}
            kwds -= required
            invalid_kwds = {args.invalid_kwds for args in arginfo}
            additional = all(args.additional for args in arginfo)

    return ArgInfo(
        nonkeyword=nonkeyword,
        required=required,
        kwds=kwds,
        invalid_kwds=invalid_kwds,
        additional=additional,
        schema_info=info,
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

    haspropsetters: ClassVar[bool] = False

    def __init__(
        self,
        classname: str,
        schema: dict[str, Any],
        rootschema: dict | None = None,
        basename: str | list[str] = "SchemaBase",
        schemarepr: object | None = None,
        rootschemarepr: object | None = None,
        nodefault: list[str] | None = None,
        **kwargs,
    ) -> None:
        self.classname = classname
        self.schema = schema
        self.rootschema = rootschema
        self.basename = basename
        self.schemarepr = schemarepr
        self.rootschemarepr = rootschemarepr
        self.nodefault = nodefault or ()
        self.kwargs = kwargs

    def subclasses(self) -> Iterator[str]:
        """
        Return an Iterator over subclass names, if any.

        NOTE
        ----
        *Does not represent subclasses**.

        Represents a ``Union`` of schemas (``SchemaInfo.anyOf``).
        """
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
            method_code=(
                self.overload_code(indent=4) if type(self).haspropsetters else None
            ),
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
            ext_summary: list[str] = process_description(desc).splitlines()
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
            it = chain.from_iterable(
                (f"{p} : {p_info.to_type_repr()}", f"    {p_info.deep_description}")
                for p, p_info in arg_info.iter_args(
                    arg_info.required, arg_kwds, arg_invalid_kwds
                )
            )
            doc.extend(chain(["", "Parameters", "----------", ""], it))
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
            f"{p}: {info.properties[p].to_type_repr(target='annotation', use_undefined=True)} = Undefined"
            for p in chain(init_required, self.init_kwds)
        )
        args.extend(it)
        super_args.extend(
            f"{p}={p}" for p in chain(_nodefault, init_required, self.init_kwds)
        )

        if arg_info.additional:
            args.append(DOUBLESTAR_ARGS)
            super_args.append(DOUBLESTAR_ARGS)
        return args, super_args

    # TODO: Resolve 45x ``list[core.ConditionalValueDef...] annotations
    def overload_signature(
        self, prop: str, info: SchemaInfo | Iterable[SchemaInfo], /
    ) -> Iterator[str]:
        """Yields a single, fully annotated ``@overload``, signature."""
        TARGET: Literal["annotation"] = "annotation"
        yield "@overload"
        signature = "def {0}(self, {1}) -> {2}: ..."
        if isinstance(info, SchemaInfo):
            if info.properties:
                it = (
                    f"{name}: {p_info.to_type_repr(target=TARGET, use_undefined=True)} = Undefined"
                    for name, p_info in info.properties.items()
                )
                content = f"{KWD_ONLY}, {', '.join(it)}"
            elif isinstance(info.type, str):
                if info.is_array() and (title := info.child(info.items).title):
                    tp = f"list[core.{title}]"
                else:
                    tp = info.to_type_repr(target=TARGET, use_concrete=True)
                content = f"{ANON}: {tp}, {POS_ONLY}"
            else:
                msg = f"Assumed unreachable\n{info!r}"
                raise NotImplementedError(msg)
        else:
            tp = SchemaInfo.to_type_repr_batched(info, target=TARGET, use_concrete=True)
            content = f"{ANON}: {tp}, {POS_ONLY}"
        yield signature.format(prop, content, self.classname)

    def _overload_expand(
        self, prop: str, info: SchemaInfo | Iterable[SchemaInfo], /
    ) -> Iterator[str]:
        children: Iterable[SchemaInfo]
        if isinstance(info, SchemaInfo):
            children = info.anyOf if info.is_anyOf() else (info,)
        else:
            children = info
        for child in children:
            if child.is_anyOf() and not child.is_union_flattenable():
                yield from self._overload_expand(prop, child)
            else:
                yield from self.overload_signature(prop, child)

    def overload_dispatch(self, prop: str, info: SchemaInfo, /) -> Iterator[str]:
        """
        For a given property ``prop``, decide how to represent all valid signatures.

        In this context, dispatching between **3** kinds of ``@overload``:
        - ``Union``
            1. The subset of basic types form a single signature
            2. More complex types are recursed into, possibly expanding to multiple signatures
        - Others
            3. Only one signature is required
        """
        if info.is_anyOf():
            grouped = Grouped(info.anyOf, SchemaInfo.is_flattenable)
            if (expand := grouped.falsy) and len(expand) == 1 and expand[0].properties:
                grouped.truthy.append(expand[0])
            if flatten := grouped.truthy:
                yield from self.overload_signature(prop, flatten)
            if expand := grouped.falsy:
                yield from self._overload_expand(prop, expand)
        else:
            yield from self.overload_signature(prop, info)

    def overload_code(self, indent: int = 0) -> str:
        """Return all ``@overload`` for property setter methods and as an indented code block."""
        indented = "\n" + indent * " "
        it = starmap(
            self.overload_dispatch,
            self.arg_info.iter_args(arg_kwds, exclude=self.nodefault),
        )
        return indented.join(chain.from_iterable(it))
