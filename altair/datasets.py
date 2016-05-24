"""
Load datasets from https://github.com/vega/vega-datasets.

The datasets are return as `pandas.DataFrame` objects.
"""

try:
    from urllib.error import URLError, HTTPError
    from urllib.request import urlopen
except ImportError:
    # Python 2.X
    from urllib2 import URLError, HTTPError, urlopen

import pandas as pd

_datasets = \
{'anscombe': {'filename': 'anscombe.json', 'format': 'json'},
 'barley': {'filename': 'barley.json', 'format': 'json'},
 'birdstrikes': {'filename': 'birdstrikes.json', 'format': 'json'},
 'budget': {'filename': 'budget.json', 'format': 'json'},
 'budgets': {'filename': 'budgets.json', 'format': 'json'},
 'burtin': {'filename': 'burtin.json', 'format': 'json'},
 'cars': {'filename': 'cars.json', 'format': 'json'},
 'climate': {'filename': 'climate.json', 'format': 'json'},
 'countries': {'filename': 'countries.json', 'format': 'json'},
 'crimea': {'filename': 'crimea.json', 'format': 'json'},
 'driving': {'filename': 'driving.json', 'format': 'json'},
 'flare': {'filename': 'flare.json', 'format': 'json'},
 'flights-10k': {'filename': 'flights-10k.json', 'format': 'json'},
 'flights-20k': {'filename': 'flights-20k.json', 'format': 'json'},
 'flights-2k': {'filename': 'flights-2k.json', 'format': 'json'},
 'flights-5k': {'filename': 'flights-5k.json', 'format': 'json'},
 'gapminder': {'filename': 'gapminder.json', 'format': 'json'},
 'iris': {'filename': 'iris.json', 'format': 'json'},
 'jobs': {'filename': 'jobs.json', 'format': 'json'},
 'miserables': {'filename': 'miserables.json', 'format': 'json'},
 'monarchs': {'filename': 'monarchs.json', 'format': 'json'},
 'movies': {'filename': 'movies.json', 'format': 'json'},
 'points': {'filename': 'points.json', 'format': 'json'},
 'population': {'filename': 'population.json', 'format': 'json'},
 'unemployment-across-industries': {'filename': 'unemployment-across-industries.json',
  'format': 'json'},
 'us-10m': {'filename': 'us-10m.json', 'format': 'json'},
 'weather': {'filename': 'weather.json', 'format': 'json'},
 'weball26': {'filename': 'weball26.json', 'format': 'json'},
 'wheat': {'filename': 'wheat.json', 'format': 'json'},
 'world-110m': {'filename': 'world-110m.json', 'format': 'json'},
 'airports': {'filename': 'airports.csv', 'format': 'csv'},
 'flights-3m': {'filename': 'flights-3m.csv', 'format': 'csv'},
 'flights-airport': {'filename': 'flights-airport.csv', 'format': 'csv'},
 'seattle-temps': {'filename': 'seattle-temps.csv', 'format': 'csv'},
 'seattle-weather': {'filename': 'seattle-weather.csv', 'format': 'csv'},
 'sf-temps': {'filename': 'sf-temps.csv', 'format': 'csv'},
 'sp500': {'filename': 'sp500.csv', 'format': 'csv'},
 'stocks': {'filename': 'stocks.csv', 'format': 'csv'}}

_base_url = 'https://vega.github.io/vega-datasets/data/'


def connection_ok():
    """Check web connection.

    Returns True if web connection is OK, False otherwise.
    """
    try:
        response = urlopen(_base_url, timeout=1)
        # if an index page is ever added, this will pass through
        return True
    except HTTPError:
        # There's no index for _base_url so Error 404 is expected
        return True
    except URLError:
        # This is raised if there is no internet connection
        return False


def list_datasets():
    """List the available datasets."""
    return list(_datasets.keys())


def load_dataset(name):
    """Load a dataset by name as a pandas.DataFrame."""
    item = _datasets.get(name)
    if name is None:
        raise ValueError('No such dataset {0} exists, '
                         'use list_datasets to get a list'.format(name))
    url = _base_url + item['filename']
    if item['format'] == 'json':
        return pd.read_json(url)
    elif item['format'] == 'csv':
        return pd.read_csv(url)
