from __future__ import annotations
import importlib
from pathlib import Path
import re
import sys
from typing import Any, Iterator, Sequence
import warnings

from docutils import nodes, utils, frontend
from docutils.parsers.rst import Directive
from docutils.parsers.rst.directives import flag
from myst_parser.docutils_ import Parser
from sphinx import addnodes

sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from tools.schemapi.utils import fix_docstring_issues, SchemaInfo


def type_description(schema: dict[str, Any]) -> str:
    """Return a concise type description for the given schema"""
    if not schema or not isinstance(schema, dict) or schema.keys() == {"description"}:
        return "any"
    elif "$ref" in schema:
        return ":class:`{}`".format(schema["$ref"].split("/")[-1])
    elif "enum" in schema:
        return "[{}]".format(", ".join(repr(s) for s in schema["enum"]))
    elif "type" in schema:
        if isinstance(schema["type"], list):
            return "[{}]".format(", ".join(schema["type"]))
        elif schema["type"] == "array":
            return "array({})".format(type_description(schema.get("items", {})))
        elif schema["type"] == "object":
            return "dict"
        else:
            return "`{}`".format(schema["type"])
    elif "anyOf" in schema:
        return "anyOf({})".format(
            ", ".join(type_description(s) for s in schema["anyOf"])
        )
    else:
        warnings.warn(
            f"cannot infer type for schema with keys {schema.keys()}" "",
            stacklevel=1,
        )
        return "--"


def prepare_table_header(
    titles: Sequence[str], widths: Sequence[float]
) -> tuple[nodes.table, nodes.tbody]:
    """Build docutil empty table"""
    ncols = len(titles)
    assert len(widths) == ncols

    tgroup = nodes.tgroup(cols=ncols)
    for width in widths:
        tgroup += nodes.colspec(colwidth=width)
    header = nodes.row()
    for title in titles:
        header += nodes.entry("", nodes.paragraph(text=title))
    tgroup += nodes.thead("", header)

    tbody = nodes.tbody()
    tgroup += tbody

    return nodes.table("", tgroup), tbody


reClassDef = re.compile(r":class:`([^`]+)`")
reCode = re.compile(r"`([^`]+)`")


def add_class_def(node: nodes.paragraph, classDef: str) -> nodes.paragraph:
    """Add reference on classDef to node"""

    ref = addnodes.pending_xref(
        reftarget=classDef,
        reftype="class",
        refdomain="py",  # py:class="None" py:module="altair" refdoc="user_guide/marks"
        refexplicit=False,
        # refdoc="",
        refwarn=False,
    )
    ref["py:class"] = "None"
    ref["py:module"] = "altair"

    ref += nodes.literal(text=classDef, classes=["xref", "py", "py-class"])
    node += ref
    return node


def add_text(node: nodes.paragraph, text: str) -> nodes.paragraph:
    """Add text with inline code to node"""
    is_text = True
    for part in reCode.split(text):
        if part:
            if is_text:
                node += nodes.Text(part, part)
            else:
                node += nodes.literal(part, part)

        is_text = not is_text

    return node


def build_row(
    item: tuple[str, dict[str, Any]], rootschema: dict[str, Any] | None
) -> nodes.row:
    """Return nodes.row with property description"""

    prop, propschema, _ = item
    row = nodes.row()

    # Property

    row += nodes.entry("", nodes.paragraph(text=prop), classes=["vl-prop"])

    # Type
    str_type = type_description(propschema)
    par_type = nodes.paragraph()

    is_text = True
    for part in reClassDef.split(str_type):
        if part:
            if is_text:
                add_text(par_type, part)
            else:
                add_class_def(par_type, part)
        is_text = not is_text

    # row += nodes.entry('')
    row += nodes.entry("", par_type, classes=["vl-type-def"])

    # Description
    md_parser = Parser()
    # str_descr = "***Required.*** " if required else ""
    description = SchemaInfo(propschema, rootschema).deep_description
    description = description or " "
    str_descr = ""
    str_descr += description
    str_descr = fix_docstring_issues(str_descr)
    document_settings = frontend.get_default_settings()
    document_settings.setdefault("raw_enabled", True)
    doc_descr = utils.new_document("schema_description", document_settings)
    md_parser.parse(str_descr, doc_descr)

    # row += nodes.entry('', *doc_descr.children, classes="vl-decsr")
    row += nodes.entry("", *doc_descr.children, classes=["vl-decsr"])

    return row


def build_schema_table(
    items: Iterator[tuple[str, dict[str, Any]]], rootschema: dict[str, Any] | None
) -> nodes.table:
    """Return schema table of items (iterator of prop, schema.item, required)"""
    table, tbody = prepare_table_header(
        ["Property", "Type", "Description"], [10, 20, 50]
    )
    for item in items:
        tbody += build_row(item, rootschema)

    return table


def select_items_from_schema(
    schema: dict[str, Any], props: list[str] | None = None
) -> nodes.Generator[tuple[Any, Any, bool] | tuple[str, Any, bool], Any, None]:
    """Return iterator  (prop, schema.item, required) on prop, return all in None"""
    properties = schema.get("properties", {})
    required = schema.get("required", [])
    if not props:
        for prop, item in properties.items():
            yield prop, item, prop in required
    else:
        for prop in props:
            try:
                yield prop, properties[prop], prop in required
            except KeyError as err:
                msg = f"Can't find property: {prop}"
                raise Exception(msg) from err


def prepare_schema_table(
    schema: dict[str, Any],
    rootschema: dict[str, Any] | None,
    props: list[str] | None = None,
) -> nodes.table:
    items = select_items_from_schema(schema, props)
    return build_schema_table(items, rootschema)


def validate_properties(properties: str) -> list[str]:
    return properties.strip().split()


class AltairObjectTableDirective(Directive):
    """
    Directive for building a table of attribute descriptions.

    Usage:

    .. altair-object-table:: altair.MarkConfig

    """

    has_content = False
    required_arguments = 1

    option_spec = {"properties": validate_properties, "dont-collapse-table": flag}

    def run(self) -> list:
        objectname = self.arguments[0]
        modname, classname = objectname.rsplit(".", 1)
        module = importlib.import_module(modname)
        cls: type[Any] = getattr(module, classname)
        schema = cls.resolve_references(cls._schema)

        properties = self.options.get("properties", None)
        dont_collapse_table = "dont-collapse-table" in self.options

        result = []
        if not dont_collapse_table:
            html = "<details><summary><a>Click to show table</a></summary>"
            raw_html = nodes.raw("", html, format="html")
            result += [raw_html]
        # create the table from the object
        result.append(prepare_schema_table(schema, cls._rootschema, props=properties))

        if not dont_collapse_table:
            html = "</details>"
            raw_html = nodes.raw("", html, format="html")
            result += [raw_html]

        return result


def setup(app) -> None:
    app.add_directive("altair-object-table", AltairObjectTableDirective)
