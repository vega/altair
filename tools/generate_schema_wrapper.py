"""Generate a schema wrapper from a schema."""

from __future__ import annotations

import argparse
import copy
import json
import sys
import textwrap
from collections import deque
from dataclasses import dataclass
from itertools import chain
from operator import attrgetter
from pathlib import Path
from typing import Any, Final, Iterable, Iterator, Literal
from urllib import request

import vl_convert as vlc

sys.path.insert(0, str(Path.cwd()))


from tools.schemapi import CodeSnippet, SchemaInfo, codegen
from tools.schemapi.utils import (
    SchemaProperties,
    TypeAliasTracer,
    finalize_type_reprs,
    get_valid_identifier,
    import_type_checking,
    import_typing_extensions,
    indent_docstring,
    resolve_references,
    rst_syntax_for_class,
    ruff_format_py,
    ruff_write_lint_format_str,
    spell_literal,
)

SCHEMA_VERSION: Final = "v5.20.1"


HEADER_COMMENT = """\
# The contents of this file are automatically written by
# tools/generate_schema_wrapper.py. Do not modify directly.
"""

HEADER: Final = f"""{HEADER_COMMENT}
from __future__ import annotations\n
"""

SCHEMA_URL_TEMPLATE: Final = "https://vega.github.io/schema/{library}/{version}.json"
SCHEMA_FILE = "vega-lite-schema.json"
THEMES_FILE = "vega-themes.json"

CHANNEL_MYPY_IGNORE_STATEMENTS: Final = """\
# These errors need to be ignored as they come from the overload methods
# which trigger two kind of errors in mypy:
# * all of them do not have an implementation in this file
# * some of them are the only overload methods -> overloads usually only make
#   sense if there are multiple ones
# However, we need these overloads due to how the propertysetter works
# mypy: disable-error-code="no-overload-impl, empty-body, misc"
"""

BASE_SCHEMA: Final = """
class {basename}(SchemaBase):
    _rootschema = load_schema()
    @classmethod
    def _default_wrapper_classes(cls) -> Iterator[type[Any]]:
        return _subclasses({basename})
"""

LOAD_SCHEMA: Final = '''
def load_schema() -> dict:
    """Load the json schema associated with this module's functions"""
    schema_bytes = pkgutil.get_data(__name__, "{schemafile}")
    if schema_bytes is None:
        raise ValueError("Unable to load {schemafile}")
    return json.loads(
        schema_bytes.decode("utf-8")
    )
'''


CHANNEL_MIXINS: Final = """
class FieldChannelMixin:
    _encoding_name: str
    def to_dict(
        self,
        validate: bool = True,
        ignore: list[str] | None = None,
        context: dict[str, Any] | None = None,
    ) -> dict | list[dict]:
        context = context or {}
        ignore = ignore or []
        shorthand = self._get("shorthand")  # type: ignore[attr-defined]
        field = self._get("field")  # type: ignore[attr-defined]

        if shorthand is not Undefined and field is not Undefined:
            msg = f"{self.__class__.__name__} specifies both shorthand={shorthand} and field={field}. "
            raise ValueError(msg)

        if isinstance(shorthand, (tuple, list)):
            # If given a list of shorthands, then transform it to a list of classes
            kwds = self._kwds.copy()  # type: ignore[attr-defined]
            kwds.pop("shorthand")
            return [
                self.__class__(sh, **kwds).to_dict(  # type: ignore[call-arg]
                    validate=validate, ignore=ignore, context=context
                )
                for sh in shorthand
            ]

        if shorthand is Undefined:
            parsed = {}
        elif isinstance(shorthand, str):
            data: nw.DataFrame | Any = context.get("data", None)
            parsed = parse_shorthand(shorthand, data=data)
            type_required = "type" in self._kwds  # type: ignore[attr-defined]
            type_in_shorthand = "type" in parsed
            type_defined_explicitly = self._get("type") is not Undefined  # type: ignore[attr-defined]
            if not type_required:
                # Secondary field names don't require a type argument in VegaLite 3+.
                # We still parse it out of the shorthand, but drop it here.
                parsed.pop("type", None)
            elif not (type_in_shorthand or type_defined_explicitly):
                if isinstance(data, nw.DataFrame):
                    msg = (
                        f'Unable to determine data type for the field "{shorthand}";'
                        " verify that the field name is not misspelled."
                        " If you are referencing a field from a transform,"
                        " also confirm that the data type is specified correctly."
                    )
                    raise ValueError(msg)
                else:
                    msg = (
                        f"{shorthand} encoding field is specified without a type; "
                        "the type cannot be automatically inferred because "
                        "the data is not specified as a pandas.DataFrame."
                    )
                    raise ValueError(msg)
        else:
            # Shorthand is not a string; we pass the definition to field,
            # and do not do any parsing.
            parsed = {"field": shorthand}
        context["parsed_shorthand"] = parsed

        return super(FieldChannelMixin, self).to_dict(
            validate=validate, ignore=ignore, context=context
        )


class ValueChannelMixin:
    _encoding_name: str
    def to_dict(
        self,
        validate: bool = True,
        ignore: list[str] | None = None,
        context: dict[str, Any] | None = None,
    ) -> dict:
        context = context or {}
        ignore = ignore or []
        condition = self._get("condition", Undefined)  # type: ignore[attr-defined]
        copy = self  # don't copy unless we need to
        if condition is not Undefined:
            if isinstance(condition, core.SchemaBase):
                pass
            elif "field" in condition and "type" not in condition:
                kwds = parse_shorthand(condition["field"], context.get("data", None))
                copy = self.copy(deep=["condition"])  # type: ignore[attr-defined]
                copy["condition"].update(kwds)  # type: ignore[index]
        return super(ValueChannelMixin, copy).to_dict(
            validate=validate, ignore=ignore, context=context
        )


class DatumChannelMixin:
    _encoding_name: str
    def to_dict(
        self,
        validate: bool = True,
        ignore: list[str] | None = None,
        context: dict[str, Any] | None = None,
    ) -> dict:
        context = context or {}
        ignore = ignore or []
        datum = self._get("datum", Undefined)  # type: ignore[attr-defined] # noqa
        copy = self  # don't copy unless we need to
        return super(DatumChannelMixin, copy).to_dict(
            validate=validate, ignore=ignore, context=context
        )
"""

MARK_MIXIN: Final = '''
class MarkMethodMixin:
    """A mixin class that defines mark methods"""

{methods}
'''

MARK_METHOD: Final = '''
def mark_{mark}(self, {method_args}, **kwds) -> Self:
    """Set the chart's mark to '{mark}' (see :class:`{mark_def}`)."""
    kwds = dict({dict_args}, **kwds)
    copy = self.copy(deep=False)  # type: ignore[attr-defined]
    if any(val is not Undefined for val in kwds.values()):
        copy.mark = core.{mark_def}(type="{mark}", **kwds)
    else:
        copy.mark = "{mark}"
    return copy
'''

CONFIG_METHOD: Final = """
@use_signature(core.{classname})
def {method}(self, *args, **kwargs) -> Self:
    copy = self.copy(deep=False)  # type: ignore[attr-defined]
    copy.config = core.{classname}(*args, **kwargs)
    return copy
"""

CONFIG_PROP_METHOD: Final = """
@use_signature(core.{classname})
def configure_{prop}(self, *args, **kwargs) -> Self:
    copy = self.copy(deep=['config'])  # type: ignore[attr-defined]
    if copy.config is Undefined:
        copy.config = core.Config()
    copy.config["{prop}"] = core.{classname}(*args, **kwargs)
    return copy
"""
UNIVERSAL_TYPED_DICT = '''
class {name}(TypedDict{metaclass_kwds}):{comment}
    """{doc}"""

    {typed_dict_args}
'''
ENCODE_KWDS: Literal["EncodeKwds"] = "EncodeKwds"
THEME_CONFIG: Literal["ThemeConfig"] = "ThemeConfig"
ENCODE_KWDS_SUMMARY: Final = (
    "Encoding channels map properties of the data to visual properties of the chart."
)
THEME_CONFIG_SUMMARY: Final = (
    "Top-Level Configuration ``TypedDict`` for creating a consistent theme."
)
EXTRA_ITEMS_MESSAGE: Final = """\
    Notes
    -----
    The following keys may be specified as string literals **only**:

        {invalid_kwds}

    See `PEP728`_ for type checker compatibility.

    .. _PEP728:
        https://peps.python.org/pep-0728/#reference-implementation
"""

ENCODE_METHOD: Final = '''
class _EncodingMixin:
    def encode({method_args}) -> Self:
        """Map properties of the data to visual properties of the chart (see :class:`FacetedEncoding`)
        {docstring}"""
        # Compat prep for `infer_encoding_types` signature
        kwargs = locals()
        kwargs.pop("self")
        args = kwargs.pop("args")
        if args:
            kwargs = {{k: v for k, v in kwargs.items() if v is not Undefined}}

        # Convert args to kwargs based on their types.
        kwargs = _infer_encoding_types(args, kwargs)
        # get a copy of the dict representation of the previous encoding
        # ignore type as copy method comes from SchemaBase
        copy = self.copy(deep=['encoding'])  # type: ignore[attr-defined]
        encoding = copy._get('encoding', {{}})
        if isinstance(encoding, core.VegaLiteSchema):
            encoding = {{k: v for k, v in encoding._kwds.items() if v is not Undefined}}
        # update with the new encodings, and apply them to the copy
        encoding.update(kwargs)
        copy.encoding = core.FacetedEncoding(**encoding)
        return copy
'''


# NOTE: Not yet reasonable to generalize `TypeAliasType`, `TypeVar`
# Revisit if this starts to become more common
TYPING_EXTRA: Final = '''
T = TypeVar("T")
OneOrSeq = TypeAliasType("OneOrSeq", Union[T, Sequence[T]], type_params=(T,))
"""
One of ``T`` specified type(s), or a `Sequence` of such.

Examples
--------
The parameters ``short``, ``long`` accept the same range of types::

    # ruff: noqa: UP006, UP007

    def func(
        short: OneOrSeq[str | bool | float],
        long: Union[str, bool, float, Sequence[Union[str, bool, float]],
    ): ...
"""

class Value(TypedDict, Generic[T]):
    """
    A `Generic`_ single item ``dict``.

    Parameters
    ----------
    value: T
        Wrapped value.

    .. _Generic:
        https://typing.readthedocs.io/en/latest/spec/generics.html#generics

    """

    value: T


ColorHex = Annotated[
    LiteralString,
    re.compile(r"#[0-9a-f]{2}[0-9a-f]{2}[0-9a-f]{2}([0-9a-f]{2})?", re.IGNORECASE),
]
"""
A `hexadecimal`_ color code.

Corresponds to the ``json-schema`` string format:

    {"format": "color-hex", "type": "string"}

Examples
--------
:

    "#f0f8ff"
    "#7fffd4"
    "#000000"
    "#0000FF"
    "#0000ff80"

.. _hexadecimal:
    https://www.w3schools.com/html/html_colors_hex.asp
"""

def is_color_hex(obj: Any) -> TypeIs[ColorHex]:
    """Return ``True`` if the object is a hexadecimal color code."""
    # NOTE: Extracts compiled pattern from metadata,
    # to avoid defining  in multiple places.
    it = iter(get_args(ColorHex))
    next(it)
    pattern: re.Pattern[str] = next(it)
    return bool(pattern.fullmatch(obj))

'''

_ChannelType = Literal["field", "datum", "value"]


class SchemaGenerator(codegen.SchemaGenerator):
    schema_class_template = textwrap.dedent(
        '''
    class {classname}({basename}):
        """{docstring}"""
        _schema = {schema!r}

        {init_code}
    '''
    )


class FieldSchemaGenerator(SchemaGenerator):
    schema_class_template = textwrap.dedent(
        '''
    @with_property_setters
    class {classname}(FieldChannelMixin, core.{basename}):
        """{docstring}"""
        _class_is_valid_at_instantiation = False
        _encoding_name = "{encodingname}"

        {method_code}

        {init_code}
    '''
    )


class ValueSchemaGenerator(SchemaGenerator):
    schema_class_template = textwrap.dedent(
        '''
    @with_property_setters
    class {classname}(ValueChannelMixin, core.{basename}):
        """{docstring}"""
        _class_is_valid_at_instantiation = False
        _encoding_name = "{encodingname}"

        {method_code}

        {init_code}
    '''
    )


class DatumSchemaGenerator(SchemaGenerator):
    schema_class_template = textwrap.dedent(
        '''
    @with_property_setters
    class {classname}(DatumChannelMixin, core.{basename}):
        """{docstring}"""
        _class_is_valid_at_instantiation = False
        _encoding_name = "{encodingname}"

        {method_code}

        {init_code}
    '''
    )


def schema_class(*args, **kwargs) -> str:
    return SchemaGenerator(*args, **kwargs).schema_class()


def schema_url(version: str = SCHEMA_VERSION) -> str:
    return SCHEMA_URL_TEMPLATE.format(library="vega-lite", version=version)


def download_schemafile(
    version: str, schemapath: Path, skip_download: bool = False
) -> Path:
    url = schema_url(version=version)
    schemadir = Path(schemapath)
    schemadir.mkdir(parents=True, exist_ok=True)
    fp = schemadir / SCHEMA_FILE
    if not skip_download:
        request.urlretrieve(url, fp)
    elif not fp.exists():
        msg = f"Cannot skip download: {fp!s} does not exist"
        raise ValueError(msg)
    return fp


def _vega_lite_props_only(
    themes: dict[str, dict[str, Any]], props: SchemaProperties, /
) -> Iterator[tuple[str, dict[str, Any]]]:
    """Removes properties that are allowed in `Vega` but not `Vega-Lite` from theme definitions."""
    keep = props.keys()
    for name, theme_spec in themes.items():
        yield name, {k: v for k, v in theme_spec.items() if k in keep}


def update_vega_themes(fp: Path, /, indent: str | int | None = 2) -> None:
    root = load_schema(fp.parent / SCHEMA_FILE)
    vl_props = SchemaInfo({"$ref": "#/definitions/Config"}, root).properties
    themes = dict(_vega_lite_props_only(vlc.get_themes(), vl_props))
    data = json.dumps(themes, indent=indent, sort_keys=True)
    fp.write_text(data, encoding="utf8")

    theme_names = sorted(iter(themes))
    TypeAliasTracer.update_aliases(("VegaThemes", spell_literal(theme_names)))


def load_schema(fp: Path, /) -> dict[str, Any]:
    """Reads and returns the root schema from ``fp``."""
    with fp.open(encoding="utf8") as f:
        root_schema = json.load(f)
    return root_schema


def load_schema_with_shorthand_properties(fp: Path, /) -> dict[str, Any]:
    schema = load_schema(fp)
    encoding_def = "FacetedEncoding"
    encoding = SchemaInfo(schema["definitions"][encoding_def], rootschema=schema)
    shorthand = {
        "anyOf": [
            {"type": "string"},
            {"type": "array", "items": {"type": "string"}},
            {"$ref": "#/definitions/RepeatRef"},
        ],
        "description": "shorthand for field, aggregate, and type",
    }
    for propschema in encoding.properties.values():
        def_dict = get_field_datum_value_defs(propschema, schema)
        if field_ref := def_dict.get("field", None):
            defschema: dict[str, Any] = {"$ref": field_ref}
            defschema = copy.deepcopy(resolve_references(defschema, schema))
            # For Encoding field definitions, we patch the schema by adding the
            # shorthand property.
            defschema["properties"]["shorthand"] = shorthand
            if "required" not in defschema:
                defschema["required"] = ["shorthand"]
            elif "shorthand" not in defschema["required"]:
                defschema["required"].append("shorthand")
            schema["definitions"][field_ref.split("/")[-1]] = defschema
    return schema


def copy_schemapi_util() -> None:
    """Copy the schemapi utility into altair/utils/ and its test file to tests/utils/."""
    # copy the schemapi utility file
    source_fp = Path(__file__).parent / "schemapi" / "schemapi.py"
    destination_fp = Path(__file__).parent / ".." / "altair" / "utils" / "schemapi.py"

    print(f"Copying\n {source_fp!s}\n  -> {destination_fp!s}")
    with source_fp.open(encoding="utf8") as source, destination_fp.open(
        "w", encoding="utf8"
    ) as dest:
        dest.write(HEADER_COMMENT)
        dest.writelines(source.readlines())
    if sys.platform == "win32":
        ruff_format_py(destination_fp)


def recursive_dict_update(schema: dict, root: dict, def_dict: dict) -> None:
    if "$ref" in schema:
        next_schema = resolve_references(schema, root)
        if "properties" in next_schema:
            definition = schema["$ref"]
            properties = next_schema["properties"]
            for k in def_dict:
                if k in properties:
                    def_dict[k] = definition
        else:
            recursive_dict_update(next_schema, root, def_dict)
    elif "anyOf" in schema:
        for sub_schema in schema["anyOf"]:
            recursive_dict_update(sub_schema, root, def_dict)


def get_field_datum_value_defs(
    propschema: SchemaInfo, root: dict[str, Any]
) -> dict[_ChannelType, str]:
    def_dict: dict[_ChannelType, str | None] = dict.fromkeys(
        ("field", "datum", "value")
    )
    _schema = propschema.schema
    schema = _schema if isinstance(_schema, dict) else dict(_schema)
    if propschema.is_reference() and "properties" in schema:
        if "field" in schema["properties"]:
            def_dict["field"] = propschema.ref
        else:
            msg = "Unexpected schema structure"
            raise ValueError(msg)
    else:
        recursive_dict_update(schema, root, def_dict)

    return {i: j for i, j in def_dict.items() if j}


def toposort(graph: dict[str, list[str]]) -> list[str]:
    """
    Topological sort of a directed acyclic graph.

    Parameters
    ----------
    graph : dict of lists
        Mapping of node labels to list of child node labels.
        This is assumed to represent a graph with no cycles.

    Returns
    -------
    order : list
        topological order of input graph.
    """
    # Once we drop support for Python 3.8, this can potentially be replaced
    # with graphlib.TopologicalSorter from the standard library.
    stack: list[str] = []
    visited: dict[str, Literal[True]] = {}

    def visit(nodes):
        for node in sorted(nodes, reverse=True):
            if not visited.get(node):
                visited[node] = True
                visit(graph.get(node, []))
                stack.insert(0, node)

    visit(graph)
    return stack


def generate_vegalite_schema_wrapper(fp: Path, /) -> str:
    """Generate a schema wrapper at the given path."""
    # TODO: generate simple tests for each wrapper
    basename = "VegaLiteSchema"
    rootschema = load_schema_with_shorthand_properties(fp)
    definitions: dict[str, SchemaGenerator] = {}
    graph: dict[str, list[str]] = {}

    for name in rootschema["definitions"]:
        defschema = {"$ref": "#/definitions/" + name}
        defschema_repr = {"$ref": "#/definitions/" + name}
        name = get_valid_identifier(name)
        definitions[name] = SchemaGenerator(
            name,
            schema=defschema,
            schemarepr=defschema_repr,
            rootschema=rootschema,
            basename=basename,
            rootschemarepr=CodeSnippet(f"{basename}._rootschema"),
        )
    for name, schema in definitions.items():
        graph[name] = []
        for child_name in schema.subclasses():
            child_name = get_valid_identifier(child_name)
            graph[name].append(child_name)
            child: SchemaGenerator = definitions[child_name]
            if child.basename == basename:
                child.basename = [name]
            else:
                assert isinstance(child.basename, list)
                child.basename.append(name)

    # Specify __all__ explicitly so that we can exclude the ones from the list
    # of exported classes which are also defined in the channels or api modules which takes
    # precedent in the generated __init__.py files one and two levels up.
    # Importing these classes from multiple modules confuses type checkers.
    EXCLUDE = {"Color", "Text", "LookupData", "Dict", "FacetMapping"}
    it = (c for c in definitions.keys() - EXCLUDE if not c.startswith("_"))
    all_ = [*sorted(it), "Root", "VegaLiteSchema", "SchemaBase", "load_schema"]
    contents = [
        HEADER,
        "from typing import Any, Literal, Union, Protocol, Sequence, List, Iterator, TYPE_CHECKING",
        "import pkgutil",
        "import json\n",
        "from narwhals.dependencies import is_pandas_dataframe as _is_pandas_dataframe",
        "from altair.utils.schemapi import SchemaBase, Undefined, UndefinedType, _subclasses # noqa: F401\n",
        import_type_checking(
            "from altair import Parameter",
            "from altair.typing import Optional",
            "from ._typing import * # noqa: F403",
        ),
        "\n" f"__all__ = {all_}\n",
        LOAD_SCHEMA.format(schemafile=SCHEMA_FILE),
        BASE_SCHEMA.format(basename=basename),
        schema_class(
            "Root",
            schema=rootschema,
            basename=basename,
            schemarepr=CodeSnippet(f"{basename}._rootschema"),
        ),
    ]

    for name in toposort(graph):
        contents.append(definitions[name].schema_class())

    contents.append("")  # end with newline
    return "\n".join(contents)


@dataclass
class ChannelInfo:
    supports_arrays: bool
    deep_description: str
    field_class_name: str
    datum_class_name: str | None = None
    value_class_name: str | None = None

    @property
    def is_field_only(self) -> bool:
        return not (self.datum_class_name or self.value_class_name)

    @property
    def all_names(self) -> Iterator[str]:
        """All channels are expected to have a field class."""
        yield self.field_class_name
        yield from self.non_field_names

    @property
    def non_field_names(self) -> Iterator[str]:
        if self.is_field_only:
            yield from ()
        else:
            if self.datum_class_name:
                yield self.datum_class_name
            if self.value_class_name:
                yield self.value_class_name


def generate_vegalite_channel_wrappers(
    fp: Path, /, version: str, imports: list[str] | None = None
) -> str:
    schema = load_schema_with_shorthand_properties(fp)
    encoding_def = "FacetedEncoding"
    encoding = SchemaInfo(schema["definitions"][encoding_def], rootschema=schema)
    channel_infos: dict[str, ChannelInfo] = {}
    class_defs: list[Any] = []

    for prop, propschema in encoding.properties.items():
        def_dict = get_field_datum_value_defs(propschema, schema)
        supports_arrays = any(
            schema_info.is_array() for schema_info in propschema.anyOf
        )
        classname: str = prop[0].upper() + prop[1:]
        channel_info = ChannelInfo(
            supports_arrays=supports_arrays,
            deep_description=propschema.deep_description,
            field_class_name=classname,
        )

        for encoding_spec, definition in def_dict.items():
            basename = definition.rsplit("/", maxsplit=1)[-1]
            basename = get_valid_identifier(basename)

            gen: SchemaGenerator
            defschema = {"$ref": definition}
            kwds: dict[str, Any] = {
                "basename": basename,
                "schema": defschema,
                "rootschema": schema,
                "encodingname": prop,
                "haspropsetters": True,
            }
            if encoding_spec == "field":
                gen = FieldSchemaGenerator(classname, nodefault=[], **kwds)
            elif encoding_spec == "datum":
                temp_name = f"{classname}Datum"
                channel_info.datum_class_name = temp_name
                gen = DatumSchemaGenerator(temp_name, nodefault=["datum"], **kwds)
            elif encoding_spec == "value":
                temp_name = f"{classname}Value"
                channel_info.value_class_name = temp_name
                gen = ValueSchemaGenerator(temp_name, nodefault=["value"], **kwds)
            else:
                raise NotImplementedError

            class_defs.append(gen.schema_class())

        channel_infos[prop] = channel_info

    # NOTE: See https://github.com/vega/altair/pull/3482#issuecomment-2241577342
    COMPAT_EXPORTS = (
        "DatumChannelMixin",
        "FieldChannelMixin",
        "ValueChannelMixin",
        "with_property_setters",
    )
    it = chain.from_iterable(info.all_names for info in channel_infos.values())
    all_ = list(chain(it, COMPAT_EXPORTS))
    imports = imports or [
        "import sys",
        "from typing import Any, overload, Sequence, List, Literal, Union, TYPE_CHECKING, TypedDict",
        import_typing_extensions((3, 10), "TypeAlias"),
        "import narwhals.stable.v1 as nw",
        "from altair.utils.schemapi import Undefined, with_property_setters",
        "from altair.utils import infer_encoding_types as _infer_encoding_types",
        "from altair.utils import parse_shorthand",
        "from . import core",
        "from ._typing import * # noqa: F403",
    ]
    contents = [
        HEADER,
        CHANNEL_MYPY_IGNORE_STATEMENTS,
        *imports,
        import_type_checking(
            "from altair import Parameter, SchemaBase",
            "from altair.typing import Optional",
            textwrap.indent(import_typing_extensions((3, 11), "Self"), "    "),
        ),
        "\n" f"__all__ = {sorted(all_)}\n",
        CHANNEL_MIXINS,
        *class_defs,
        *generate_encoding_artifacts(
            channel_infos, ENCODE_METHOD, facet_encoding=encoding
        ),
    ]
    return "\n".join(contents)


def generate_vegalite_mark_mixin(fp: Path, /, markdefs: dict[str, str]) -> str:
    schema = load_schema(fp)
    code: list[str] = []

    for mark_enum, mark_def in markdefs.items():
        _def = schema["definitions"][mark_enum]
        marks: list[Any] = _def["enum"] if "enum" in _def else [_def["const"]]
        info = SchemaInfo({"$ref": f"#/definitions/{mark_def}"}, rootschema=schema)
        mark_args = generate_mark_args(info)

        for mark in marks:
            # TODO: only include args relevant to given type?
            mark_method = MARK_METHOD.format(mark=mark, mark_def=mark_def, **mark_args)
            code.append("\n    ".join(mark_method.splitlines()))

    return MARK_MIXIN.format(methods="\n".join(code))


def generate_mark_args(
    info: SchemaInfo, /
) -> dict[Literal["method_args", "dict_args"], str]:
    args = codegen.get_args(info)
    method_args: deque[str] = deque()
    dict_args: deque[str] = deque()
    for p, p_info in args.iter_args(args.required | args.kwds, exclude="type"):
        dict_args.append(f"{p}={p}")
        method_args.append(
            f"{p}: {p_info.to_type_repr(target='annotation', use_undefined=True)} = Undefined"
        )
    return {"method_args": ", ".join(method_args), "dict_args": ", ".join(dict_args)}


def _typed_dict_args(info: SchemaInfo, /) -> str:
    args = codegen.get_args(info)
    return "\n    ".join(
        f"{p}: {p_info.to_type_repr(target='annotation', use_concrete=True)}"
        for p, p_info in args.iter_args(args.required, args.kwds)
    )


def _typed_dict_doc(info: SchemaInfo, /, *, summary: str | None = None) -> str:
    args = codegen.get_args(info)
    it = chain.from_iterable(
        (p, f"    {p_info.deep_description}")
        for p, p_info in args.iter_args(args.required, args.kwds)
    )
    lines = (
        summary or f"{info.title} ``TypedDict`` wrapper.",
        "",
        "Parameters",
        "----------",
    )
    return indent_docstring(chain(lines, it), indent_level=4, lstrip=False)


def generate_typed_dict(
    info: SchemaInfo,
    name: str,
    *,
    summary: str | None = None,
    override_args: Iterable[str] | None = None,
) -> str:
    """
    _summary_.

    TODO: Tidy up, finish doc

    Parameters
    ----------
    info
        Schema.
    name
        Full target class name.
        Include a pre/post-fix if ``SchemaInfo.title`` already exists.
    summary
        When provided, used instead of generated summary line.
    override_args
        Inject custom handling for types.

    Notes
    -----
    - Internally handles keys that are not valid python identifiers
    """
    TARGET: Literal["annotation"] = "annotation"
    arg_info = codegen.get_args(info)
    metaclass_kwds = ", total=False"
    comment = ""
    td_args = (
        _typed_dict_args(info)
        if override_args is None
        else "\n    ".join(override_args)
    )
    td_doc = _typed_dict_doc(info, summary=summary)
    if kwds := arg_info.invalid_kwds:
        metaclass_kwds = f", closed=True{metaclass_kwds}"
        comment = "  # type: ignore[call-arg]"
        kwds_all_tps = chain.from_iterable(
            info.to_type_repr(as_str=False, target=TARGET, use_concrete=True)
            for _, info in arg_info.iter_args(kwds)
        )
        td_args = (
            f"{td_args}\n    "
            f"__extra_items__: {finalize_type_reprs(kwds_all_tps, target=TARGET)}"
        )
        td_doc = (
            f"{td_doc}\n"
            f"{EXTRA_ITEMS_MESSAGE.format(invalid_kwds=repr(sorted(kwds)))}"
        )

    return UNIVERSAL_TYPED_DICT.format(
        name=name,
        metaclass_kwds=metaclass_kwds,
        comment=comment,
        doc=td_doc,
        typed_dict_args=td_args,
    )


def generate_config_typed_dicts(fp: Path, /) -> Iterator[str]:
    KWDS: Literal["Kwds"] = "Kwds"
    config = SchemaInfo({"$ref": "#/definitions/Config"}, load_schema(fp))

    relevant: dict[str, SchemaInfo] = {
        x.title: x
        for x in sorted(find_theme_config_targets(config), key=attrgetter("refname"))
        if x.refname != "Config"
    }
    SchemaInfo._remap_title.update({"HexColor": "ColorHex"})
    SchemaInfo._remap_title.update((k, f"{k}{KWDS}") for k in relevant)

    config_sub: Iterator[str] = (
        generate_typed_dict(info, name=f"{info.title}{KWDS}")
        for info in relevant.values()
    )
    config_sub_names = (f"{nm}{KWDS}" for nm in relevant)
    yield f"__all__ = {[*config_sub_names, THEME_CONFIG]}\n\n"
    yield "\n".join(config_sub)
    yield generate_typed_dict(config, THEME_CONFIG, summary=THEME_CONFIG_SUMMARY)


def find_theme_config_targets(info: SchemaInfo, depth: int = 0, /) -> set[SchemaInfo]:
    """Equivalent to `get_all_objects`."""
    MAX_DEPTH = 6
    seen: set[SchemaInfo] = set()
    if info.is_theme_config_target() and info not in seen:
        seen.add(info)
    if depth < MAX_DEPTH:
        for prop_info in info.iter_descendants():
            seen.update(find_theme_config_targets(prop_info, depth + 1))
    return seen


def generate_vegalite_config_mixin(fp: Path, /) -> str:
    class_name = "ConfigMethodMixin"
    code = [
        f"class {class_name}:",
        '    """A mixin class that defines config methods"""',
    ]
    schema = load_schema(fp)
    info = SchemaInfo({"$ref": "#/definitions/Config"}, rootschema=schema)

    # configure() method
    method = CONFIG_METHOD.format(classname="Config", method="configure")
    code.append("\n    ".join(method.splitlines()))

    # configure_prop() methods
    for prop, prop_info in info.properties.items():
        classname = prop_info.refname
        if classname and classname.endswith("Config"):
            method = CONFIG_PROP_METHOD.format(classname=classname, prop=prop)
            code.append("\n    ".join(method.splitlines()))
    return "\n".join(code)


def vegalite_main(skip_download: bool = False) -> None:
    version = SCHEMA_VERSION
    vn = version.split(".")[0]
    fp = (Path(__file__).parent / ".." / "altair" / "vegalite" / vn).resolve()
    schemapath = fp / "schema"
    schemafile = download_schemafile(
        version=version,
        schemapath=schemapath,
        skip_download=skip_download,
    )

    fp_themes = schemapath / THEMES_FILE
    print(f"Updating themes\n {schemafile!s}\n  ->{fp_themes!s}")
    update_vega_themes(fp_themes)

    # Generate __init__.py file
    outfile = schemapath / "__init__.py"
    print(f"Writing {outfile!s}")
    content = [
        "# ruff: noqa\n",
        "from .core import *\nfrom .channels import *\n",
        f"SCHEMA_VERSION = '{version}'\n",
        f"SCHEMA_URL = {schema_url(version)!r}\n",
    ]
    ruff_write_lint_format_str(outfile, content)

    TypeAliasTracer.update_aliases(("Map", "Mapping[str, Any]"))

    files: dict[Path, str | Iterable[str]] = {}

    # Generate the core schema wrappers
    fp_core = schemapath / "core.py"
    print(f"Generating\n {schemafile!s}\n  ->{fp_core!s}")
    files[fp_core] = generate_vegalite_schema_wrapper(schemafile)

    # Generate the channel wrappers
    fp_channels = schemapath / "channels.py"
    print(f"Generating\n {schemafile!s}\n  ->{fp_channels!s}")
    files[fp_channels] = generate_vegalite_channel_wrappers(schemafile, version=version)

    # generate the mark mixin
    markdefs = {k: f"{k}Def" for k in ["Mark", "BoxPlot", "ErrorBar", "ErrorBand"]}
    fp_mixins = schemapath / "mixins.py"
    print(f"Generating\n {schemafile!s}\n  ->{fp_mixins!s}")
    mixins_imports = (
        "from typing import Any, Sequence, List, Literal, Union",
        "from altair.utils import use_signature, Undefined",
        "from . import core",
    )

    mark_mixin = generate_vegalite_mark_mixin(schemafile, markdefs)
    config_mixin = generate_vegalite_config_mixin(schemafile)
    content_mixins = [
        HEADER,
        "\n\n",
        "\n".join(mixins_imports),
        "\n\n",
        import_type_checking(
            "import sys",
            textwrap.indent(import_typing_extensions((3, 11), "Self"), "    "),
            "from altair.typing import Optional",
            "from ._typing import * # noqa: F403",
            "from altair import Parameter, SchemaBase",
        ),
        "\n\n\n",
        mark_mixin,
        "\n\n\n",
        config_mixin,
    ]
    files[fp_mixins] = content_mixins

    # Generate theme-related Config hierarchy of TypedDict
    fp_theme_config: Path = schemapath / "_config.py"
    content_theme_config = [
        HEADER,
        "from typing import Any, TYPE_CHECKING, Literal, Sequence, TypedDict, Union",
        import_typing_extensions((3, 14), "TypedDict", include_sys=True),
        "\n\n",
        import_type_checking("from ._typing import * # noqa: F403"),
        "\n\n",
        *generate_config_typed_dicts(schemafile),
    ]
    files[fp_theme_config] = content_theme_config

    # Write `_typing.py` TypeAlias, for import in generated modules
    fp_typing = schemapath / "_typing.py"
    msg = (
        f"Generating\n {schemafile!s}\n  ->{fp_typing!s}\n"
        f"Tracer cache collected {TypeAliasTracer.n_entries!r} entries."
    )
    print(msg)
    TypeAliasTracer.write_module(
        fp_typing,
        "OneOrSeq",
        "Value",
        "ColorHex",
        "is_color_hex",
        header=HEADER,
        extra=TYPING_EXTRA,
    )
    # Write the pre-generated modules
    for fp, contents in files.items():
        print(f"Writing\n {schemafile!s}\n  ->{fp!s}")
        ruff_write_lint_format_str(fp, contents)


def generate_encoding_artifacts(
    channel_infos: dict[str, ChannelInfo],
    fmt_method: str,
    *,
    facet_encoding: SchemaInfo,
) -> Iterator[str]:
    """
    Generate ``Chart.encode()`` and related typing structures.

    - `TypeAlias`(s) for each parameter to ``Chart.encode()``
    - Mixin class that provides the ``Chart.encode()`` method
    - `TypedDict`, utilising/describing these structures as part of https://github.com/pola-rs/polars/pull/17995.

    Notes
    -----
    - `Map`/`Dict` stands for the return types of `alt.(datum|value)`, and any encoding channel class.
        - See discussions in https://github.com/vega/altair/pull/3208
    - We could be more specific about what types are accepted in the `List`
        - but this translates poorly to an IDE
        - `info.supports_arrays`
    """
    signature_args: list[str] = ["self", "*args: Any"]
    type_aliases: list[str] = []
    typed_dict_args: list[str] = []
    signature_doc_params: list[str] = ["", "Parameters", "----------"]

    for channel, info in channel_infos.items():
        alias_name: str = f"Channel{channel[0].upper()}{channel[1:]}"

        it: Iterator[str] = info.all_names
        it_rst_names: Iterator[str] = (rst_syntax_for_class(c) for c in info.all_names)

        docstring_types: list[str] = ["str", next(it_rst_names), "Dict"]
        tp_inner: str = ", ".join(chain(("str", next(it), "Map"), it))
        tp_inner = f"Union[{tp_inner}]"

        if info.supports_arrays:
            docstring_types.append("List")
            tp_inner = f"OneOrSeq[{tp_inner}]"

        doc_types_flat: str = ", ".join(chain(docstring_types, it_rst_names))

        type_aliases.append(f"{alias_name}: TypeAlias = {tp_inner}")
        # We use the full type hints instead of the alias in the signatures below
        # as IDEs such as VS Code would else show the name of the alias instead
        # of the expanded full type hints. The later are more useful to users.
        typed_dict_args.append(f"{channel}: {tp_inner}")
        signature_args.append(f"{channel}: Optional[{tp_inner}] = Undefined")

        description: str = f"    {info.deep_description}"

        signature_doc_params.extend((f"{channel} : {doc_types_flat}", description))

    method: str = fmt_method.format(
        method_args=", ".join(signature_args),
        docstring=indent_docstring(signature_doc_params, indent_level=8, lstrip=False),
    )
    typed_dict = generate_typed_dict(
        facet_encoding,
        ENCODE_KWDS,
        summary=ENCODE_KWDS_SUMMARY,
        override_args=typed_dict_args,
    )
    artifacts: Iterable[str] = *type_aliases, method, typed_dict
    yield from artifacts


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="generate_schema_wrapper.py", description="Generate the Altair package."
    )
    parser.add_argument(
        "--skip-download", action="store_true", help="skip downloading schema files"
    )
    args = parser.parse_args()
    copy_schemapi_util()
    vegalite_main(args.skip_download)

    # The modules below are imported after the generation of the new schema files
    # as these modules import Altair. This allows them to use the new changes
    from tools import generate_api_docs, update_init_file

    generate_api_docs.write_api_file()
    update_init_file.update__all__variable()


if __name__ == "__main__":
    main()
