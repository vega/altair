import sys
from toolz import curried
import uuid
from weakref import WeakValueDictionary

from typing import Union, Dict, Set, MutableMapping

if sys.version_info >= (3, 8):
    from typing import TypedDict, Final
else:
    from typing_extensions import TypedDict, Final

from altair.utils.core import _DataFrameLike
from altair.utils.data import _DataType, _ToValuesReturnType, MaxRowsError
from altair.vegalite.data import default_data_transformer

# Temporary storage for dataframes that have been extracted
# from charts by the vegafusion data transformer. Use a WeakValueDictionary
# rather than a dict so that the Python interpreter is free to garbage
# collect the stored DataFrames.
extracted_inline_tables: MutableMapping[str, _DataFrameLike] = WeakValueDictionary()

# Special URL prefix that VegaFusion uses to denote that a
# dataset in a Vega spec corresponds to an entry in the `inline_datasets`
# kwarg of vf.runtime.pre_transform_spec().
VEGAFUSION_PREFIX: Final = "vegafusion+dataset://"


class _ToVegaFusionReturnUrlDict(TypedDict):
    url: str


@curried.curry
def vegafusion_data_transformer(
    data: _DataType, max_rows: int = 100000
) -> Union[_ToVegaFusionReturnUrlDict, _ToValuesReturnType]:
    """VegaFusion Data Transformer"""
    if hasattr(data, "__geo_interface__"):
        # Use default transformer for geo interface objects
        # # (e.g. a geopandas GeoDataFrame)
        return default_data_transformer(data)
    elif hasattr(data, "__dataframe__"):
        table_name = f"table_{uuid.uuid4()}".replace("-", "_")
        extracted_inline_tables[table_name] = data
        return {"url": VEGAFUSION_PREFIX + table_name}
    else:
        # Use default transformer if we don't recognize data type
        return default_data_transformer(data)


def get_inline_table_names(vega_spec: dict) -> Set[str]:
    """Get a set of the inline datasets names in the provided Vega spec

    Inline datasets are encoded as URLs that start with the table://
    prefix.

    Parameters
    ----------
    vega_spec: dict
        A Vega specification dict

    Returns
    -------
    set of str
        Set of the names of the inline datasets that are referenced
        in the specification.

    Examples
    --------
    >>> spec = {
    ...     "data": [
    ...         {
    ...             "name": "foo",
    ...             "url": "https://path/to/file.csv"
    ...         },
    ...         {
    ...             "name": "bar",
    ...             "url": "table://inline_dataset_123"
    ...         }
    ...     ]
    ... }
    >>> get_inline_table_names(spec)
    {'inline_dataset_123'}
    """
    table_names = set()

    # Process datasets
    for data in vega_spec.get("data", []):
        url = data.get("url", "")
        if url.startswith(VEGAFUSION_PREFIX):
            name = url[len(VEGAFUSION_PREFIX) :]
            table_names.add(name)

    # Recursively process child marks, which may have their own datasets
    for mark in vega_spec.get("marks", []):
        table_names.update(get_inline_table_names(mark))

    return table_names


def get_inline_tables(vega_spec: dict) -> Dict[str, _DataFrameLike]:
    """Get the inline tables referenced by a Vega specification

    Note: This function should only be called on a Vega spec that corresponds
    to a chart that was processed by the vegafusion_data_transformer.
    Furthermore, this function may only be called once per spec because
    the returned dataframes are deleted from internal storage.

    Parameters
    ----------
    vega_spec: dict
        A Vega specification dict

    Returns
    -------
    dict from str to dataframe
        dict from inline dataset name to dataframe object
    """
    table_names = get_inline_table_names(vega_spec)
    tables = {}
    for table_name in table_names:
        try:
            tables[table_name] = extracted_inline_tables.pop(table_name)
        except KeyError:
            # named dataset that was provided by the user
            pass
    return tables


def compile_with_vegafusion(vegalite_spec: dict) -> dict:
    """Compile a Vega-Lite spec to Vega and pre-transform with VegaFusion

    Note: This function should only be called on a Vega-Lite spec
    that was generated with the "vegafusion" data transformer enabled.
    In particular, this spec may contain references to extract datasets
    using table:// prefixed URLs.

    Parameters
    ----------
    vegalite_spec: dict
        A Vega-Lite spec that was generated from an Altair chart with
        the "vegafusion" data transformer enabled

    Returns
    -------
    dict
        A Vega spec that has been pre-transformed by VegaFusion
    """
    from altair import vegalite_compilers, data_transformers

    try:
        import vegafusion as vf  # type: ignore
    except ImportError as e:
        raise ImportError(
            'The "vegafusion" data transformer requires the vegafusion-python-embed\n'
            "and vegafusion packages. These can be installed with pip using:\n"
            '    pip install "vegafusion[embed]"\n'
            "Or with conda using:\n"
            "    conda install -c conda-forge vegafusion-python-embed vegafusion"
        ) from e

    # Compile Vega-Lite spec to Vega
    compiler = vegalite_compilers.get()
    if compiler is None:
        raise ValueError("No active vega-lite compiler plugin found")

    vega_spec = compiler(vegalite_spec)

    # Retrieve dict of inline tables referenced by the spec
    inline_tables = get_inline_tables(vega_spec)

    # Pre-evaluate transforms in vega spec with vegafusion
    row_limit = data_transformers.options.get("max_rows", None)
    transformed_vega_spec, warnings = vf.runtime.pre_transform_spec(
        vega_spec,
        vf.get_local_tz(),
        inline_datasets=inline_tables,
        row_limit=row_limit,
    )

    # Check from row limit warning and convert to MaxRowsError
    for warning in warnings:
        if warning.get("type") == "RowLimitExceeded":
            raise MaxRowsError(
                "The number of dataset rows after filtering and aggregation exceeds\n"
                f"the current limit of {row_limit}. Try adding an aggregation to reduce\n"
                "the size of the dataset that must be loaded into the browser. Or, disable\n"
                "the limit by calling alt.data_transformers.disable_max_rows(). Note that\n"
                "disabling this limit may cause the browser to freeze or crash."
            )

    return transformed_vega_spec


def using_vegafusion() -> bool:
    """Check whether the vegafusion data transfomer is enabled"""
    from altair.vegalite.v5.data import data_transformers

    return data_transformers.active == "vegafusion"
