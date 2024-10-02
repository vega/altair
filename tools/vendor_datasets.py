from __future__ import annotations

import json
import pkgutil
import sys
import textwrap
from functools import partial
from io import BytesIO
from pathlib import Path
from typing import Any, Iterable, Literal, cast
from urllib.request import urlopen

if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias

import pandas as pd
import polars as pl

# This is the tag in http://github.com/vega/vega-datasets from
# which the datasets in this repository are sourced.
SOURCE_TAG = "v1.29.0"  # 5 years ago
CURRENT_TAG = "v2.9.0"
USE_TAG = CURRENT_TAG

BASE_URL = f"https://cdn.jsdelivr.net/npm/vega-datasets@{USE_TAG}/data/"

ExtSupported: TypeAlias = Literal[".csv", ".json", ".tsv"]


def _load_dataset_info() -> dict[str, dict[str, Any]]:
    """
    Loads dataset info from three package files.

    vega_datasets/datasets.json
    vega_datasets/dataset_info.json
    vega_datasets/local_datasets.json

    It returns a dictionary with dataset information.
    """

    def load_json(path: str) -> dict[str, Any]:
        raw = pkgutil.get_data("vega_datasets", path)
        if raw is None:
            msg = f"Cannot locate package path vega_datasets:{path}"
            raise ValueError(msg)
        return json.loads(raw.decode())

    info = load_json("datasets.json")
    descriptions = load_json("dataset_info.json")
    local_datasets = load_json("local_datasets.json")

    for name in info:
        info[name]["is_local"] = name in local_datasets
    for name in descriptions:
        info[name].update(descriptions[name])

    return info


class Dataset:
    """Class to load a particular dataset by name."""

    _instance_doc = """Loader for the {name} dataset.

    {data_description}

    {bundle_info}
    Dataset source: {url}

    Usage
    -----

        >>> from vega_datasets import data
        >>> {methodname} = data.{methodname}()
        >>> type({methodname})
        {return_type}

    Equivalently, you can use

        >>> {methodname} = data('{name}')

    To get the raw dataset rather than the dataframe, use

        >>> data_bytes = data.{methodname}.raw()
        >>> type(data_bytes)
        bytes

    To find the dataset url, use

        >>> data.{methodname}.url
        '{url}'
    {additional_docs}
    Attributes
    ----------
    filename : string
        The filename in which the dataset is stored
    url : string
        The full URL of the dataset at http://vega.github.io
    format : string
        The format of the dataset: usually one of {{'csv', 'tsv', 'json'}}
    pkg_filename : string
        The path to the local dataset within the vega_datasets package
    is_local : bool
        True if the dataset is available locally in the package
    filepath : string
        If is_local is True, the local file path to the dataset.

    {reference_info}
    """
    _additional_docs = ""
    _reference_info = """
    For information on this dataset, see https://github.com/vega/vega-datasets/
    """
    base_url = "https://cdn.jsdelivr.net/npm/vega-datasets@" + SOURCE_TAG + "/data/"
    _dataset_info = _load_dataset_info()
    _pd_read_kwds: dict[str, Any] = {}
    _return_type = pd.DataFrame
    name: str

    @classmethod
    def init(cls, name: str) -> Dataset:
        """Return an instance of this class or an appropriate subclass."""
        clsdict = {
            subcls.name: subcls
            for subcls in cls.__subclasses__()
            if hasattr(subcls, "name")
        }
        return clsdict.get(name, cls)(name)

    def __init__(self, name: str):
        info = self._infodict(name)
        self.name = name
        self.methodname = name.replace("-", "_")
        self.filename = info["filename"]
        self.url = self.base_url + info["filename"]
        self.format = info["format"]
        self.pkg_filename = "_data/" + self.filename
        self.is_local = info["is_local"]
        self.description = info.get("description", None)
        self.references = info.get("references", None)
        self.__doc__ = self._make_docstring()

    @classmethod
    def list_datasets(cls) -> list[str]:
        """Return a list of names of available datasets."""
        return sorted(cls._dataset_info.keys())

    @classmethod
    def list_local_datasets(cls) -> list[str]:
        return sorted(
            name for name, info in cls._dataset_info.items() if info["is_local"]
        )

    @classmethod
    def _infodict(cls, name: str) -> dict[str, str]:
        """Load the info dictionary for the given name."""
        info = cls._dataset_info.get(name, None)
        if info is None:
            msg = (
                f"No such dataset {name} exists, "
                "use list_datasets() to get a list "
                "of available datasets."
            )
            raise ValueError(msg)
        return info

    def raw(self, use_local: bool = True) -> bytes:
        """Load the raw dataset from remote URL or local file."""
        if use_local and self.is_local:
            out = pkgutil.get_data("vega_datasets", self.pkg_filename)
            if out is not None:
                return out
            msg = f"Cannot locate package path vega_datasets:{self.pkg_filename}"
            raise ValueError(msg)
        else:
            return urlopen(self.url).read()

    def __call__(self, use_local: bool = True, **kwargs) -> pd.DataFrame:
        """Load and parse the dataset from remote URL or local file."""
        datasource = BytesIO(self.raw(use_local=use_local))

        kwds = self._pd_read_kwds.copy()
        kwds.update(kwargs)

        if self.format == "json":
            return pd.read_json(datasource, **kwds)
        elif self.format == "csv":
            return pd.read_csv(datasource, **kwds)
        elif self.format == "tsv":
            kwds.setdefault("sep", "\t")
            return pd.read_csv(datasource, **kwds)
        else:
            msg = (
                f"Unrecognized file format: {self.format}. "
                "Valid options are ['json', 'csv', 'tsv']."
            )
            raise ValueError(msg)

    @property
    def filepath(self) -> str:
        if not self.is_local:
            msg = "filepath is only valid for local datasets"
            raise ValueError(msg)
        else:
            return str((Path(__file__).parent / "_data" / self.filename).resolve())

    def _make_docstring(self) -> str:
        info = self._infodict(self.name)

        # construct, indent, and line-wrap dataset description
        description = info.get("description", "")
        if not description:
            description = (
                "This dataset is described at " "https://github.com/vega/vega-datasets/"
            )
        wrapper = textwrap.TextWrapper(
            width=70, initial_indent="", subsequent_indent=4 * " "
        )
        description = "\n".join(wrapper.wrap(description))

        # construct, indent, and join references
        reflist: Iterable[str] = info.get("references", [])
        reflist = (f".. [{i + 1}] " + ref for i, ref in enumerate(reflist))
        wrapper = textwrap.TextWrapper(
            width=70, initial_indent=4 * " ", subsequent_indent=7 * " "
        )
        reflist = ("\n".join(wrapper.wrap(ref)) for ref in reflist)
        references: str = "\n\n".join(reflist)
        if references.strip():
            references = "References\n    ----------\n" + references

        # add information about bundling of data
        if self.is_local:
            bundle_info = (
                "This dataset is bundled with vega_datasets; "
                "it can be loaded without web access."
            )
        else:
            bundle_info = (
                "This dataset is not bundled with vega_datasets; "
                "it requires web access to load."
            )

        return self._instance_doc.format(
            additional_docs=self._additional_docs,
            data_description=description,
            reference_info=references,
            bundle_info=bundle_info,
            return_type=self._return_type,
            **self.__dict__,
        )


def getattr_to_df(name: str, /) -> pl.DataFrame:
    """Subset of what `Dataset` does."""
    js_name = name.replace("_", "-")
    file_name = DATASETS_JSON[js_name]["filename"]
    suffix = Path(file_name).suffix
    if suffix in {".csv", ".json", ".tsv"}:
        extension = cast(ExtSupported, suffix)
    else:
        raise NotImplementedError(suffix, file_name)

    url = f"{BASE_URL}{file_name}"
    with urlopen(url) as f:
        content = ext_fn(extension)(f)
    return content


class DSet:
    def __init__(self, name: str, /) -> None:
        self.name: str = name
        js_name = name.replace("_", "-")
        file_name = DATASETS_JSON[js_name]["filename"]
        suffix = Path(file_name).suffix
        self.extension: ExtSupported
        if suffix in {".csv", ".json", ".tsv"}:
            self.extension = cast(ExtSupported, suffix)
        else:
            raise NotImplementedError(suffix, file_name)

        self.url: str = f"{BASE_URL}{file_name}"

    def __call__(self, **kwds: Any) -> pl.DataFrame:
        with urlopen(self.url) as f:
            content = ext_fn(self.extension, **kwds)(f)
        return content

    def __repr__(self) -> str:
        return (
            f"{type(self).__name__}(\n  "
            f"name={self.name!r},\n  "
            f"url={self.url!r}\n"
            ")"
        )


def ext_fn(ext: ExtSupported, /):
    """Very basic mapping to `polars` eager functions."""
    if ext == ".csv":
        return pl.read_csv
    elif ext == ".json":
        return pl.read_json
    elif ext == ".tsv":
        return partial(pl.read_csv, separator="\t")
    else:
        raise


DATASET_NAMES_USED = [
    "airports",
    "anscombe",
    "barley",
    "cars",
    "co2_concentration",
    "countries",
    "disasters",
    "driving",
    "earthquakes",
    "flights_2k",
    "flights_5k",
    "flights_airport",
    "gapminder_health_income",
    "github",
    "income",
    "iowa_electricity",
    "iris",
    "jobs",
    "londonBoroughs",
    "londonCentroids",
    "londonTubeLines",
    "monarchs",
    "movies",
    "normal_2d",
    "ohlc",
    "population",
    "population_engineers_hurricanes",
    "seattle_weather",
    "sp500",
    "stocks",
    "unemployment",
    "unemployment_across_industries",
    "us_10m",
    "us_employment",
    "us_state_capitals",
    "us_unemployment",
    "wheat",
    "windvectors",
    "world_110m",
    "zipcodes",
]

DATASETS_JSON = {
    # "7zip": {"filename": "7zip.png", "format": "png"},
    "airports": {"filename": "airports.csv", "format": "csv"},
    "annual-precip": {"filename": "annual-precip.json", "format": "json"},
    "anscombe": {"filename": "anscombe.json", "format": "json"},
    "barley": {"filename": "barley.json", "format": "json"},
    "birdstrikes": {"filename": "birdstrikes.json", "format": "json"},
    "budget": {"filename": "budget.json", "format": "json"},
    "budgets": {"filename": "budgets.json", "format": "json"},
    "burtin": {"filename": "burtin.json", "format": "json"},
    "cars": {"filename": "cars.json", "format": "json"},
    "climate": {"filename": "climate.json", "format": "json"},
    "co2-concentration": {"filename": "co2-concentration.csv", "format": "csv"},
    "countries": {"filename": "countries.json", "format": "json"},
    "crimea": {"filename": "crimea.json", "format": "json"},
    "disasters": {"filename": "disasters.csv", "format": "csv"},
    "driving": {"filename": "driving.json", "format": "json"},
    "earthquakes": {"filename": "earthquakes.json", "format": "json"},
    # "ffox": {"filename": "ffox.png", "format": "png"},
    "flare": {"filename": "flare.json", "format": "json"},
    "flare-dependencies": {"filename": "flare-dependencies.json", "format": "json"},
    "flights-10k": {"filename": "flights-10k.json", "format": "json"},
    "flights-200k": {"filename": "flights-200k.json", "format": "json"},
    "flights-20k": {"filename": "flights-20k.json", "format": "json"},
    "flights-2k": {"filename": "flights-2k.json", "format": "json"},
    "flights-3m": {"filename": "flights-3m.csv", "format": "csv"},
    "flights-5k": {"filename": "flights-5k.json", "format": "json"},
    "flights-airport": {"filename": "flights-airport.csv", "format": "csv"},
    "gapminder": {"filename": "gapminder.json", "format": "json"},
    "gapminder-health-income": {
        "filename": "gapminder-health-income.csv",
        "format": "csv",
    },
    # "gimp": {"filename": "gimp.png", "format": "png"},
    "github": {"filename": "github.csv", "format": "csv"},
    "graticule": {"filename": "graticule.json", "format": "json"},
    "income": {"filename": "income.json", "format": "json"},
    "iowa-electricity": {"filename": "iowa-electricity.csv", "format": "csv"},
    "iris": {"filename": "iris.json", "format": "json"},
    "jobs": {"filename": "jobs.json", "format": "json"},
    "la-riots": {"filename": "la-riots.csv", "format": "csv"},
    "londonBoroughs": {"filename": "londonBoroughs.json", "format": "json"},
    "londonCentroids": {"filename": "londonCentroids.json", "format": "json"},
    "londonTubeLines": {"filename": "londonTubeLines.json", "format": "json"},
    "lookup_groups": {"filename": "lookup_groups.csv", "format": "csv"},
    "lookup_people": {"filename": "lookup_people.csv", "format": "csv"},
    "miserables": {"filename": "miserables.json", "format": "json"},
    "monarchs": {"filename": "monarchs.json", "format": "json"},
    "movies": {"filename": "movies.json", "format": "json"},
    "normal-2d": {"filename": "normal-2d.json", "format": "json"},
    "obesity": {"filename": "obesity.json", "format": "json"},
    "ohlc": {"filename": "ohlc.json", "format": "json"},
    "points": {"filename": "points.json", "format": "json"},
    "population": {"filename": "population.json", "format": "json"},
    "population_engineers_hurricanes": {
        "filename": "population_engineers_hurricanes.csv",
        "format": "csv",
    },
    "seattle-temps": {"filename": "seattle-temps.csv", "format": "csv"},
    "seattle-weather": {"filename": "seattle-weather.csv", "format": "csv"},
    "sf-temps": {"filename": "sf-temps.csv", "format": "csv"},
    "sp500": {"filename": "sp500.csv", "format": "csv"},
    "stocks": {"filename": "stocks.csv", "format": "csv"},
    "udistrict": {"filename": "udistrict.json", "format": "json"},
    "unemployment": {"filename": "unemployment.tsv", "format": "tsv"},
    "unemployment-across-industries": {
        "filename": "unemployment-across-industries.json",
        "format": "json",
    },
    "uniform-2d": {"filename": "uniform-2d.json", "format": "json"},
    "us-10m": {"filename": "us-10m.json", "format": "json"},
    "us-employment": {"filename": "us-employment.csv", "format": "csv"},
    "us-state-capitals": {"filename": "us-state-capitals.json", "format": "json"},
    "volcano": {"filename": "volcano.json", "format": "json"},
    "weather": {"filename": "weather.json", "format": "json"},
    "weball26": {"filename": "weball26.json", "format": "json"},
    "wheat": {"filename": "wheat.json", "format": "json"},
    "windvectors": {"filename": "windvectors.csv", "format": "csv"},
    "world-110m": {"filename": "world-110m.json", "format": "json"},
    "zipcodes": {"filename": "zipcodes.csv", "format": "csv"},
}


class Stocks(Dataset):
    name = "stocks"
    _additional_docs = """
    For convenience, the stocks dataset supports pivoted output using the
    optional `pivoted` keyword. If pivoted is set to True, each company's
    price history will be returned in a separate column:

        >>> df = data.stocks()  # not pivoted
        >>> df.head(3)
          symbol       date  price
        0   MSFT 2000-01-01  39.81
        1   MSFT 2000-02-01  36.35
        2   MSFT 2000-03-01  43.22

        >>> df_pivoted = data.stocks(pivoted=True)
        >>> df_pivoted.head()
        symbol       AAPL   AMZN  GOOG     IBM   MSFT
        date
        2000-01-01  25.94  64.56   NaN  100.52  39.81
        2000-02-01  28.66  68.87   NaN   92.11  36.35
        2000-03-01  33.95  67.00   NaN  106.11  43.22
    """
    _pd_read_kwds = {"parse_dates": ["date"]}

    def __call__(self, pivoted=False, use_local=True, **kwargs):
        """
        Load and parse the dataset from remote URL or local file.

        Parameters
        ----------
        pivoted : boolean, default False
            If True, then pivot data so that each stock is in its own column.
        use_local : boolean
            If True (default), then attempt to load the dataset locally. If
            False or if the dataset is not available locally, then load the
            data from an external URL.
        **kwargs :
            additional keyword arguments are passed to data parser (usually
            pd.read_csv or pd.read_json, depending on the format of the data
            source)

        Returns
        -------
        data : DataFrame
            parsed data
        """
        __doc__ = super().__call__.__doc__  # noqa:F841
        data = super().__call__(use_local=use_local, **kwargs)
        if pivoted:
            data = data.pivot(index="date", columns="symbol", values="price")
        return data


class Cars(Dataset):
    name = "cars"
    _pd_read_kwds = {"convert_dates": ["Year"]}


class Climate(Dataset):
    name = "climate"
    _pd_read_kwds = {"convert_dates": ["DATE"]}


class Github(Dataset):
    name = "github"
    _pd_read_kwds = {"parse_dates": ["time"]}


class IowaElectricity(Dataset):
    name = "iowa-electricity"
    _pd_read_kwds = {"parse_dates": ["year"]}


class LARiots(Dataset):
    name = "la-riots"
    _pd_read_kwds = {"parse_dates": ["death_date"]}


class Miserables(Dataset):
    name = "miserables"
    _return_type = tuple
    _additional_docs = """
    The miserables data contains two dataframes, ``nodes`` and ``links``,
    both of which are returned from this function.
    """

    def __call__(self, use_local=True, **kwargs):
        __doc__ = super().__call__.__doc__  # noqa:F841
        dct = json.loads(self.raw(use_local=use_local).decode(), **kwargs)
        nodes = pd.DataFrame.from_records(dct["nodes"], index="index")
        links = pd.DataFrame.from_records(dct["links"])
        return nodes, links


class SeattleTemps(Dataset):
    name = "seattle-temps"
    _pd_read_kwds = {"parse_dates": ["date"]}


class SeattleWeather(Dataset):
    name = "seattle-weather"
    _pd_read_kwds = {"parse_dates": ["date"]}


class SFTemps(Dataset):
    name = "sf-temps"
    _pd_read_kwds = {"parse_dates": ["date"]}


class Sp500(Dataset):
    name = "sp500"
    _pd_read_kwds = {"parse_dates": ["date"]}


class UnemploymentAcrossIndustries(Dataset):
    name = "unemployment-across-industries"
    _pd_read_kwds = {"convert_dates": ["date"]}


class US_10M(Dataset):
    name = "us-10m"
    _return_type = dict
    _additional_docs = """
    The us-10m dataset is a TopoJSON file, with a structure that is not
    suitable for storage in a dataframe. For this reason, the loader returns
    a simple Python dictionary.
    """

    def __call__(self, use_local=True, **kwargs):
        __doc__ = super().__call__.__doc__  # noqa:F841
        return json.loads(self.raw(use_local=use_local).decode(), **kwargs)


class World_110M(Dataset):
    name = "world-110m"
    _return_type = dict
    _additional_docs = """
    The world-100m dataset is a TopoJSON file, with a structure that is not
    suitable for storage in a dataframe. For this reason, the loader returns
    a simple Python dictionary.
    """

    def __call__(self, use_local=True, **kwargs):
        __doc__ = super().__call__.__doc__  # noqa:F841
        return json.loads(self.raw(use_local=use_local).decode(), **kwargs)


class ZIPCodes(Dataset):
    name = "zipcodes"
    _pd_read_kwds = {"dtype": {"zip_code": "object"}}


class DataLoader:
    """
    Load a dataset from a local file or remote URL.

    There are two ways to call this; for example to load the iris dataset, you
    can call this object and pass the dataset name by string:

        >>> from vega_datasets import data
        >>> df = data("iris")

    or you can call the associated named method:

        >>> df = data.iris()

    Optionally, additional parameters can be passed to either of these

    Optional parameters
    -------------------
    return_raw : boolean
        If True, then return the raw string or bytes.
        If False (default), then return a pandas dataframe.
    use_local : boolean
        If True (default), then attempt to load the dataset locally. If
        False or if the dataset is not available locally, then load the
        data from an external URL.
    **kwargs :
        additional keyword arguments are passed to the pandas parsing function,
        either ``read_csv()`` or ``read_json()`` depending on the data format.
    """

    _datasets = {name.replace("-", "_"): name for name in Dataset.list_datasets()}

    def list_datasets(self):
        return Dataset.list_datasets()

    def __call__(self, name, return_raw=False, use_local=True, **kwargs):
        loader = getattr(self, name.replace("-", "_"))
        if return_raw:
            return loader.raw(use_local=use_local, **kwargs)
        else:
            return loader(use_local=use_local, **kwargs)

    def __getattr__(self, dataset_name):
        if dataset_name in self._datasets:
            return Dataset.init(self._datasets[dataset_name])
        else:
            msg = f"No dataset named '{dataset_name}'"
            raise AttributeError(msg)

    def __dir__(self):
        return list(self._datasets.keys())


class LocalDataLoader(DataLoader):
    _datasets = {name.replace("-", "_"): name for name in Dataset.list_local_datasets()}

    def list_datasets(self):
        return Dataset.list_local_datasets()

    def __getattr__(self, dataset_name):
        if dataset_name in self._datasets:
            return Dataset.init(self._datasets[dataset_name])
        elif dataset_name in DataLoader._datasets:
            msg = (
                f"'{dataset_name}' dataset is not available locally. To "
                f"download it, use ``vega_datasets.data.{dataset_name}()"
            )
            raise ValueError(msg)
        else:
            msg = f"No dataset named '{dataset_name}'"
            raise AttributeError(msg)
