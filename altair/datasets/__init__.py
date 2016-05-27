"""
Load datasets from https://github.com/vega/vega-datasets.

The datasets are return as `pandas.DataFrame` objects.
"""

from .core import connection_ok, list_datasets, load_dataset, URLError
