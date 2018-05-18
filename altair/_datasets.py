"""Datasets for use with Altair

The functions here are merely thin wrappers for data access routines in the
vega_datasets package.
"""
import warnings


ERR_MESSAGE = """
The vega_datasets package must be installed in order to use altair.datasets.
See http://github.com/altair-viz/vega_datasets/ for information.
"""


class VegaDatasetsMock(object):
    def __call__(self, *args, **kwargs):
        raise ImportError(ERR_MESSAGE)

    def __getitem__(self, *args):
        raise ImportError(ERR_MESSAGE)

    def __getattr__(self, attr):
        raise ImportError(ERR_MESSAGE)


try:
    from vega_datasets import data as datasets
except ImportError:
    datasets = VegaDatasetsMock()


def load_dataset(name):
    """Load a dataset by name as a pandas.DataFrame."""
    return datasets.data(name)


def list_datasets():
    """List the available datasets."""
    return datasets.list_datasets()
