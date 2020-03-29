"""Generate a schema wrapper from a schema"""
import argparse
import copy
import os
import sys
import json
import re
from os.path import abspath, join, dirname

import textwrap
from urllib import request

import m2r

# import schemapi from here
sys.path.insert(0, abspath(dirname(__file__)))
from schemapi import codegen  # noqa: E402
from schemapi.codegen import CodeSnippet  # noqa: E402
from schemapi.utils import (
    get_valid_identifier,
    SchemaInfo,
    indent_arglist,
    resolve_references,
)  # noqa: E402
import generate_api_docs  # noqa: E402

# Map of version name to github branch name.
SCHEMA_VERSION = {
    "vega": {"v5": "v5.10.0"},
    "vega-lite": {"v3": "v3.4.0", "v4": "v4.8.1"},
}

reLink = re.compile(r"(?<=\[)([^\]]+)(?=\]\([^\)]+\))", re.M)
reSpecial = re.compile(r"[*_]{2,3}|`", re.M)


class SchemaGenerator(codegen.SchemaGenerator):
    schema_class_template = textwrap.dedent(
        '''
    class {classname}({basename}):
        """{docstring}"""
        _schema = {schema!r}

        {init_code}
    '''
    )

    def _process_description(self, description):
        description = "".join(
            [
                reSpecial.sub("", d) if i % 2 else d
                for i, d in enumerate(reLink.split(description))
            ]
        )  # remove formatting from links
        description = m2r.convert(description)
        description = description.replace(m2r.prolog, "")
        description = description.replace(":raw-html-m2r:", ":raw-html:")
        description = description.replace(r"\ ,", ",")
        description = description.replace(r"\ ", " ")
        # turn explicit references into anonymous references
        description = description.replace(">`_", ">`__")
        description += "\n"
        return description.strip()


def schema_class(*args, **kwargs):
    return SchemaGenerator(*args, **kwargs).schema_class()


SCHEMA_URL_TEMPLATE = "https://vega.github.io/schema/" "{library}/{version}.json"

BASE_SCHEMA = """
class {basename}(SchemaBase):
    _rootschema = load_schema()
    @classmethod
    def _default_wrapper_classes(cls):
        return _subclasses({basename})
"""

LOAD_SCHEMA = '''
import pkgutil
import json

def load_schema():
    """Load the json schema associated with this module's functions"""
    return json.loads(pkgutil.get_data(__name__, '{schemafile}').decode('utf-8'))
'''


CHANNEL_MIXINS = """
class FieldChannelMixin(object):
    def to_dict(self, validate=True, ignore=(), context=None):
        context = context or {}
        shorthand = self._get('shorthand')
        field = self._get('field')

        if shorthand is not Undefined and field is not Undefined:
            raise ValueError("{} specifies both shorthand={} and field={}. "
                             "".format(self.__class__.__name__, shorthand, field))

        if isinstance(shorthand, (tuple, list)):
            # If given a list of shorthands, then transform it to a list of classes
            kwds = self._kwds.copy()
            kwds.pop('shorthand')
            return [self.__class__(sh, **kwds).to_dict(validate=validate, ignore=ignore, context=context)
                    for sh in shorthand]

        if shorthand is Undefined:
            parsed = {}
        elif isinstance(shorthand, str):
            parsed = parse_shorthand(shorthand, data=context.get('data', None))
            type_required = 'type' in self._kwds
            type_in_shorthand = 'type' in parsed
            type_defined_explicitly = self._get('type') is not Undefined
            if not type_required:
                # Secondary field names don't require a type argument in VegaLite 3+.
                # We still parse it out of the shorthand, but drop it here.
                parsed.pop('type', None)
            elif not (type_in_shorthand or type_defined_explicitly):
                if isinstance(context.get('data', None), pd.DataFrame):
                    raise ValueError("{} encoding field is specified without a type; "
                                     "the type cannot be inferred because it does not "
                                     "match any column in the data.".format(shorthand))
                else:
                    raise ValueError("{} encoding field is specified without a type; "
                                     "the type cannot be automatically inferred because "
                                     "the data is not specified as a pandas.DataFrame."
                                     "".format(shorthand))
        else:
            # Shorthand is not a string; we pass the definition to field,
            # and do not do any parsing.
            parsed = {'field': shorthand}

        # Set shorthand to Undefined, because it's not part of the base schema.
        self.shorthand = Undefined
        self._kwds.update({k: v for k, v in parsed.items()
                           if self._get(k) is Undefined})
        return super(FieldChannelMixin, self).to_dict(
            validate=validate,
            ignore=ignore,
            context=context
        )


class ValueChannelMixin(object):
    def to_dict(self, validate=True, ignore=(), context=None):
        context = context or {}
        condition = getattr(self, 'condition', Undefined)
        copy = self  # don't copy unless we need to
        if condition is not Undefined:
            if isinstance(condition, core.SchemaBase):
                pass
            elif 'field' in condition and 'type' not in condition:
                kwds = parse_shorthand(condition['field'], context.get('data', None))
                copy = self.copy(deep=['condition'])
                copy.condition.update(kwds)
        return super(ValueChannelMixin, copy).to_dict(validate=validate,
                                                      ignore=ignore,
                                                      context=context)
"""


class FieldSchemaGenerator(SchemaGenerator):
    schema_class_template = textwrap.dedent(
        '''
    class {classname}(FieldChannelMixin, core.{basename}):
        """{docstring}"""
        _class_is_valid_at_instantiation = False
        _encoding_name = "{encodingname}"

        {init_code}
    '''
    )


class ValueSchemaGenerator(SchemaGenerator):
    schema_class_template = textwrap.dedent(
        '''
    class {classname}(ValueChannelMixin, core.{basename}):
        """{docstring}"""
        _class_is_valid_at_instantiation = False
        _encoding_name = "{encodingname}"

        {init_code}
    '''
    )


HEADER = """\
# The contents of this file are automatically written by
# tools/generate_schema_wrapper.py. Do not modify directly.
"""


def schema_url(library, version):
    version = SCHEMA_VERSION[library][version]
    return SCHEMA_URL_TEMPLATE.format(library=library, version=version)


def download_schemafile(library, version, schemapath, skip_download=False):
    url = schema_url(library, version)
    if not os.path.exists(schemapath):
        os.makedirs(schemapath)
    filename = os.path.join(schemapath, "{library}-schema.json".format(library=library))
    if not skip_download:
        request.urlretrieve(url, filename)
    elif not os.path.exists(filename):
        raise ValueError("Cannot skip download: {} does not exist".format(filename))
    return filename


def copy_schemapi_util():
    """
    Copy the schemapi utility and its test file into altair/utils/
    """
    # copy the schemapi utility file
    source_path = abspath(join(dirname(__file__), "schemapi", "schemapi.py"))
    destination_path = abspath(
        join(dirname(__file__), "..", "altair", "utils", "schemapi.py")
    )

    print("Copying\n {}\n  -> {}".format(source_path, destination_path))
    with open(source_path, "r", encoding="utf8") as source:
        with open(destination_path, "w", encoding="utf8") as dest:
            dest.write(HEADER)
            dest.writelines(source.readlines())

    # Copy the schemapi test file
    source_path = abspath(
        join(dirname(__file__), "schemapi", "tests", "test_schemapi.py")
    )
    destination_path = abspath(
        join(dirname(__file__), "..", "altair", "utils", "tests", "test_schemapi.py")
    )

    print("Copying\n {}\n  -> {}".format(source_path, destination_path))
    with open(source_path, "r", encoding="utf8") as source:
        with open(destination_path, "w", encoding="utf8") as dest:
            dest.write(HEADER)
            dest.writelines(source.readlines())


def toposort(graph):
    """Topological sort of a directed acyclic graph.

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
    stack = []
    visited = {}

    def visit(nodes):
        for node in sorted(nodes, reverse=True):
            if not visited.get(node):
                visited[node] = True
                visit(graph.get(node, []))
                stack.insert(0, node)

    visit(graph)
    return stack


def generate_vegalite_schema_wrapper(schema_file):
    """Generate a schema wrapper at the given path."""
    # TODO: generate simple tests for each wrapper
    basename = "VegaLiteSchema"

    with open(schema_file, encoding="utf8") as f:
        rootschema = json.load(f)

    definitions = {}

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
            rootschemarepr=CodeSnippet("{}._rootschema".format(basename)),
        )

    graph = {}

    for name, schema in definitions.items():
        graph[name] = []
        for child in schema.subclasses():
            child = get_valid_identifier(child)
            graph[name].append(child)
            child = definitions[child]
            if child.basename == basename:
                child.basename = [name]
            else:
                child.basename.append(name)

    contents = [
        HEADER,
        "from altair.utils.schemapi import SchemaBase, Undefined, _subclasses",
        LOAD_SCHEMA.format(schemafile="vega-lite-schema.json"),
    ]
    contents.append(BASE_SCHEMA.format(basename=basename))
    contents.append(
        schema_class(
            "Root",
            schema=rootschema,
            basename=basename,
            schemarepr=CodeSnippet("{}._rootschema".format(basename)),
        )
    )

    for name in toposort(graph):
        contents.append(definitions[name].schema_class())

    contents.append("")  # end with newline
    return "\n".join(contents)


def generate_vega_schema_wrapper(schema_file):
    """Generate a schema wrapper at the given path."""
    # TODO: generate simple tests for each wrapper
    basename = "VegaSchema"

    with open(schema_file, encoding="utf8") as f:
        rootschema = json.load(f)
    contents = [
        HEADER,
        "from altair.utils.schemapi import SchemaBase, Undefined, _subclasses",
        LOAD_SCHEMA.format(schemafile="vega-schema.json"),
    ]
    contents.append(BASE_SCHEMA.format(basename=basename))
    contents.append(
        schema_class(
            "Root",
            schema=rootschema,
            basename=basename,
            schemarepr=CodeSnippet("{}._rootschema".format(basename)),
        )
    )
    for deflist in ["defs", "refs"]:
        for name in rootschema[deflist]:
            defschema = {"$ref": "#/{}/{}".format(deflist, name)}
            defschema_repr = {"$ref": "#/{}/{}".format(deflist, name)}
            contents.append(
                schema_class(
                    get_valid_identifier(name),
                    schema=defschema,
                    schemarepr=defschema_repr,
                    rootschema=rootschema,
                    basename=basename,
                    rootschemarepr=CodeSnippet("Root._schema"),
                )
            )
    contents.append("")  # end with newline
    return "\n".join(contents)


def generate_vegalite_channel_wrappers(schemafile, version, imports=None):
    # TODO: generate __all__ for top of file
    with open(schemafile, encoding="utf8") as f:
        schema = json.load(f)
    if imports is None:
        imports = [
            "from . import core",
            "import pandas as pd",
            "from altair.utils.schemapi import Undefined",
            "from altair.utils import parse_shorthand",
        ]
    contents = [HEADER]
    contents.extend(imports)
    contents.append("")

    contents.append(CHANNEL_MIXINS)

    if version == "v2":
        encoding_def = "EncodingWithFacet"
    else:
        encoding_def = "FacetedEncoding"

    encoding = SchemaInfo(schema["definitions"][encoding_def], rootschema=schema)

    for prop, propschema in encoding.properties.items():
        if propschema.is_reference():
            definitions = [propschema.ref]
        elif propschema.is_anyOf():
            definitions = [s.ref for s in propschema.anyOf if s.is_reference()]
        else:
            raise ValueError("either $ref or anyOf expected")
        for definition in definitions:
            defschema = {"$ref": definition}
            basename = definition.split("/")[-1]
            classname = prop[0].upper() + prop[1:]

            if "Value" in basename:
                Generator = ValueSchemaGenerator
                classname += "Value"
                nodefault = ["value"]
            else:
                Generator = FieldSchemaGenerator
                nodefault = []
                defschema = copy.deepcopy(resolve_references(defschema, schema))

                # For Encoding field definitions, we patch the schema by adding the
                # shorthand property.
                defschema["properties"]["shorthand"] = {
                    "type": "string",
                    "description": "shorthand for field, aggregate, and type",
                }
                defschema["required"] = ["shorthand"]

            gen = Generator(
                classname=classname,
                basename=basename,
                schema=defschema,
                rootschema=schema,
                encodingname=prop,
                nodefault=nodefault,
            )
            contents.append(gen.schema_class())
    return "\n".join(contents)


MARK_METHOD = '''
def mark_{mark}({def_arglist}):
    """Set the chart's mark to '{mark}'

    For information on additional arguments, see :class:`{mark_def}`
    """
    kwds = dict({dict_arglist})
    copy = self.copy(deep=False)
    if any(val is not Undefined for val in kwds.values()):
        copy.mark = core.{mark_def}(type="{mark}", **kwds)
    else:
        copy.mark = "{mark}"
    return copy
'''


def generate_vegalite_mark_mixin(schemafile, markdefs):
    with open(schemafile, encoding="utf8") as f:
        schema = json.load(f)

    imports = ["from altair.utils.schemapi import Undefined", "from . import core"]

    code = [
        "class MarkMethodMixin(object):",
        '    """A mixin class that defines mark methods"""',
    ]

    for mark_enum, mark_def in markdefs.items():
        marks = schema["definitions"][mark_enum]["enum"]
        info = SchemaInfo({"$ref": "#/definitions/" + mark_def}, rootschema=schema)

        # adapted from SchemaInfo.init_code
        nonkeyword, required, kwds, invalid_kwds, additional = codegen._get_args(info)
        required -= {"type"}
        kwds -= {"type"}

        def_args = ["self"] + [
            "{}=Undefined".format(p) for p in (sorted(required) + sorted(kwds))
        ]
        dict_args = ["{0}={0}".format(p) for p in (sorted(required) + sorted(kwds))]

        if additional or invalid_kwds:
            def_args.append("**kwds")
            dict_args.append("**kwds")

        for mark in marks:
            # TODO: only include args relevant to given type?
            mark_method = MARK_METHOD.format(
                mark=mark,
                mark_def=mark_def,
                def_arglist=indent_arglist(def_args, indent_level=10 + len(mark)),
                dict_arglist=indent_arglist(dict_args, indent_level=16),
            )
            code.append("\n    ".join(mark_method.splitlines()))

    return imports, "\n".join(code)


CONFIG_METHOD = """
@use_signature(core.{classname})
def {method}(self, *args, **kwargs):
    copy = self.copy(deep=False)
    copy.config = core.{classname}(*args, **kwargs)
    return copy
"""

CONFIG_PROP_METHOD = """
@use_signature(core.{classname})
def configure_{prop}(self, *args, **kwargs):
    copy = self.copy(deep=['config'])
    if copy.config is Undefined:
        copy.config = core.Config()
    copy.config["{prop}"] = core.{classname}(*args, **kwargs)
    return copy
"""


def generate_vegalite_config_mixin(schemafile):
    imports = ["from . import core", "from altair.utils import use_signature"]
    code = [
        "class ConfigMethodMixin(object):",
        '    """A mixin class that defines config methods"""',
    ]
    with open(schemafile, encoding="utf8") as f:
        schema = json.load(f)
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
    return imports, "\n".join(code)


def vegalite_main(skip_download=False):
    library = "vega-lite"

    for version in SCHEMA_VERSION[library]:
        path = abspath(join(dirname(__file__), "..", "altair", "vegalite", version))
        schemapath = os.path.join(path, "schema")
        schemafile = download_schemafile(
            library=library,
            version=version,
            schemapath=schemapath,
            skip_download=skip_download,
        )

        # Generate __init__.py file
        outfile = join(schemapath, "__init__.py")
        print("Writing {}".format(outfile))
        with open(outfile, "w", encoding="utf8") as f:
            f.write("# flake8: noqa\n")
            f.write("from .core import *\nfrom .channels import *\n")
            f.write(
                "SCHEMA_VERSION = {!r}\n" "".format(SCHEMA_VERSION[library][version])
            )
            f.write("SCHEMA_URL = {!r}\n" "".format(schema_url(library, version)))

        # Generate the core schema wrappers
        outfile = join(schemapath, "core.py")
        print("Generating\n {}\n  ->{}".format(schemafile, outfile))
        file_contents = generate_vegalite_schema_wrapper(schemafile)
        with open(outfile, "w", encoding="utf8") as f:
            f.write(file_contents)

        # Generate the channel wrappers
        outfile = join(schemapath, "channels.py")
        print("Generating\n {}\n  ->{}".format(schemafile, outfile))
        code = generate_vegalite_channel_wrappers(schemafile, version=version)
        with open(outfile, "w", encoding="utf8") as f:
            f.write(code)

        # generate the mark mixin
        if version == "v2":
            markdefs = {"Mark": "MarkDef"}
        else:
            markdefs = {
                k: k + "Def" for k in ["Mark", "BoxPlot", "ErrorBar", "ErrorBand"]
            }
        outfile = join(schemapath, "mixins.py")
        print("Generating\n {}\n  ->{}".format(schemafile, outfile))
        mark_imports, mark_mixin = generate_vegalite_mark_mixin(schemafile, markdefs)
        config_imports, config_mixin = generate_vegalite_config_mixin(schemafile)
        imports = sorted(set(mark_imports + config_imports))
        with open(outfile, "w", encoding="utf8") as f:
            f.write(HEADER)
            f.write("\n".join(imports))
            f.write("\n\n\n")
            f.write(mark_mixin)
            f.write("\n\n\n")
            f.write(config_mixin)


def vega_main(skip_download=False):
    library = "vega"

    for version in SCHEMA_VERSION[library]:
        path = abspath(join(dirname(__file__), "..", "altair", "vega", version))
        schemapath = os.path.join(path, "schema")
        schemafile = download_schemafile(
            library=library,
            version=version,
            schemapath=schemapath,
            skip_download=skip_download,
        )

        # Generate __init__.py file
        outfile = join(schemapath, "__init__.py")
        print("Writing {}".format(outfile))
        with open(outfile, "w", encoding="utf8") as f:
            f.write("# flake8: noqa\n")
            f.write("from .core import *\n\n")
            f.write(
                "SCHEMA_VERSION = {!r}\n" "".format(SCHEMA_VERSION[library][version])
            )
            f.write("SCHEMA_URL = {!r}\n" "".format(schema_url(library, version)))

        # Generate the core schema wrappers
        outfile = join(schemapath, "core.py")
        print("Generating\n {}\n  ->{}".format(schemafile, outfile))
        file_contents = generate_vega_schema_wrapper(schemafile)
        with open(outfile, "w", encoding="utf8") as f:
            f.write(file_contents)


def main():
    parser = argparse.ArgumentParser(
        prog="generate_schema_wrapper.py", description="Generate the Altair package."
    )
    parser.add_argument(
        "--skip-download", action="store_true", help="skip downloading schema files"
    )
    args = parser.parse_args()
    copy_schemapi_util()
    vegalite_main(args.skip_download)
    vega_main(args.skip_download)

    generate_api_docs.write_api_file()


if __name__ == "__main__":
    main()
