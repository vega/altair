from ..plugin_registry import PluginRegistry


class RegistryTest(PluginRegistry):
    pass


def test_plugin_registry():
    plugins = RegistryTest()

    assert plugins.names() == []
    assert plugins.active == ''
    assert plugins.get() is None
    assert repr(plugins) == "RegistryTest(active='', registered=[])"

    plugins.register('new_plugin', lambda x: x ** 2)
    assert plugins.names() == ['new_plugin']
    assert plugins.active == ''
    assert plugins.get() is None
    assert repr(plugins) == ("RegistryTest(active='', "
                             "registered=['new_plugin'])")

    plugins.enable('new_plugin')
    assert plugins.names() == ['new_plugin']
    assert plugins.active == 'new_plugin'
    assert plugins.get()(3) == 9
    assert repr(plugins) == ("RegistryTest(active='new_plugin', "
                             "registered=['new_plugin'])")
