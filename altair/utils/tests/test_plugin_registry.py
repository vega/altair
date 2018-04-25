from ..plugin_registry import PluginRegistry
from typing import Callable


class TypedCallableRegistry(PluginRegistry[Callable[[int], int]]):
    pass


class GeneralCallableRegistry(PluginRegistry):
    pass


def test_plugin_registry():
    plugins = TypedCallableRegistry()

    assert plugins.names() == []
    assert plugins.active == ''
    assert plugins.get() is None
    assert repr(plugins) == "TypedCallableRegistry(active='', registered=[])"

    plugins.register('new_plugin', lambda x: x ** 2)
    assert plugins.names() == ['new_plugin']
    assert plugins.active == ''
    assert plugins.get() is None
    assert repr(plugins) == ("TypedCallableRegistry(active='', "
                             "registered=['new_plugin'])")

    plugins.enable('new_plugin')
    assert plugins.names() == ['new_plugin']
    assert plugins.active == 'new_plugin'
    assert plugins.get()(3) == 9
    assert repr(plugins) == ("TypedCallableRegistry(active='new_plugin', "
                             "registered=['new_plugin'])")


def test_plugin_registry_extra_options():
    plugins = GeneralCallableRegistry()

    plugins.register('metadata_plugin', lambda x, p=2: x ** p)
    plugins.enable('metadata_plugin')
    assert plugins.get()(3) == 9

    plugins.enable('metadata_plugin', p=3)
    assert plugins.get()(3) == 27


def test_plugin_registry_context():
    plugins = GeneralCallableRegistry()

    plugins.register('default', lambda x, p=2: x ** p)

    # At first there is no plugin enabled
    assert plugins.active == ''
    assert plugins.options == {}

    # Make sure the context is set and reset correctly
    with plugins.enable_context('default', p=6):
        assert plugins.active == 'default'
        assert plugins.options == {'p': 6}

    assert plugins.active == ''
    assert plugins.options == {}

    # Make sure the context is reset even if there is an error
    try:
        with plugins.enable_context('default', p=6):
            raise ValueError()
    except ValueError:
        pass

    assert plugins.active == ''
    assert plugins.options == {}
