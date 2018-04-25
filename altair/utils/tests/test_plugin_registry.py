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
