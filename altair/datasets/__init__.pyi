"""
Type stubs for altair.datasets module.

This file provides type information for the dynamic dataset accessors
to help static type checkers like Pylance and mypy understand the
available dataset attributes.

The contents of this file are automatically generated from the dataset
metadata. Do not modify directly.
"""

from typing import Any, Union
from ._data import DataObject, DatasetAccessor
from ._loader import Loader
from ._reader import load, url

# Type for the data object with all available dataset attributes
class DataObjectWithDatasets(DataObject):
    # All available datasets from _typing.py Dataset type
    airports: DatasetAccessor
    annual_precip: DatasetAccessor
    anscombe: DatasetAccessor
    barley: DatasetAccessor
    birdstrikes: DatasetAccessor
    budget: DatasetAccessor
    budgets: DatasetAccessor
    burtin: DatasetAccessor
    cars: DatasetAccessor
    co2_concentration: DatasetAccessor
    countries: DatasetAccessor
    crimea: DatasetAccessor
    disasters: DatasetAccessor
    driving: DatasetAccessor
    earthquakes: DatasetAccessor
    ffox: DatasetAccessor
    flare: DatasetAccessor
    flare_dependencies: DatasetAccessor
    flights_10k: DatasetAccessor
    flights_200k_arrow: DatasetAccessor
    flights_200k_json: DatasetAccessor
    flights_20k: DatasetAccessor
    flights_2k: DatasetAccessor
    flights_3m: DatasetAccessor
    flights_5k: DatasetAccessor
    flights_airport: DatasetAccessor
    football: DatasetAccessor
    gapminder: DatasetAccessor
    gapminder_health_income: DatasetAccessor
    gimp: DatasetAccessor
    github: DatasetAccessor
    global_temp: DatasetAccessor
    icon_7zip: DatasetAccessor
    income: DatasetAccessor
    iowa_electricity: DatasetAccessor
    jobs: DatasetAccessor
    la_riots: DatasetAccessor
    london_boroughs: DatasetAccessor
    london_centroids: DatasetAccessor
    london_tube_lines: DatasetAccessor
    lookup_groups: DatasetAccessor
    lookup_people: DatasetAccessor
    miserables: DatasetAccessor
    monarchs: DatasetAccessor
    movies: DatasetAccessor
    normal_2d: DatasetAccessor
    obesity: DatasetAccessor
    ohlc: DatasetAccessor
    penguins: DatasetAccessor
    platformer_terrain: DatasetAccessor
    political_contributions: DatasetAccessor
    population: DatasetAccessor
    population_engineers_hurricanes: DatasetAccessor
    seattle_weather: DatasetAccessor
    seattle_weather_hourly_normals: DatasetAccessor
    sp500: DatasetAccessor
    sp500_2000: DatasetAccessor
    species: DatasetAccessor
    stocks: DatasetAccessor
    udistrict: DatasetAccessor
    unemployment: DatasetAccessor
    unemployment_across_industries: DatasetAccessor
    uniform_2d: DatasetAccessor
    us_10m: DatasetAccessor
    us_employment: DatasetAccessor
    us_state_capitals: DatasetAccessor
    volcano: DatasetAccessor
    weather: DatasetAccessor
    weekly_weather: DatasetAccessor
    wheat: DatasetAccessor
    windvectors: DatasetAccessor
    world_110m: DatasetAccessor
    zipcodes: DatasetAccessor

# Export the data object with proper typing
data: DataObjectWithDatasets

# Export other functions and classes
__all__ = ["data", "Loader", "load", "url"]
