__version__ = '1.1.0.dev0'

from .api import (
    Label,
    Formula,
    Data,
    FacetScaleConfig,
    AxisConfig,
    Shape,
    Axis,
    ScaleConfig,
    Transform,
    Legend,
    LegendConfig,
    Column,
    SortField,
    Text,
    MarkConfig,
    FacetConfig,
    Config,
    Order,
    Path,
    Scale,
    Encoding,
    Facet,
    Size,
    FacetGridConfig,
    Row,
    Bin,
    X, Y,
    Color,
    Opacity,
    Chart,
    LayeredChart,
    FacetedChart,
    CellConfig,
    Detail,
)

from .datasets import (
    list_datasets,
    load_dataset
)

from . import expr

from .tutorial import tutorial

# def test():
#     import pytest
#     return pytest.main(__path__)
