from ...utils import PluginRegistry
from typing import Callable, Dict, Union
from mypy_extensions import DefaultNamedArg, Arg
import pandas as pd


SpecType = dict


DataModelType = dict

MimeBundleType = Dict[str, object]


DataModelTransformerType = Callable[[Union[DataModelType, pd.DataFrame]], DataModelType]


VegaLiteRendererType = Callable[
    [Arg(SpecType), DefaultNamedArg(DataModelType, 'data')],
    MimeBundleType
]


renderers = PluginRegistry[VegaLiteRendererType]()


data_transformers = PluginRegistry[DataModelTransformerType]

