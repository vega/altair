"""Datasets for use with Altair

The functions here are merely thin wrappers for data access routines in the
vega_datasets package.
"""

def load_dataset(name):
    """Load a dataset by name as a pandas.DataFrame."""
    import vega_datasets
    return vega_datasets.data(name)


def list_datasets():
    """List the available datasets."""
    import vega_datasets
    return vega_datasets.data.list_datasets()
