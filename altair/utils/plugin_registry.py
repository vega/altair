from typing import Generic, TypeVar, cast

import entrypoints
from toolz import curry


PluginType = TypeVar('PluginType')


class PluginEnabler(object):
    """Context manager for enabling plugins

    This object lets you use enable() as a context manager to
    temporarily enable a given plugin::

        with plugins.enable('name'):
            do_something()  # 'name' plugin temporarily enabled
        # plugins back to original state
    """
    def __init__(self, registry, name, **options):
        self.registry = registry
        self.name = name
        self.options = options
        self.original_state = registry._get_state()
        self.registry._enable(name, **options)

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.registry._set_state(self.original_state)

    def __repr__(self):
        return "{}.enable({!r})".format(self.registry.__class__.__name__, self.name)


class PluginRegistry(Generic[PluginType]):
    """A registry for plugins.

    This is a plugin registry that allows plugins to be loaded/registered
    in two ways:

    1. Through an explicit call to ``.register(name, value)``.
    2. By looking for other Python packages that are installed and provide
       a setuptools entry point group.

    When you create an instance of this class, provide the name of the
    entry point group to use::

        reg = PluginRegister('my_entrypoint_group')

    """
    # this is a mapping of name to error message to allow custom error messages
    # in case an entrypoint is not found
    entrypoint_err_messages = {}

    # global settings is a key-value mapping of settings that are stored globally
    # in the registry rather than passed to the plugins
    _global_settings = {}

    def __init__(self, entry_point_group='', plugin_type=object):
        # type: (str, Any) -> None
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
        self._active_name = ''  # type: str
        self._plugins = {}      # type: dict
        self._options = {}      # type: dict
        self._global_settings = self.__class__._global_settings.copy()  # type: dict

    def register(self, name, value):
        # type: (str, Union[PluginType, None]) -> PluginType
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

    def names(self):
        # type: () -> List[str]
        """List the names of the registered and entry points plugins."""
        exts = list(self._plugins.keys())
        more_exts = [ep.name for ep in entrypoints.get_group_all(self.entry_point_group)]
        exts.extend(more_exts)
        return sorted(set(exts))

    def _get_state(self):
        """Return a dictionary representing the current state of the registry"""
        return {'_active': self._active,
                '_active_name': self._active_name,
                '_plugins': self._plugins.copy(),
                '_options': self._options.copy(),
                '_global_settings': self._global_settings.copy()}

    def _set_state(self, state):
        """Reset the state of the registry"""
        assert set(state.keys()) == {'_active', '_active_name',
                                     '_plugins', '_options', '_global_settings'}
        for key, val in state.items():
            setattr(self, key, val)

    def _enable(self, name, **options):
        # type: (str, **Any) -> None
        if name not in self._plugins:
            try:
                ep = entrypoints.get_single(self.entry_point_group, name)
            except entrypoints.NoSuchEntryPoint:
                if name in self.entrypoint_err_messages:
                    raise ValueError(self.entrypoint_err_messages[name])
                else:
                    raise
            value = cast(PluginType, ep.load())
            assert isinstance(value, self.plugin_type)
            self.register(name, value)
        self._active_name = name
        self._active = self._plugins[name]
        for key in set(options.keys()) & set(self._global_settings.keys()):
            self._global_settings[key] = options.pop(key)
        self._options = options

    def enable(self, name=None, **options):
        # type: (str, **Any) -> PluginEnabler
        """Enable a plugin by name.

        This can be either called directly, or used as a context manager.

        Parameters
        ----------
        name : string (optional)
            The name of the plugin to enable. If not specified, then use the
            current active name.
        **options :
            Any additional parameters will be passed to the plugin as keyword
            arguments

        Returns
        -------
        PluginEnabler:
            An object that allows enable() to be used as a context manager
        """
        if name is None:
            name = self.active
        return PluginEnabler(self, name, **options)


    @property
    def active(self):
        # type: () -> str
        """Return the name of the currently active plugin"""
        return self._active_name

    @property
    def options(self):
        # type: () -> str
        """Return the current options dictionary"""
        return self._options

    def get(self):
        # type: () -> PluginType
        """Return the currently active plugin."""
        if self._options:
            return curry(self._active, **self._options)
        else:
            return self._active

    def __repr__(self):
        # type: () -> str
        return ("{}(active={!r}, registered={!r})"
                "".format(self.__class__.__name__,
                          self._active_name,
                          list(self.names())))
