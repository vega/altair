from __future__ import annotations
import json
import random
import hashlib
from typing import (
    Any,
    List,
    MutableMapping,
    Sequence,
    TYPE_CHECKING,
    Protocol,
    TypedDict,
    Literal,
    TypeVar,
    Union,
    Dict,
    overload,
    runtime_checkable,
)
from typing_extensions import TypeAlias
from pathlib import Path
from functools import partial
import sys

import pandas as pd

from ._importers import import_pyarrow_interchange
from .core import sanitize_dataframe, sanitize_arrow_table, DataFrameLike
from .core import sanitize_geo_interface
from .plugin_registry import PluginRegistry

if sys.version_info >= (3, 13):
    from typing import TypeIs
else:
    from typing_extensions import TypeIs

if TYPE_CHECKING:
    import pyarrow as pa


@runtime_checkable
class SupportsGeoInterface(Protocol):
    __geo_interface__: MutableMapping


DataType: TypeAlias = Union[
    Dict[Any, Any], pd.DataFrame, SupportsGeoInterface, DataFrameLike
]

TDataType = TypeVar("TDataType", bound=DataType)

VegaLiteDataDict: TypeAlias = Dict[
    str, Union[str, Dict[Any, Any], List[Dict[Any, Any]]]
]
ToValuesReturnType: TypeAlias = Dict[str, Union[Dict[Any, Any], List[Dict[Any, Any]]]]
SampleReturnType = Union[pd.DataFrame, Dict[str, Sequence], "pa.lib.Table", None]


def is_data_type(obj: Any) -> TypeIs[DataType]:
    return isinstance(obj, (dict, pd.DataFrame, DataFrameLike, SupportsGeoInterface))


# ==============================================================================
# Data transformer registry
#
# A data transformer is a callable that takes a supported data type and returns
# a transformed dictionary version of it which is compatible with the VegaLite schema.
# The dict objects will be the Data portion of the VegaLite schema.
#
# Renderers only deal with the dict form of a
# VegaLite spec, after the Data model has been put into a schema compliant
# form.
# ==============================================================================
class DataTransformerType(Protocol):
    @overload
    def __call__(self, data: None = None, **kwargs) -> DataTransformerType: ...
    @overload
    def __call__(self, data: DataType, **kwargs) -> VegaLiteDataDict: ...
    def __call__(
        self, data: DataType | None = None, **kwargs
    ) -> DataTransformerType | VegaLiteDataDict: ...


class DataTransformerRegistry(PluginRegistry[DataTransformerType]):
    _global_settings = {"consolidate_datasets": True}

    @property
    def consolidate_datasets(self) -> bool:
        return self._global_settings["consolidate_datasets"]

    @consolidate_datasets.setter
    def consolidate_datasets(self, value: bool) -> None:
        self._global_settings["consolidate_datasets"] = value


# ==============================================================================
class MaxRowsError(Exception):
    """Raised when a data model has too many rows."""


@overload
def limit_rows(data: None = ..., max_rows: int | None = ...) -> partial: ...
@overload
def limit_rows(data: DataType, max_rows: int | None = ...) -> DataType: ...
def limit_rows(
    data: DataType | None = None, max_rows: int | None = 5000
) -> partial | DataType:
    """Raise MaxRowsError if the data model has more than max_rows.

    If max_rows is None, then do not perform any check.
    """
    if data is None:
        return partial(limit_rows, max_rows=max_rows)
    check_data_type(data)

    def raise_max_rows_error():
        msg = (
            "The number of rows in your dataset is greater "
            f"than the maximum allowed ({max_rows}).\n\n"
            "Try enabling the VegaFusion data transformer which "
            "raises this limit by pre-evaluating data\n"
            "transformations in Python.\n"
            "    >> import altair as alt\n"
            '    >> alt.data_transformers.enable("vegafusion")\n\n'
            "Or, see https://altair-viz.github.io/user_guide/large_datasets.html "
            "for additional information\n"
            "on how to plot large datasets."
        )
        raise MaxRowsError(msg)

    if isinstance(data, SupportsGeoInterface):
        if data.__geo_interface__["type"] == "FeatureCollection":
            values = data.__geo_interface__["features"]
        else:
            values = data.__geo_interface__
    elif isinstance(data, pd.DataFrame):
        values = data
    elif isinstance(data, dict):
        if "values" in data:
            values = data["values"]
        else:
            return data
    elif isinstance(data, DataFrameLike):
        pa_table = arrow_table_from_dfi_dataframe(data)
        if max_rows is not None and pa_table.num_rows > max_rows:
            raise_max_rows_error()
        # Return pyarrow Table instead of input since the
        # `arrow_table_from_dfi_dataframe` call above may be expensive
        return pa_table

    if max_rows is not None and len(values) > max_rows:
        raise_max_rows_error()

    return data


@overload
def sample(
    data: None = ..., n: int | None = ..., frac: float | None = ...
) -> partial: ...
@overload
def sample(
    data: DataType, n: int | None = ..., frac: float | None = ...
) -> SampleReturnType: ...
def sample(
    data: DataType | None = None,
    n: int | None = None,
    frac: float | None = None,
) -> partial | SampleReturnType:
    """Reduce the size of the data model by sampling without replacement."""
    if data is None:
        return partial(sample, n=n, frac=frac)
    check_data_type(data)
    if isinstance(data, pd.DataFrame):
        return data.sample(n=n, frac=frac)
    elif isinstance(data, dict):
        if "values" in data:
            values = data["values"]
            if not n:
                if frac is None:
                    msg = "frac cannot be None if n is None and data is a dictionary"
                    raise ValueError(msg)
                n = int(frac * len(values))
            values = random.sample(values, n)
            return {"values": values}
        else:
            # Maybe this should raise an error or return something useful?
            return None
    elif isinstance(data, DataFrameLike):
        pa_table = arrow_table_from_dfi_dataframe(data)
        if not n:
            if frac is None:
                msg = "frac cannot be None if n is None with this data input type"
                raise ValueError(msg)
            n = int(frac * len(pa_table))
        indices = random.sample(range(len(pa_table)), n)
        return pa_table.take(indices)
    else:
        # Maybe this should raise an error or return something useful? Currently,
        # if data is of type SupportsGeoInterface it lands here
        return None


_FormatType = Literal["csv", "json"]


class _FormatDict(TypedDict):
    type: _FormatType


class _ToFormatReturnUrlDict(TypedDict):
    url: str
    format: _FormatDict


@overload
def to_json(
    data: None = ...,
    prefix: str = ...,
    extension: str = ...,
    filename: str = ...,
    urlpath: str = ...,
) -> partial: ...


@overload
def to_json(
    data: DataType,
    prefix: str = ...,
    extension: str = ...,
    filename: str = ...,
    urlpath: str = ...,
) -> _ToFormatReturnUrlDict: ...


def to_json(
    data: DataType | None = None,
    prefix: str = "altair-data",
    extension: str = "json",
    filename: str = "{prefix}-{hash}.{extension}",
    urlpath: str = "",
) -> partial | _ToFormatReturnUrlDict:
    """
    Write the data model to a .json file and return a url based data model.
    """
    kwds = _to_text_kwds(prefix, extension, filename, urlpath)
    if data is None:
        return partial(to_json, **kwds)
    else:
        data_str = _data_to_json_string(data)
        return _to_text(data_str, **kwds, format=_FormatDict(type="json"))


@overload
def to_csv(
    data: None = ...,
    prefix: str = ...,
    extension: str = ...,
    filename: str = ...,
    urlpath: str = ...,
) -> partial: ...


@overload
def to_csv(
    data: dict | pd.DataFrame | DataFrameLike,
    prefix: str = ...,
    extension: str = ...,
    filename: str = ...,
    urlpath: str = ...,
) -> _ToFormatReturnUrlDict: ...


def to_csv(
    data: dict | pd.DataFrame | DataFrameLike | None = None,
    prefix: str = "altair-data",
    extension: str = "csv",
    filename: str = "{prefix}-{hash}.{extension}",
    urlpath: str = "",
) -> partial | _ToFormatReturnUrlDict:
    """Write the data model to a .csv file and return a url based data model."""
    kwds = _to_text_kwds(prefix, extension, filename, urlpath)
    if data is None:
        return partial(to_csv, **kwds)
    else:
        data_str = _data_to_csv_string(data)
        return _to_text(data_str, **kwds, format=_FormatDict(type="csv"))


def _to_text(
    data: str,
    prefix: str,
    extension: str,
    filename: str,
    urlpath: str,
    format: _FormatDict,
) -> _ToFormatReturnUrlDict:
    data_hash = _compute_data_hash(data)
    filename = filename.format(prefix=prefix, hash=data_hash, extension=extension)
    Path(filename).write_text(data, encoding="utf-8")
    url = str(Path(urlpath, filename))
    return _ToFormatReturnUrlDict({"url": url, "format": format})


def _to_text_kwds(prefix: str, extension: str, filename: str, urlpath: str, /) -> dict[str, str]:  # fmt: skip
    return {"prefix": prefix, "extension": extension, "filename": filename, "urlpath": urlpath}  # fmt: skip


def to_values(data: DataType) -> ToValuesReturnType:
    """Replace a DataFrame by a data model with values."""
    check_data_type(data)
    if isinstance(data, SupportsGeoInterface):
        if isinstance(data, pd.DataFrame):
            data = sanitize_dataframe(data)
        # Maybe the type could be further clarified here that it is
        # SupportGeoInterface and then the ignore statement is not needed?
        data_sanitized = sanitize_geo_interface(data.__geo_interface__)  # type: ignore[arg-type]
        return {"values": data_sanitized}
    elif isinstance(data, pd.DataFrame):
        data = sanitize_dataframe(data)
        return {"values": data.to_dict(orient="records")}
    elif isinstance(data, dict):
        if "values" not in data:
            msg = "values expected in data dict, but not present."
            raise KeyError(msg)
        return data
    elif isinstance(data, DataFrameLike):
        pa_table = sanitize_arrow_table(arrow_table_from_dfi_dataframe(data))
        return {"values": pa_table.to_pylist()}
    else:
        # Should never reach this state as tested by check_data_type
        msg = f"Unrecognized data type: {type(data)}"
        raise ValueError(msg)


def check_data_type(data: DataType) -> None:
    if not is_data_type(data):
        msg = f"Expected dict, DataFrame or a __geo_interface__ attribute, got: {type(data)}"
        raise TypeError(msg)


# ==============================================================================
# Private utilities
# ==============================================================================
def _compute_data_hash(data_str: str) -> str:
    return hashlib.sha256(data_str.encode()).hexdigest()[:32]


def _data_to_json_string(data: DataType) -> str:
    """Return a JSON string representation of the input data"""
    check_data_type(data)
    if isinstance(data, SupportsGeoInterface):
        if isinstance(data, pd.DataFrame):
            data = sanitize_dataframe(data)
        # Maybe the type could be further clarified here that it is
        # SupportGeoInterface and then the ignore statement is not needed?
        data = sanitize_geo_interface(data.__geo_interface__)  # type: ignore[arg-type]
        return json.dumps(data)
    elif isinstance(data, pd.DataFrame):
        data = sanitize_dataframe(data)
        return data.to_json(orient="records", double_precision=15)
    elif isinstance(data, dict):
        if "values" not in data:
            msg = "values expected in data dict, but not present."
            raise KeyError(msg)
        return json.dumps(data["values"], sort_keys=True)
    elif isinstance(data, DataFrameLike):
        pa_table = arrow_table_from_dfi_dataframe(data)
        return json.dumps(pa_table.to_pylist())
    else:
        msg = "to_json only works with data expressed as " "a DataFrame or as a dict"
        raise NotImplementedError(msg)


def _data_to_csv_string(data: dict | pd.DataFrame | DataFrameLike) -> str:
    """return a CSV string representation of the input data"""
    check_data_type(data)
    if isinstance(data, SupportsGeoInterface):
        msg = (
            f"to_csv does not yet work with data that "
            f"is of type {type(SupportsGeoInterface).__name__!r}.\n"
            f"See https://github.com/vega/altair/issues/3441"
        )
        raise NotImplementedError(msg)
    elif isinstance(data, pd.DataFrame):
        data = sanitize_dataframe(data)
        return data.to_csv(index=False)
    elif isinstance(data, dict):
        if "values" not in data:
            msg = "values expected in data dict, but not present"
            raise KeyError(msg)
        return pd.DataFrame.from_dict(data["values"]).to_csv(index=False)
    elif isinstance(data, DataFrameLike):
        # experimental interchange dataframe support
        import pyarrow as pa
        import pyarrow.csv as pa_csv

        pa_table = arrow_table_from_dfi_dataframe(data)
        csv_buffer = pa.BufferOutputStream()
        pa_csv.write_csv(pa_table, csv_buffer)
        return csv_buffer.getvalue().to_pybytes().decode()
    else:
        msg = "to_csv only works with data expressed as " "a DataFrame or as a dict"
        raise NotImplementedError(msg)


def arrow_table_from_dfi_dataframe(dfi_df: DataFrameLike) -> pa.Table:
    """Convert a DataFrame Interchange Protocol compatible object to an Arrow Table"""
    import pyarrow as pa

    # First check if the dataframe object has a method to convert to arrow.
    # Give this preference over the pyarrow from_dataframe function since the object
    # has more control over the conversion, and may have broader compatibility.
    # This is the case for Polars, which supports Date32 columns in direct conversion
    # while pyarrow does not yet support this type in from_dataframe
    for convert_method_name in ("arrow", "to_arrow", "to_arrow_table"):
        convert_method = getattr(dfi_df, convert_method_name, None)
        if callable(convert_method):
            result = convert_method()
            if isinstance(result, pa.Table):
                return result

    pi = import_pyarrow_interchange()
    return pi.from_dataframe(dfi_df)
