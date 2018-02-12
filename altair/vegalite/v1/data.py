from ...utils import PluginRegistry
from ..data import (MaxRowsError, curry, default_data_transformer, limit_rows,
                    pipe, sample, to_csv, to_json, to_values)


#==============================================================================
# VegaLite 1 data transformers
#==============================================================================


ENTRY_POINT_GROUP = 'altair.vegalite.v1.data_transformer'  # type: str


data_transformers = PluginRegistry(entry_point_group=ENTRY_POINT_GROUP)  # type: PluginRegistry
data_transformers.register('default', default_data_transformer)
data_transformers.register('json', to_json)
data_transformers.register('csv', to_csv)
data_transformers.enable('default')
