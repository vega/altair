from ..utils.core import sanitize_dataframe
from ..utils.data import (
    MaxRowsError,
    curry,
    limit_rows,
    pipe,
    sample,
    to_csv,
    to_json,
    to_values,
    check_data_type,
)
from ..utils.data import DataTransformerRegistry as _DataTransformerRegistry
from ..utils.data import DataType, ToValuesReturnType
from ..utils.plugin_registry import PluginEnabler
from typing import Optional, Union, overload, Callable


@overload
def default_data_transformer(
    data: None = ..., max_rows: int = ...
) -> Callable[[DataType], ToValuesReturnType]: ...
@overload
def default_data_transformer(
    data: DataType, max_rows: int = ...
) -> ToValuesReturnType: ...
def default_data_transformer(
    data: Optional[DataType] = None, max_rows: int = 5000
) -> Union[Callable[[DataType], ToValuesReturnType], ToValuesReturnType]:
    if data is None:

        def pipe(data: DataType, /) -> ToValuesReturnType:
            data = limit_rows(data, max_rows=max_rows)
            return to_values(data)

        return pipe

    else:
        return to_values(limit_rows(data, max_rows=max_rows))


class DataTransformerRegistry(_DataTransformerRegistry):
    def disable_max_rows(self) -> PluginEnabler:
        """Disable the MaxRowsError."""
        options = self.options
        if self.active in ("default", "vegafusion"):
            options = options.copy()
            options["max_rows"] = None
        return self.enable(**options)


__all__ = (
    "DataTransformerRegistry",
    "MaxRowsError",
    "curry",
    "sanitize_dataframe",
    "default_data_transformer",
    "limit_rows",
    "pipe",
    "sample",
    "to_csv",
    "to_json",
    "to_values",
    "check_data_type",
)
