from typing import Callable, Generic, List, TypeVar, Union, cast

import entrypoints



PluginType = TypeVar('PluginType')


class PluginRegistry(Generic[PluginType]):
    """A registry for plugins.

    This is a plugin registry that allows plugins to be loaded/registered
    in two ways:

    1. Through an explicit call to ``.register(name, value)``.
    2. By looking for other Python packages that are installed and provide
       a setuptools entry point group.

    When you create an instance of this claass, provide the name of the 
    entry point group to use::

        reg = PluginRegister('my_entrypoint_group')

    """

    def __init__(self, entry_point_group: str = '', plugin_type=object) -> None:
        """Create a PluginRegistry for a named entry point group.
        
        Parameters
        ==========
        entry_point_group: str
            The name of the entry point group.
        plugin_type: object
            A type that will optionally be used for runtime type checking of
            loaded plugins using isinstance.
        """
        self.entry_point_group = entry_point_group
        self.plugin_type = plugin_type
        self._active = None     # type: None
        self._plugins = {}      # type: dict
        self._options = {}      # type: dict
    

    def register(self, name: str, value: Union[PluginType,None]) -> PluginType:
        """Register a plugin by name and value.

        This method is used for explicit registration of a plugin and shouldn't be
        used to manage entry point managed plugins, which are auto-loaded.

        Parameters
        ==========
        name: str
            The name of the plugin.
        value: PluginType or None
            The actual plugin object to register or None to unregister that plugin.

        Returns
        =======
        plugin: PluginType
            The plugin that was registered or unregistered.
        """
        if value is None and name in self._plugins:
            return self._plugins.pop(name)
        else:
            assert isinstance(value, self.plugin_type)
            self._plugins[name] = value
            return value


    def names(self) -> List[str]:
        """List the names of the registered and entry points plugins."""
        exts = list(self._plugins.keys())
        more_exts = [ep.name for ep in entrypoints.get_group_all(self.entry_point_group)]
        exts.extend(more_exts)
        return exts


    def enable(self, name: str) -> None:
        """Enable a plugin by name."""
        if name not in self._plugins:
            ep = entrypoints.get_single(self.entry_point_group, name)
            value = cast(PluginType, ep.load())
            assert isinstance(value, self.plugin_type)
            self.register(name, value)
        self._active = self._plugins[name]


    def get(self) -> PluginType:
        """Return the currently active plugin."""
        return self._active

