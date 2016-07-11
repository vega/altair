__version__ = '1.0.0rc3'

from .api import (
    load_vegalite_spec,
    Label,
    Formula,
    StackOffset,
    Data,
    FacetScaleConfig,
    AxisConfig,
    Shape,
    Axis,
    AggregateOp,
    ScaleConfig,
    NiceTime,
    Transform,
    VerticalAlign,
    SortOrder,
    Legend,
    LegendConfig,
    Column,
    FontWeight,
    SortField,
    Text,
    MarkConfig,
    TimeUnit,
    FacetConfig,
    FontStyle,
    Config,
    Order,
    HorizontalAlign,
    Path,
    Scale,
    Encoding,
    Facet,
    Size,
    FacetGridConfig,
    Row,
    Bin,
    AxisOrient,
    X, Y,
    Color,
    Opacity,
    DataFormat,
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

from .tutorial import tutorial

