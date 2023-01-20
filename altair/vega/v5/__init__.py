# flake8: noqa
import warnings
from ...utils.deprecation import AltairFutureWarning
from .display import vega, Vega, renderers
from .schema import *

from .data import (
    pipe,
    curry,
    limit_rows,
    sample,
    to_json,
    to_csv,
    to_values,
    default_data_transformer,
)

warnings.warn(
    "This module is deprecated and will be removed in Altair 5. "
    "Use `import altair as alt` instead of `import altair.vega.v5 as alt`.",
    AltairFutureWarning,
)
