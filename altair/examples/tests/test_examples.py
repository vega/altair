import pytest
import pkgutil

# this is the package we are inspecting -- for example 'email' from stdlib
import altair.examples

try:
    # Python 3.X
    from urllib.error import URLError
except ImportError:
    # Python 2.X
    from urllib2 import URLError


def iter_submodules(package, include_packages=False):
    """Iterate importable submodules of a module"""
    prefix = package.__name__ + "."
    for importer, modname, ispkg in pkgutil.iter_modules(package.__path__,
                                                         prefix):
        if not include_packages and ispkg:
            continue

        try:
            yield __import__(modname, fromlist="dummy")
        except URLError:
            pytest.xfail("Expected failure: no internet connection")


@pytest.mark.parametrize('example', iter_submodules(altair.examples))
def test_examples_output(example):
    assert example.v.to_dict() == example.expected_output
