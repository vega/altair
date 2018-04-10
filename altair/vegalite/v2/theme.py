"""Tools for enabling and registering chart themes"""

from ...utils import PluginRegistry

# The entry point group that can be used by other packages to declare other
# renderers that will be auto-detected. Explicit registration is also
# allowed by the PluginRegistery API.
ENTRY_POINT_GROUP = 'altair.vegalite.v2.theme'  # type: str

class ThemeRegistry(PluginRegistry[dict]):
    pass

theme = ThemeRegistry(entry_point_group=ENTRY_POINT_GROUP)

theme.register('default', {"config": {"view": {"width": 400, "height": 300}}})
theme.register('opaque', {"config": {"background": "white",
                                     "view": {"width": 400, "height": 300}}})
theme.register('none', {})
theme.enable('default')
