import pytest
import pkgutil

# this is the package we are inspecting -- for example 'email' from stdlib
import altair.examples

def iter_submodules(package, include_packages=False):
    """Iterate importable submodules of a module"""
    prefix = package.__name__ + "."
    for importer, modname, ispkg in pkgutil.iter_modules(package.__path__,
                                                         prefix):
        if not include_packages and ispkg:
            continue
        yield __import__(modname, fromlist="dummy")


@pytest.mark.parametrize('example', iter_submodules(altair.examples))
def test_examples_output(example):
    assert example.v.to_dict() == example.expected_output
