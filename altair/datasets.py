"""Datasets for use with Altair

The functions here are merely thin wrappers for data access routines in the
vega_datasets package.
"""
from vega_datasets import data


def load_dataset(name):
    """Load a dataset by name as a pandas.DataFrame."""
    return data(name)


def list_datasets():
    """List the available datasets."""
    return data.list_datasets()
