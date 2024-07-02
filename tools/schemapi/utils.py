"""Utilities for working with schemas"""

from __future__ import annotations
from itertools import chain
import keyword
import re
import subprocess
import textwrap
import urllib
from typing import Any, Final, Iterable, TYPE_CHECKING, Iterator, Sequence
from operator import itemgetter
from tools.schemapi.schemapi import _resolve_references as resolve_references

if TYPE_CHECKING:
    from typing_extensions import LiteralString
    from pathlib import Path

EXCLUDE_KEYS: Final = ("definitions", "title", "description", "$schema", "id")

jsonschema_to_python_types = {
    "string": "str",
    "number": "float",
    "integer": "int",
    "object": "dict",
    "boolean": "bool",
    "array": "list",
    "null": "None",
}


class _TypeAliasTracer:
    """Recording all `enum` -> `Literal` translations.

    Rewrites as `TypeAlias` to be reused anywhere, and not clog up method definitions.

    Parameters
    ----------
    fmt
        A format specifier to produce the `TypeAlias` name.

        Will be provided a `SchemaInfo.title` as a single positional argument.
    *ruff_check
        Optional [ruff rule codes](https://docs.astral.sh/ruff/rules/),
        each prefixed with `--select ` and follow a `ruff check --fix ` call.

        If not provided, uses `[tool.ruff.lint.select]` from `pyproject.toml`.
    ruff_format
        Optional argument list supplied to [ruff format](https://docs.astral.sh/ruff/formatter/#ruff-format)

    Attributes
    ----------
    _literals: dict[str, str]
        `{alias_name: literal_statement}`
    _literals_invert: dict[str, str]
        `{literal_statement: alias_name}`
    aliases: list[tuple[str, str]]
        `_literals` sorted by `alias_name`
    _imports: Sequence[str]
        Prefined import statements to appear at beginning of module.
    """

    def __init__(
        self,
        fmt: str = "{}_T",
        *ruff_check: str,
        ruff_format: Sequence[str] | None = None,
    ) -> None:
        self.fmt: str = fmt
        self._literals: dict[str, str] = {}
        self._literals_invert: dict[str, str] = {}
        self.aliases: list[tuple[str, str]] = []
        self._imports: Sequence[str] = (
            "from __future__ import annotations\n",
            "from typing import Literal, Mapping, Any",
            "from typing_extensions import TypeAlias",
        )
        self._cmd_check: list[str] = ["--fix"]
        self._cmd_format: Sequence[str] = ruff_format or ()
        for c in ruff_check:
            self._cmd_check.extend(("--select", c))

    def _update_literals(self, name: str, tp: str, /) -> None:
        """Produces an inverted index, to reuse a `Literal` when `SchemaInfo.title` is empty."""
        self._literals[name] = tp
        self._literals_invert[tp] = name

    def add_literal(
        self, info: SchemaInfo, tp: str, /, *, replace: bool = False
    ) -> str:
        """`replace=True` returns the eventual alias name.

        - Doing so will mean that the `_typing` module must be written first, before the source of `info`.
        - Otherwise, `ruff` will raise an error during `check`/`format`, as the import will be invalid.
        - Where a `title` is not found, an attempt will be made to find an existing alias definition that had one.
        """
        if info.title:
            alias = self.fmt.format(info.title)
            if alias not in self._literals:
                self._update_literals(alias, tp)
            if replace:
                tp = alias
        elif (alias := self._literals_invert.get(tp)) and replace:
            tp = alias
        return tp

    def generate_aliases(self) -> Iterator[str]:
        """Represents a line per `TypeAlias` declaration.

        Additionally, stores in `self.aliases` an alphabetically sorted list of tuples.
        """
        self.aliases = sorted(self._literals.items(), key=itemgetter(0))
        for name, statement in self.aliases:
            yield f"{name}: TypeAlias = {statement}"

    def write_module(
        self,
        fp: Path,
        *extra_imports: str,
        header: LiteralString,
        extra_aliases: LiteralString,
    ) -> None:
        """Write all collected `TypeAlias`'s to `fp`.

        Parameters
        ----------
        fp
            Path to new module.
        *extra_imports
            Follows `self._imports` block.
        header
            `tools.generate_schema_wrapper.HEADER`.
        extra_aliases
            `tools.generate_schema_wrapper.EXTRA_ALIASES`.
        """
        ruff_format = ["ruff", "format", fp]
        if self._cmd_format:
            ruff_format.extend(self._cmd_format)
        commands = (["ruff", "check", fp, *self._cmd_check], ruff_format)
        static = (header, "\n", *self._imports, *extra_imports, "\n\n", extra_aliases)
        it = chain(static, self.generate_aliases())
        fp.write_text("\n".join(it), encoding="utf-8")
        for cmd in commands:
            r = subprocess.run(cmd, check=True)
            r.check_returncode()

    @property
    def n_entries(self) -> int:
        """Number of unique `TypeAlias` defintions collected."""
        return len(self._literals)


TypeAliasTracer = _TypeAliasTracer("{}_T", "I001", "I002")
"""An instance of `_TypeAliasTracer`.

Collects a cache of unique `Literal` types used globally.

These are then converted to `TypeAlias` statements, written to another module.

Allows for a single definition to be reused multiple times,
rather than repeating long literals in every method definition.
"""


def get_valid_identifier(
    prop: str,
    replacement_character: str = "",
    allow_unicode: bool = False,
    url_decode: bool = True,
) -> str:
    """Given a string property, generate a valid Python identifier

    Parameters
    ----------
    prop: string
        Name of property to decode.
    replacement_character: string, default ''
        The character to replace invalid characters with.
    allow_unicode: boolean, default False
        If True, then allow Python 3-style unicode identifiers.
    url_decode: boolean, default True
        If True, decode URL characters in identifier names.

    Examples
    --------
    >>> get_valid_identifier('my-var')
    'myvar'

    >>> get_valid_identifier('if')
    'if_'

    >>> get_valid_identifier('$schema', '_')
    '_schema'

    >>> get_valid_identifier('$*#$')
    '_'

    >>> get_valid_identifier("Name%3Cstring%3E")
    'Namestring'
    """
    # Decode URL characters.
    if url_decode:
        prop = urllib.parse.unquote(prop)

    # Deal with []
    prop = prop.replace("[]", "Array")

    # First substitute-out all non-valid characters.
    flags = re.UNICODE if allow_unicode else re.ASCII
    valid = re.sub(r"\W", replacement_character, prop, flags=flags)

    # If nothing is left, use just an underscore
    if not valid:
        valid = "_"

    # first character must be a non-digit. Prefix with an underscore
    # if needed
    if re.match(r"^[\d\W]", valid):
        valid = "_" + valid

    # if the result is a reserved keyword, then add an underscore at the end
    if keyword.iskeyword(valid):
        valid += "_"
    return valid


def is_valid_identifier(var: str, allow_unicode: bool = False):
    """Return true if var contains a valid Python identifier

    Parameters
    ----------
    val : string
        identifier to check
    allow_unicode : bool (default: False)
        if True, then allow Python 3 style unicode identifiers.
    """
    flags = re.UNICODE if allow_unicode else re.ASCII
    is_valid = re.match(r"^[^\d\W]\w*\Z", var, flags)
    return is_valid and not keyword.iskeyword(var)


class SchemaProperties:
    """A wrapper for properties within a schema"""

    def __init__(
        self,
        properties: dict[str, Any],
        schema: dict,
        rootschema: dict | None = None,
    ) -> None:
        self._properties = properties
        self._schema = schema
        self._rootschema = rootschema or schema

    def __bool__(self) -> bool:
        return bool(self._properties)

    def __dir__(self) -> list[str]:
        return list(self._properties.keys())

    def __getattr__(self, attr):
        try:
            return self[attr]
        except KeyError:
            return super().__getattr__(attr)

    def __getitem__(self, attr):
        dct = self._properties[attr]
        if "definitions" in self._schema and "definitions" not in dct:
            dct = dict(definitions=self._schema["definitions"], **dct)
        return SchemaInfo(dct, self._rootschema)

    def __iter__(self):
        return iter(self._properties)

    def items(self):
        return ((key, self[key]) for key in self)

    def keys(self):
        return self._properties.keys()

    def values(self):
        return (self[key] for key in self)


class SchemaInfo:
    """A wrapper for inspecting a JSON schema"""

    def __init__(
        self, schema: dict[str, Any], rootschema: dict[str, Any] | None = None
    ) -> None:
        if not rootschema:
            rootschema = schema
        self.raw_schema = schema
        self.rootschema = rootschema
        self.schema = resolve_references(schema, rootschema)

    def child(self, schema: dict) -> SchemaInfo:
        return self.__class__(schema, rootschema=self.rootschema)

    def __repr__(self) -> str:
        keys = []
        for key in sorted(self.schema.keys()):
            val = self.schema[key]
            rval = repr(val).replace("\n", "")
            if len(rval) > 30:
                rval = rval[:30] + "..."
            if key == "definitions":
                rval = "{...}"
            elif key == "properties":
                rval = "{\n    " + "\n    ".join(sorted(map(repr, val))) + "\n  }"
            keys.append(f'"{key}": {rval}')
        return "SchemaInfo({\n  " + "\n  ".join(keys) + "\n})"

    @property
    def title(self) -> str:
        if self.is_reference():
            return get_valid_identifier(self.refname)
        else:
            return ""

    def get_python_type_representation(
        self,
        for_type_hints: bool = False,
        altair_classes_prefix: str | None = None,
        return_as_str: bool = True,
        additional_type_hints: list[str] | None = None,
    ) -> str | list[str]:
        # This is a list of all types which can be used for the current SchemaInfo.
        # This includes Altair classes, standard Python types, etc.
        type_representations: list[str] = []
        TP_CHECK_ONLY = {"Parameter", "SchemaBase"}
        """Most common annotations are include in `TYPE_CHECKING` block.
        They do not require `core.` prefix, and this saves many lines of code.

        Eventually a more robust solution would apply to more types from `core`.
        """

        if self.title:
            if for_type_hints:
                # To keep type hints simple, we only use the SchemaBase class
                # as the type hint for all classes which inherit from it.
                class_names = ["SchemaBase"]
                if self.title == "ExprRef":
                    # In these cases, a value parameter is also always accepted.
                    # It would be quite complex to further differentiate
                    # between a value and a selection parameter based on
                    # the type system (one could
                    # try to check for the type of the Parameter.param attribute
                    # but then we would need to write some overload signatures for
                    # api.param).
                    class_names.append("Parameter")
                if self.title == "ParameterExtent":
                    class_names.append("Parameter")

                prefix = (
                    "" if not altair_classes_prefix else altair_classes_prefix + "."
                )
                # If there is no prefix, it might be that the class is defined
                # in the same script and potentially after this line -> We use
                # deferred type annotations using quotation marks.
                if not prefix:
                    class_names = [f'"{n}"' for n in class_names]
                else:
                    class_names = (
                        n if n in TP_CHECK_ONLY else f"{prefix}{n}" for n in class_names
                    )
                    # class_names = [f"{prefix}{n}" for n in class_names]
                type_representations.extend(class_names)
            else:
                # use RST syntax for generated sphinx docs
                type_representations.append(rst_syntax_for_class(self.title))

        if self.is_empty():
            type_representations.append("Any")
        elif self.is_enum():
            s = ", ".join(f"{s!r}" for s in self.enum)
            tp_str = f"Literal[{s}]"
            if for_type_hints:
                tp_str = TypeAliasTracer.add_literal(self, tp_str, replace=True)
            type_representations.append(tp_str)
        elif self.is_anyOf():
            type_representations.extend(
                [
                    s.get_python_type_representation(
                        for_type_hints=for_type_hints,
                        altair_classes_prefix=altair_classes_prefix,
                        return_as_str=False,
                    )
                    for s in self.anyOf
                ]
            )
        elif isinstance(self.type, list):
            options = []
            subschema = SchemaInfo(dict(**self.schema))
            for typ_ in self.type:
                subschema.schema["type"] = typ_
                options.append(
                    subschema.get_python_type_representation(
                        # We always use title if possible for nested objects
                        for_type_hints=for_type_hints,
                        altair_classes_prefix=altair_classes_prefix,
                    )
                )
            type_representations.extend(options)
        elif self.is_object():
            type_representations.append("dict")
        elif self.is_array():
            # A list is invariant in its type parameter. This means that e.g.
            # List[str] is not a subtype of List[Union[core.FieldName, str]]
            # and hence we would need to explicitly write out the combinations,
            # so in this case:
            # List[core.FieldName], List[str], List[core.FieldName, str]
            # However, this can easily explode to too many combinations.
            # Furthermore, we would also need to add additional entries
            # for e.g. int wherever a float is accepted which would lead to very
            # long code.
            # As suggested in the mypy docs,
            # https://mypy.readthedocs.io/en/stable/common_issues.html#variance,
            # we revert to using Sequence which works as well for lists and also
            # includes tuples which are also supported by the SchemaBase.to_dict
            # method. However, it is not entirely accurate as some sequences
            # such as e.g. a range are not supported by SchemaBase.to_dict but
            # this tradeoff seems worth it.
            type_representations.append(
                "Sequence[{}]".format(
                    self.child(self.items).get_python_type_representation(
                        for_type_hints=for_type_hints,
                        altair_classes_prefix=altair_classes_prefix,
                    )
                )
            )
        elif self.type in jsonschema_to_python_types:
            type_representations.append(jsonschema_to_python_types[self.type])
        else:
            msg = "No Python type representation available for this schema"
            raise ValueError(msg)

        # Shorter types are usually the more relevant ones, e.g. `str` instead
        # of `SchemaBase`. Output order from set is non-deterministic -> If
        # types have same length names, order would be non-deterministic as it is
        # returned from sort. Hence, we sort as well by type name as a tie-breaker,
        # see https://docs.python.org/3.10/howto/sorting.html#sort-stability-and-complex-sorts
        # for more infos.
        type_representations = sorted(
            # Using lower as we don't want to prefer uppercase such as "None" over
            # "str"
            set(flatten(type_representations)),
            key=lambda x: x.lower(),
        )  # Secondary sort
        type_representations = sorted(
            type_representations,
            key=len,
        )  # Primary sort
        if additional_type_hints:
            type_representations.extend(additional_type_hints)

        if return_as_str:
            type_representations_str = ", ".join(type_representations)
            # If it's not for_type_hints but instead for the docstrings, we don't want
            # to include Union as it just clutters the docstrings.
            if len(type_representations) > 1 and for_type_hints:
                # Use parameterised `TypeAlias` instead of exposing `UndefinedType`
                # `Union` is collapsed by `ruff` later
                if type_representations_str.endswith(", UndefinedType"):
                    s = type_representations_str.replace(", UndefinedType", "")
                    s = f"Optional[Union[{s}]]"
                else:
                    s = f"Union[{type_representations_str}]"
                return s
            return type_representations_str
        else:
            return type_representations

    @property
    def properties(self) -> SchemaProperties:
        return SchemaProperties(
            self.schema.get("properties", {}), self.schema, self.rootschema
        )

    @property
    def definitions(self) -> SchemaProperties:
        return SchemaProperties(
            self.schema.get("definitions", {}), self.schema, self.rootschema
        )

    @property
    def required(self) -> list:
        return self.schema.get("required", [])

    @property
    def patternProperties(self) -> dict:
        return self.schema.get("patternProperties", {})

    @property
    def additionalProperties(self) -> bool:
        return self.schema.get("additionalProperties", True)

    @property
    def type(self) -> str | list[Any] | None:
        return self.schema.get("type", None)

    @property
    def anyOf(self) -> list[SchemaInfo]:
        return [self.child(s) for s in self.schema.get("anyOf", [])]

    @property
    def oneOf(self) -> list[SchemaInfo]:
        return [self.child(s) for s in self.schema.get("oneOf", [])]

    @property
    def allOf(self) -> list[SchemaInfo]:
        return [self.child(s) for s in self.schema.get("allOf", [])]

    @property
    def not_(self) -> SchemaInfo:
        return self.child(self.schema.get("not", {}))

    @property
    def items(self) -> dict:
        return self.schema.get("items", {})

    @property
    def enum(self) -> list:
        return self.schema.get("enum", [])

    @property
    def refname(self) -> str:
        return self.raw_schema.get("$ref", "#/").split("/")[-1]

    @property
    def ref(self) -> str | None:
        return self.raw_schema.get("$ref", None)

    @property
    def description(self) -> str:
        return self._get_description(include_sublevels=False)

    @property
    def deep_description(self) -> str:
        return self._get_description(include_sublevels=True)

    def _get_description(self, include_sublevels: bool = False) -> str:
        desc = self.raw_schema.get("description", self.schema.get("description", ""))
        if not desc and include_sublevels:
            for item in self.anyOf:
                sub_desc = item._get_description(include_sublevels=False)
                if desc and sub_desc:
                    raise ValueError(
                        "There are multiple potential descriptions which could"
                        + " be used for the currently inspected schema. You'll need to"
                        + " clarify which one is the correct one.\n"
                        + str(self.schema)
                    )
                if sub_desc:
                    desc = sub_desc
        return desc

    def is_reference(self) -> bool:
        return "$ref" in self.raw_schema

    def is_enum(self) -> bool:
        return "enum" in self.schema

    def is_empty(self) -> bool:
        return not (set(self.schema.keys()) - set(EXCLUDE_KEYS))

    def is_compound(self) -> bool:
        return any(key in self.schema for key in ["anyOf", "allOf", "oneOf"])

    def is_anyOf(self) -> bool:
        return "anyOf" in self.schema

    def is_allOf(self) -> bool:
        return "allOf" in self.schema

    def is_oneOf(self) -> bool:
        return "oneOf" in self.schema

    def is_not(self) -> bool:
        return "not" in self.schema

    def is_object(self) -> bool:
        if self.type == "object":
            return True
        elif self.type is not None:
            return False
        elif (
            self.properties
            or self.required
            or self.patternProperties
            or self.additionalProperties
        ):
            return True
        else:
            msg = "Unclear whether schema.is_object() is True"
            raise ValueError(msg)

    def is_value(self) -> bool:
        return not self.is_object()

    def is_array(self) -> bool:
        return self.type == "array"


def indent_docstring(
    lines: list[str], indent_level: int, width: int = 100, lstrip=True
) -> str:
    """Indent a docstring for use in generated code"""
    final_lines = []

    for i, line in enumerate(lines):
        stripped = line.lstrip()
        if stripped:
            leading_space = len(line) - len(stripped)
            indent = indent_level + leading_space
            wrapper = textwrap.TextWrapper(
                width=width - indent,
                initial_indent=indent * " ",
                subsequent_indent=indent * " ",
                break_long_words=False,
                break_on_hyphens=False,
                drop_whitespace=True,
            )
            list_wrapper = textwrap.TextWrapper(
                width=width - indent,
                initial_indent=indent * " " + "* ",
                subsequent_indent=indent * " " + "  ",
                break_long_words=False,
                break_on_hyphens=False,
                drop_whitespace=True,
            )
            for line in stripped.split("\n"):
                line_stripped = line.lstrip()
                line_stripped = fix_docstring_issues(line_stripped)
                if line_stripped == "":
                    final_lines.append("")
                elif line_stripped.startswith("* "):
                    final_lines.extend(list_wrapper.wrap(line_stripped[2:]))
                # Matches lines where an attribute is mentioned followed by the accepted
                # types (lines starting with a character sequence that
                # does not contain white spaces or '*' followed by ' : ').
                # It therefore matches 'condition : anyOf(...' but not '**Notes** : ...'
                # These lines should not be wrapped at all but appear on one line
                elif re.match(r"[^\s*]+ : ", line_stripped):
                    final_lines.append(indent * " " + line_stripped)
                else:
                    final_lines.extend(wrapper.wrap(line_stripped))

        # If this is the last line, put in an indent
        elif i + 1 == len(lines):
            final_lines.append(indent_level * " ")
        # If it's not the last line, this is a blank line that should not indent.
        else:
            final_lines.append("")
    # Remove any trailing whitespaces on the right side
    stripped_lines = []
    for i, line in enumerate(final_lines):
        if i + 1 == len(final_lines):
            stripped_lines.append(line)
        else:
            stripped_lines.append(line.rstrip())
    # Join it all together
    wrapped = "\n".join(stripped_lines)
    if lstrip:
        wrapped = wrapped.lstrip()
    return wrapped


def fix_docstring_issues(docstring: str) -> str:
    # All lists should start with '*' followed by a whitespace. Fixes the ones
    # which either do not have a whitespace or/and start with '-' by first replacing
    # "-" with "*" and then adding a whitespace where necessary
    docstring = re.sub(
        r"^-(?=[ `\"a-z])",
        "*",
        docstring,
        flags=re.MULTILINE,
    )
    # Now add a whitespace where an asterisk is followed by one of the characters
    # in the square brackets of the regex pattern
    docstring = re.sub(
        r"^\*(?=[`\"a-z])",
        "* ",
        docstring,
        flags=re.MULTILINE,
    )

    # Links to the vega-lite documentation cannot be relative but instead need to
    # contain the full URL.
    docstring = docstring.replace(
        "types#datetime", "https://vega.github.io/vega-lite/docs/datetime.html"
    )
    return docstring


def rst_syntax_for_class(class_name: str) -> str:
    return f":class:`{class_name}`"


def flatten(container: Iterable) -> Iterable:
    """Flatten arbitrarily flattened list

    From https://stackoverflow.com/a/10824420
    """
    for i in container:
        if isinstance(i, (list, tuple)):
            yield from flatten(i)
        else:
            yield i


def ruff_format_str(code: str | list[str]) -> str:
    if isinstance(code, list):
        code = "\n".join(code)

    r = subprocess.run(
        # Name of the file does not seem to matter but ruff requires one
        ["ruff", "format", "--stdin-filename", "placeholder.py"],
        input=code.encode(),
        check=True,
        capture_output=True,
    )
    return r.stdout.decode()


def ruff_format_py(fp: Path, /, *extra_args: str) -> None:
    """Format an existing file.

    Running on `win32` after writing lines will ensure "lf" is used before:
    ```bash
    ruff format --diff --check .
    ```
    """

    cmd = ["ruff", "format", fp]
    if extra_args:
        cmd.extend(extra_args)
    r = subprocess.run(cmd, check=True)
    r.check_returncode()


def ruff_write_lint_format_str(
    fp: Path, code: str | Iterable[str], /, *, encoding: str = "utf-8"
) -> None:
    """Combined steps of writing, `ruff check`, `ruff format`.

    Notes
    -----
    - `fp` is written to first, as the size before formatting will be the smallest
        - Better utilizes `ruff` performance, rather than `python` str and io
    - `code` is no longer bound to `list`
    - Encoding set as default
    - `I001/2` are `isort` rules, to sort imports.
    """
    commands = (
        ["ruff", "check", fp, "--fix"],
        ["ruff", "check", fp, "--fix", "--select", "I001", "--select", "I002"],
    )
    if not isinstance(code, str):
        code = "\n".join(code)
    fp.write_text(code, encoding=encoding)
    for cmd in commands:
        r = subprocess.run(cmd, check=True)
        r.check_returncode()
    ruff_format_py(fp)
