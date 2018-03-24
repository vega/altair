"""Datasets for use with Altair

The functions here are merely thin wrappers for data access routines in the
vega_datasets package.
"""
import warnings

MSG = ("load_dataset is deprecated. "
       "Please use the vega_datasets package instead.")


def load_dataset(name):
    """Load a dataset by name as a pandas.DataFrame."""
    warnings.warn(MSG, DeprecationWarning)
    import vega_datasets
    return vega_datasets.data(name)


def list_datasets():
    """List the available datasets."""
    warnings.warn(MSG, DeprecationWarning)
    import vega_datasets
    return vega_datasets.data.list_datasets()
