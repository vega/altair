import json
import os
import random
import hashlib
import warnings

import pandas as pd
from toolz import curried
from typing import Callable

from .core import sanitize_dataframe
from .core import sanitize_geo_interface
from .deprecation import AltairDeprecationWarning
from .plugin_registry import PluginRegistry


# ==============================================================================
# Data transformer registry
# ==============================================================================
DataTransformerType = Callable


class DataTransformerRegistry(PluginRegistry[DataTransformerType]):
    _global_settings = {"consolidate_datasets": True}

    @property
    def consolidate_datasets(self):
        return self._global_settings["consolidate_datasets"]

    @consolidate_datasets.setter
    def consolidate_datasets(self, value):
        self._global_settings["consolidate_datasets"] = value


# ==============================================================================
# Data model transformers
#
# A data model transformer is a pure function that takes a dict or DataFrame
# and returns a transformed version of a dict or DataFrame. The dict objects
# will be the Data portion of the VegaLite schema. The idea is that user can
# pipe a sequence of these data transformers together to prepare the data before
# it hits the renderer.
#
# In this version of Altair, renderers only deal with the dict form of a
# VegaLite spec, after the Data model has been put into a schema compliant
# form.
#
# A data model transformer has the following type signature:
# DataModelType = Union[dict, pd.DataFrame]
# DataModelTransformerType = Callable[[DataModelType, KwArgs], DataModelType]
# ==============================================================================


class MaxRowsError(Exception):
    """Raised when a data model has too many rows."""

    pass


@curried.curry
def limit_rows(data, max_rows=5000):
    """Raise MaxRowsError if the data model has more than max_rows.

    If max_rows is None, then do not perform any check.
    """
    check_data_type(data)
    if hasattr(data, "__geo_interface__"):
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
    elif hasattr(data, "__dataframe__"):
        values = data
    if max_rows is not None and len(values) > max_rows:
        raise MaxRowsError(
            "The number of rows in your dataset is greater "
            f"than the maximum allowed ({max_rows}).\n\n"
            "See https://altair-viz.github.io/user_guide/large_datasets.html "
            "for information on how to plot large datasets, "
            "including how to install third-party data management tools and, "
            "in the right circumstance, disable the restriction"
        )
    return data


@curried.curry
def sample(data, n=None, frac=None):
    """Reduce the size of the data model by sampling without replacement."""
    check_data_type(data)
    if isinstance(data, pd.DataFrame):
        return data.sample(n=n, frac=frac)
    elif isinstance(data, dict):
        if "values" in data:
            values = data["values"]
            n = n if n else int(frac * len(values))
            values = random.sample(values, n)
            return {"values": values}
    elif hasattr(data, "__dataframe__"):
        # experimental interchange dataframe support
        pi = import_pyarrow_interchange()
        pa_table = pi.from_dataframe(data)
        n = n if n else int(frac * len(pa_table))
        indices = random.sample(range(len(pa_table)), n)
        return pa_table.take(indices)


@curried.curry
def to_json(
    data,
    prefix="altair-data",
    extension="json",
    filename="{prefix}-{hash}.{extension}",
    urlpath="",
):
    """
    Write the data model to a .json file and return a url based data model.
    """
    data_json = _data_to_json_string(data)
    data_hash = _compute_data_hash(data_json)
    filename = filename.format(prefix=prefix, hash=data_hash, extension=extension)
    with open(filename, "w") as f:
        f.write(data_json)
    return {"url": os.path.join(urlpath, filename), "format": {"type": "json"}}


@curried.curry
def to_csv(
    data,
    prefix="altair-data",
    extension="csv",
    filename="{prefix}-{hash}.{extension}",
    urlpath="",
):
    """Write the data model to a .csv file and return a url based data model."""
    data_csv = _data_to_csv_string(data)
    data_hash = _compute_data_hash(data_csv)
    filename = filename.format(prefix=prefix, hash=data_hash, extension=extension)
    with open(filename, "w") as f:
        f.write(data_csv)
    return {"url": os.path.join(urlpath, filename), "format": {"type": "csv"}}


@curried.curry
def to_values(data):
    """Replace a DataFrame by a data model with values."""
    check_data_type(data)
    if hasattr(data, "__geo_interface__"):
        if isinstance(data, pd.DataFrame):
            data = sanitize_dataframe(data)
        data = sanitize_geo_interface(data.__geo_interface__)
        return {"values": data}
    elif isinstance(data, pd.DataFrame):
        data = sanitize_dataframe(data)
        return {"values": data.to_dict(orient="records")}
    elif isinstance(data, dict):
        if "values" not in data:
            raise KeyError("values expected in data dict, but not present.")
        return data
    elif hasattr(data, "__dataframe__"):
        # experimental interchange dataframe support
        pi = import_pyarrow_interchange()
        pa_table = pi.from_dataframe(data)
        return {"values": pa_table.to_pylist()}


def check_data_type(data):
    """Raise if the data is not a dict or DataFrame."""
    if not isinstance(data, (dict, pd.DataFrame)) and not any(
        hasattr(data, attr) for attr in ["__geo_interface__", "__dataframe__"]
    ):
        raise TypeError(
            "Expected dict, DataFrame or a __geo_interface__ attribute, got: {}".format(
                type(data)
            )
        )


# ==============================================================================
# Private utilities
# ==============================================================================


def _compute_data_hash(data_str):
    return hashlib.md5(data_str.encode()).hexdigest()


def _data_to_json_string(data):
    """Return a JSON string representation of the input data"""
    check_data_type(data)
    if hasattr(data, "__geo_interface__"):
        if isinstance(data, pd.DataFrame):
            data = sanitize_dataframe(data)
        data = sanitize_geo_interface(data.__geo_interface__)
        return json.dumps(data)
    elif isinstance(data, pd.DataFrame):
        data = sanitize_dataframe(data)
        return data.to_json(orient="records", double_precision=15)
    elif isinstance(data, dict):
        if "values" not in data:
            raise KeyError("values expected in data dict, but not present.")
        return json.dumps(data["values"], sort_keys=True)
    elif hasattr(data, "__dataframe__"):
        # experimental interchange dataframe support
        pi = import_pyarrow_interchange()
        pa_table = pi.from_dataframe(data)
        return json.dumps(pa_table.to_pylist())
    else:
        raise NotImplementedError(
            "to_json only works with data expressed as " "a DataFrame or as a dict"
        )


def _data_to_csv_string(data):
    """return a CSV string representation of the input data"""
    check_data_type(data)
    if hasattr(data, "__geo_interface__"):
        raise NotImplementedError(
            "to_csv does not work with data that "
            "contains the __geo_interface__ attribute"
        )
    elif isinstance(data, pd.DataFrame):
        data = sanitize_dataframe(data)
        return data.to_csv(index=False)
    elif isinstance(data, dict):
        if "values" not in data:
            raise KeyError("values expected in data dict, but not present")
        return pd.DataFrame.from_dict(data["values"]).to_csv(index=False)
    elif hasattr(data, "__dataframe__"):
        # experimental interchange dataframe support
        pi = import_pyarrow_interchange()
        import pyarrow as pa
        import pyarrow.csv as pa_csv

        pa_table = pi.from_dataframe(data)
        csv_buffer = pa.BufferOutputStream()
        pa_csv.write_csv(pa_table, csv_buffer)
        return csv_buffer.getvalue().to_pybytes().decode()
    else:
        raise NotImplementedError(
            "to_csv only works with data expressed as " "a DataFrame or as a dict"
        )


def pipe(data, *funcs):
    """
    Pipe a value through a sequence of functions

    Deprecated: use toolz.curried.pipe() instead.
    """
    warnings.warn(
        "alt.pipe() is deprecated, and will be removed in a future release. "
        "Use toolz.curried.pipe() instead.",
        AltairDeprecationWarning,
        stacklevel=1,
    )
    return curried.pipe(data, *funcs)


def curry(*args, **kwargs):
    """Curry a callable function

    Deprecated: use toolz.curried.curry() instead.
    """
    warnings.warn(
        "alt.curry() is deprecated, and will be removed in a future release. "
        "Use toolz.curried.curry() instead.",
        AltairDeprecationWarning,
        stacklevel=1,
    )
    return curried.curry(*args, **kwargs)


def import_pyarrow_interchange():
    import pkg_resources

    try:
        pkg_resources.require("pyarrow>=11.0.0")
        # The package is installed and meets the minimum version requirement
        import pyarrow.interchange as pi

        return pi
    except pkg_resources.DistributionNotFound as err:
        # The package is not installed
        raise ImportError(
            "Usage of the DataFrame Interchange Protocol requires the package 'pyarrow', but it is not installed."
        ) from err
    except pkg_resources.VersionConflict as err:
        # The package is installed but does not meet the minimum version requirement
        raise ImportError(
            "The installed version of 'pyarrow' does not meet the minimum requirement of version 11.0.0. "
            "Please update 'pyarrow' to use the DataFrame Interchange Protocol."
        ) from err
