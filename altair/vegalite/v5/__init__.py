# flake8: noqa
from .schema import *
from .api import *

from ...datasets import list_datasets, load_dataset

from ... import expr
from ...expr import datum

from .display import VegaLite, renderers

from .data import (
    MaxRowsError,
    pipe,
    curry,
    limit_rows,
    sample,
    to_json,
    to_csv,
    to_values,
    default_data_transformer,
    data_transformers,
)

class _ExprType():
    def __init__(self, expr):
         vars(self).update(expr.__dict__)

    def __call__(self, expr, **kwargs):
        return ExprRef(expr, **kwargs)


expr = _ExprType(expr)
