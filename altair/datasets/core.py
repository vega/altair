import os
import json
import pandas as pd

try:
    from urllib.error import URLError, HTTPError
    from urllib.request import urlopen
except ImportError:
    # Python 2.X
    from urllib2 import URLError, HTTPError, urlopen

try:
    from functools import lru_cache
except ImportError:
    # Python 2.X: function not available
    lru_cache = lambda maxsize=128, typed=False: (lambda y: y)


BASE_URL = 'https://vega.github.io/vega-datasets/data/'


@lru_cache()
def _datasets_json():
    json_file = os.path.join(os.path.dirname(__file__), 'datasets.json')
    with open(json_file) as f:
        return json.loads(f.read())


def connection_ok():
    """Check web connection.

    Returns True if web connection is OK, False otherwise.
    """
    try:
        response = urlopen(BASE_URL, timeout=1)
        # if an index page is ever added, this will pass through
        return True
    except HTTPError:
        # There's no index for BASE_URL so Error 404 is expected
        return True
    except URLError:
        # This is raised if there is no internet connection
        return False


def list_datasets():
    """List the available datasets."""
    return sorted(_datasets_json().keys())


@lru_cache()
def load_dataset(name, url_only=False):
    """Load a dataset by name as a pandas.DataFrame."""
    item = _datasets_json().get(name, None)
    if item is None:
        raise ValueError('No such dataset {0} exists, '
                         'use list_datasets to get a list'.format(name))
    url = BASE_URL + item['filename']
    if url_only:
        return url
    elif item['format'] == 'json':
        return pd.read_json(url)
    elif item['format'] == 'tsv':
        return pd.read_csv(url, sep='\t')
    elif item['format'] == 'csv':
        return pd.read_csv(url)
    else:
        raise ValueError("Unrecognized file format: {0}. "
                         "Valid options are ['json', 'csv', 'tsv']."
                         "".format(item['format']))
