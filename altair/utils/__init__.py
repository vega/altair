from .core import (
    infer_vegalite_type_for_pandas,
    infer_encoding_types,
    sanitize_pandas_dataframe,
    sanitize_narwhals_dataframe,
    parse_shorthand,
    use_signature,
    update_nested,
    display_traceback,
    SchemaBase,
    SHORTHAND_KEYS,
)
from .html import spec_to_html
from .plugin_registry import PluginRegistry
from .deprecation import AltairDeprecationWarning, deprecated, deprecated_warn
from .schemapi import Undefined, Optional, is_undefined


__all__ = (
    "SHORTHAND_KEYS",
    "AltairDeprecationWarning",
    "Optional",
    "PluginRegistry",
    "SchemaBase",
    "Undefined",
    "deprecated",
    "deprecated_warn",
    "display_traceback",
    "infer_encoding_types",
    "infer_vegalite_type_for_pandas",
    "is_undefined",
    "parse_shorthand",
    "sanitize_narwhals_dataframe",
    "sanitize_pandas_dataframe",
    "spec_to_html",
    "update_nested",
    "use_signature",
)
