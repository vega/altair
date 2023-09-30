"""Utilities for working with schemas"""

import keyword
import re
import textwrap
import urllib
from typing import Final, Optional, List, Dict, Any, Iterable

from .schemapi import _resolve_references as resolve_references


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
        properties: Dict[str, Any],
        schema: dict,
        rootschema: Optional[dict] = None,
    ) -> None:
        self._properties = properties
        self._schema = schema
        self._rootschema = rootschema or schema

    def __bool__(self) -> bool:
        return bool(self._properties)

    def __dir__(self) -> List[str]:
        return list(self._properties.keys())

    def __getattr__(self, attr):
        try:
            return self[attr]
        except KeyError:
            return super(SchemaProperties, self).__getattr__(attr)

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
        self, schema: Dict[str, Any], rootschema: Optional[Dict[str, Any]] = None
    ) -> None:
        if not rootschema:
            rootschema = schema
        self.raw_schema = schema
        self.rootschema = rootschema
        self.schema = resolve_references(schema, rootschema)

    def child(self, schema: dict) -> "SchemaInfo":
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
            keys.append('"{}": {}'.format(key, rval))
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
        altair_classes_prefix: Optional[str] = None,
    ) -> str:
        # This is a list of all types which can be used for the current SchemaInfo.
        # This includes Altair classes, standard Python types, etc.
        type_representations: List[str] = []
        if self.title:
            # Add the name of the current Altair class
            if for_type_hints:
                class_names = [self.title]
                if self.title == "ExprRef":
                    # In these cases, a value parameter is also always accepted.
                    # We use the _ParameterProtocol to indicate this although this
                    # protocol would also pass for selection parameters but
                    # due to how the Parameter class is defined, it would be quite
                    # complex to further differentiate between a value and
                    # a selection parameter based on the type system (one could
                    # try to check for the type of the Parameter.param attribute
                    # but then we would need to write some overload signatures for
                    # api.param).
                    class_names.append("_ParameterProtocol")

                prefix = (
                    "" if not altair_classes_prefix else altair_classes_prefix + "."
                )
                # If there is no prefix, it might be that the class is defined
                # in the same script and potentially after this line -> We use
                # deferred type annotations using quotation marks.
                if not prefix:
                    class_names = [f'"{n}"' for n in class_names]
                else:
                    class_names = [f"{prefix}{n}" for n in class_names]
                type_representations.extend(class_names)
            else:
                # use RST syntax for generated sphinx docs
                type_representations.append(":class:`{}`".format(self.title))

        if self.is_empty():
            type_representations.append("Any")
        elif self.is_enum():
            type_representations.append(
                "Literal[{}]".format(", ".join(map(repr, self.enum)))
            )
        elif self.is_anyOf():
            type_representations.extend(
                [
                    s.get_python_type_representation(
                        for_type_hints=for_type_hints,
                        altair_classes_prefix=altair_classes_prefix,
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
            if for_type_hints:
                type_representations.append("dict")
            else:
                type_representations.append(
                    "Dict[required=[{}]]".format(", ".join(self.required))
                )
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
            raise ValueError("No Python type representation available for this schema")

        type_representations = sorted(set(flatten(type_representations)))
        type_representations_str = ", ".join(type_representations)
        if len(type_representations) > 1:
            type_representations_str = f"Union[{type_representations_str}]"
        return type_representations_str

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
    def type(self) -> Optional[str]:
        return self.schema.get("type", None)

    @property
    def anyOf(self) -> List["SchemaInfo"]:
        return [self.child(s) for s in self.schema.get("anyOf", [])]

    @property
    def oneOf(self) -> List["SchemaInfo"]:
        return [self.child(s) for s in self.schema.get("oneOf", [])]

    @property
    def allOf(self) -> List["SchemaInfo"]:
        return [self.child(s) for s in self.schema.get("allOf", [])]

    @property
    def not_(self) -> "SchemaInfo":
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
    def ref(self) -> Optional[str]:
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
            raise ValueError("Unclear whether schema.is_object() is True")

    def is_value(self) -> bool:
        return not self.is_object()

    def is_array(self) -> bool:
        return self.type == "array"


def indent_docstring(
    lines: List[str], indent_level: int, width: int = 100, lstrip=True
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


def flatten(container: Iterable) -> Iterable:
    """Flatten arbitrarily flattened list

    From https://stackoverflow.com/a/10824420
    """
    for i in container:
        if isinstance(i, (list, tuple)):
            for j in flatten(i):
                yield j
        else:
            yield i
